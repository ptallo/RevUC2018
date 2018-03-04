import auth
import spotipy

def createNewPlaylist(twitterObject):
	spotify = spotipy.Spotify(auth=auth.token)
	if token:
		playlist = spotify.user_playlist_create(auth.username,twitterHandle + "'s Custom Playlist", public=True,"This is a public playlist custom made for "+twitterHandle)