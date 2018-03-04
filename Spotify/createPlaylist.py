import auth
import spotipy
import searchSpotify

def createNewPlaylist():
	spotify = spotipy.Spotify(auth=auth.token)
	if auth.token:
		word="happy day night crazy west tomorrow"
		
		#playlist = spotify.user_playlist_create(auth.username,twitterHandle + "'s Custom Playlist", public=True,"This is a public playlist custom made for "+twitterHandle)