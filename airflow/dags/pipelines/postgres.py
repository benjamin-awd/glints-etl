from airflow.decorators import task
from helpers.postgres_client import PostgresClient


@task
def extract_from_postgres_to_staging(
        user: str,
        password: str,
        host: str,
        port: str,
        database: str,
        schema: str,
        table: str,
        staging_folder: str,
        staging_filename: str
):
    """
    Task that conducts a batch extract of data from PostgreSQL database
    to CSV file stored in staging folder.
    """

    connection = PostgresClient.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database)

    cursor = connection.cursor()

    # Export Postgres data to CSV
    with open(f"{staging_folder}/{staging_filename}.csv", "w") as f:
        export_sql_query = f"""COPY (SELECT * FROM {schema}.{table})
                               TO STDOUT WITH CSV HEADER"""
        cursor.copy_expert(export_sql_query, f)


@task
def load_from_staging_to_postgres(
        user: str,
        password: str,
        host: str,
        port: str,
        database: str,
        staging_folder: str,
        staging_filename: str,
        schema: str,
        table: str,
):
    """
    Task that conducts a batch load from a CSV file in staging folder
    to target Postgres database.
    """
    connection = PostgresClient.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database)

    cursor = connection.cursor()

    with open(f"{staging_folder}/{staging_filename}.csv", "r") as f:
        # Skip header and copy CSV to table, overwriting existing data
        next(f)
        cursor.copy_expert(
            sql=f"""
            TRUNCATE {schema}.{table};
            COPY {schema}.{table} FROM STDIN WITH CSV;
            """,
            file=f)

    connection.commit()
