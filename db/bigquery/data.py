import datetime
from google.cloud import bigquery
import pandas as pd
PROJECT='storyscore-356114'

def get_table_id(dataset_name, table_name):
    return ('.').join([PROJECT, dataset_name, table_name]);

def create_load_job_config(schema, job_type='WRITE_APPEND'):
    return bigquery.LoadJobConfig(
    # Specify a (partial) schema. All columns are always written to the
    # table. The schema is used to assist in data type definitions.
    schema=schema,
    # Optionally, set the write disposition. BigQuery appends loaded rows
    # to an existing table by default, but with WRITE_TRUNCATE write
    # disposition it replaces the table with the loaded data.
    write_disposition="WRITE_TRUNCATE"
)

def upload_dataframe(dataframe: pd.DataFrame, table_id: str, config):
    client = bigquery.Client()
    job = client.load_table_from_dataframe(
        dataframe, table_id, job_config=config
    )  # Make an API request.
    job.result()  # Wait for the job to complete.;
