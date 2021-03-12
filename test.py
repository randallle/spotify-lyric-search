import requests

# declare parameters for post request
AUTH_URL = "https://accounts.spotify.com/api/token"
CLIENT_ID = ""
CLIENT_SECRET = ""

# send post request
auth_response = requests.post(AUTH_URL,
                             {"grant_type": "client_credentials",
                              "client_id": CLIENT_ID,
                              "client_secret": CLIENT_SECRET
                              })

# convert data to json
auth_response_data = auth_response.json()

# retrieve access token
access_token = auth_response_data["access_token"]

