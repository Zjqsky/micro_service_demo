# -*- coding: UTF-8 -*-
from peewee import *
from utils.consul import consul_client
from utils.logger import logger
from settings import COMMON_MYSQL
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin


class RetryMySQLDatabase(ReconnectMixin, PooledMySQLDatabase):
    _instance = None

    @staticmethod
    def get_db_instance(consul_name="", database_name="", user="", password=""):
        if not RetryMySQLDatabase._instance:
            service, addr = consul_client.get_service(consul_name)
            if service is None:
                logger.logger.error("get mysql server failed")
                return None

            RetryMySQLDatabase._instance = RetryMySQLDatabase(
                database_name,
                max_connections=20,
                stale_timeout=300,
                host=service['Address'],
                user=user,
                password=password,
                port=service['Port']
            )
        return RetryMySQLDatabase._instance


COMMON_DB = RetryMySQLDatabase.get_db_instance(**COMMON_MYSQL)
