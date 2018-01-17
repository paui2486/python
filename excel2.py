#!/usr/bin/env python
"""
Program:
This program will record log into Excel.
History:
20170707 Kuanlin Chen
"""
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
import logging
#匯入模組(Module)
import sys
import xlwt
import time

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

#def output(filename):
    #使用Worksheet裡的write函式將值寫入
  #  sheet1.write(0,0,'日期')
 #   sheet1.write(0,1,'總和')

   # book.save(filename)

if __name__ == '__main__':
    categories = ['育兒','健康','社會','教育','娛樂','汽車','美食','家居','旅遊','時尚','文化','其他','軍事','國際','職場','科技','科學','遊戲','體育','動漫','宗教','歷史']
    dayago = 7
    dayagos = "7"    

    categorieslen = len(categories); 
    for cat in range(0,categorieslen):
        body3 ={
    "size" : 0,
    "query": {
    "bool": {
      "must": [
      {"term": {"language": "zh-TW"}}      ,{"match": {"categories": categories[cat]}},
        {"range" :{"updated" : {
          "gt":"now-7d/d",
          "lt":"now"
        }}}
      ]

    }
  },
    "aggs" : {
        "articles_over_time" : {
            "date_histogram" : {
                "field" : "updated",
                "interval" : "day",
                "format" : "yyyy-MM-dd"
            }
        }
    }
}
        res = esCluster.search(index="articles", doc_type="article", body=body3)
        singlelen = (len(res["aggregations"]["articles_over_time"]["buckets"]));
        for num in range(0,singlelen):
            date = (res["aggregations"]["articles_over_time"]["buckets"][num]["key_as_string"])
            count = (res["aggregations"]["articles_over_time"]["buckets"][num]["doc_count"])
            print (date)
            print (count)
            if singlelen != 7:
                singlelen = 7
            else:
                singlelen = 7
            #sheet1.write((num+(cat*7)),0,categories[cat])#原本是七天 singlelen是單一分類長度 便動態
            sheet1.write((num+(cat*singlelen)),0,date)
            sheet1.write((num+(cat*singlelen)),1,categories[cat])
            sheet1.write((num+(cat*singlelen)),2,count)
            #filename = "/home/paul/seven days ago"+time.strftime("%Y-%m-%d", time.localtime())+".csv"
            filename = "/home/paul/example2.csv"
            output(filename)
