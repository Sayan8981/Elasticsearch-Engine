# Import elasticsearch module
from elasticsearch import Elasticsearch 
#import json


# Method to store data in elasticsearch
def send_data_to_es(data):
 es=Elasticsearch(['http://localhost:9200/'])
 res = es.index(index='employee', document=data)
 print(res)

# Method to get data from elasticsearch
def get_data_from_es():
 es=Elasticsearch(['http://localhost:9200/'], http_auth=('elastic', 'Don9891das@'))
 r = es.search(index="employee", body={"query": {"match": {'Name':'ana'}}})
 print(r)
 print(type(r))
 print(r["hits"]["hits"][0]["_source"])

# Main function from where the execution starts
if __name__== "__main__":
 # Define a dictoinary having required data to be stored in ES
 data = {"Name": "Ana", "Age":78, "address": "England"}
 # Call method to store data in ES
 #send_data_to_es(data)
 # Call method to get data from ES
 get_data_from_es()