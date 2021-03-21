import requests
from secrets import spotify_user_id, spotify_token

BASE_URL = "https://api.spotify.com/v1/"

class SpotifyClient:

    def __init__(self, spotify_user_id, spotify_token):
        self.userId = spotify_user_id
        self.token = spotify_token

    def getSavedTracks(self, headers):
        url = BASE_URL + "me/tracks"
        r = requests.get(url, headers=headers, params = {"limit":50})

