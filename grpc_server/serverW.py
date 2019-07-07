# -*- coding: utf-8 -*-
import grpc
import time
from concurrent import futures
from W_pb2_grpc import add_gRPCServicer_to_server, gRPCServicer
from W_pb2 import ServerResponse
import pymongo
from datetime import datetime, timedelta
from models import Card

_HOST = 'localhost'
_PORT = '8188'

_ONE_HOUR_IN_SECONDS = 60 * 60
_KEEP_HOURS = 4

mongo_client = pymongo.MongoClient(host=_HOST, port=27017)
gpu_db = mongo_client.gpustat


class gRPCServicerImpl(gRPCServicer):
    def GetMessage(self, request, context):
        ip = context.peer().split(':')[1]
        time = datetime.utcnow()
        print("called from %s (%d cards)" % (ip, len(request.cards)))
        collection = gpu_db[ip]
        cards = [Card(card=c, ip=ip, time=time) for c in request.cards]
        collection.insert_many([c.to_json() for c in cards])
        return ServerResponse(success='%s, your GPU\' info is collected.' % request.cards[0].gpu_name)


def clean():
    print("Clean the data before %d hours" % _KEEP_HOURS)
    for collection in gpu_db.list_collection_names():
        if collection.startswith('10.141'):
            result = gpu_db[collection].delete_many({"time": {"$lt": datetime.utcnow() - timedelta(hours=_KEEP_HOURS)}})
            print(collection, result.deleted_count)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_gRPCServicer_to_server(gRPCServicerImpl(), server)
    server.add_insecure_port('[::]:' + _PORT)
    server.start()
    try:
        while True:
            clean()
            time.sleep(_ONE_HOUR_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
