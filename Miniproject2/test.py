from tkinter import *
root = Tk() #GUI   #log erbij if time premits

def testbutton1():
    print("ACCEPTED YAY.")
def testbutton2():
    print("REJECTED AWHH...")

#Labels
thelabel = Label(root, text="tweet")  #teskst

#frames
topFrame = Frame(root)
bottomFrame = Frame(root)

#buttons
button1 = Button(text="Accept", fg="green", command=testbutton1)  #button Accept
button2 = Button(text="Reject", fg="red", command=testbutton2)  #button REject

#icons
twitter =  PhotoImage(file="twitter.png")
label = Label(root, image=twitter)

#********** Status Bar *************

status = Label(root, text="Preparing to do nothing...",bd=1, relief=SUNKEN, anchor=W)

#packs
thelabel.pack()
topFrame.pack()
Label.pack()
bottomFrame.pack(side=BOTTOM)
status.pack(side=BOTTOM, fill=X)
button1.pack(side=LEFT)
button2.pack(side=LEFT)

root.mainloop() #Main


