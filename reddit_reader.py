import praw
client_id = ""
client_secret = ""
username = ""
password = ""
user_agent = "reddit_reader"
reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    username=username",
                    password=password,
                    user_agent="reddit_reader")

sub_input = input("subreddit: ")
sub = reddit.subreddit(sub_input)
sub_hot = sub.hot(limit=9)
for post in sub_hot:
    comments = post.comments
    if not post.stickied:
        print("***************************\n", post.title, "    ↑:", post.ups, "    ↓:", post.downs)
        for comment in comments:
            print("     comment:", comment.body)
