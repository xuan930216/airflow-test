# the DAG object, we will use it to initialize a DAG
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta
#we have chice to pass arguments to each task, also can define a default params
#dictionary tehn we can use when define task
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 12, 11),
    'email': ['xuzhang@luxola.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)

}

dag = DAG('tutorial', default_args=default_args, schedule_interval=timedelta(days=1))

t1 = BashOperator(task_id='print_date', bash_command='date', dag=dag)
t2 = BashOperator(task_id='sleep', bash_command='sleep 5', dag=dag)

t1 >> t2