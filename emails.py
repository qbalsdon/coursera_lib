#!/usr/bin/env python3

from lib import *

user = os.environ['USER']
generate_email("automation@example.com", user+"@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "./processed.pdf")
