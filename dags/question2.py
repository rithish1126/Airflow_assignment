from airflow import DAG 
from datetime import datetime
from airflow.operators.python_operator import PythonOperator 
from airflow.operators.email_operator import EmailOperator

def start():# Dummy task that runs this function before sending the mail
    print("start")
with DAG(dag_id="mail",start_date=datetime(2023,4,22),schedule_interval="@daily") as dag:
    dummytask=PythonOperator( #Dummy task that runs the above function
        task_id="dummytask",
        python_callable=start
    )
     
    sendmail = EmailOperator( #Send Mail task that sends the mail to the specified mail using the EmailOperator
        task_id='sendmail', 
        to='rithish.p@sigmoidanalytics.com', 
        subject='Hi there', 
        html_content="Date: {{ ds }}", 
    )

dummytask >> sendmail