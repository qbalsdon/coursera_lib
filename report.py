#!/usr/bin/env python3

from lib import *

source_dir = "./supplier-data/descriptions/"
result = {}
def process(file):
    global result
    name = file.decode('utf-8')
    if ".txt" in name:
        print(name)
        src = source_dir+name
        with open(src) as f:
            content = f.read().splitlines()
            f.close()
        result[content[0]] = content[1]

def churn(data):
    response=[]
    for key in sorted(data.keys()):
        response = response + ["<br/>", "name: "+key, "weight:" + data[key]]
    return response

iterateFiles(source_dir, process)
#print(result)
#print(churn(result))

generate_report("processed.pdf",churn(result))
