import spotipy
import auth
import songClass
import json


def searchForSongs(word):
    print('The word is: ' + word)
    spotify = spotipy.Spotify(auth=auth.token)
    results = spotify.search(word, limit=1, offset=0, type='track')
    tracks=results['tracks']['items']
    trackArr = []
    for x in range(1):
        results = spotify.next(results['tracks'])
        tracks.extend(results['tracks']['items'])
    for track in tracks:
        newSong = songClass.songClass(track['uri'], track['id'])
        print(track['uri'])
        print(track['id'])
        trackArr.append(track['id'])
    return trackArr