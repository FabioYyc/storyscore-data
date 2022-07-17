import datetime
from google.cloud import bigquery
import pandas as pd
PROJECT='storyscore-356114'

def get_table_id(dataset_name, table_name):
    return ('.').join([PROJECT, dataset_name, table_name]);

def get_table_ref(client: bigquery.Client, dataset_id, table_id):
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    return table_ref

def get_gbp_table_id(dataset_name, table_name):
    return ('.').join([dataset_name, table_name]);

def create_load_job_config(job_type='WRITE_TRUNCATE'):
    return bigquery.LoadJobConfig(
    write_disposition=job_type,
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    autodetect=True
    )

def upload_json(filename: str, dataset_id: str, table_id: str, config):
    print('uploading table: %s'%(table_id))
    client = bigquery.Client(project=PROJECT)
    table_ref = get_table_ref(client, dataset_id, table_id)
    print(table_ref)
    with open(filename, "rb") as source_file:
        job = client.load_table_from_file(
            source_file, table_ref, job_config=config
        )  # Make an API request.
        job.result()  # Wait for the job to complete.;
    table = client.get_table(table_ref)  # Make an API request.
    print(
        "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(table.schema), table_id
        )
    )
