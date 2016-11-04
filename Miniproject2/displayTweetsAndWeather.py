from tkinter import *
import time
from TwitterAPI import TwitterAPI
import pyowm
import threading

api = TwitterAPI("tdErmVotisBBi0qgClWPvC2zD", "UUNAAxEqqHbBgWOLKG6ZoWvZj1fcYuDZrc7VrmaMqJnfKiY7s5",
                 "791235928564039680-e1gd5nWxWkObyGM5V9wMhqp6AmgCOJF", "b6Ha49AWq3KPAASIxQUbqn83OtE4KVOOcnJhp3gsIPcUL")
owm = pyowm.OWM("a40051c6d53e900889105abcdc376832")

tweetList = []

tweetString = "Geen tweets binnengekomen..."

tempratuur = 0.0

windspeed = 0.0

windangle = 0.0

def setTweetList(tweet):
    global tweetList
    tweetList.append(tweet)

def convertTweetList(tweetlist):
    global tweetString
    tweetString = "\n".join(tweetlist);

def setTweetString(string):
    global tweetString
    tweetString = string

def setTemp(temp):
    global tempratuur;
    tempratuur = temp;

def setWindSpeed(ws):
    global windspeed;
    windspeed = ws;

def setWindAngle(wa):
    global windangle;
    windangle = wa;


def guiStart():
    root = Tk()  # GUI   #log erbij if time premits

    root.title("DisplayTweetsAndWeather")  # GUI NAME
    root.minsize(width=400, height=60)
    root.maxsize(width=2000, height=400)
    labelString = StringVar();
    labelString.set(tweetString);


    # Labels
    thelabel = Label(root, textvariable=labelString)

    # frames
    topFrame = Frame(root)
    bottomFrame = Frame(root)

    #images
    photo = PhotoImage(file="ns.png")
    image =  Label(image=photo,)

    # packs
    thelabel.pack(fill=X,side=BOTTOM)
    topFrame.pack()
    bottomFrame.pack(side=BOTTOM)
    image.pack(side=LEFT, fill='both', expand='yes')


    def checkChanges():

        if(len(tweetList) != 0 and not tempratuur):
            convertTweetList(tweetList);
        else:
            tempString = str(tempratuur)
            windSpeedString = str(windspeed)
            windAngleString = str(windangle)

            setTweetString("Tempratuur in Utrecht   : " + tempString + "°C" + "\n"
                           + "Windsnelheid in Utrecht : " + windSpeedString + "m/s : " + windAngleString + "°")

        labelString.set(tweetString);
        root.after(2000, checkChanges)

    root.after(2000, checkChanges)
    root.mainloop();

def getTweets():
    starttime = time.time()  # start clock

    while True:
        try:
            r = api.request('statuses/home_timeline',{'count': 5})  # api reqeust take from twitter last 5 tweets (json file)
            print(r.status_code);
            for item in r.get_iterator():  # per tweet doe X
                if 'text' in item:  # Als een variable 'text' text dan kijkt hij naar de lengte van de lijst 5
                    if len(tweetList) < 5:  # check if 5-
                        setTweetList(item["text"])  # put tweets in list
                    else:  # if ==5
                        if item["text"] in tweetList:  # if tweet been here before
                            observation = owm.weather_at_place("Utrecht,NL")  # show weather
                            w = observation.get_weather()
                            weatherCelcius = w.get_temperature('celsius')
                            weatherWindsnelheid = w.get_wind()
                            setTemp(weatherCelcius.get("temp"))
                            setWindSpeed(weatherWindsnelheid.get("speed"))
                            setWindAngle(weatherWindsnelheid.get("deg"))
                        else:
                            tweetList.pop(0);  # if tweets is not in list before then remove first tweet
                            setTweetList(item["text"])  # add new tweet
                            setTemp(0.0);
        except Exception as e:
            print(e);  # erorr handling

        time.sleep(60.0 - ((time.time() - starttime) % 60.0))  # wait 60s or else we get blocked max 15 reqeusts per 15 mins
