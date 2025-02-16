from sqlalchemy import create_engine
import json
import psycopg2
import os


def config(conn_name):
    path = os.getcwd()
    with open(path+'/config.json') as file:
        conf = json.load(file)[conn_name]
    return conf

def get_conn(conf,conn_name):
    try:
        engine = create_engine(f"postgresql+psycopg2://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['db']}")
        print("[INFO] Connection Success...")
        return engine
    except Exception as e:
        print(f"[INFO] can't success connect to postgres {conn_name}")
        print(str(e))
