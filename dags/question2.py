from airflow import DAG 
from datetime import datetime
from airflow.operators.dummy_operator import DummyOperator 
from airflow.operators.email_operator import EmailOperator


with DAG(dag_id="mail",start_date=datetime(2023,4,22),schedule_interval="@daily") as dag:
    dummytask=DummyOperator( #Dummy task that runs the above function
        task_id="dummytask",
        
    )
     
    sendmail = EmailOperator( #Send Mail task that sends the mail to the specified mail using the EmailOperator
        task_id='sendmail', 
        to='rithish.p@sigmoidanalytics.com', 
        subject='Hi there', 
        html_content="Date: {{ ds }}", 
    )

dummytask >> sendmail
