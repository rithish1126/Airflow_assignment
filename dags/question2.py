from airflow import DAG 
from datetime import datetime
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.email_operator import EmailOperator

def start():
    print("start")
with DAG(dag_id="send_mail",start_date=datetime(2023,4,22),schedule_interval="@daily") as dag:
    dummytask=PythonOperator(
        task_id="dummy_task",
        python_callable=start
    )
     
    sendmail = EmailOperator( 
        task_id='sendmail', 
        to='rithish.p@sigmoidanalytics.com', 
        subject='Hi there', 
        html_content="Date: {{ ds }}", 
    )

dummytask >> sendmail