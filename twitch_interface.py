from requests import get, post
import json
from key_file import *


def get_token():
    response = post('https://id.twitch.tv/oauth2/token?client_id=kkzwxbs5w3gchcu3rx4yhkdgce648t&client_secret=4hexl2k2bdl7r1s0e992ipscdhol62&grant_type=client_credentials&scope=user:edit')
    result = json.loads(response.text)
    return result['access_token']


def get_streamer_data(username):
    token = get_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Client-Id': client_id
    }
    method = get

    url = f'https://api.twitch.tv/helix/users?login={username}'
    result = method(url, headers=headers)
    result_dict = json.loads(result.text)
    return{
        'platform': 'twitch',
        'name': result_dict['data'][0]['login'],
        'image_url': result_dict['data'][0]['profile_image_url'],
        'channel_url': f'https://www.twitch.tv/{str.lower(username)}'
    }


def subscribe_user(username):
    token = get_token()
    method = "POST"
    url = "https://api.twitch.tv/helix/eventsub/subscriptions"
    params = {
        'Authorization': f'Bearer: {token}',
        'Client-Id': client_id,
        'Context-Type': 'application/json',
    }
    data = '/{"type":"users.update","version":"1"."condtion":/{"user_id":"'\
        f'{username}'\
        '"/},"transport":/{"method":"webhook","callback":"'\
        f'{call_back_url}'\
        '","secret":"'\
        f'{secret}'\
        '"/}/}'
