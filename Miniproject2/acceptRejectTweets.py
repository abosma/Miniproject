#imports
from TwitterAPI import TwitterAPI
import time
from tkinter import *

root = Tk() #GUI   #log erbij if time premits

api = TwitterAPI("qaDlX0kYOQ99OhOrFHDc9li07", "cLhI4Oe8D6grpDhns1udDaIxfp3SNMqECVOvHZU27mrFTR1to0", "791235928564039680-960nSheLDOtSIKiK7wwV0C7dsjQfTRb", "HZn6PJ8VyHNpuNzrx3xP4YyHJdcubqLwwqOAy8f4ji0H7")

global tweetStatus;

tweetStatus = "Not doing anything..."

def follow(file):
    file.seek(0,2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def acceptTweet(lineTweet):
    r = api.request('statuses/update', {'status':lineTweet})
    tweetStatus = "Tweet gepost: " + lineTweet;

def rejectTweet(lineTweet):
    lineTweet = lineTweet.replace("\n", "");
    f = open("Log.txt", "a");
    f.write(lineTweet + " : " + time.strftime("%a %d %b %Y, %T \n"));
    f.close();
    tweetStatus = "Tweet opgeslagen in de log";


if __name__ == '__main__':
    logfile = open("C:/Users/User/Documents/Visual Studio 2015/Projects/Miniproject2/Miniproject2/Tweets.txt","r")
    loglines = follow(logfile)
    for line in loglines:
        while True:
            thelabel = Label(root, text=line)
            topFrame = Frame(root)
            bottomFrame = Frame(root)

            #buttons
            button1 = Button(text="Accept", fg="green", command=acceptTweet(line))  #button Accept
            button2 = Button(text="Reject", fg="red", command=rejectTweet(line))  #button REject

            #icons
            twitter =  PhotoImage(file="twitter.png")
            label = Label(root, image=twitter)

            #********** Status Bar *************

            status = Label(root, text=tweetStatus,bd=1, relief=SUNKEN, anchor=W)

            #packs
            thelabel.pack()
            topFrame.pack()
            bottomFrame.pack(side=BOTTOM)
            status.pack(side=BOTTOM, fill=X)
            button1.pack(side=LEFT)
            button2.pack(side=LEFT)

            root.mainloop() #Main



