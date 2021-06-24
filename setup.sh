#!/bin/sh
sudo apt-get install git -y
git clone https://github.com/qbalsdon/coursera_lib.git
cp coursera_lib/*.py .
sudo chmod +x lib.py
sudo chmod +x changeImage.py
sudo chmod +x emails.py
sudo chmod +x report.py
sudo chmod +x run.py
sudo chmod +x ~/download_drive_file.sh
sudo chmod +x supplier_image_upload.py
./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
tar xf ~/supplier-data.tar.gz

./changeImage.py
./supplier_image_upload.py
sudo chmod +x example_upload.py
./example_upload.py
./run.py $1


PEM="qwikLABS-L2517-31336330.pem"
USR="student-02-93bf73818937"
ADD="35.223.61.254"
scp -i ~/Downloads/${PEM} ${USR}@${ADD}:/home/${USR}/processed.pdf processed.pdf


cd coursera_lib/ && git pull origin main; cd .. && cp coursera_lib/lib.py lib.py && sudo chmod +x lib.py
