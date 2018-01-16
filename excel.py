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

sys.path.append('../')

from config.ESConfig import *
from config.LoggingConfig import *
#建立Workbook物件
book = xlwt.Workbook(encoding="utf-8")
#使用Workbook裡的add_sheet函式來建立Worksheet
sheet1 = book.add_sheet("Sheet1")

def main(orig_args):
    filename = "/home/paul/example.csv"
    output(filename)

def output(filename):
    #使用Worksheet裡的write函式將值寫入
    sheet1.write(0,0,'日期')
    sheet1.write(0,1,'比數')

    categories = ['育兒','健康','社會','教育','娛樂','汽車','美食','家居','旅遊','時尚','文化','其他','軍事','國際','職場','科技','科學','遊戲','體育']

    body =[{
    "size" : 0,
    "query": {
    "bool": {
      "must": [
      {"term": {"language": "zh-TW"}},
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
                "interval" : "day"
            }
        }
    }
},{
    "size" : 0,
    "query": {
    "bool": {
      "must": [
      {"term": {"language": "zh-TW"}}      ,{"match": {"categories": "科技"}},
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
                "interval" : "day"
            }
        }
    }
}]
    res = esCluster.search(index="articles", doc_type="article", body=body[0])
#print (res["aggregations"]["articles_over_time"]["buckets"])
    for out in range(0,1):
      for num in range(0,7):
       print (res["aggregations"]["articles_over_time"]["buckets"][num]["key_as_string"])
       print (res["aggregations"]["articles_over_time"]["buckets"][num]["doc_count"])
       date = (res["aggregations"]["articles_over_time"]["buckets"][num]["key_as_string"])
       count = (res["aggregations"]["articles_over_time"]["buckets"][num]["doc_count"])
       sheet1.write((num+1),0,date)
       sheet1.write((num+1),1,count)
    book.save(filename)
  
if __name__ == '__main__':
    main(sys.argv)

