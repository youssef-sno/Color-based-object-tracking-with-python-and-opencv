print(__doc__)
#Authors : Zouhir Amrani && Youssef Snoussi
#Contact : youssef.snoussi199@hotmail.com



from tkinter import * 
import cv2
from tkinter.filedialog import *
from tkinter.messagebox import *
from track import *
from colorDetect import *



# interface graphique
def COLOR1(x):
	# creation de la fenetre et la nommer
	win1= Tk()
	win1.title("Detection de couleurs dans une image")
	photo = PhotoImage(file="track2.png")
	#integrer une photo a l'interieur de la fenetre
	canvas = Canvas(win1,width=1000, height=600)
	canvas.create_image(0, 0, anchor=NW, image=photo)

	#les fonction executer lors de l'appuis d'un bouton
	def red():
		showinfo('info', "Apuyer sur 'q' pour arrêter l'affichage ")
		imgeDetect(x,'red')

	def blue():
		showinfo('info', "Apuyer sur 'q' pour arrêter l'affichage ")
		imgeDetect(x,'blue')

	def yellow():
		showinfo('info', "Apuyer sur 'q' pour arrêter l'affichage ")
		imgeDetect(x,'yellow')

	def green():
		showinfo('inf', "Apuyer sur 'q' pour arrêter l'affichage ")
		imgeDetect(x,'green')

	def orange():
		showinfo('Titre 3', "Apuyer sur 'q' pour arrêter l'affichage ")
		imgeDetect(x,'orange')
		
 	#creatin des bouttons
	Button(text='   red  ',command=red ,width =10 ,bg='red').place( x=40, y=470)
	Button(text='  blue  ',command=blue,width =10 ,bg='blue').place( x=140, y=470)
	Button(text='  green ',command=green,width =10 ,bg='green').place( x=240, y=470)
	Button(text=' yellow ',command=yellow,width =10 ,bg='yellow').place( x=340, y=470)
	Button(text=' orange ',command=orange,width =10 ,bg='orange').place( x=440, y=470)
	#affichage de la fenetre
	canvas.pack()
	win1.mainloop()


