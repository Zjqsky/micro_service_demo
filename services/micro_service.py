# -*- coding: UTF-8 -*-

from protos import micro_service_pb2, micro_service_pb2_grpc, base_pb2, base_pb2_grpc
from services.base_service import rpc_client_wrap, init_client


class MicroService:
    def __init__(self):
        self.service_conf = dict(
            name='micro_service',
            # addr='127.0.0.1:31019',
        )
        self.service_client = init_client(self)

    def get_client(self, conn):
        return micro_service_pb2_grpc.MicroServiceStub(channel=conn)

    @rpc_client_wrap
    def do_micro(self, text, *args, **kwargs):
        req = micro_service_pb2.DoMicroReq()
        req.text = text

        return self.service_client.DoMicro(req)


micro_service_client = MicroService()
