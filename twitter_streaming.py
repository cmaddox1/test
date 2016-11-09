
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1053232980-n1smbhCN7H2dJDdGSXKhtpswYj3xq1gInihAHCS"
access_token_secret = "hmF1Rk2nrlfZnoOn9VBsKDfD1pnnVPsQp0OsxBNT0SB4a"
consumer_key = "nL3UK4lG6eJSoRMesaXyh4jMi"
consumer_secret = "QAmwiRsadck4vdQNdliPXLhI3UwN5XoWCkqPf0u589645HIRhM"



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['wcw', 'Woman crush Wednesday'])

