import spotipy
import spotipy.util as util
#from twitter import TweetData
import json
import os

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
    results = spotify.next(results['tracks'])
    try:
        tracks.extend(results['tracks']['items'])
    except TypeError:
        pass
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

def getPlaylist():
    spotify = spotipy.Spotify(auth=token)
    userID = 1258592749
    playlistID = '75Jkqn3PbntniS7Q4Pf3YK'
    playlistInfo = spotify.user_playlist_tracks(userID, playlist_id=playlistID)
    newPlaylistInfo = json.dumps(playlistInfo['items'])
    data = json.loads(newPlaylistInfo)
    print(data)
    print(type(newPlaylistInfo))
    print(type(data))



    '''
    file = open("/Users/christopherochs/HackAThon/TwitterSpotifyML/RevUC2018/SpotifyPlaylistOutput.txt","w")
    file.write(playlistInfo['items'])
    file.close()
    '''

getPlaylist()

