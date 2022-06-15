-- Create sales table
CREATE TABLE public.sales(
id              INT PRIMARY KEY,
creation_date   VARCHAR(8),
sale_value      INT
);

-- Create read/write user for Airflow ETL
CREATE USER airflow WITH password 'airflow';
GRANT CONNECT ON DATABASE target_postgres TO airflow;
GRANT USAGE ON SCHEMA public TO airflow;
GRANT SELECT, INSERT, UPDATE, TRUNCATE ON sales TO airflow;
