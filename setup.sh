#!/bin/sh

sudo apt-get install git -y
git clone https://github.com/qbalsdon/coursera_lib.git
cp coursera_lib/lib.py lib.py
sudo chmod +x lib.py
