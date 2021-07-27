#!/usr/bin/env python

from nntplib import NNTP
import time,datetime

"""
This 
Use your own news server or go to https://www.eternal-september.org/

INSTRUCTIONS

(1) Make an article.txt file:

	From: myemail@gmail.com (My Name)
	Newsgroups: alt.magick
	Subject: Post Topic
	Message-I.D.: <unique-string-1234@dont-email.me>
	Date: Monday, 26 Jul 2021 13:30:58 -0400 (EDT)

	Test.


(2) Install screen:
	
	sudo apt install screen

(3) Run the kill switch:

	sudo screen -S killswitch ./switch.py

	Input the date & time for the post

	Type: 'Ctrl + A' , then 'd'

	The kill switch now runs in the background

(4) To cancel the kill switch:
        
        To find the kill switch:
	sudo screen -ls

	Then attach to it with:
	screen -r killswitch

	Terminate the program:
	Ctrl+c

	Exit the screen:
	exit	

"""

print("\n[Time Of Future Post]\n")
print("Year: ", end="")
year = int(input())    

print("Month: ", end="")
month = int(input())    

print("Day: ", end="")
day = int(input())    

print("Hour: ", end="")
hour = int(input())    

print("Minute: ", end="")
minute = int(input())    

t = datetime.datetime.today()
future = datetime.datetime(year,month,day,hour,minute)

while(1):
	if t > future:
		s = NNTP('news.eternal-september.org')
		s.login(user='username', password='password', usenetrc=False)
		f = open('article.txt', 'rb')
		s.post(f)
		s.quit()
		quit()
	t = datetime.datetime.today()
