# Dhruv's approach
https://github.com/ds-cr/airflowAssgn/tree/master

Q1)Create a dag with following tasks:
a. Task to create a simple table
b.Task to insert few custom values in to the created table in previous step.
c.Task to select the values from the table

Created a Dag that is scheduled to run once and under this dag
He has made three tasks with the postgres operator namely 1)create_pet_table, 2)insert_pets, 3)select_pets
a)So the create_pet_table first creates the table schema
b)the insert_pets then insert values into this table
c)select_pets then select* from this table to show the contents

Q2)Create a dag with following tasks:
a. A dummy task which always succeeds
b. Upon successful completion of the task your setup of airflow environment should be

Created a Dag that is scheduled to run daily and under this dag
Created a Dummy task that always succeeds with the pythonoperator 
Then used the Email operator to send mail to himself and has edited the airflow.cfg file to add the email password and details and then has mentioned the path of this cfg file in dockercompose.yml file

Q3)Create a dag with the following tasks:
a. A dummy task which can succeed/fail.
b. Upon success/failure send an alert message to slack workspace.

Created a dag that is scheduled daily and under this dag
a task with python operator that calls a function that generates a random number and if this number is even the task fails and if odd the task succeeds
then if the above task passes a message is sent to the slack account saying task passed using the slackwebhook operator and failed if the above task fails

# Amit's Approach
https://github.com/amitshuklasigmoid/Airflow-Assignment

Q1)Create a dag with following tasks:
a. Task to create a simple table
b.Task to insert few custom values in to the created table in previous step.
c.Task to select the values from the table

Created a Dag that is scheduled to run daily and under this dag
He has made three tasks with the postgres operator namely 1)create_table, 2)insert_values, 3)select_values
a)So the create_table first creates the table schema
b)the insert_values then insert values into this table
c)select_values then select* from this table to show the contents

Q2)Create a dag with following tasks:
a. A dummy task which always succeeds
b. Upon successful completion of the task your setup of airflow environment should be

Created a Dag that is scheduled to run daily and under this dag
and an email operator to send mail from the mail mentioned in docker-compose.yml along with the smtp password of the mail

Q3)Create a dag with the following tasks:
a. A dummy task which can succeed/fail.
b. Upon success/failure send an alert message to slack workspace.

Created a Dag that is scheduled to run daily and under this dag
Created a slack webhook token and provided the token details in host and password part.
then made a task that runs a python function that generates a random number and if that number is less than or equal 50 raises an exception using the python operator
based on if the previous task failed or not the next task runs based on the trigger_rule, if task succeed sends a message on slaack saying ":large_blue_circle: Your task is successfully completed "
and if the previous task raises error the task sends a message on slack saying ":red_circle: Your task has been failed"




