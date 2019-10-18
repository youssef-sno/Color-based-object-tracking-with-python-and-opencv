print(__doc__)
#Authors : Zouhir Amrani && Youssef Snoussi
#Contact : youssef.snoussi199@hotmail.com


from tkinter import * 
import cv2
from tkinter.filedialog import *
from track import *
from tkinter.messagebox import *
from colorDetect import *
from button import *
from buttonD import *
from cap import *
# interface graphique
def intrfaceP():
	# creation de la fenetre et la nommer
	win = Tk()
	win.title("Suivi d'objets")

	#integrer une photo a l'interieur de la fenetre
	photo = PhotoImage(file="track2.png")

	canvas = Canvas(win,width=1000, height=600)
	canvas.create_image(0, 0, anchor=NW, image=photo)
	
	#les fonction executer lors de l'appuis d'un bouton
	def cap_magic_temp():
		pass 
	
	def cap_magic():
		win.destroy()
		CAP(0)
		intrfaceP()


	def T_video():
		filepath = askopenfilename(title="Ouvrir une image",filetypes=[('avi files','.avi'),('all files','.*')])
		if filepath != '':
			win.destroy()
			COLOR(filepath)
			intrfaceP()
		else:
			pass
	
	def T_temp():
		win.destroy()
		COLOR(0)
		intrfaceP()

	def D_image():
 		filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
 		if filepath == '':
 			pass
 		else:
 			win.destroy()
 			COLOR1(filepath)
 			intrfaceP()

 	#creatin des bouttons
	Button(text='Suivi en temps reel', width =30, command=T_temp, bg ="white").place( x=40, y=430)
	Button(text='Suivi par video enregistrer', width =30,  command=T_video, bg ="red").place(x=300, y=430)
	Button(text='Cap magic en temps reel', width =30,  command=cap_magic, bg ="yellow").place(x=40, y=470)
	Button(text='Cap magic par video enregistrer', width =30,  command=cap_magic_temp, bg ="cyan").place(x=300, y=470)
	Button(text='Detection de couleurs dans une image', width =67,  command=D_image, bg ="pink").place(x=40, y=510)
	#affichage de la fenetre
	canvas.pack()
	win.mainloop()

intrfaceP()
