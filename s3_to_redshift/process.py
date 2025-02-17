from .transfer_file_from_S3_to_Redshift import transfer_file_from_s3_to_redshift
from utils import get_config_value, threads
import logging
from typing import Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_all_s3_files(redshift_host,
                         redshift_port,
                         redshift_user,
                         redshift_dbname,
                         redshift_password,
                         redshift_landing_schema,
                         s3_bucket,
                         aws_access_key_id,
                         aws_secret_access_key,
                         file_to_table_mapping,
                         file_type,
                         ignore_header):
    parameters_list = []
    for file_name, table_name in file_to_table_mapping.items():
        parameters_list.append((redshift_host,
                               redshift_port,
                               redshift_user,
                               redshift_password,
                               redshift_dbname,
                               s3_bucket,
                               file_name,
                               aws_access_key_id,
                               aws_secret_access_key,
                               redshift_landing_schema,
                               table_name,
                               file_type,
                               ignore_header))

    threads(transfer_file_from_s3_to_redshift, parameters_list, len(parameters_list))
    logger.info(f"\t\tfinished processing all files")



if __name__ == "__main__":
    REDSHIFT_HOST = get_config_value('RedShift', 'redshift_host')
    REDSHIFT_PORT = get_config_value('RedShift', 'redshift_port')
    REDSHIFT_USER = get_config_value('RedShift', 'redshift_user')
    REDSHIFT_DBNAME = get_config_value('RedShift', 'redshift_dbname')
    REDSHIFT_PASSWORD = get_config_value('RedShift', 'redshift_password')
    REDSHIFT_LANDING_SCHEMA = get_config_value('RedShift', 'redshift_landing_schema')
    S3_BUCKET = get_config_value('S3', 's3_bucket')
    AWS_ACCESS_KEY_ID = get_config_value('AWS', 'aws_access_key_id')
    AWS_SECRET_ACCESS_KEY = get_config_value('AWS', 'aws_secret_access_key')
    file_to_table_mapping: Dict[str, str] = eval(get_config_value('S3', 'file_to_table_mapping'))
    file_type = 'csv'
    ignore_header = 1
    process_all_s3_files(REDSHIFT_HOST,
                               REDSHIFT_PORT,
                               REDSHIFT_USER,
                               REDSHIFT_DBNAME,
                               REDSHIFT_PASSWORD,
                               REDSHIFT_LANDING_SCHEMA,
                               S3_BUCKET,
                               AWS_ACCESS_KEY_ID,
                               AWS_SECRET_ACCESS_KEY,
                               file_to_table_mapping,
                               file_type,
                               ignore_header)
