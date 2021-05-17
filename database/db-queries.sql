-- create a table to store items (stories, comments, etc.) from HackerNews
CREATE TABLE items (
       id SERIAL PRIMARY KEY,
       by TEXT,
       item_id INTEGER,
       kids INTEGER[] DEFAULT NULL,
       parent INTEGER DEFAULT NULL,
       text TEXT DEFAULT NULL,
       time TIMESTAMPTZ DEFAULT NULL,
       type TEXT DEFAULT NULL
);

-- insert some values
INSERT INTO items (by, item_id, kids, parent, text, time, TYPE)
VALUES ('norvig',
        2921983,
        '{ 2922097, 2922429, 2924562, 2922709, 2922573, 2922140, 2922141}',
        2921506,
        'Aw shucks, guys ... you make me blush with your compliments.<p>Tell you what, Ill make a deal: I''ll keep writing if you keep reading. K?',
        to_timestamp(1314211127),
        'comment');
