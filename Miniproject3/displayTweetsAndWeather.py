import time
from TwitterAPI import TwitterAPI
import pyowm

api = TwitterAPI("tdErmVotisBBi0qgClWPvC2zD", "UUNAAxEqqHbBgWOLKG6ZoWvZj1fcYuDZrc7VrmaMqJnfKiY7s5", "791235928564039680-e1gd5nWxWkObyGM5V9wMhqp6AmgCOJF", "b6Ha49AWq3KPAASIxQUbqn83OtE4KVOOcnJhp3gsIPcUL")
owm = pyowm.OWM("a40051c6d53e900889105abcdc376832")
tweets = [];

starttime = time.time()

while True:
    try:
        r = api.request('statuses/home_timeline', {'count':5})
        print(r.status_code);
        for item in r.get_iterator():
            if 'text' in item:
                if len(tweets) < 5:
                    tweets.append(item["text"])
                    print(item["text"]);
                else:
                    if item["text"] in tweets:
                        observation = owm.weather_at_place("Utrecht,NL")
                        w = observation.get_weather()
                        weatherCelcius = w.get_temperature('celsius')
                        weatherWindsnelheid = w.get_wind()
                        print("Tempratuur in Utrecht   : °C " + str(weatherCelcius.get("temp")))
                        print("Windsnelheid in Utrecht : " + str(weatherWindsnelheid.get("speed")) + " " + str(weatherWindsnelheid("deg") + "°"))
                    else:
                        tweets.pop(0);
                        tweets.append(item["text"])
                        for tweet in tweets:
                            print(tweet);
    except Exception as e:
        print(e);

    time.sleep(60.0 - ((time.time() - starttime) % 60.0))