import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


base_url = 'https://api.spotify.com/v1'

clientID = 'ca24e70ef438475ab53fc53c5838ff74'
Client_secret = 'b6f11da3989d4cd9919b86e3bd03c3e3'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=clientID,
                                                           client_secret=Client_secret))

results = sp.search(q='As It WasHarry Styles', limit=1)

song = results["tracks"]["items"][0]["external_urls"]["spotify"]

print(song)