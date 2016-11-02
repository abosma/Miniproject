#imports
from TwitterAPI import TwitterAPI
from tkinter import *
import time
import threading

api = TwitterAPI("qaDlX0kYOQ99OhOrFHDc9li07", "cLhI4Oe8D6grpDhns1udDaIxfp3SNMqECVOvHZU27mrFTR1to0", "791235928564039680-960nSheLDOtSIKiK7wwV0C7dsjQfTRb", "HZn6PJ8VyHNpuNzrx3xP4YyHJdcubqLwwqOAy8f4ji0H7")

tweetString = "Aan het wachten op een tweet...";
tweetStatusString = "Momenteel niks aan het doen...";
buttonState = "disabled";

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

def setButtonState(status):
    global buttonState;
    buttonState = status;

def logFiles():
    logfile = open("D:/GithubProjects/atillabosma/Miniproject/Miniproject2/Tweets.txt","r")
    loglines = follow(logfile)
    for line in loglines:
        while True:
            setButtonState("normal");
            setTweet(line);
            break;

def acceptTweet():
    if(tweetString == ""):
        return
    else:
        r = api.request('statuses/update', {'status':tweetString})
        print(r.status_code);
        setStatus("Tweet gepost op twitter: " + tweetString);
        setTweet("");
        setButtonState("disabled")

def rejectTweet():
    if(tweetString == ""):
        return
    else:
        logString = tweetString;
        f = open("Log.txt", "a");
        f.write(logString + " : " + time.strftime("%a %d %b %Y, %T \n"));
        f.close();
        setStatus("Tweet in de log gezet: " + logString);
        setTweet("");
        setButtonState("disabled")

def startGUI():
    root = Tk() #GUI   #log erbij if time premits

    root.title("Twitter Accept/Reject");
    root.minsize(width=400,height=150);
    root.maxsize(width=2000,height=150);

    #icons
    twitter =  PhotoImage(file="twitter.png")
    label = Label(root, image=twitter)

    #********** Status Bar *************
    tweetStatus = StringVar();
    tweetStatus.set(tweetStatusString);

    tweet = StringVar();
    tweet.set(tweetString);

    buttonStatus = StringVar();
    buttonStatus.set("disabled");

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
    button1 = Button(root,text="Accept", fg="green", command=lambda:acceptTweet())  #button Accept
    button2 = Button(root,text="Reject", fg="red", command=lambda:rejectTweet())  #button REject

    button1.config(state=buttonStatus.get());
    button2.config(state=buttonStatus.get());

    button1.pack(side=LEFT)
    button2.pack(side=RIGHT)

    def checkChanges():
        tweetStatus.set(tweetStatusString);

        tweet.set(tweetString);
        
        buttonStatus.set(buttonState);
        
        button1.config(state=buttonStatus.get());
        button2.config(state=buttonStatus.get());

        root.after(2000,checkChanges)
            
    root.after(2000,checkChanges)
    root.mainloop();

fileThread = threading.Thread(name='fileLogThread', target=logFiles)
guiThread = threading.Thread(name='guiStartThread', target=startGUI)

fileThread.start()
guiThread.start()



