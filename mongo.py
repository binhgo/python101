import pymongo
from pymongo import MongoClient

client = MongoClient('35.247.143.204',
                     username='nhanh',
                     password='qH5QX7q6cMtCGa7bnBeo',
                     authSource='admin',
                     authMechanism='SCRAM-SHA-1')


def cLog():
    db = client["nhanh_stg_core_order"]
    col = db["logs"]
    return col


def cOrder():
    db = client["nhanh_stg_core_order"]
    col = db["core_order"]
    return col


def connectMgo():
    client = MongoClient('35.247.143.204',
                         username='nhanh',
                         password='qH5QX7q6cMtCGa7bnBeo',
                         authSource='admin',
                         authMechanism='SCRAM-SHA-1')

    db = client["test"]
    col = db["test_b"]

    mydict = {"name": "John", "address": "Highway 8888"}
    rs = col.insert_one(mydict)
    print(rs.inserted_id)

    filter = {"_id": rs.inserted_id}
    data = col.find_one(filter)
    print(data)


if __name__ == '__main__':
    connectMgo()
