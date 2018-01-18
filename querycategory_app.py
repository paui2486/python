# -*- coding: utf-8 -*-
# 待修這邊會有一篇文章兩種屬性
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
#上面這邊 引用套件
import logging
import xlwt
import time
import sys

sys.path.append('../')

from config.ESConfig import *
from config.LoggingConfig import *
#建立Workbook物件
book = xlwt.Workbook(encoding="utf-8")
#使用Workbook裡的add_sheet函式來建立Worksheet
sheet1 = book.add_sheet("Sheet1")

def output(filename):
    #使用Worksheet裡的write函式將值寫入

    book.save(filename)

if __name__ == "__main__":

    s = Search(using=esCluster, index='fiiser', doc_type='app') \
     .query()
   
    categories = {} 
    
    response = s.execute()
    for hit in s.scan():
        logging.info(hit.categories)
        if categories.get(hit.categories) == None:
            categories[hit.categories] = 0
        elif categories.get(hit.categories) != None:
            categories[hit.categories] = categories[hit.categories] + 1 
    
    print (categories)
    print (len(categories))
    #for i in range(0,(len(categories))):
    #    print (categories)
    sheet1.write(0,0,str(categories))
    filename = "/home/paul/querycategory_app.csv"
    output(filename)
