#!/usr/bin/env python3

from lib import *
from PIL import Image

save_path = "./supplier-data/images"

def process(file):
    name = file.decode('utf-8')
    if ".tiff" in name:
        im = Image.open(save_path +"/"+name)
        im = im.resize((600, 400))
        saveAsJpg(im, save_path+"/"+name.replace(".tiff",".jpeg"))

iterateFiles(save_path, process)
