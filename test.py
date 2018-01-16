# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
#上面這邊 引用套件
import logging
import sys
sys.path.append('../')

from config.ESConfig import * 
from config.LoggingConfig import *

if __name__ == "__main__":

    s = Search(using=esCluster, index='articles', doc_type='article') \
        .query(Q('bool', must=[Q('exists', field='title')])) \
        .sort('-updated') \
        .extra(from_=0, size=10)
    
    response = s.execute()

    #for hit in s.scan():
    for hit in response:
        logging.info(hit)

# vim: expandtab softtabstop=4 tabstop=4 shiftwidth=4 ts=4 sw=4
# s = Search(using=esCluster, index='articles', doc_type='article') \
# 這行是選擇哪個index and type
