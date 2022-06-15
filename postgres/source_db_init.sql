-- Create sales table
CREATE TABLE public.sales(
id              INT PRIMARY KEY,
creation_date   VARCHAR(8),
sale_value      INT
);

-- Create sample data for source table
INSERT INTO public.sales(id, creation_date, sale_value)
VALUES
    (0, '12-12-21', '1000'),
    (1, '13-12-21', '2000');

-- Create read-only user for Airflow ETL
CREATE USER airflow_readonly WITH PASSWORD 'airflow_readonly';
GRANT CONNECT ON DATABASE source_postgres TO airflow_readonly;
GRANT USAGE ON SCHEMA public TO airflow_readonly;
GRANT SELECT ON sales TO airflow_readonly;
