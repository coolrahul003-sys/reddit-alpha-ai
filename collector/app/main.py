from sqlalchemy.exc import SQLAlchemyError

from .database import SessionLocal
from .logger import logger
from .models import Post
from .reddit_client import RedditClient


def collect_posts():
    session = SessionLocal()
    collected = 0

    try:
        client = RedditClient()
        logger.info("Connected to Reddit API")

        posts = client.fetch_posts()

        for data in posts:
            exists = session.query(Post).filter_by(
                reddit_id=data["reddit_id"]
            ).first()

            if exists:
                continue

            session.add(Post(**data))
            collected += 1

        session.commit()
        print(f"Posts collected: {collected}")

    except SQLAlchemyError:
        session.rollback()
        logger.exception("Database error")
        raise
    except Exception:
        logger.exception("Collector failed")
        raise
    finally:
        session.close()


if __name__ == "__main__":
    collect_posts()
