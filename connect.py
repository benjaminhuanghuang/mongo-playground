from pymongo import MongoClient

SOURCE_SERVER = "localhost"

TARGET_SERVER = "mongoServer"
TARGET_USER_NAME = "abc"
TARGET_PASSWORD = "abc123"

DB_NAME = "TargeDB"

CONN_STR = 'mongodb://{}//TargetDB'
CONN_STR_AUTH = 'mongodb://{}:{}@{}/TargetDB?authMechanism=SCRAM-SHA-1'



def connect_server_auth(address, user_name, password):
    try:
        if user_name and password:
            conn_str = CONN_STR_AUTH.format(user_name, password, address)
        else:
            conn_str = CONN_STR.format(address)
        conn = MongoClient(conn_str)
        return conn

    except Exception as e:
        print("Connect to server {} failed with error {}".format(address, e.message))


def connect_server(address):
    try:
        conn_str = CONN_STR.format(address)
        conn = MongoClient(conn_str)
        return conn
    except Exception as e:
        print("Connect to server {} failed with error {}".format(address, e.message))