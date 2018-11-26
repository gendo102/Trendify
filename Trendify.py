# https://spotipy.readthedocs.io/en/latest/#authorization-code-flow
# https://github.com/plamere/spotipy
# The MIT License (MIT)
# Copyright (c) 2014 Paul Lamere

# Edited By: Ananya Vittal and Kathleen Gendotti

# pip install spotipy

import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials


# Authorize with client id and client secret
client_id = "1c65cc2af3e74c5bb4c116447dce2d59"
client_secret = "9f3aedb877604a2ba0499296a4f2a720"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print

def one():
    # User inputs artist name and prints popular tracks
    artist_name = " "
    artist_name = raw_input("Enter an artist name to display their popular tracks: ")
    results = sp.search(q=artist_name, limit=20)
    for i, t in enumerate(results['tracks']['items']):
        print ' ', i, t['name']
    print

def two():
    # User inputs artist name and prints related artists
    artist_name = raw_input("Enter an artist name to display related artists: ")
    result = sp.search(q='artist:' + artist_name, type='artist')
    try:
        name = result['artists']['items'][0]['name']
        uri = result['artists']['items'][0]['uri']

        related = sp.artist_related_artists(uri)
        print'Related artists for', name
        for artist in related['artists']:
            print ' ', artist['name']
    except:
        print "usage show_related.py [artist-name]"

    print

def three():
    # Authenticates user and displays user's favorite songs
    username = raw_input("Enter the username to your Spotify account: ")
    scope = 'user-library-read'
    client_id = '1c65cc2af3e74c5bb4c116447dce2d59'
    client_secret = '9f3aedb877604a2ba0499296a4f2a720'
    redirect_uri = 'https://www.spotify.com/us/'

    token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        print "Loading your Favorite Songs..."
        print
        for item in results['items']:
            track = item['track']
            print track['name'] + ' - ' + track['artists'][0]['name']
    else:
        print "Can't get token for", username

print

def four():
    username = raw_input("Enter the username to your Spotify account: ")
    scope = 'user-library-read'
    client_id = '1c65cc2af3e74c5bb4c116447dce2d59'
    client_secret = '9f3aedb877604a2ba0499296a4f2a720'
    redirect_uri = 'https://www.spotify.com/us/'

    token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.current_user_playlists(limit=50)
        for i, item in enumerate(results['items']):
            print("%d %s" %(i, item['name']))
    else:
        print("Can't get token for", username)
print

options = { 1: one,
            2: two,
            3: three,
            4: four,
}

print("Welcome to Trendify!")
display_menu = raw_input("Would you like to view the menu? (Y/N)")
while(display_menu != "N"):
    print("\n Menu: ")
    print("Option #1: Display an artists popular tracks")
    print("Option #2: Display related artists")
    print("Option #3: Display your most played songs")
    print("Option #4: Display your playlists")
    print("Option #5: Exit")
    number = raw_input("Please enter the number of the option you want: ")
    if(number == "1"):
        options[1]()
    elif(number == "2"):
        options[2]()
    elif(number == "3"):
        options[3]()
    elif(number == "4"):
        options[4]()
    elif(number == "5"):
        exit()
