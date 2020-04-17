import sqlalchemy as db
import pandas as pd

engine = db.create_engine('sqlite:///twitch.db')
connection = engine.connect()

streams = pd.read_csv('Twitch/video_play.csv')
chats = pd.read_csv('Twitch/chat.csv')

streams.to_sql('stream', con=connection, if_exists='replace')
streams.to_sql('chat', con=connection, if_exists='replace')