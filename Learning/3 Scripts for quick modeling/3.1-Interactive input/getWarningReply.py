from abaqus import *
from abaqusConstants import *

reply = getWarningReply(message='Would you like to close the window?', buttons = (YES,NO))
if reply == YES:
	print('clicked YES')
elif reply == NO:
	print('clicked NO')
