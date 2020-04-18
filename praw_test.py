import praw
import os

# grab credentials from bash profile and create praw object
reddit = praw.Reddit(client_id=os.environ.get('REDDIT_client_id'),
                     client_secret=os.environ.get('REDDIT_client_secret'),
                     user_agent='Reddit Scraping')
