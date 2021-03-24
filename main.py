from spotifyclient import SpotifyClient

import requests
import json

def main():
    my_client = SpotifyClient()
    songs = my_client.get_saved_tracks()
    print(songs)
    # "Only endpoints that do not access user information can be accessed"
    # Resolve this issue via a different authorization flow

main()