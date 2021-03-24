import unittest
from unittest.mock import patch
import api


class test_api(unittest.TestCase):
    def test_get_user_data(self):
        class TestUser():
            username = 'cousin'
            stream_url = 'test'
            profile_pic_url = 'pic'
            platform = 'platform'

        with patch('api.Streamer.get') as s_mock:
            s_mock.return_value = TestUser
            result = api.get_user_data('test')
            assert result == '{"username": "cousin", "stream_url": "test", "pic_url": "pic", "platform": "platform"}'


unittest.main()
