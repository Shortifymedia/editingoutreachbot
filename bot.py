import tweepy
import time

# =============================
# 1. AUTHENTICATION
# =============================

api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("✅ Authentication successful")
except:
    print("❌ Authentication failed")

# =============================
# 2. SEARCH QUERY
# =============================

search_query = (
    "short form content OR video editor OR reels editor OR tiktok editor OR "
    "youtube shorts editor OR need a video editor OR hiring editor OR edit my video "
    "-filter:retweets"
)

# =============================
# 3. BOT LOGIC
# =============================

def run_bot():
    print("🤖 Bot started...")

    # Search tweets
    tweets = api.search_tweets(q=search_query, count=5, lang="en", result_type="recent")

    for tweet in tweets:
        try:
            print(f"🔍 Found tweet from @{tweet.user.screen_name}: {tweet.text}")

            # Reply text (customize this to your style!)
            reply_text = (
                f"Hey @{tweet.user.screen_name}, I’m a short-form video editor 🎬 "
                "I can help turn your content into viral TikToks, Reels, or Shorts 🚀. "
                "DM me if you’re interested!"
            )

            # Reply to tweet
            api.update_status(
                status=reply_text,
                in_reply_to_status_id=tweet.id,
                auto_populate_reply_metadata=True
            )
            print(f"✅ Replied to @{tweet.user.screen_name}")

            # Avoid spamming (wait a bit between replies)
            time.sleep(15)

        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(5)

# =============================
# 4. RUN LOOP
# =============================

while True:
    run_bot()
    print("⏳ Waiting 5 minutes before next run...")
    time.sleep(300)  # Run every 5 minutes
