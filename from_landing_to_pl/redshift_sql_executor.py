from db_connections import RedshiftConnection
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def execute_sql_file_on_redshift(parameters_list: tuple):
    (
        redshift_host,
        redshift_port,
        redshift_user,
        redshift_password,
        redshift_dbname,
        sql_file_path
    ) = parameters_list

    rd_conn = RedshiftConnection(redshift_host, redshift_port, redshift_user, redshift_password, redshift_dbname)
    with rd_conn as rd_conn:
        try:
            with open(sql_file_path, 'r') as file:
                sql_query = file.read()
            rd_conn.execute(sql_query)
            logger.info(f"Finished executing {sql_file_path} query")
        except Exception as e:
            logger.error(f"Error executing SQL query: {e}")


