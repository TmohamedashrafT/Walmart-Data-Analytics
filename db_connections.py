from abc import ABC, abstractmethod
import psycopg2
import logging
from psycopg2 import OperationalError
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DatabaseConnection(ABC):
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self,exc_type, exc_val, exc_tb):
        pass

class RedshiftConnection(DatabaseConnection):
    def __init__(self, redshift_host, redshift_port, redshift_user, redshift_password, redshift_dbname):
        self.redshift_host = redshift_host
        self.redshift_port = redshift_port
        self.redshift_user = redshift_user
        self.redshift_password = redshift_password
        self.redshift_dbname = redshift_dbname
        self.conn = None
        self.cur = None

    def __enter__(self):

        try:
            self.conn = psycopg2.connect(
                host=self.redshift_host,
                port=self.redshift_port,
                dbname=self.redshift_dbname,
                user=self.redshift_user,
                password=self.redshift_password
            )
            if self.conn:
                logger.info("Connection to Redshift established successfully")
            self.cursor = self.conn.cursor()
            return self.cursor
        except OperationalError as e:
            logger.error("Error connecting to Redshift: {}".format(e))

    def __exit__(self,exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        logger.info("Connection to Redshift closed successfully")

