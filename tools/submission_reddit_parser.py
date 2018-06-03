from datetime import datetime

import praw
from newspaper import Article, ArticleException

from model.reddit_submission import insert_submission, get_submission

r = praw.Reddit(user_agent='Submission Extraction (by /u/TOXMEH)',
                client_id='oY_MSuWjZiNVpg', client_secret="sA47tklI0MTXYTIHpSUmVWxKjwA",
                username='TOXMEH', password='Reddit171296')


class SubredditLatest(object):
    """Get all available submissions within a subreddit newer than x."""

    def __init__(self, subreddit, dt):

        # master list of all available submissions
        self.total_list = []

        # subreddit must be a string of the subreddit name (e.g., "soccer")
        self.subreddit = subreddit

        # dt must be a utc datetime object
        self.dt = dt

    def __call__(self):
        self.get_submissions(self)
        return self.total_list

    def get_submissions(self, paginate=False):
        """Get limit of subreddit submissions."""
        limit = 100  # Reddit maximum limit

        if paginate is True:
            try:
                # get limit of items past the last item in the total list
                submissions = r.subreddit(self.subreddit).new(limit=limit,
                                                              params={"after": self.total_list[-1].fullname})
            except IndexError:
                print("param error")
                return
        else:
            submissions = r.subreddit(self.subreddit).new(limit=limit)

        submissions_list = [
            # iterate through the submissions generator object
            x for x in submissions
            # add item if item.created_utc is newer than dt
            if datetime.utcfromtimestamp(x.created_utc).date() >= self.dt
        ]
        self.total_list += submissions_list

        # if you've hit the limit, recursively run this function again to get
        # all of the available items
        if len(submissions_list) == limit:
            self.get_submissions(paginate=True)
        else:
            return


if __name__ == '__main__':
    # time = get_last_date()
    # if time is None:
    time = datetime(2012, 1, 1).date()
    # time = get_min_date() + timedelta(days=1)

    for submission in SubredditLatest("economics", time)():

        if get_submission(submission.id) is None and submission.score >= 10:
            article = Article(submission.url)
            article.download()
            try:
                article.parse()
            except ArticleException:
                continue

            insert_submission(id=submission.id, date_val=datetime.fromtimestamp(submission.created).date(),
                              title=submission.title,
                              url=submission.url,
                              score=submission.score, text=article.text)
