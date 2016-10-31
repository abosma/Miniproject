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
button1 = Button(bottomFrame, text="Accept", fg="green", command=testbutton1)  #button Accept
button2 = Button(bottomFrame, text="Reject", fg="red", command=testbutton2)  #button REject

#packs
thelabel.pack()
topFrame.pack()
bottomFrame.pack(side=BOTTOM)
button1.pack(side=LEFT)
button2.pack(side=RIGHT)

root.mainloop() #Main


