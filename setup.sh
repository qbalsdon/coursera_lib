#!/bin/sh

sudo apt-get install git -y
git clone https://github.com/qbalsdon/coursera_lib.git
cp coursera_lib/*.py .
sudo chmod +x lib.py



PEM="qwikLABS-L2517-31336330.pem"
USR="student-02-93bf73818937"
ADD="35.223.61.254"
scp -i ~/Downloads/${PEM} ${USR}@${ADD}:/home/${USR}/processed.pdf processed.pdf
