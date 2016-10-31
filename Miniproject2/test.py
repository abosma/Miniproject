from tkinter import *
root = Tk() #GUI   #log erbij if time premits

#Labels
thelabel = Label(root, text="tweet")  #teskst

#frames
topFrame = Frame(root)
bottomFrame = Frame(root)

#buttons
button1 = Button(bottomFrame, text="Accept", fg="green")  #button Accept
button2 = Button(bottomFrame, text="Reject", fg="red")  #button REject

#packs
thelabel.pack()
topFrame.pack()
bottomFrame.pack(side=BOTTOM)
button1.pack(side=LEFT)
button2.pack(side=RIGHT)


root.mainloop() #Main