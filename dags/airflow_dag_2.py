import datetime as dt

import sys
sys.path.append('/opt/airflow/dags/programs/hello_world')

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

import time

from programs.trigger_hello import trigger_hello_world

def print_world():
    print('hello world')
    time.sleep(60)


default_args = {
        'owner': 'me',
        'start_date': dt.datetime(2022, 9, 19),
        'retries': 1,
        'retry_delay': dt.timedelta(minutes=5),
        }

with DAG('triggered_dag',
        default_args=default_args,
        ) as dag:
        begin = DummyOperator(
            task_id="begin"
        )
        trigger = PythonOperator(task_id='trigger_hello_world',
            python_callable=trigger_hello_world)
        finish = DummyOperator(
            task_id="finish"
        )
        

begin >> trigger >> finish