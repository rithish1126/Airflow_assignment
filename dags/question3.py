from airflow.hooks.base_hook import BaseHook
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow.operators.python_operator import PythonOperator
from airflow import AirflowException
from airflow import DAG
from datetime import datetime
import random


slack_webhook_token = BaseHook.get_connection("slack").password
channel = BaseHook.get_connection("slack").login

def RandomFunc():
    num=random.randint(1,10)
    if(num<=5):
        raise AirflowException("Task Failed")
with DAG(dag_id="slack_dag",start_date=datetime(2023,4,22),schedule_interval="@daily") as dag:
    conditional_task=PythonOperator(
        task_id="conditional_task",
        python_callable=RandomFunc
    )
    
    slack_alert_failed = SlackWebhookOperator(
        task_id='slack_failed',
        webhook_token=slack_webhook_token,
        message="Task failed",
        channel=channel,
        username='airflow',
        http_conn_id="slack",
        trigger_rule='all_failed'
    )
    
    slack_alert_passed = SlackWebhookOperator(
        task_id='slack_passed',
        webhook_token=slack_webhook_token,
        message="Task Passed",
        channel=channel,
        username='airflow',
        http_conn_id="slack",
        trigger_rule='all_success'
    )
    
    conditional_task >> [slack_alert_failed,slack_alert_passed]