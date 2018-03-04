import spotipy
import auth
import json
import songClass


def searchForSongs(word):
    print('The word is: ' + word)
    spotify = spotipy.Spotify(auth=auth.token)
    results = spotify.search(word, limit=1, offset=0, type='track')
    trackArr = []
    tracks = results['tracks']['items']
    for x in range(10):
        results = spotify.next(results['tracks'])
        tracks.extend(results['tracks']['items'])
    for track in tracks:
        newSong = songClass.songClass(track['name'], track['id'])
        print(track['name'])
        print(track['id'])
        trackArr.append(newSong)
    return trackArr