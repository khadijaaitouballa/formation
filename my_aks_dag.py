from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor
from datetime import datetime, timedelta
from airflow.sdk.api.client import ApiClient

client = ApiClient(
    base_url="http://airflow-api-server:8080/execution/",
    username="myuser",
    password="Hps001002003*$*"
)

default_args = {
    "owner": "haitam",
    "retries": 1,
    "retry_delay": timedelta(minutes=3),
}

with DAG(
    dag_id="full_etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args
):

    # ----------------------------
    # 1. VALIDATION JOB
    # ----------------------------
    submit_validation = SparkKubernetesOperator(
        task_id="submit_validation",
        namespace="data-pipeline",
        application_file="/opt/airflow/deploy/validation_job.yaml",
    )

    monitor_validation = SparkKubernetesSensor(
        task_id="monitor_validation",
        namespace="data-pipeline",
        application_name="validationjob",
    )

    # ----------------------------
    # 2. NORMALIZATION JOB
    # ----------------------------
    submit_normalization = SparkKubernetesOperator(
        task_id="submit_normalization",
        namespace="data-pipeline",
        application_file="/opt/airflow/deploy/normalization_job.yaml",
    )

    monitor_normalization = SparkKubernetesSensor(
        task_id="monitor_normalization",
        namespace="data-pipeline",
        application_name="normalizationjob",
    )

    # ----------------------------
    # CHAINING
    # ----------------------------
    submit_validation >> monitor_validation >> submit_normalization >> monitor_normalization

# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime, timedelta

# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# with DAG(
#     dag_id='hello_aks_workflow',
#     default_args=default_args,
#     description='A simple DAG to run on AKS',
#     schedule=timedelta(days=1),
#     start_date=datetime(2025, 12, 1),
#     catchup=False,
# ) as dag:
    
#     def print_hello():
#         print("Hello from Airflow on AKS!")

#     hello_task = PythonOperator(
#         task_id='hello_task',
#         python_callable=print_hello,
#     )
