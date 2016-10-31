from tkinter import *
from tkinter import messagebox
root = Tk()
filename = None

def Tweet():
    global filename
    tweet =  text.get(0.0, END)    # read tweet
    if (len(tweet) > 140):
        messagebox.showerror('Error', "Meer dan 140 characters ingevoerd, typ minder dan 140 characters in.")
    elif (len(tweet) <= 0):
        messagebox.showerror('Error', "Geen text ingevoerd, typ AUB iets in.")
    else:
        f = open("Tweets.txt", "a");
        f.write(tweet + "\n");
        text.delete(0.0, END)
        f.close();


root.title("Tweet")

root.minsize(width=400,height=400)
root.maxsize(width=1000,height=1000)

text = Text(root)
button1 = Button(text="Submit", fg="green", command=Tweet)  #Tweet button

text.pack()
button1.pack()

root.mainloop() # the window is now displayed

#while True:
 #   a = input("Typ jouw tweet in: ");
  #  if(len(a) > 140):
  #      print("Meer dan 140 characters ingevoerd, typ minder dan 140 characters in.");
   #     continue;
   # elif(len(a) <= 0):
  #      print("Geen text ingevoerd, typ AUB iets in");
  #      continue;
  #  else:
  #      f = open("Tweets.txt", "a");
  #      f.write(a + "\n");
   #     f.close();


