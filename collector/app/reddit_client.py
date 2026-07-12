import praw
from datetime import datetime, timezone

from .config import settings


class RedditClient:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=settings.reddit_client_id,
            client_secret=settings.reddit_client_secret,
            user_agent=settings.reddit_user_agent,
        )
        self.subreddit = self.reddit.subreddit(settings.subreddit_name)

    def fetch_posts(self):
        seen = {}

        for submission in self.subreddit.new(limit=100):
            seen[submission.id] = submission

        for submission in self.subreddit.hot(limit=100):
            seen[submission.id] = submission

        for submission in self.subreddit.top(limit=100, time_filter="month"):
            seen[submission.id] = submission

        return [self._map_post(post) for post in seen.values()]

    def _map_post(self, post):
        return {
            "reddit_id": post.id,
            "title": post.title,
            "body": post.selftext,
            "author": str(post.author) if post.author else None,
            "subreddit": str(post.subreddit),
            "score": post.score,
            "comment_count": post.num_comments,
            "url": post.url,
            "created_at": datetime.fromtimestamp(post.created_utc, tz=timezone.utc),
        }
