from datetime import datetime
from airflow.models import DAG
from os.path import join
from plugins.operators.twitter_operator import TwitterOperator

with DAG(dag_id='twitter_dag', start_date=datetime.now()) as dag:
    twitter_operator = TwitterOperator(
            query = 'AluraOnline', 
            file_path=join(
                '/home/vegh/Desktop/Estudos/airflow-datapipeline/datalake',
                'twitter_aluraonline',
                'extract_date={{ ds }}',
                'AluraOnline_{{ ds_nodash }}.json'),
            task_id = 'test_run'
        )
    