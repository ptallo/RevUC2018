import sys
import spotipy
import spotipy.util as util

SPOTIPY_CLIENT_ID='58a4cf7549014e37a775cc19ce2fcb68'
SPOTIPY_CLIENT_SECRET='62641c88588a4d4f8effd925b3c1206c'
SPOTIPY_REDIRECT_URI='http://localhost/'

scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public '
scope += 'playlist-modify-private streaming ugc-image-upload user-follow-modify '
scope += 'user-follow-read user-library-read user-library-modify user-read-private '
scope += 'user-top-read user-read-playback-state user-modify-playback-state '
scope += 'user-read-currently-playing user-read-recently-played'
username='obnijrubnzhegv3mrw8c4rr7f'

token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI)
