from db_connections import RedshiftConnection
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def transfer_file_from_s3_to_redshift(parameters_list: tuple):
    (
        redshift_host,
        redshift_port,
        redshift_user,
        redshift_password,
        redshift_dbname,
        s3_bucket,
        s3_key,
        aws_access_key_id,
        aws_secret_access_key,
        destination_schema,
        destination_table,
        file_type,
        ignore_header
    ) = parameters_list

    # Attempt to establish a connection
    rd_conn = RedshiftConnection(redshift_host, redshift_port, redshift_user, redshift_password, redshift_dbname)

    # Check if the connection is successful
    with rd_conn as rd_conn:
        copy_command = f"""
        COPY {destination_schema}.{destination_table} 
        FROM 's3://{s3_bucket}/{s3_key}'
        CREDENTIALS 'aws_access_key_id={aws_access_key_id};aws_secret_access_key={aws_secret_access_key}'
        {file_type}
        IGNOREHEADER {ignore_header}
        DATEFORMAT 'DD/MM/YYYY'
        TIMEFORMAT 'DD/MM/YYYY HH:MI:SS';
        """
        try:
            rd_conn.execute(copy_command)
            logger.info(f"Finished copying {s3_key} to {destination_table}")
        except Exception as e:
            print(f"Error loading data: {e}")



