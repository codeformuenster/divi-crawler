import copy

import pymongo

USER_NAME = "root"
PASSWORD = "challenge1757"


def _getConnection():
    return pymongo.MongoClient(
        "mongodb://" + USER_NAME + ":" + PASSWORD + "@bene.gridpiloten.de:27017/"
    )


def _getRawDB():
    return _getConnection()["raw"]


def _insertMeta(meta):
    return _getRawDB()["medical_resorce_meta"].insert(meta)


def insertData(dataList, meta):
    # make deep copy, in order to avoid mutation of original data
    dataList = copy.deepcopy(dataList)
    meta = copy.deepcopy(meta)
    # upload to database
    meta = _insertMeta(meta)
    for data in dataList:
        data["meta_info"] = meta
        _getRawDB()["medical_resorce"].insert(data)
