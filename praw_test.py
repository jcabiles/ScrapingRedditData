import praw
import os
import pandas as pd

# grab credentials from bash profile and create praw object
reddit = praw.Reddit(client_id=os.environ.get('REDDIT_client_id'),
                     client_secret=os.environ.get('REDDIT_client_secret'),
                     user_agent='Reddit Scraping')

posts = []
all_subreddit = reddit.subreddit('all')
for post in all_subreddit.hot(limit=10):
    if not post.stickied:
       posts.append([post.title, post.score, post.id, post.subreddit,
                    post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit',
                                    'url', 'num_comments', 'body', 'created'])
print(posts)

posts.columns

for id in posts['id']:
    submission = reddit.submission(id)
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        print(comment.body)
    print("""
    ####################
    NEXT SET OF COMMENTS 
    ####################
    """)



for id in posts['id']:
    submission = reddit.submission(id)
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        for k, v in comment.__dict__.items():
            print(f'{k}, and {v}')



test_submission = reddit.submission('g3fcge')
list_comments = test_submission.comments.list()
random_comment = list_comments[0]
dir(list_comments[0])

random_comment.controversiality


"""
This shows us all the values associated with the methods inside the 
comment object.
"""
random_comment.__dict__


"""
Next steps:
- figure out how to grab each key value pairs in this dictionary
- inside of dataframe: store key as column name, value as value
- loop through each comment... assign comment id in first column then
 the key-value pairs in subsequent columns
 
"""