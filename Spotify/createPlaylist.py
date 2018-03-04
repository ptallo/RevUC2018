from twitter import TweetData
import auth
import spotipy
import searchSpotify
import songClass

def createNewPlaylist(TweetData):
	spotify = spotipy.Spotify(auth=auth.token)
	if auth.token:
         playlist = spotify.user_playlist_create(auth.username, TweetData.getUserName() + "'s Custom Playlist")
         playlistID = playlist['id']
         songs = []
         uris = 'uris'
         words = TweetData.getTimeline()[0]
         for word in words.split():
            songsTemp = searchSpotify.searchForSongs(words)
            songs.extend(songsTemp)
         print('  ')
         print(len(songs))
         spotify.user_playlist_add_tracks(auth.username, playlistID, songs, position=None)
         TweetData.setPlaylistLink(playlist['external_urls']['spotify'])
