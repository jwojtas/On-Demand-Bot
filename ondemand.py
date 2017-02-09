#Imports
import praw
import getpass
import time
import random
import sys
import prawconfig
from twilio.rest import TwilioRestClient
#Imports

#creates the reddit instance
reddit = praw.Reddit(client_id=prawconfig.client_id, client_secret=prawconfig.client_secret, password= prawconfig.password,
 user_agent=prawconfig.user_agent, username=prawconfig.username)

 #Lists the available functions
def flist():
	print("Available functions: (Q to quit)\n")

	print("login\n")
	
	print("top25\n")

	print("Hot\n")	

	print("new\n")

	print("random\n")
	
#shows the currently logged in user
def login():
	print("Current user:") ;print(reddit.user.me())
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print(".")
	time.sleep(1)
	print("\n")
	main()
	
#shows and allows you to select from given functions
def main():
	flist()
	n=input("Enter a function:")
	if n== "login" or n=="Login" or n=="LOGIN": #Runs login
		login()
	elif n=="top25" or n=="Top25" or n=="TOP25": # Runs top25
		top25()
	elif n== "hot" or n=="Hot" or n=="HOT": #runs hot
		hot()
	elif n=="new" or n=="New" or n=="NEW": #Runs new
		new()
	elif n== "random" or n == "Random" or n=="RANDOM" or n=="ran" or n=="RAN" or n=="Ran":
		num = random.randint(1,3)
		ran(num)
	elif n =="q" or n=="Q":
		sys.exit()
	else:
		print("Not a valid function")
		main()
		
#Gets top25 posts of the day from a given subreddit	
def top25():
	fil = open("links.txt", 'w')
	sr = input('Enter Subreddit:')
	topreddit = reddit.subreddit(sr)
	fil.write("*TOP25*"); fil.write("\n")
	fil.write(topreddit.display_name); fil.write("\n")
	for submission in topreddit.top('day', limit=25):
		fil.write(submission.url)
		fil.write("\n")
	fil.write("*TOP25*")
	fil.close()
	mail()
	a =input("(Q) quit or back to menu?(any other key)")
	if a=='q' or a=="Q":
		sys.exit()
	else:
		main()

#Gets hot posts of a given subreddit( limited to 25)	
def hot():
	fil = open("links.txt", 'w')
	sr = input('Enter Subreddit:')
	hotreddit = reddit.subreddit(sr)
	fil.write("*HOT*") ; fil.write("\n")
	fil.write(hotreddit.display_name) ; fil.write("\n")
	for submission in hotreddit.top(limit=25):
		fil.write(submission.url)
		fil.write("\n")
	fil.write("*HOT*")
	fil.close()
	mail()
	a =input("(Q) quit or back to menu?(any other key)")
	if a=='q' or a=="Q":
		sys.exit()
	else:
		main()
		
#Gets new posts of a given subreddit(Limited to 25)
def new():
	fil = open("links.txt", 'w')
	sr = input('Enter Subreddit:')
	newreddit = reddit.subreddit(sr)
	fil.write("*NEW*") ; fil.write("\n")
	fil.write(newreddit.display_name) ; fil.write("\n")
	for submission in newreddit.top(limit=25):
		fil.write(submission.url)
		fil.write("\n")
	fil.write("*NEW*")
	fil.close()
	mail()
	a =input("(Q) quit or back to menu?(any other key)")
	if a=='q' or a=="Q":
		sys.exit()
	else:
		main()
		
# Gets either top 25, hot, or new posts from a random subreddit	
def ran(z):
	fil = open("links.txt","w")
	ranreddit = reddit.subreddit("random")
	if z== 1:
		fil.write("*TOP25*")
		fil.write(topreddit.display_name) ; fil.write("\n")
		for submission in topreddit.top('day', limit=25):
			fil.write(submission.url)
			fil.write("\n")
		fil.write("*TOP25*")
		fil.close()
		mail()
		a =input("(Q) quit or back to menu?(any other key)")
		if a=='q' or a=="Q":
			sys.exit()
		else:
			main()
	
	elif z==2:
		fil.write("*HOT*") ; fil.write("\n")
		fil.write(hotreddit.display_name) ; fil.write("\n")
		for submission in hotreddit.top(limit=25):
			fil.write(submission.url)
			fil.write("\n")
		fil.write("*HOT*")
		fil.close()
		mail()
		a =input("(Q) quit or back to menu?(any other key)")
		if a=='q' or a=="Q":
			sys.exit()
		else:
			main()
	
	elif z==3:
		fil.write("*NEW*") ; fil.write("\n")
		fil.write(newreddit.display_name) ; fil.write("\n")
		for submission in newreddit.top(limit=25):
			fil.write(submission.url)
			fil.write("\n")
		fil.write("*NEW*")
		fil.close()
		mail()
		a =input("(Q) quit or back to menu?(any other key)")
		if a=='q' or a=="Q":
			sys.exit()
		else:
			main()
		
	else:
		print("Not valid")
		a =input("(Q) quit or back to menu?(any other key)")
		if a=='q' or a=="Q":
			sys.exit()
		else:
			main()	

#sends the links in  a PM to the specified user.	
def mail():
	e =input("Press enter to send as Reddit PM or any other key + enter for  a text")
	if e== "":
		f =open("links.txt", "r")
		fs = f.read()
		reddit.redditor(prawconfig.receiver).message('List',fs)
		f.close()
	else:
		text()
	

#Sends me a text message with the links
def text():
	fa = open("links.txt", "r")
	fb= fa.read()
	twilioclient = TwilioRestClient(prawconfig.accountSID, prawconfig.authToken)
	message = twilioclient.messages.create(body=fb, from_=prawconfig.myTwilioNumber, to=prawconfig.myCellPhone)

	#_____________________________CREATE__FUNCTIONS__ABOVE__RUN__MAIN__BELOW_____________________________________________
main()