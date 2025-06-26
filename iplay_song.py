import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import sys

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
redirect_uri = "http://127.0.0.1:8000/callback"

query = " ".join(sys.argv[1:])
scope = "user-read-playback-state user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))

results = sp.search(q=query, type='track', limit=1)
tracks = results['tracks']['items']

if tracks:
    webbrowser.open(tracks[0]['external_urls']['spotify'])
else:
    print("Song not found.")
