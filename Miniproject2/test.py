from tkinter import *

f = open("Tweets.txt", "a");  # edits file
tweet = tweet.replace("\n", "");
f.write(tweet);  # writest the file
text.delete(0.0, END)  # ereases text so it resets
f.close();  # end of line


root = Tk() #GUI   #log erbij if time premits

root.title("DisplayTweetsAndWeather")  # GUI NAME

#Labels
thelabel = Label(root, text="tweet")  #teskst

#frames
topFrame = Frame(root)
bottomFrame = Frame(root)

#buttons




#icons

#********** Status Bar *************

#packs
thelabel.pack()

topFrame.pack()
bottomFrame.pack(side=BOTTOM)

root.mainloop() #Main


