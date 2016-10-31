import time
from TwitterAPI import TwitterAPI

api = TwitterAPI("tdErmVotisBBi0qgClWPvC2zD", "UUNAAxEqqHbBgWOLKG6ZoWvZj1fcYuDZrc7VrmaMqJnfKiY7s5", "791235928564039680-e1gd5nWxWkObyGM5V9wMhqp6AmgCOJF", "b6Ha49AWq3KPAASIxQUbqn83OtE4KVOOcnJhp3gsIPcUL")

starttime=time.time()

while True:
    try:
        r = api.request('statuses/home_timeline', {'count':5})
        for item in r.get_iterator():
            if 'text' in item:
                print(item["text"]);
    except Exception as e:
        print(e);
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))