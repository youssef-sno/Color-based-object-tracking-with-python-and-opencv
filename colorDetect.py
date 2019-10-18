print(__doc__)
#Authors : Zouhir Amrani && Youssef Snoussi
#Contact : youssef.snoussi199@hotmail.com



import cv2
import numpy as np

def imgeDetect(x,color):
	# dictionnaire des couleurs HSV
	clr = {"orangeLower": [1,190,200], "orangeUpper": [18,255,255],
	"redLower":[160,20,70] , "redUpper":[190,255,255],
	"yellowLower":[27,200,176], "yellowUpper":[180,255,255],
	"greenLower":[53, 168,10],"greenUpper":[95, 255,198],
	"blueLower":[94, 80,20], "blueUpper":[126, 255,255]

	}
	# dictionnaire des couleurs BGR
	coloR = {
	"red": (0,0,255), "yellow": (0,255,255),
	"green": (0,255,0), "blue":(255,0,0),
	"orange": (0,165,255)
	}

	colorLower =color+'Lower' 
	colorUpper= color+'Upper'
	print(colorLower)
	print(colorUpper)
	print(clr.get(colorUpper))

	# creation des tableau de couleurs de type indexer (0-255)
	ColorLower = np.array(clr.get(colorLower), dtype = "uint8")
	ColorUpper = np.array(clr.get(colorUpper), dtype = "uint8")

	# licture de  l'image 
	img = cv2.imread(x)
	
	#creation des maskes binaire
	#Conversion de l'espace colorimétrique de BGR à HSV 
	hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	#Génération de masque pour détecter la couleur
	blue1 = cv2.inRange(hsv_img ,ColorLower, ColorUpper)
	blue2 = cv2.morphologyEx(blue1, cv2.MORPH_CLOSE, np.ones((5,5),np.uint8),iterations=2)
	blue3 = cv2.morphologyEx(blue2, cv2.MORPH_OPEN, np.ones((5,5),np.uint8),iterations=2)
	mask = cv2.bitwise_and(img,img,mask=blue3)

	# trouver les contours 
	(cnts,_) = cv2.findContours(blue3.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	#######  PLUSIEURS OBJETS AVEC LA MEME COULEUR #######

	for i,contour in (enumerate(cnts)):
		# surface de contour 
		area = cv2.contourArea(contour)
		print(area)
		if(area>900):
			# calculer le cadre de sélection (tourné) autour
			x,y,h,w = cv2.boundingRect(contour)
			# ecrire la couleur sur limage 
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(img, color, (x,y), font, 1, coloR.get(color), 2, cv2.LINE_AA)
			# contour et puis dessinez (boxPoints : fixer les 4 points du rectangle)(minAreaRect : determine la surface minimal) 
			rect = np.int32(cv2.boxPoints(cv2.minAreaRect(contour)))
			cv2.drawContours(img, [rect], -1, (0, 255, 0), 2)

  	# affichage des resultat 	
	cv2.imshow('resultat', img)
	cv2.imshow('detection du couleur',mask)

	 

	cv2.waitKey(0)
	cv2.destroyAllWindows()





