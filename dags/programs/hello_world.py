from logging import raiseExceptions
from operator import mod
import time
import random
def print_world_script():
    print('hello world from another script')
    time.sleep(60)

def print_world_parallel_1():
    print('hello world from parallel script 1')
    time.sleep(60)
    return 'Task parallel 1'

def print_world_parallel_2(**kwargs):
    print('hello world from parallel script 2')
    time.sleep(60)
    kwargs['ti'].xcom_push(key='parallel2', value='Task parallel 2')

def print_world_parallel_3(**kwargs):
    print('hello world from parallel script 1')
    value = kwargs['ti']
    # wert_1 erhalten
    pull_value_1 = value.xcom_pull(key=None, task_ids='print_world_parallel_1')
    print(pull_value_1)
    time.sleep(60)

def print_world_parallel_4(**kwargs):
    print('hello world from parallel script 2')
    value = kwargs['ti']
    #without key
    pull_value_2 = value.xcom_pull(key = 'parallel2',task_ids='print_world_parallel_2')
    print(pull_value_2)
    time.sleep(60)


def luck (): 
    n = random.randint(0,22)
    print(n)
    if n % 2 == 0:
        raise ValueError('Sorry, bad luck')