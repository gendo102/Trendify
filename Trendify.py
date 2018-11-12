#pip install spotipy

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Authorize with client id and client secret
client_credentials_manager = SpotifyClientCredentials(client_id='1c65cc2af3e74c5bb4c116447dce2d59', client_secret='9f3aedb877604a2ba0499296a4f2a720')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = input("Enter an artist name to print their popular tracks: ")
results = sp.search(q=artist_name, limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])
