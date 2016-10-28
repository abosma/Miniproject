from TwitterAPI import TwitterAPI
import time

api = TwitterAPI("tdErmVotisBBi0qgClWPvC2zD", "UUNAAxEqqHbBgWOLKG6ZoWvZj1fcYuDZrc7VrmaMqJnfKiY7s5", "791235928564039680-e1gd5nWxWkObyGM5V9wMhqp6AmgCOJF", "b6Ha49AWq3KPAASIxQUbqn83OtE4KVOOcnJhp3gsIPcUL")

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open("C:/Users/User/Documents/Visual Studio 2015/Projects/Miniproject2/Miniproject2/Tweets.txt","r")
    loglines = follow(logfile)
    for line in loglines:
        print(line)
        while True:
            a = input("Accept of Reject: ")
            try:
                if a == "Accept":
                    a = str(a);
                    r = api.request('statuses/update', {'status':line})
                    print("Tweet gepost: " + line);
                    break;
                if a == "Reject":
                    line = line.replace("\n", "");
                    f = open("Log.txt", "a");
                    f.write(line + " : " + time.strftime("%a %d %b %Y, %T \n"));
                    f.close();
                    break;
                else:
                    print("Geen accept of reject gedecteerd, probeer het nog eens.")
            except ValueError:
                print("Geen nummers of tekens aub.");
                continue