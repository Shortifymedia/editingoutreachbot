import tweepy
import random
import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Twitter API credentials
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Authenticate
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Test authentication
try:
    user = api.verify_credentials()
    print(f"✅ Authenticated as @{user.screen_name}")
except Exception as e:
    print(f"❌ Authentication failed: {e}")

# Search query (edit as you like)
search_query = "hello -filter:retweets"

# Messages to reply with
messages = [
    "Hey @{username}, hit me up 👉 https://x.com/shortifymedia/status/1949493254438928750",
    "Hey @{username}, check DMs 👉 https://x.com/shortifymedia/status/1949493254438928750",
    "Shoot me a DM @{username} 👉 https://x.com/shortifymedia/status/1949493254438928750",
    "@{username} 👉 https://x.com/shortifymedia/status/1949493254438928750"
]

# Track replied tweets
replied_tweet_ids = set()

def reply_to_tweets():
    print(f"\n🔍 Checking for tweets matching query: '{search_query}'")
    try:
        tweets = api.search_tweets(q=search_query, lang='en', count=5, result_type='recent')
        print(f"Found {len(tweets)} tweets.")

        for tweet in tweets:
            tweet_id = tweet.id
            username = tweet.user.screen_name
            print(f"Processing tweet ID {tweet_id} from @{username}")

            if tweet_id in replied_tweet_ids:
                print(f"➡ Already replied to @{username}, skipping.")
                continue

            # Pick random message
            message = random.choice(messages).replace("{username}", username)
            print(f"✉ Prepared message: {message}")

            try:
                api.update_status(
                    status=message,
                    in_reply_to_status_id=tweet_id,
                    auto_populate_reply_metadata=True
                )
                replied_tweet_ids.add(tweet_id)
                print(f"✅ Replied to @{username}")
            except Exception as e:
                print(f"❌ Failed to reply to @{username}: {e}")

    except Exception as e:
        print(f"❌ Error fetching tweets: {e}")

    print("⏱ Loop finished.\n")

# Flask routes
@app.route("/")
def home():
    return "Bot is running! Visit /run-bot to trigger it."

@app.route("/run-bot")
def run_bot_route():
    reply_to_tweets()
    return "Bot checked for tweets! See logs for details."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
