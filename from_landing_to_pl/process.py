from utils import get_config_value, threads
from .redshift_sql_executor import execute_sql_file_on_redshift
import logging
import os
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_all_walmart_tables(redshift_host,
                               redshift_port,
                               redshift_user,
                               redshift_password,
                               redshift_dbname,
                               sql_population_path,
                               sql_file_paths):
    base_path = os.path.dirname(__file__)
    parameters_list = []
    for sql_file_path in sql_file_paths:
        parameters_list.append((redshift_host,
                                redshift_port,
                                redshift_user,
                                redshift_password,
                                redshift_dbname,
                                os.path.join(base_path, sql_population_path, sql_file_path)))

    threads(execute_sql_file_on_redshift, parameters_list, len(parameters_list))
    logger.info(f"\t\tfinished processing all tables")


if __name__ == '__main__':
    REDSHIFT_HOST = get_config_value('RedShift', 'redshift_host')
    REDSHIFT_PORT = get_config_value('RedShift', 'redshift_port')
    REDSHIFT_USER = get_config_value('RedShift', 'redshift_user')
    REDSHIFT_DBNAME = get_config_value('RedShift', 'redshift_dbname')
    REDSHIFT_PASSWORD = get_config_value('RedShift', 'redshift_password')
    sql_populaion_path = get_config_value('RedShift', 'sql_populaion_path')
    sql_file_paths: List[str] = eval(get_config_value('RedShift', 'population_files_from_landing_to_walmart'))
    process_all_walmart_tables(REDSHIFT_HOST,
                               REDSHIFT_PORT,
                               REDSHIFT_USER,
                               REDSHIFT_PASSWORD,
                               REDSHIFT_DBNAME,
                               sql_populaion_path,
                               sql_file_paths)





