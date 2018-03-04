import spotipy

class songClass:

	def __init__(self, songName, songID):
		self.album = ''
		self.artists = []
		self.availableMarket = []
		self.disc_num = 0
		self.duration = 0.0000
		self.explicit = False
		self.playalbe = True
		self.trackID = songID
		self.name = songName
		self.popularity = 0
		self.trackNum = 0
		self.uri = ''

	def getName(self):
		return self.name

	def getTrackID(self):
		return self.trackID

