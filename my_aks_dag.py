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
    dag_id="my_aks_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
) as dag:

    # Line 25: Ensure there are exactly 4 spaces (or 1 tab) here
    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=my_function,
    )
