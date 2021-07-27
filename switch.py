#!/usr/bin/env python
#
# MIT License
#
# Copyright (c) 2021 Corey White
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from nntplib import NNTP
import time,datetime

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
