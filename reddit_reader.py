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
    if not post.stickied:
        print(post.title, "id:", post.id)

submission_id = input("id: ")
submission = reddit.submission(submission_id)
submissionList = []
submission.comments.replace_more(limit=10)
commentLimit = 10
commentCounter = 0
for comment in submission.comments.list():
    bod = comment.body
    if commentCounter == commentLimit:
        break
    submissionList.append(bod.replace("\n", ""))
    commentCounter += 1

print(submissionList)
    