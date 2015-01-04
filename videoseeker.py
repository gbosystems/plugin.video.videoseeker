import sys
import xbmcplugin, xbmcgui, xbmcaddon, xbmc
import urlparse
from threading import Thread

class GSPlayer( xbmc.Player ):

	offset = '0.0'
	playbackStarted = False

	def __init__( self ):
		pass

	def isPlaybackStarted(self):
		return self.playbackStarted

	def onPlayBackStarted( self ):
		self.seekTime(float(offset))
		self.playbackStarted = True

def Log(message):
	toPrint = "VIDEOSEEKER: " + message
	print toPrint
	return

def SeekerThread(offset):
	player = GSPlayer()
	player.offset = offset
	while(not player.isPlaybackStarted()):
		xbmc.sleep(100)

# Setup
addon_handle = int(sys.argv[1])
Log("VideoSeeker started.")
Log("VideoSeeker args: " + sys.argv[2])

# Handle the arguments
parsed = urlparse.urlparse(sys.argv[2])
params = urlparse.parse_qs(sys.argv[2][1:])
media = params['media'][0]
offset = params['offset'][0]

# Start a monitor thread
thread = Thread(target = SeekerThread, args = (offset, ))
thread.start()

# Make the item to be played
listitem = xbmcgui.ListItem(path=media)
xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)