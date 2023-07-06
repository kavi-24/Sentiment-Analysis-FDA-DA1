import requests
import constants
from textblob import TextBlob
import re

def extract_youtube_video_id(url):
    pattern = r"(?<=v=|\/videos\/|embed\/|youtu.be\/|\/v\/|\/e\/|watch\?v=|\&v=|\?v=)([^#\&\?]*)(?=\?|\&|\#|$|\z)"
    match = re.search(pattern, url)
    if match:
        video_id = match.group(1)
        return video_id
    else:
        return None

def get_comments(vid_id):
    data = requests.get(f"https://www.googleapis.com/youtube/v3/commentThreads?key={constants.API_KEY}&textFormat=plainText&part=snippet&videoId={vid_id}&maxResults=50")


def get_tweet_sentiment(comment):
    analysis = TextBlob(comment)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
