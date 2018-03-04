
import auth
import spotipy
import searchSpotify
import songClass

def createNewPlaylist(twitterHandle):
	spotify = spotipy.Spotify(auth=auth.token)
	if auth.token:
         playlist = spotify.user_playlist_create(auth.username, twitterHandle + "'s Custom Playlist")
         playlistID = playlist['id']
         songs = []
         uris = 'uris'
         words="happy day night crazy west tomorrow"
         for word in words.split():
            songsTemp = searchSpotify.searchForSongs(word)
            songs.extend(songsTemp)
         print('  ')
         print(len(songs))
         spotify.user_playlist_add_tracks(auth.username, playlistID, songs, position=None)

         url = playlist['external_urls']['spotify']
