from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# 1. Define the function the task will run
def print_hello():
    return "Hello from Airflow on AKS!"

# 2. Setup the DAG
with DAG(
    dag_id="my_aks_dag",
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["example"],
) as dag:

    # 3. Define the task (exactly 4 spaces in)
    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=print_hello,
    )

    hello_task
