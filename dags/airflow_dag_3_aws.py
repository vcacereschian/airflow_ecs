import datetime as dt

import sys
sys.path.append('/opt/airflow/dags/programs/hello_world')

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

import time

from programs.s3_connection import transform

default_args = {
        'owner': 'me',
        'start_date': dt.datetime(2022, 9, 18),
        'retries': 1,
        'retry_delay': dt.timedelta(minutes=5),
        }

with DAG('aws_s3_connection',
        default_args=default_args,
        schedule_interval='0 0 * * *',
        ) as dag:
        begin = DummyOperator(
            task_id="begin"
        )
        transform_task = PythonOperator(task_id='s3_transform_task',
            python_callable=transform)
        finish = DummyOperator(
            task_id="finish"
        )
        

begin >> transform_task >> finish