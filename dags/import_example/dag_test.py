from datetime import datetime, timedelta

# Es necesario hacerlo relativo al nombre de la carpeta y tener el __init__.py
from import_example.utils import extract_dolar_price

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.python import PythonOperator

from airflow.models import Variable

configuration = Variable.get("url")


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
    'dag_Variable_and_utils',  #El nombre que se va a ver en la UI
    default_args=default_args, # Estos argumentos se van a pasar a cada Operator
    description='Un DAG tutorial mostrando cómo importar',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False, # Importante ya que va a intentar schedulear desde el 2021
    # hasta llegar al 2022 cada un día 
    tags=['webeasysearch'],
) as dag:

    t1 = PythonOperator(
        task_id="extract_dolar_price",
        python_callable=extract_dolar_price,
        # La key del diccionario debe ser igual que el argumento de la función
        # El orden importa. Si la función toma primero el url entonces darlo como primera key:value
        op_kwargs={"url": configuration},
        )

    t1
