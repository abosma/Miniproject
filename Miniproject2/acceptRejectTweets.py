#imports
from TwitterAPI import TwitterAPI
from tkinter import *
import time
import threading

api = TwitterAPI("qaDlX0kYOQ99OhOrFHDc9li07", "cLhI4Oe8D6grpDhns1udDaIxfp3SNMqECVOvHZU27mrFTR1to0", "791235928564039680-960nSheLDOtSIKiK7wwV0C7dsjQfTRb", "HZn6PJ8VyHNpuNzrx3xP4YyHJdcubqLwwqOAy8f4ji0H7")

tweetString = "Aan het wachten op een tweet...";
tweetStatusString = "Momenteel niks aan het doen...";

def follow(file):
    file.seek(0,2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def setTweet(line):
    global tweetString;
    tweetString = line;

def setStatus(status):
    global tweetStatusString;
    tweetStatusString = status;

def logFiles():
    logfile = open("D:/GithubProjects/atillabosma/Miniproject/Miniproject2/Tweets.txt","r")
    loglines = follow(logfile)
    for line in loglines:
        while True:
            setTweet(line);
            break;

def acceptTweet():
    r = api.request('statuses/update', {'status':tweetString})
    print(r.status_code);
    setStatus("Tweet gepost op twitter.");

def rejectTweet():
    logString = tweetString;
    logString = logString.replace("\n", "");
    f = open("Log.txt", "a");
    f.write(logString + " : " + time.strftime("%a %d %b %Y, %T \n"));
    f.close();
    setStatus("Tweet in de log gezet.");

def startGUI():
    root = Tk() #GUI   #log erbij if time premits

    #icons
    twitter =  PhotoImage(file="twitter.png")
    label = Label(root, image=twitter)

    #********** Status Bar *************
    tweetStatus = StringVar();
    tweetStatus.set(tweetStatusString);

    tweet = StringVar();
    tweet.set(tweetString);

    status = Label(root, textvariable=tweetStatus,bd=1, relief=SUNKEN, anchor=W)

    topFrame = Frame(root)
    bottomFrame = Frame(root)

    #packs
    topFrame.pack()
    bottomFrame.pack(side=BOTTOM)
    status.pack(side=BOTTOM, fill=X)

    thelabel = Label(root, textvariable=tweet)
    thelabel.pack()

    #buttons
    button1 = Button(text="Accept", fg="green", command=lambda:acceptTweet())  #button Accept
    button2 = Button(text="Reject", fg="red", command=lambda:rejectTweet())  #button REject

    button1.pack()
    button2.pack()

    def checkChanges():
        tweetStatus.set(tweetStatusString);
        tweet.set(tweetString);
        root.after(2000,checkChanges)
            
    root.after(2000,checkChanges)
    root.mainloop();

fileThread = threading.Thread(name='fileLogThread', target=logFiles)
guiThread = threading.Thread(name='guiStartThread', target=startGUI)

fileThread.start()
guiThread.start()



