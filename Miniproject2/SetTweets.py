while True:
    a = input("Typ jouw tweet in: ");
    f = open("Tweets.txt", "a");
    f.write(a + "\n");
    f.close();