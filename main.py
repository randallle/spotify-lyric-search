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

    sample = my_client.get_saved_tracks().json()
    # print(json.dumps(sample, indent=4, sort_keys=True))
    
    songs_list = sample["items"]

    for song_details in songs_list:
        # print(song_details.keys())
        # print(json.dumps(song_details, indent=4, sort_keys=True))
        print("-", song_details["track"]["name"], "by:", song_details["track"]["artists"][0]["name"])

main()