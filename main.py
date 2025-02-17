import logging
from datetime import datetime
from utils import get_config_value
from typing import Dict,List
from from_landing_to_pl.process import process_all_walmart_tables
from s3_to_redshift.process import process_all_s3_files

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



REDSHIFT_HOST = get_config_value('RedShift', 'redshift_host')
REDSHIFT_PORT = get_config_value('RedShift', 'redshift_port')
REDSHIFT_USER = get_config_value('RedShift', 'redshift_user')
REDSHIFT_DBNAME = get_config_value('RedShift', 'redshift_dbname')
REDSHIFT_PASSWORD = get_config_value('RedShift', 'redshift_password')
REDSHIFT_LANDING_SCHEMA = get_config_value('RedShift', 'redshift_landing_schema')
S3_BUCKET = get_config_value('S3', 's3_bucket')
AWS_ACCESS_KEY_ID = get_config_value('AWS', 'aws_access_key_id')
AWS_SECRET_ACCESS_KEY = get_config_value('AWS', 'aws_secret_access_key')

sql_populaion_path = get_config_value('RedShift', 'sql_populaion_path')
sql_file_paths: List[str] = eval(get_config_value('RedShift', 'population_files_from_landing_to_walmart'))
file_to_table_mapping: Dict[str, str] = eval(get_config_value('S3', 'file_to_table_mapping'))
file_type = get_config_value('S3', 'file_type')
ignore_header = get_config_value('S3', 'ignore_header')
fact_file: List[str] = eval(get_config_value('RedShift', 'fact_file'))
def main():
    start_time = datetime.now()
    logger.info(f"Start time: {start_time}")

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
    process_all_walmart_tables(REDSHIFT_HOST,
                               REDSHIFT_PORT,
                               REDSHIFT_USER,
                               REDSHIFT_PASSWORD,
                               REDSHIFT_DBNAME,
                               sql_populaion_path,
                               sql_file_paths)
    process_all_walmart_tables(REDSHIFT_HOST,
                               REDSHIFT_PORT,
                               REDSHIFT_USER,
                               REDSHIFT_PASSWORD,
                               REDSHIFT_DBNAME,
                               sql_populaion_path,
                               fact_file)


    end_time = datetime.now()
    logger.info(f"Time Elapsed: {end_time - start_time}")
    logger.info(f"End time: {end_time}")


if __name__ == '__main__':
    main()