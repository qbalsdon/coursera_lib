#!/usr/bin/env python3

import os
import requests
from PIL import Image

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import shutil
import psutil
import socket

def imageData(im):
    print(im.format, im.size, im.mode)

def resize(im, w, h):
    im2 = im.resize((w,h))

def saveAsJpg(im, name):
    result = im.convert("RGB")
    result.save(name, "JPEG")

def iterateFiles(dirStr, processFile, filecheck=None):
    directory = os.fsencode(dirStr)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filecheck == None:
            processFile(file)
        else:
            if filecheck(file):
                processFile(file)

def uploadImage(file, url):
    with open(file, "rb") as stream:
        result = requests.post(url, files={'file': stream})
        if (result.ok):
            print("  ~~ UPLOAD: Success ~~")
        else:
            print("  !! Error !!")
        stream.close()

def generate_report(filename, title, summary, data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    additional_info = ""
    for line in summary:
        additional_info = additional_info + line + "<br/>"
    report_info = Paragraph(additional_info, styles["BodyText"])

    report.build([report_title, empty_line, report_info])

 def generate_email(sender, receiver, subject, body = None, file = None):
     msg = EmailMessage()
     msg['Subject'] = subject
     msg['From'] = sender
     msg['To'] = receiver
     if body != None:
         msg.set_content(body)

     if file != None:
         msg.attach(MIMEText(message, "plain"))
            with open(file, "rb") as f:
                #attach = email.mime.application.MIMEApplication(f.read(),_subtype="pdf")
                attach = MIMEApplication(f.read(),_subtype="pdf")
            attach.add_header('Content-Disposition','attachment',filename=str(file))
            msg.attach(attach)

     # Send the message via our own SMTP server.
     server = smtplib.SMTP('localhost')
     server.send_message(msg)
     server.quit()

def send_error(username, error):
    generate_email("automation@example.com", username+"@example.com", error, "Please check your system and resolve the issue as soon as possible.")

def health_check(username):
    cpu = psutil.cpu_percent(60)
    if cpu >= 80:
        send_error(username, "Error - CPU usage is over 80%")

    stat = shutil.disk_usage(".")
    if stat.free / stat.total <= 0.2:
        send_error(username, "Error - Available disk space is less than 20%")

    mem = psutil.virtual_memory()
    if available < 500000000:
        send_error(username, "Error - Available memory is less than 500MB")

    name = socket.gethostbyname('localhost')
    if name != "127.0.0.1":
        send_error(username, "Error - localhost cannot be resolved to 127.0.0.1")
