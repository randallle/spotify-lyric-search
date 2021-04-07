from spotifyclient import SpotifyClient
from spotifysecrets import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

import requests
import json

def main():
    my_client = SpotifyClient(
        client_id=SPOTIFY_CLIENT_ID, 
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri="https://www.google.com/",
        scope="user-library-read"
    )

    print(my_client.get_saved_tracks().json())

main()