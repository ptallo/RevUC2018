import spotipy
import auth
import json
import songClass

def searchForSongs(word):
	spotify = spotipy.Spotify(auth=auth.token)
	results = spotify.search(word, limit=1, offset=0,type='track')
	#file = open("outputfile.txt", 'w')
	#file.write(json.dumps(results))
	trackStr = ''
	tracks = results['tracks']['items']
	for x in range(10):
		results = spotify.next(results['tracks'])
		tracks.extend(results['tracks']['items'])
	for track in tracks:
		trackStr += track['name']
		trackStr += ' '
	print(trackStr)



