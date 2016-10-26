#from TwitterAPI import TwitterAPI
#api = TwitterAPI("tdErmVotisBBi0qgClWPvC2zD", "UUNAAxEqqHbBgWOLKG6ZoWvZj1fcYuDZrc7VrmaMqJnfKiY7s5", "791235928564039680-e1gd5nWxWkObyGM5V9wMhqp6AmgCOJF", "b6Ha49AWq3KPAASIxQUbqn83OtE4KVOOcnJhp3gsIPcUL")

#file = "C:/Users/User/documents/visual studio 2015/Projects/Miniproject/Miniproject/Tweets.txt";

#while True:
#    tweets = [line.rstrip("\n") for line in open(file)];
#    for item in tweets:
#        print(item)
#        a = str(input("Accept of Reject: "))
#        if(a == "Accept"):
#            r = api.request('statuses/update', {'status':item})
#            print("Tweet gepost: " + item);
#        elif(a == "Reject"):
#            continue;

import time
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open("C:/Users/User/documents/visual studio 2015/Projects/Miniproject/Miniproject/Tweets.txt","r")
    loglines = follow(logfile)
    for line in loglines:
        print(line);