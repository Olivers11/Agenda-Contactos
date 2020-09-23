import eel 
import sys
from modules.classes import *
sys.path.append('..')
eel.init('templates')

obj = App()

@eel.expose
def Hello():
	main()


@eel.expose
def INIT(n, t):
	obj.InsertContact(n, t)
	obj.PrintElements()


@eel.expose
def GET(n):
	return obj.NameForPosition(n)
	


@eel.expose
def DELETE(n):
	obj.Delete(n)



eel.start("index.html", size=(600,700))