# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
#上面這邊 引用套件
import logging
import xlwt
import time
import sys
from collections import Counter
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

    categories = {}
    cars = ['Volvo','BMW','Toyota','audi','audi']
    #cars = ['Volvo','BMW','Toyota','audi','subre']
    #int i = 0 
    #for i in range(0,len(cars))
    for hit in cars:
        logging.info(hit)
        if categories.get(hit) == None:
            categories[hit] = 0
        elif categories.get(hit) != None:
            categories[hit] = categories[hit] + 1
    
    print (categories)
    #sheet1.write(0,0,categories)
    #filename = "/home/paul/testdict.csv"
    #output(filename)
