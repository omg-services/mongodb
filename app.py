# -*- coding: utf-8 -*-
import json
import os

from bson import ObjectId
from pymongo import MongoClient

from flask import Flask, make_response, request


class ObjectIdEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)

        return super().encode(o)


class Handler:
    app = Flask(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.mongo = MongoClient(os.getenv('MONGODB_URI',
                                           'mongodb://localhost:27017/'))

    def find_many(self):
        return self.find()

    def find_one(self):
        return self.find(one=True)

    def find(self, one: bool = False):
        req = request.get_json()
        db = req['db']
        coll = req['coll']
        query = req['query']
        sort = req.get('sort')
        fields = req.get('fields', {})

        kwargs = {}

        if sort:
            kwargs['sort'] = sort

        if fields:
            kwargs['projection'] = fields

        if one:
            res = self.mongo[db][coll].find_one(query, **kwargs)
            return self.end(res)

        cur = self.mongo[db][coll].find(query, **kwargs)
        records = []
        for doc in cur:
            records.append(doc)

        return self.end(records)

    def insert(self):
        req = request.get_json()
        db = req['db']
        coll = req['coll']
        doc = req['doc']

        return self.end({
            '_id': str(self.mongo[db][coll].insert_one(doc).inserted_id)
        })

    @staticmethod
    def end(res):
        resp = make_response(json.dumps(res, cls=ObjectIdEncoder))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp


if __name__ == '__main__':
    handler = Handler()
    handler.app.add_url_rule('/find', 'find', handler.find,
                             methods=['post'])
    handler.app.add_url_rule('/findOne', 'findOne', handler.find_one,
                             methods=['post'])
    handler.app.add_url_rule('/insert', 'insert',
                             handler.insert, methods=['post'])
    handler.app.run(host='0.0.0.0', port=8000)
