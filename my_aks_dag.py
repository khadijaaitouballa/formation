from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='hello_aks_workflow',
    default_args=default_args,
    description='A simple DAG to run on AKS',
    schedule=timedelta(days=1),
    start_date=datetime(2025, 12, 1),
    catchup=False,
) as dag:
    
    def print_hello():
        print("Hello from Airflow on AKS!")

    hello_task = PythonOperator(
        task_id='hello_task',
        python_callable=print_hello,
    )
