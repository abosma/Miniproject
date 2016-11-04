import displayTweetsAndWeather
import acceptRejectTweets
import SetTweets
import threading

startThreads1 = threading.Thread(target=displayTweetsAndWeather.startThreads).start()
startThreads2 = threading.Thread(target=acceptRejectTweets.startThreads).start()
startThreads3 = threading.Thread(target=SetTweets.startThreads).start()