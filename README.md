# README
This repository is a ETL pipeline consisting of an Airflow and Postgres Docker-Compose application stack, linked together via a Docker network.

The code in the Airflow folder uses a DAG to extract data from a source Postgres database, which is kept in a staging folder before being loaded to another target Postgres database.

# Usage
Clone the repository

```
git clone https://github.com/benjamin-awd/glints-etl
```

Navigate to the `airflow` folder and launch the Airflow application stack

```
cd ~/dev/glints-etl/airflow
export AIRFLOW_UID=50000
docker-compose up
```

Next, open a new terminal window and navigate to the `postgres` folder and launch the Postgres application stack
```
cd ~/dev/glints-etl/postgres
docker-compose up
```

Access the Airflow Webserver via https://localhost:5884 and turn on the `etl_sales` DAG.

Use `psql` (or any other tool) to verify that the data has been successfully loaded from the source database into the target database.

If you need to reset the environment, run 
```docker-compose down --remove-orphans --volumes``` for both the Postgres and Airflow folders.

# Validation
Use psql to login to target database with
```
$ PGPASSWORD=target_postgres psql -U target_postgres -p 25432 -h localhost
```

Check the database before enabling/running the DAG
```
target_postgres=# SELECT * FROM sales;
 id | creation_date | sale_value
----+---------------+------------
(0 rows)
```

Check the database after enabling/running the DAG
```
target_postgres=# SELECT * FROM sales;
 id | creation_date | sale_value
----+---------------+------------
  0 | 12-12-21      |       1000
  1 | 13-12-21      |       2000
(2 rows)
```

The source database can be accessed with 
```
$ PGPASSWORD=source_postgres psql -U source_postgres -p 15432 -h localhost
```

# Requirements
This repository was built and tested with Docker Engine 20.10.17 and Docker Compose v2.6.0 on a Ubuntu distribution running on Windows 10 + WSL2.

No additional packages are needed since all necessary packages  are installed within the Airflow docker-compose.yaml.