import tweepy
import random
import os
import time


# Twitter API credentials from environment variables
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Search query (change to your original after testing)
search_query = "hello -filter:retweets"

# Messages to reply with
messages = [
    "Hey @{username}, hit me up 👉 https://x.com/shortifymedia/status/1949493254438928750?s=46&t=MlHIHg7BQmO7XM2tfbnj3w",
    "Hey @{username}, check DMs. 👉 https://x.com/shortifymedia/status/1949493254438928750?s=46&t=MlHIHg7BQmO7XM2tfbnj3w",
    "Shoot me a DM @{username} 👉 https://x.com/shortifymedia/status/1949493254438928750?s=46&t=MlHIHg7BQmO7XM2tfbnj3w",
    "@{username} 👉 https://x.com/shortifymedia/status/1949493254438928750?s=46&t=MlHIHg7BQmO7XM2tfbnj3w"
]

# Set to store IDs of tweets already replied to
replied_tweet_ids = set()

def reply_to_tweets():
    try:
        tweets = api.search_tweets(q=search_query, lang='en', count=10, result_type='recent')
        print(f"Found {len(tweets)} tweets matching query.")
        for tweet in tweets:
            tweet_id = tweet.id
            if tweet_id in replied_tweet_ids:
                continue  # Skip if already replied

            username = tweet.user.screen_name
            message = random.choice(messages).replace("{username}", username)
            print(f"Replying to @{username} — Tweet ID: {tweet_id}")
            try:
                api.update_status(
                    status=message,
                    in_reply_to_status_id=tweet_id,
                    auto_populate_reply_metadata=True
                )
                replied_tweet_ids.add(tweet_id)  # Mark as replied
            except Exception as e:
                print(f"❌ Failed to reply to @{username}: {e}")

    except Exception as e:
        print(f"❌ Error fetching tweets: {e}")


if __name__ == "__main__":
    print("Bot started. Running continuously...")
    while True:
        reply_to_tweets()
        time.sleep(60)  # Wait 60 seconds before checking again
if __name__ == "__main__":
    print("Bot started. Running continuously...")
    while True:
        reply_to_tweets()
        time.sleep(60)  # Wait 60 seconds before checking again
