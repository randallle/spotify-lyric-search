import requests
import json

# Import/declare global variables
from spotifysecrets import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
BASE_URL = "https://api.spotify.com/v1/"

class SpotifyClient:

    # Constructor 
    def __init__(self):
        self.spotify_client_id = SPOTIFY_CLIENT_ID
        self.spotify_client_secret = SPOTIFY_CLIENT_SECRET
        self.accessToken = self.get_access_token(self.spotify_client_id, self.spotify_client_secret)
        self.headers = {"Authorization": f"Bearer {self.accessToken}"}

    
    # Requests access and returns the authorization token to be assigned as an instance variable in the constructor 
    def get_access_token(self, client_id, client_secret):
        auth_response = requests.post(
            "https://accounts.spotify.com/api/token",
            {
                "grant_type": "client_credentials",
                "client_id": client_id,
                "client_secret": client_secret,
                "scope": "user-library-read"
            }
        )
        print(auth_response.json())
        return auth_response.json()["access_token"]

    # Gets the last 50 saved tracks and returns them in a JSON format
    def get_saved_tracks(self):
        query = BASE_URL + "me/tracks"
        response = requests.get(
            query,
            headers = self.headers,
            params = {
                "limit": 50
            }
        )

        return response
    
    