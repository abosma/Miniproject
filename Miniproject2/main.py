from multiprocessing import Process
import displayTweetsAndWeather
import acceptRejectTweets
import SetTweets


if __name__ == '__main__':
    Process(target=acceptRejectTweets.startGUI).start()
    Process(target=SetTweets.tweetGUI).start()
    Process(target=displayTweetsAndWeather.guiStart).start()
    Process(target=displayTweetsAndWeather.getTweets).start()
    Process(target=acceptRejectTweets.logFiles).start()