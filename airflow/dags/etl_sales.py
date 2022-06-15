from pipelines.postgres import (extract_from_postgres_to_staging,
                                load_from_staging_to_postgres)
from airflow.decorators import dag
from datetime import datetime


@dag(dag_id="etl_sales", start_date=datetime(2022, 6, 14))
def etl_sales_dag():
    """DAG that conducts a batch extract of data
    from source Postgres database to staging area."""

    # Extract data from source Postgres database to staging folder
    extract = extract_from_postgres_to_staging(
        user="airflow_readonly",
        password="airflow_readonly",
        host="source_postgres",
        port="5432",
        database="source_postgres",
        schema="public",
        table="sales",
        staging_folder="data",
        staging_filename="sales")

    # Load data from staging folder to target Postgres database
    load = load_from_staging_to_postgres(
        user="airflow",
        password="airflow",
        host="target_postgres",
        port="5432",
        database="target_postgres",
        staging_folder="data",
        staging_filename="sales",
        schema="public",
        table="sales"
    )

    extract >> load


extract_sales = etl_sales_dag()
