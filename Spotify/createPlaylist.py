import spotipy
import spotipy.util as util
from twitter import TweetData
import json

SPOTIPY_CLIENT_ID='58a4cf7549014e37a775cc19ce2fcb68'
SPOTIPY_CLIENT_SECRET='be9d8b777a8a48b59a62ced8bdf094b3'
SPOTIPY_REDIRECT_URI='http://localhost/'

scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public '
scope += 'playlist-modify-private streaming ugc-image-upload user-follow-modify '
scope += 'user-follow-read user-library-read user-library-modify user-read-private '
scope += 'user-top-read user-read-playback-state user-modify-playback-state '
scope += 'user-read-currently-playing user-read-recently-played'
username='obnijrubnzhegv3mrw8c4rr7f'

token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)

spotify = spotipy.Spotify(auth=token)

def searchForSongs(word):
    results = spotify.search(word, limit=1, offset=0, type='track')
    tracks=results['tracks']['items']
    trackArr = []
    for x in range(1):
        results = spotify.next(results['tracks'])
        tracks.extend(results['tracks']['items'])
    for track in tracks:
        trackArr.append(track['id'])
    return trackArr

def createNewPlaylist(TweetData, keywords):
	if token:
         playlist = spotify.user_playlist_create(username, TweetData.getUserName() + "'s Custom Playlist")
         playlistID = playlist['id']
         songs = []
         for word in keywords:
            songsTemp = searchForSongs(word)
            songs.extend(songsTemp)
         spotify.user_playlist_add_tracks(username, playlistID, songs, position=None)
         TweetData.setPlaylistLink(playlist['external_urls']['spotify'])
