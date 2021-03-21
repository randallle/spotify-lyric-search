import requests
from secrets import spotify_user_id, spotify_token

BASE_URL = ""

class GeniusClient:

    def __init__(self, genius_user_id, genius_token):
        self.userId = spotify_user_id
        self.token = spotify_token
    
    def getSongLyrics(self):
        pass