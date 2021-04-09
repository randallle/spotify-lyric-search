import requests
import json
import os
import base64
import six
import six.moves.urllib.parse as urllibparse
from six.moves.urllib_parse import parse_qsl, urlparse
import webbrowser

# Import/declare global variables
from spotifysecrets import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
BASE_URL = "https://api.spotify.com/v1/"

class SpotifyClient:
    OAUTH_AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
    OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

    # Constructor 
    def __init__(
        self,
        client_id=None,
        client_secret=None,
        redirect_uri=None,
        state=None,
        scope=None,
        username=None,
        open_browser=True,
    ):
        self.spotify_client_id = client_id
        self.spotify_client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.state = state
        self.scope = scope

        self.token = self.get_access_token()
        self.headers = {
            'Authorization': 'Bearer {token}'.format(token=self.token)
        }

    def get_authorization_url(self):
        
        payload = {
            "client_id": self.spotify_client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "scope": self.scope
        }
        
        urlparams = urllibparse.urlencode(payload)

        return "%s?%s" % (self.OAUTH_AUTHORIZE_URL, urlparams)

    def parse_auth_response(self, url):
        url_components = urlparse(url)
        query = url_components.query
        form = dict(parse_qsl(query))
        return tuple(form.get(param) for param in ["state", "code"])

    def get_auth_response(self):
        url = self.get_authorization_url()
        webbrowser.open(url)
        redirect_url = input("Enter the URL you were redirected to: ")
        state, code = self.parse_auth_response(redirect_url)
        return code
    
    def make_authorization_headers(self, client_id, client_secret):
        auth_header = base64.b64encode(
            six.text_type(client_id + ":" + client_secret).encode("ascii")
        )
        return {"Authorization": "Basic %s" % auth_header.decode("ascii")}

    def get_access_token(self):
        payload = {
            "grant_type": "authorization_code",
            "code": self.get_auth_response(),
            "redirect_uri": self.redirect_uri
        }

        headers = self.make_authorization_headers(self.spotify_client_id, self.spotify_client_secret)

        response = requests.post(
            self.OAUTH_TOKEN_URL,
            data=payload,
            headers=headers
        )

        return response.json()["access_token"]




    # Requests access and returns the authorization token to be assigned as an instance variable in the constructor 
    # def get_access_token(self, client_id, client_secret):
    #     auth_response = requests.post(
    #         "https://accounts.spotify.com/api/token",
    #         {
    #             "grant_type": "client_credentials",
    #             "client_id": client_id,
    #             "client_secret": client_secret,
    #             "scope": "user-library-read"
    #         }
    #     )
    #     print(auth_response.json())
    #     return auth_response.json()["access_token"]

    # Gets the last 50 saved tracks and returns them in a JSON format
    def get_saved_tracks(self):
        query = BASE_URL + "me/tracks"
        response = requests.get(
            query,
            headers = self.headers,
            params = {
                "limit": 50,
                "offset": 0
            }
        )
        return response
    
    