print(__doc__)
#Authors : Zouhir Amrani && Youssef Snoussi
#Contact : youssef.snoussi199@hotmail.com



from tkinter import * 
import cv2
from tkinter.filedialog import *
from tkinter.messagebox import *
from track import *


# interface graphique
def COLOR(x):
	# creation de la fenetre et la nommer
	win1= Tk()
	win1.title("choix de couleur")
	#integrer une photo a l'interieur de la fenetre
	photo = PhotoImage(file="track2.png")

	canvas = Canvas(win1,width=1000, height=600)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	#les fonction executer lors de l'appuis d'un bouton	
	def red():
		
		TRACK(x,'red')

	def blue():
		TRACK(x,'blue')

	def yellow():
		TRACK(x,'yellow')

	def green():
		TRACK(x,'green')

	def orange():
		TRACK(x,'orange')
		
 	#creatin des bouttons
	Button(text='   red  ',command=red,width =10  ,bg='red').place( x=40, y=500)
	Button(text='  blue  ',command=blue,width =10 ,bg='blue').place( x=140, y=500)
	Button(text='  green ',command=green,width =10 ,bg='green').place( x=240, y=500)
	Button(text=' yellow ',command=yellow,width =10 ,bg='yellow').place( x=340, y=500)
	Button(text=' orange ',command=orange,width =10 ,bg='orange').place( x=440, y=500)
	#affichage de la fenetre
	canvas.pack()
	win1.mainloop()

