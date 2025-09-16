import tweepy
import random
import os
from flask import Flask

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

search_query = (
    "looking for editor OR need editor OR hiring editor OR shorts editor OR shortform editor -filter:retweets"
)

messages = [
    "Hey @{username}, hit me up 👉 https://x.com/shortifymedia/status/1949493254438928750?s=46&t=MlHIHg7BQmO7XM2tfbnj3w",
    "Hey @{username}, check DMs. 👉 https://x.com/shortifymedia/status/1949493254438928750?s=46&t=MlHIHg7BQmO7XM2tfbnj3w",
    "Shoot me a DM @{username} 👉 https://x.com/shortifymedia/status/1949493254438928750?s=46&t=MlHIHg7BQmO7XM2tfbnj3w",
    "@{username} 👉 https://x.com/shortifymedia/status/1949493254438928750?s=46&t=MlHIHg7BQmO7XM2tfbnj3w"
]

def reply_to_tweets():
    try:
        tweets = api.search_tweets(q=search_query, lang='en', count=5, result_type='recent')
        for tweet in tweets:
            username = tweet.user.screen_name
            tweet_id = tweet.id
            message = random.choice(messages).replace("{username}", username)
            print(f"Replying to @{username} — Tweet ID: {tweet_id}")
            api.update_status(
                status=message,
                in_reply_to_status_id=tweet_id,
                auto_populate_reply_metadata=True
            )
    except Exception as e:
        print(f"❌ Error occurred: {e}")

@app.route("/")
def home():
    reply_to_tweets()
    return "Bot ran successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
