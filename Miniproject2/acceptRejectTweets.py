from TwitterAPI import TwitterAPI
import time

api = TwitterAPI("qaDlX0kYOQ99OhOrFHDc9li07", "cLhI4Oe8D6grpDhns1udDaIxfp3SNMqECVOvHZU27mrFTR1to0", "791235928564039680-960nSheLDOtSIKiK7wwV0C7dsjQfTRb", "HZn6PJ8VyHNpuNzrx3xP4YyHJdcubqLwwqOAy8f4ji0H7")

def follow(file):
    file.seek(0,2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

<<<<<<< HEAD
if __name__ == '__main__':
    logfile = open("C:/Users/Wenfrie/PycharmProjects/Miniproject/Miniproject2/Tweets.txt","r") #path
    loglines = follow(logfile)
    for line in loglines:
        while True:
            print(line);

            a = input("Accept of Reject: ")
            try:
                if a == "Accept":   #accept the tweet
                    a = str(a);
                    r = api.request('statuses/update', {'status':line})  #post line
                    print("Tweet gepost: " + line);
                    break;
                if a == "Reject":  #reject the tweet
                    line = line.replace("\n", "");
                    f = open("Log.txt", "a");
                    f.write(line + " : " + time.strftime("%a %d %b %Y, %T \n"));   #weekday ,day of the month , month shortened , year, time(0:00:00)
                    f.close();
                    break;
                else:
                    print("Geen accept of reject gedecteerd, probeer het nog eens.")
            except ValueError:
                print("Geen nummers of tekens aub.");
                continue
=======
def acceptReject():
    if a == "Accept":
        a = str(a);
        r = api.request('statuses/update', {'status':line})
        print("Tweet gepost: " + line);
        return True;
    if a == "Reject":
        line = line.replace("\n", "");
        f = open("Log.txt", "a");
        f.write(line + " : " + time.strftime("%a %d %b %Y, %T \n"));
        f.close();
        return True;
    else:
        print("Geen accept of reject gedecteerd, probeer het nog eens.")
        return False;

logfile = open("C:/Users/User/Documents/Visual Studio 2015/Projects/Miniproject2/Miniproject2/Tweets.txt","r")
loglines = follow(logfile)
for line in loglines:
    while True:
        print(line);
        a = input("Accept of Reject: ")
        try:
            if acceptReject() == True:
                break;
            else:
                continue;
        except ValueError:
            print("Geen nummers of tekens aub.");
            continue
>>>>>>> origin/master
