-- create a table to store items (stories, comments, etc.) from HackerNews
CREATE TABLE items (
       by TEXT,
       id SERIAL,
       kids INTEGER[] DEFAULT NULL,
       parent INTEGER DEFAULT NULL,
       text TEXT DEFAULT NULL,
       time TIMESTAMPTZ DEFAULT NULL,
       type TEXT DEFAULT NULL,
       PRIMARY KEY (id)       
);
