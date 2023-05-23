from airflow.hooks.base_hook import BaseHook
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow.operators.python_operator import PythonOperator
from airflow import AirflowException
from airflow import DAG
from datetime import datetime
import random


slack_webhook_token = BaseHook.get_connection("slack").password
channel = BaseHook.get_connection("slack").login

def Randomfunction():
    num=random.randint(1,10) #generate random number from 1 to 10 to decide the next flow of course
    if(num<=5):
        raise AirflowException("Task Failed")
with DAG(dag_id="slack",start_date=datetime(2023,4,22),schedule_interval="@daily") as dag:
    if_task=PythonOperator( # task that decides next course depending on the output of Randomfunction
        task_id="if_task",
        python_callable=Randomfunction
    )
    
    failed_case = SlackWebhookOperator( #Task when failed
        task_id='failed_case',
        webhook_token=slack_webhook_token, #uses the token generated on slack api 
        message="Task failed",
        channel=channel,
        username='airflow',
        http_conn_id="slack",
        trigger_rule='all_failed'
    )
    
    success_case = SlackWebhookOperator(#Task when Succeeds
        task_id='Success',
        webhook_token=slack_webhook_token,#uses the token generated on slack api 
        message="Task Passed",
        channel=channel,
        username='airflow',
        http_conn_id="slack",
        trigger_rule='all_success'
    )
    #Order
    if_task >> [failed_case,success_case]