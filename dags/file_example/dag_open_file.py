import json
import requests
from datetime import datetime, timedelta

import os

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# Guardo en my_dir el path absoluto hasta el directorio donde se encuentra el dag
my_dir = os.path.dirname(os.path.abspath(__file__))
# Sumo al path previo el nombre del archivo para abrirlo
configuration_file_path = os.path.join(my_dir, "test.json")
# Al tener el path apuntando al archivo, lo puedo abrir con with open
with open(configuration_file_path) as json_file:
    configuration = json.load(json_file)

print(configuration)


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
    'dag_tutorial',  #El nombre que se va a ver en la UI
    default_args=default_args, # Estos argumentos se van a pasar a cada Operator
    description='Un DAG tutorial',
    schedule_interval='10 * * * *',
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

    def extract_dolar(url, **context):
        print(url)
        print(context)
        json_response = requests.get(url).json()
        for index, type in enumerate(('Oficial','Blue')):
            buyer = json_response[index]['casa']['compra'][:-1]
            seller = json_response[index]['casa']['venta'][:-1]
            print(f"{type} | {buyer} | {seller}")
        return

    t3 = PythonOperator(
        task_id="extract_dolar_price",
        python_callable=extract_dolar,
        op_kwargs=configuration,
        )

    t1 >> [t2, t3]
