from TwitterAPI import TwitterAPI
api = TwitterAPI("tdErmVotisBBi0qgClWPvC2zD", "UUNAAxEqqHbBgWOLKG6ZoWvZj1fcYuDZrc7VrmaMqJnfKiY7s5", "791235928564039680-e1gd5nWxWkObyGM5V9wMhqp6AmgCOJF", "b6Ha49AWq3KPAASIxQUbqn83OtE4KVOOcnJhp3gsIPcUL")

file = "C:/Users/User/documents/visual studio 2015/Projects/Miniproject/Miniproject/Tweets.txt";
tweets = [line.rstrip("\n") for line in open(file)];

for item in tweets:
    print(item)
    a = str(input("Accept of Reject: "))
    if(a == "Accept"):
        r = api.request('statuses/update', {'status':item})
        print("Tweet gepost: " + item);
    elif(a == "Reject"):
        continue;