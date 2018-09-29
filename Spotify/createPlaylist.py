import spotipy
import spotipy.util as util
#from twitter import TweetData
import json
import os

SPOTIPY_CLIENT_ID='25337649bc04488da3e0b18801feea86'
SPOTIPY_CLIENT_SECRET='ae422600a201405081753306b0720f4a'
SPOTIPY_REDIRECT_URI='http://localhost/'

scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public '
scope += 'playlist-modify-private streaming ugc-image-upload user-follow-modify '
scope += 'user-follow-read user-library-read user-library-modify user-read-private '
scope += 'user-top-read user-read-playback-state user-modify-playback-state '
scope += 'user-read-currently-playing user-read-recently-played'
username = 'obnijrubnzhegv3mrw8c4rr7f'

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

def getPlaylistSongsGenres():
    spotify = spotipy.Spotify(auth=token)
    userID = 1258592749
    playlistID = '1fVHU0nJqHmHlF7tzOkYC4'
    acceptedGenres = ['pop', 'rock', 'country', 'rap', 'hip hop', 'jazz', 'edm', 'classical']

    playlistInfo = spotify.user_playlist_tracks(userID, playlist_id=playlistID, offset=0)
    newPlaylistInfo = json.dumps(playlistInfo['items'])
    data = json.loads(newPlaylistInfo)

    file = open("/Users/christopherochs/HackAThon/TwitterSpotifyML/RevUC2018/SpotifyPlaylistOutput.txt", "w")

    for x in range(9):
        playlistInfo = spotify.user_playlist_tracks(userID, playlist_id=playlistID, offset=x*100)
        newPlaylistInfo = json.dumps(playlistInfo['items'])
        data += json.loads(newPlaylistInfo)

    for item in data:
        trackName = item['track']['name']
        artistID = item['track']['artists'][0]['id']
        artistInfo = spotify.artist(artistID)
        artistGenres = artistInfo['genres']
        approvedGenres = ''
        for genre in artistGenres:
            if(genre in acceptedGenres):
                if (approvedGenres != ''):
                    approvedGenres += (', ' + genre)
                else:
                    approvedGenres += (genre)
        if approvedGenres != '':
            file.write(trackName + ' : ' + approvedGenres + '\n')
    print(len(data))

    file.close()

