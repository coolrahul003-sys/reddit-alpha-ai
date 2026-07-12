from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str
    reddit_client_id: str
    reddit_client_secret: str
    reddit_user_agent: str = "reddit-alpha-ai-collector"
    subreddit_name: str = "Stocks_Picks"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)


settings = Settings()
