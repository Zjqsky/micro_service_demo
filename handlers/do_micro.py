#! /usr/bin/env python
# -*- coding: utf-8 -*-

from models import area
from handlers.base_handler import rpc_server_wrap
from utils.mysql import COMMON_DB
from protos import micro_service_pb2
import json


@rpc_server_wrap
def do_micro(request, response):
    text = request.text
    
    if text == 'micro_req':
        response.data.text = 'micro_resp'
        response.data.m[110] = 'ret'
        for str_val in ['micro', 'resp']:
            str_ret = response.data.strs.add()
            str_ret.str = str_val
        response.data.status = micro_service_pb2.Data.NORMAL

    with COMMON_DB.connection_context():
        area_list = area.Area.select().dicts()
        for area_data in area_list:
            print(area_data)
    pass
