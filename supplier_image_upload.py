#!/usr/bin/env python3

from lib import *

save_path = "./supplier-data/images"
url="http://localhost/upload/"
def process(file):
    name = save_path+"/"+file.decode('utf-8')
    if ".jpeg" in name:
        print("uploading: " + name)
        uploadImage(name, url)

iterateFiles(save_path, process)
