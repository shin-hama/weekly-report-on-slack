import os
from slack_bolt import App
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

for ch in app.client.conversations_list()["channels"]:
    print(ch["name"], ch["id"])
# print(app.client.conversations_history)
