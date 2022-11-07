import datetime as dt

import sys
sys.path.append('/opt/airflow/dags/programs/hello_world')

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

import time

from programs.hello_world import print_world_script, print_world_parallel_1, print_world_parallel_2, print_world_parallel_3, print_world_parallel_4, luck

def print_world():
    print('hello world')
    time.sleep(60)


default_args = {
        'owner': 'me',
        'start_date': dt.datetime(2022, 9, 19),
        'retries': 1,
        'retry_delay': dt.timedelta(minutes=5),
        }

with DAG('airflow_tutorial_v01',
        default_args=default_args,
        schedule_interval='0 */4 * * *',
        ) as dag:
        print_hello = BashOperator(task_id='print_hello',
            bash_command='echo "hello"')
        sleep = BashOperator(task_id='sleep',
            bash_command='sleep 50')
        print_world = PythonOperator(task_id='print_world',
            python_callable=print_world)
        print_world_alt = PythonOperator(task_id='print_world_script',
            python_callable=print_world_script)
        parallel_1 = PythonOperator(task_id='print_world_parallel_1',
            python_callable=print_world_parallel_1)
        parallel_2 = PythonOperator(task_id='print_world_parallel_2',
            python_callable=print_world_parallel_2)
        parallel_3 = PythonOperator(task_id='print_world_parallel_3',
            python_callable=print_world_parallel_3)
        parallel_4 = PythonOperator(task_id='print_world_parallel_4',
            python_callable=print_world_parallel_4)
        luck_task = PythonOperator(task_id='luck',
            python_callable=luck)
        phase_1 = DummyOperator(
            task_id="phase_1"
        )
        trigger = TriggerDagRunOperator(
            task_id="trigger_dag",
            trigger_dag_id="triggered_dag",
        )
        finish = DummyOperator(
            task_id="finish"
        )


parallel_tasks = [
        parallel_1,
        parallel_2
]

parallel_tasks2 = [
        parallel_3,
        parallel_4
]


print_hello >> sleep >> print_world >> print_world_alt >> phase_1 >> parallel_tasks >> luck_task >> trigger >> parallel_tasks2 >> finish