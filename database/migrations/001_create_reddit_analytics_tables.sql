CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    reddit_id VARCHAR UNIQUE NOT NULL,
    title TEXT NOT NULL,
    body TEXT,
    author VARCHAR,
    subreddit VARCHAR NOT NULL,
    score INTEGER DEFAULT 0,
    comment_count INTEGER DEFAULT 0,
    created_at TIMESTAMP NOT NULL,
    url VARCHAR,
    processed BOOLEAN DEFAULT FALSE
);

CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    reddit_id VARCHAR UNIQUE NOT NULL,
    post_id UUID REFERENCES posts(id),
    author VARCHAR,
    body TEXT,
    score INTEGER DEFAULT 0,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR UNIQUE NOT NULL,
    total_posts INTEGER DEFAULT 0,
    total_comments INTEGER DEFAULT 0,
    karma INTEGER DEFAULT 0
);

CREATE TABLE ticker_mentions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    post_id UUID REFERENCES posts(id),
    ticker VARCHAR NOT NULL,
    sentiment VARCHAR,
    confidence FLOAT
);

CREATE TABLE ai_analysis (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    post_id UUID REFERENCES posts(id),
    summary TEXT,
    bull_case TEXT,
    bear_case TEXT,
    risk TEXT,
    price_target VARCHAR,
    recommendation VARCHAR
);
