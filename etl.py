import polars as pl
import requests
import connection
import os
import pandas

def extract(dataset: str):
    path = os.getcwd()
    df = pl.read_csv(path+dataset)
    return df

def transform(data_frame):
    df_transform = data_frame.drop_nulls()
    df_transform = df_transform.unique(maintain_order=True)
    df_transform = df_transform.with_columns(pl.col("Date").cast(pl.Date))

    return df_transform

def load(data_frame,engine):
    try:
        data_frame.write_database(
            table_name="retail_sales",
            connection=engine,
            if_table_exists = 'replace'

        )
        print("[INFO] Load Data to database Success...!")
    except Exception as e:
        print("[INFO] Load Data to database Not Success...!")
        print(str(e))






