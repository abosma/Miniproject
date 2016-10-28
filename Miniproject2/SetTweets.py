while True:
    a = input("Typ jouw tweet in: ");
    if(len(a) > 140):
        print("Meer dan 140 characters ingevoerd, typ minder dan 140 characters in.");
        continue;
    elif(len(a) <= 0):
        print("Geen text ingevoerd, typ AUB iets in");
        continue;
    else:
        f = open("Tweets.txt", "a");
        f.write(a + "\n");
        f.close();