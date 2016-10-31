from tkinter import *
from tkinter import messagebox
root = Tk()
filename = None

def Tweet():
    global filename
    tweet =  text.get(0.0, END)    # read tweet
    if (len(tweet) > 140): # check on tweet
        messagebox.showerror('Error', "Meer dan 140 characters ingevoerd, typ minder dan 140 characters in.") # error if len is > 140
    elif (len(tweet) <= 0): # check on tweet
        messagebox.showerror('Error', "Geen text ingevoerd, typ AUB iets in.") # error if no text input
    else:
        f = open("Tweets.txt", "a"); # edits file
        f.write(tweet + "\n"); # writest the file
        text.delete(0.0, END) #ereases text so it resets
        f.close(); # end of line


root.title("Tweet") #  GUI NAME

root.minsize(width=400,height=410)  #min width
root.maxsize(width=400,height=410) # max Width

text = Text(root)
button1 = Button(text="Submit", fg="green", command=Tweet)  #Tweet button

text.pack()
button1.pack()

root.mainloop() # the window is now displayed
