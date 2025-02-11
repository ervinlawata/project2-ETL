import connection
import etl

if __name__ == '__main__':
    file = "/retail_sales_datasets.csv"
    conn_name = "retail_sales"
    # Connection to database
    conf = connection.config(conn_name)
    conn = connection.get_conn(conf,conn_name)

    # Extract
    df = etl.extract(file)

    # Transform (Drop Nulls,Data Type casting,Drop Duplicate)
    df_transform = etl.transform(df)

    # Load data to database
    etl.load(df_transform,conn)