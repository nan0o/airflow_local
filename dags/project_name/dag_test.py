import json
import requests
from datetime import datetime, timedelta

import os

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

my_dir = os.path.dirname(os.path.abspath(__file__))
configuration_file_path = os.path.join(my_dir, "test.json")
with open(configuration_file_path) as json_file:
    configuration = json.load(json_file)

default_args= {
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    }

with DAG(
    'dag_name',  #El nombre que se va a ver en la UI
    default_args=default_args, # Estos argumentos se van a pasar a cada Operator
    description='Un DAG tutorial',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False, # Importante ya que va a intentar schedulear desde el 2021
    # hasta llegar al 2022 cada un día 
    tags=['webeasysearch'],
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    def extract_dolar_price(url):
        json_response = requests.get(url[0]).json()
        for index, type in enumerate(('Oficial','Blue')):
            buy = json_response[index]['casa']['compra'][:-1]
            sell = json_response[index]['casa']['venta'][:-1]
            return f"{type} | {buy} | {sell}"

    t3 = PythonOperator(
        python_callable=extract_dolar_price,
        op_args=configuration["url"]
    )

    t1 >> [t2, t3]
