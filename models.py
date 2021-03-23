from peewee import *

db = SqliteDatabase('twitch.db')


class Streamer(Model):
    platform = CharField()
    username = CharField(unique=True)
    stream_url = CharField()
    profile_pic_url = CharField()

    class Meta:
        database = db

    def __repr__(self):
        return(f'Platform: {self.platform}\nUsername: {self.username}\nStream_Url: {self.stream_url}\nProfile_pic_url: {self.profile_pic_url}')


class Stream(Model):
    streamer = ForeignKeyField(Streamer, backref='streams')
    session_title = CharField()
    session_date = DateTimeField()

    class Meta:
        database = db

# db.create_tables([Streamer, Stream])

# Usage
# test = Streamer(platform='Twitch', username='Saby',
#                 stream_url='https://twitch.tv/saby_roxxx', profile_pic_url='https://Too_ugly_for_you')
