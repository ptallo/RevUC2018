import auth
import spotipy
import searchSpotify
import songClass

def createNewPlaylist(twitterHandle):
	spotify = spotipy.Spotify(auth=auth.token)
	if auth.token:
         playlist = spotify.user_playlist_create(auth.username, twitterHandle + "'s Custom Playlist")
         songs = []
         ids = []
         words="happy day night crazy west tomorrow"
         for word in words.split():
            songsTemp = searchSpotify.searchForSongs(word)
            songs.extend(songsTemp)
         for song in songs:
             print(song.getTrackID)
             ids.append(song.getTrackID)