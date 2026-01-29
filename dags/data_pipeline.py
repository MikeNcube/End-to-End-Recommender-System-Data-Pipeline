from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def process_data():
    """Example data processing function."""
    print("Processing data...")
    # Your data processing logic here
    return "Data processed successfully"

with DAG(
    'data_pipeline',
    default_args=default_args,
    description='A simple data pipeline',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['data', 'pipeline'],
) as dag:
    
    # Task 1: Start pipeline
    start = BashOperator(
        task_id='start_pipeline',
        bash_command='echo "Starting data pipeline..."',
    )
    
    # Task 2: Process data
    process = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
    )
    
    # Task 3: End pipeline
    end = BashOperator(
        task_id='end_pipeline',
        bash_command='echo "Pipeline completed!"',
    )
    
    # Define task dependencies
    start >> process >> end
