from airflow import DAG
from datetime import datetime
from airflow.operators.postgres_operator import PostgresOperator


with DAG(dag_id="q1",start_date=datetime(2023,4,22),schedule_interval="@daily") as dag: #Dag
    createingatable=PostgresOperator(task_id="createingatable", # Creating a table on Postgres using the Postgres operator
                                  postgres_conn_id="postgres_default",# Connection ID to airflow
                                  sql="""
                                  CREATE TABLE IF NOT EXISTS supermarket 
                                  (
                                      id INT,
                                      product_name VARCHAR(25),
                                      price FLOAT,
                                      company VARCHAR(25),
                                      net_wt FLOAT
                                  )
                                  """)
    insertintotable=PostgresOperator(task_id="insertintotable", #Insertion of sample values into the above created table
                                postgres_conn_id="postgres_default",
                                sql="""
                                INSERT INTO supermarket (id,product_name,price,company,net_wt) VALUES(1,'Butter',20,'Amul',150);
                                INSERT INTO supermarket (id,product_name,price,company,net_wt) VALUES(2,'Biscuit',10,'Oreo',70);
                                """
                                )
    showcontent=PostgresOperator(task_id="showcontent",# Select statement to show the table supermarket
                                postgres_conn_id="postgres_default",
                                sql="""
                                SELECT * FROM supermarket;
                                """
        
    )
    createingatable >> insertintotable>> showcontent