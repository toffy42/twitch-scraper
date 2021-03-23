from models import Streamer, Stream
import json
import twitch_interface as partner
from peewee import IntegrityError


def get_users():
    streamers = []
    for streamer in Streamer.select():
        streamers.append(streamer.username)
    return streamers


def get_user_data(username):
    user_dict = {}
    try:
        streamer = Streamer.get(Streamer.username == username)
        user_dict['username'] = streamer.username
        user_dict['stream_url'] = streamer.stream_url
        user_dict['pic_url'] = streamer.profile_pic_url
        user_dict['platform'] = streamer.platform
        streamer_json = json.dumps(user_dict)
    except Exception as e:
        print(e)
        return []
    return streamer_json


def add_user(username):
    # partner.test_request()
    user = partner.get_streamer_data(username)

    streamer = Streamer(platform=user['platform'],
                        username=user['name'],
                        stream_url=user['channel_url'],
                        profile_pic_url=user['image_url'])
    try:
        streamer.save()
    except IntegrityError:
        pass


def delete_user(username):
    try:
        streamer = Streamer.get(Streamer.username == username)
        streamer.delete_instance()
    except IntegrityError:
        pass
