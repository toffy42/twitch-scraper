Welcome to Twitch scraper

1) Download from Git (already done, well done)
2) Install required libs from  requirements with pip
3) Run python models.py (to create the tables. Once off operation)
4) You will need twitch client_id, secret_key. See twitch docs on how to get these: https://dev.twitch.tv/docs/authentication
   This info should be saved in a file called key_file.py
   client_id = 'xxxxx'
   secret = 'xxxxx'
   Without this the project can't connect to twitch

5) Run python app.py

The server should be running.

Test Requests:
curl http://0.0.0.0:8080/v1/users  (Should return [])

curl http://0.0.0.0:8080/v1/users/add/shroud
curl http://0.0.0.0:8080/v1/users/add/tsm_viss

curl http://0.0.0.0:8080/v1/users  (Should return [shroud, tsm_viss])

curl http://0.0.0.0:8080/v1/users/delete/tsm_viss

curl http://0.0.0.0:8080/v1/users  (Should return [shroud])
