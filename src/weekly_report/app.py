import datetime
import os

from dotenv import load_dotenv
from slack_bolt import App


# Load environment variables
load_dotenv()

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

for ch in app.client.conversations_list()["channels"]:
    print(ch["name"], ch["id"])

# 今日から一週間前 0:00 から本日の 0:00 までのメッセージを取得
now = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
week_ago = now - datetime.timedelta(days=7)
latest = int()
print(week_ago)
print(week_ago.timestamp())

print(
    app.client.conversations_history(
        channel="C057276DTRU",
        oldest=str(week_ago.timestamp()),
        latest=str(now.timestamp()),
    )
)
