#!/usr/bin/env python
# Copyright (c) 2021 Corey White

import nntplib
import string
import sys
import os
import time,datetime

t = datetime.datetime.today()
print("\n[Current Time]\n")
print(t)

print("\n[Time Of Future Post]\n")

print("Year: ")
year = int(input())    

print("Month: ")
month = int(input())    

print("Day: ")
day = int(input())    

print("Hour: ")
hour = int(input())    

print("Minute: ")
minute = int(input())    

future = datetime.datetime(year,month,day,hour,minute)

while(1):

  if future < t:

    server = nntplib.NNTP('news.eternal-september.org', user='name', password='password')
    f = open(sys.argv[1], 'rb')
    server.post(f)
    server.quit()

    if os.path.exists(sys.argv[1]):

      os.remove(sys.argv[1])

    quit()

  t = datetime.datetime.today()
