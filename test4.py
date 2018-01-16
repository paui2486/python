import logging
import sys
import csv
sys.path.append('../')

from config.ESConfig import *
from config.LoggingConfig import *

if __name__ == "__main__":

    body = {
    "size" : 0,
    "query": {
    "bool": {
      "must": [
      {"term": {"language": "zh-TW"}},
      {"match": {"categories": "健康"}},
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
urls = []
for buckets in res['aggregations']['articles_over_time']['buckets']:
 key_as_string = buckets['key_as_string']
 doc_count = buckets['doc_count']
 urls.append(res)
 """return urls"""

print(res)
