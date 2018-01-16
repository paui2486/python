from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
#上面這邊 引用套件
import logging
import sys
import xlwt
import string
sys.path.append('../')

from config.ESConfig import *
from config.LoggingConfig import *

#建立Workbook物件
book = xlwt.Workbook(encoding="utf-8")
#使用Workbook裡的add_sheet函式來建立Worksheet
sheet1 = book.add_sheet("Sheet1")

def main(orig_args):
    filename = "/home/paul/example.xls"
    output(filename)

def output(filename):
    #使用Worksheet裡的write函式將值寫入
    sheet1.write(0,0,'日期')
    sheet1.write(0,1,'資料筆數')
    #將Workbook儲存為原生Excel格式的檔案
    book.save(filename)

if __name__ == "__main__":
    
    body = {
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
}
res = esCluster.search(index="articles", doc_type="article", body=body)


#print (res["aggregations"]["articles_over_time"]["buckets"])
for num in range(0,7):
 print (res["aggregations"]["articles_over_time"]["buckets"][num]["key_as_string"])
 print (res["aggregations"]["articles_over_time"]["buckets"][num]["doc_count"])

#print("\n")
