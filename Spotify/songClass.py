import spotipy

class songClass:

	def __init__(self, songURI, songID):
		self.album = ''
		self.artists = []
		self.availableMarket = []
		self.disc_num = 0
		self.duration = 0.0000
		self.explicit = False
		self.playalbe = True
		self.trackID = songID
		self.name = ''
		self.popularity = 0
		self.trackNum = 0
		self.uri = songURI

	def getName(self):
		return self.name

	def getTrackID(self):
		return self.trackID

	def getTrackURI(self):
		return self.uri

