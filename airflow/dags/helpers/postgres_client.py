import psycopg2


class PostgresClient:
    """Class to help connect to Postgres databases"""

    @staticmethod
    def connect(user, password, host, port, database):
        """Return a connection object"""
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database)

        return connection
