import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')
ARN = config.get("IAM_ROLE","ARN")
# DROP TABLES

staging_events_drop = "DROP TABLE IF EXISTS events;"
staging_songs_drop = "DROP TABLE IF EXISTS songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_create= ("""
CREATE TABLE IF NOT EXISTS events(
    artist TEXT,
    auth TEXT,
    firstName TEXT,
    gender TEXT,
    itemInSession INT,
    lastName TEXT,
    length INT,
    level TEXT,
    location TEXT,
    method TEXT,
    page TEXT,
    registration REAL,
    sessionId INT,
    song TEXT,
    status INT,
    ts BIGINT,
    userAgent TEXT,
    userId INT
    );
""")

staging_songs_create = ("""
CREATE TABLE IF NOT EXISTS songs(
    num_songs INT,
    artist_id TEXT,
    artist_latitude REAL,
    artist_longitude REAL,
    artist_location TEXT,
    artist_name TEXT,
    song_id TEXT,
    title TEXT,
    duration FLOAT,
    year INT
);
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays(
    songplay_id INT PRIMARY KEY,
    start_time TIMESTAMP,
    user_id INT,
    level CHAR(4),
    song_id INT,
    artist_id INT,
    session_id INT,
    location TEXT,
    user_agent TEXT
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
    user_id INT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender CHAR(1),
    level CHAR(4)
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
    song_id INT PRIMARY KEY,
    title TEXT,
    artist_id INT,
    year INT,
    duration FLOAT
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
    artist_id INT PRIMARY KEY,
    name TEXT,
    location TEXT,
    lattitude REAL,
    longitude REAL
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
    start_time TIMESTAMP PRIMARY KEY,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday INT
)
""")

# STAGING TABLES

staging_songs_load = ("""
    copy staging.songs
    from 's3://udacity-dend/song_data/'
    format as json 'auto'
    credentials 'aws_iam_role={}'
    region 'us-west-2';
""").format(ARN)

staging_events_load = ("""
    copy staging.events
    from 's3://udacity-dend/log_data/'
    format as json 's3://udacity-dend/log_json_path.json'
    credentials 'aws_iam_role={}'
    region 'us-west-2';
""").format(ARN)

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]

drop_staging_queries = [staging_songs_drop, staging_events_drop]
create_staging_queries = [staging_songs_create, staging_events_create]
load_staging_queries = [staging_songs_load, staging_events_load]
#load_staging_queries = [staging_events_load]
