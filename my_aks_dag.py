# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime

# # 1. Define the function the task will run
# def print_hello():
#     return "Hello from Airflow on AKS!"

# # 2. Setup the DAG
# with DAG(
#     dag_id="my_aks_dag",
#     start_date=datetime(2026, 1, 1),
#     schedule=None,
#     catchup=False,
#     tags=["example"],
# ) as dag:

#     # 3. Define the task (exactly 4 spaces in)
#     hello_task = PythonOperator(
#         task_id="hello_task",
#         python_callable=print_hello,
#     )

#     hello_task

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from datetime import datetime

with DAG(
    dag_id="aks_pod_operator_test",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    # This task launches a real Kubernetes Pod in your cluster
    run_container_task = KubernetesPodOperator(
        task_id="run_aks_container",
        name="hello-from-aks",
        namespace="airflow",  # Ensure this matches your Airflow namespace
        image="busybox",       # A tiny image to test with
        cmds=["sh", "-c", "echo 'Hello from a separate AKS Pod!' && sleep 10"],
        is_delete_operator_pod=True, # Automatically clean up the pod after it finishes
        get_logs=True,               # Stream the pod logs back to the Airflow UI
    )
