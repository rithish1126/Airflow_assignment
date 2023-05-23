# Airflow_assignment

## Question 1: Create a dag with following tasks:
```
with DAG(dag_id="q1",start_date=datetime(2023,4,22),schedule_interval="@daily") as dag:
```
### a. Task to create a simple table
```
 createingatable=PostgresOperator(task_id="createingatable",
                                  postgres_conn_id="postgres_default",
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
```
### b.Task to insert few custom values in to the created table in previous step.
```
insertintotable=PostgresOperator(task_id="insertintotable",
                                postgres_conn_id="postgres_default",
                                sql="""
                                INSERT INTO supermarket (id,product_name,price,company,net_wt) VALUES(1,'Butter',20,'Amul',150);
                                INSERT INTO supermarket (id,product_name,price,company,net_wt) VALUES(2,'Biscuit',10,'Oreo',70);
                                """
                                )
```

### c.Task to select the values from the table
```
showcontent=PostgresOperator(task_id="showcontent",
                                postgres_conn_id="postgres_default",
                                sql="""
                                SELECT * FROM supermarket;
                                """
        
    )
```
### Order
```
createingatable >> insertintotable>> showcontent
```
AIRFLOW WEBUI
<img width="1440" alt="Screenshot 2023-05-23 at 11 53 49 AM" src="https://github.com/rithish1126/Airflow_assignment/assets/122535424/3cab2ba7-d943-4034-b950-a1f4170220dc">

DOCKER CONTAINER:
<img width="1080" alt="Screenshot 2023-05-22 at 4 37 39 PM" src="https://github.com/rithish1126/Airflow_assignment/assets/122535424/362e4b1c-6c42-4427-9475-76a3fe11e66c">

## Question 2: Create a dag with following tasks:
```
with DAG(dag_id="mail",start_date=datetime(2023,4,22),schedule_interval="@daily") as dag:
```
### a. A dummy task which always succeeds
"start" function
```
def start():
    print("start")
```
```
dummytask=PythonOperator(
        task_id="dummytask",
        python_callable=start
    )
```
### b. Upon successful completion of the task your setup of airflow environment should be
such that it sends an email alert to your sigmoid mail id. Schedule the dag to run daily.

```
 sendmail = EmailOperator( 
        task_id='sendmail', 
        to='rithish.p@sigmoidanalytics.com', 
        subject='Hi there', 
        html_content="Date: {{ ds }}", 
    )
```
### Order
```
dummytask >> sendmail
```
<img width="1440" alt="Screenshot 2023-05-23 at 12 03 44 PM" src="https://github.com/rithish1126/Airflow_assignment/assets/122535424/3197d5b5-dd76-4530-8f69-c6c818be0b48">

<img width="1117" alt="Screenshot 2023-05-23 at 12 04 25 PM" src="https://github.com/rithish1126/Airflow_assignment/assets/122535424/cd172d53-2e07-4bed-ba95-21f3b7f8d455">

# 3) Create a dag with following tasks:

```
with DAG(dag_id="slack",start_date=datetime(2023,4,22),schedule_interval="@daily") as dag:
```

### a. A dummy task which can succeed/fail.
So I made a function that generates a random number that decides if the next course of action is success or fail
```
def Randomfunction():
    num=random.randint(1,10)
    if(num<=5):
        raise AirflowException("Task Failed")
```
Task
```
 if_task=PythonOperator(
        task_id="if_task",
        python_callable=Randomfunction
    )
```
### Upon success/failure send an alert message to slack workspace.
First created an account on slack then went on to https://api.slack.com/ to create an app and corrosponding webhook
then added a connection to airflow
### Success
```
success_case = SlackWebhookOperator(
        task_id='Success',
        webhook_token=slack_webhook_token,
        message="Task Passed",
        channel=channel,
        username='airflow',
        http_conn_id="slack",
        trigger_rule='all_success'
    )
```
### Failure
```
failed_case = SlackWebhookOperator(
        task_id='failed_case',
        webhook_token=slack_webhook_token,
        message="Task failed",
        channel=channel,
        username='airflow',
        http_conn_id="slack",
        trigger_rule='all_failed'
    )
```
### Order
```
    if_task >> [failed_case,success_case]
```
Success

<img width="1439" alt="Screenshot 2023-05-23 at 12 17 18 PM" src="https://github.com/rithish1126/Airflow_assignment/assets/122535424/0cb593bb-38c1-4473-a00f-92254aa54a2f">

<img width="1440" alt="Screenshot 2023-05-23 at 12 17 42 PM" src="https://github.com/rithish1126/Airflow_assignment/assets/122535424/7c840ebd-929c-4288-8def-23818c67413b">

Failure

<img width="1440" alt="Screenshot 2023-05-23 at 12 18 17 PM" src="https://github.com/rithish1126/Airflow_assignment/assets/122535424/2681b469-e824-43ae-8dd7-06ddb24256dc">

<img width="1440" alt="Screenshot 2023-05-23 at 12 19 12 PM" src="https://github.com/rithish1126/Airflow_assignment/assets/122535424/95cc243a-be02-4877-a3a9-3773db33e39f">
