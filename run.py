#! /usr/bin/env python3

from lib import *

import os
import requests
import json
import sys

source_dir = "./supplier-data/descriptions/"

def convertJson(source, name):
    result={}
    with open(source) as f:
        content = f.read().splitlines()
        result["name"] = content[0]
        result["weight"] = int(content[1].replace("lbs", ""))
        result["description"] = content[2]
        result["image_name"] = name
        f.close()
    return json.dumps(result)

def upload(payload):
    url = "http://"+sys.argv[1]+"/fruits/"
    result = requests.post(url, json = payload)
    if (result.ok):
        print("  ~~ UPLOAD: Success ~~")
    else:
        print("  !! Error !!")
        print(result)
        print(result.reason)
        print(payload)
        print(result.text)

def process(file):
    name = file.decode('utf-8')
    if ".txt" in name:
        print(name)
        payload = convertJson(source_dir+name, name.replace(".txt", ".jpeg"))
        upload(payload)

iterateFiles(source_dir, process)
