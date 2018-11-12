# https://spotipy.readthedocs.io/en/latest/#authorization-code-flow
# https://github.com/plamere/spotipy
# The MIT License (MIT)
# Copyright (c) 2014 Paul Lamere

# Edited By: Ananya Vittal and Kathleen Gendotti

# pip install spotipy

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Authorize with client id and client secret
client_id = "1c65cc2af3e74c5bb4c116447dce2d59"
client_secret = "9f3aedb877604a2ba0499296a4f2a720"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# User inputs artist name and prints popular tracks
artist_name = input("Enter an artist name to display their popular tracks: ")
results = sp.search(q=artist_name, limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])

print("--------------------------------------------------------")

# User inputs artist name and prints related artists
artist_name = input("Enter an artist name to display related artists: ")
result = sp.search(q='artist:' + artist_name, type='artist')
try:
    name = result['artists']['items'][0]['name']
    uri = result['artists']['items'][0]['uri']

    related = sp.artist_related_artists(uri)
    print('Related artists for', name)
    for artist in related['artists']:
        print('  ', artist['name'])
except:
    print("usage show_related.py [artist-name]")

print("--------------------------------------------------------")
