# Newsgroup Kill Switch
A dead man's switch that posts to newsgroups


Use your own usenet server or go to https://www.eternal-september.org/

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

	sudo screen -ls        (Find the kill switch)
	screen -r killswitch   (Opens the screen)	
	Ctrl+c                 (Closes the program)
	exit	               (Stops the screen)
