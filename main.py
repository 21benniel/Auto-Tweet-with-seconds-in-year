import tweepy
import time
import datetime
from tqdm import tqdm


# Current year
current_year = datetime.datetime.now().year

# Start of the current year
start_of_year = datetime.datetime(current_year, 1, 1)

# End of the current year
end_of_year = datetime.datetime(current_year, 12, 31, 23, 59, 59)

# Total number of seconds in the current year
total_seconds = int((end_of_year - start_of_year).total_seconds())
def get_progress_bar(percentage, length=25):
    """Returns a string representation of a progress bar"""
    filled = int(length * (percentage / 100))
    empty = length - filled
    return '[' + '#' * filled + '-' * empty + ']'

#
def progressmessage():
    current_time = time.time()
    # Number of seconds elapsed so far in the current year
    elapsed_seconds = int((current_time - start_of_year.timestamp()))

    # Progress in percentage
    progress = (elapsed_seconds / total_seconds) * 100
    print(total_seconds)
    print(elapsed_seconds)
    # Progress bar
    pbar = tqdm(total=100, desc='Progress', bar_format='{percentage:3.0f}% |{bar}|')
    pbar.update(int(progress))
    pbar.close()
    progress_bar = get_progress_bar(progress)

    message = "\n{} Year seconds progress: \n{}{:.2f}% ".format(current_year,progress_bar, progress)
    return message


# Twitter API credentials
consumer_key = ":)"
consumer_secret = "><"
access_token = "<>"
access_token_secret = "<>"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Tweet message

# Tweet every 12 hours
while True:
    try:
        message = progressmessage()
        # api.update_status(message)
        print("Tweeted: " + message)
        time.sleep(43200) # sleep for 12 hours
    except tweepy.TweepError as error:
        print("Error: " + str(error))
        time.sleep(60) # sleep for 1 minute and try again


