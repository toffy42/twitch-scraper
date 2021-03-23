Welcome to Twitch scraper

1) Download from Git (already done, well done)
2) Install required libs from  requirements with pip
3) Run python models.py (to create the tables. Once off operation)
4) Run python app.py

The server should be running.

Test Requests:
curl http://0.0.0.0:8080/v1/users  (Should return [])

curl http://0.0.0.0:8080/v1/users/add/shroud
curl http://0.0.0.0:8080/v1/users/add/tsm_viss

curl http://0.0.0.0:8080/v1/users  (Should return [shroud, tsm_viss])

curl http://0.0.0.0:8080/v1/users/delete/tsm_viss

curl http://0.0.0.0:8080/v1/users  (Should return [shroud])
