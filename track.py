print(__doc__)
#Authors : Zouhir Amrani && Youssef Snoussi
#Contact : youssef.snoussi199@hotmail.com


# importer les packages nécessaire
import numpy as np
import argparse
import time
import cv2

def TRACK(file,color):
	
	clr = {"orangeLower": [0,84,150], "orangeUpper": [12,255,255],
	"redLower":[160,20,70] , "redUpper":[190,255,255],
	"yellowLower":[9,0,133], "yellowUpper":[79,255,255],
	"greenLower":[25, 189,118],"greenUpper":[95, 255,198],
	"blueLower":[94, 175,20], "blueUpper":[126, 255,255]

	}

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
	
	# dtype = "uint8" est un type de donner dans python (0<int<255)
	ColorLower = np.array(clr.get(colorLower), dtype = "uint8")
	ColorUpper = np.array(clr.get(colorUpper), dtype = "uint8")
	# charger la vidéo
	camera = cv2.VideoCapture(file)

	
	while True:
		# saisir le cadre actuel
		(grabbed, frame) = camera.read()
		# vérifier pour voir si nous avons atteint la fin de la video
		if not grabbed:
			break

		# déterminer quels pixels tombent dans les limites de la couleur
		# et ensuite brouiller l'image binaire
		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		#Génération de masque pour détecter la couleur
		coloR1 = cv2.inRange(hsv_frame, ColorLower, ColorUpper)
		#ScoloR = cv2.GaussianBlur(coloR1, (3,3), 0)
		ScoloR = cv2.morphologyEx(coloR1, cv2.MORPH_OPEN, np.ones((5,5),np.uint8),iterations=2)

		# trouver des contours dans l'image
		(cnts, _) = cv2.findContours(ScoloR.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)

		
		

		# vérifier si des contours ont été trouvés
		if len(cnts) > 0:
			# trier les contours et trouver le plus grand
			cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
			#A jouter le nom du couleur 
			x,y,h,w = cv2.boundingRect(cnt)
			print(file)
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(frame, color, (x,y), font, 1, coloR.get(color), 2, cv2.LINE_AA)
			# calculer le cadre de sélection (tourné) autour 
			# contour et puis dessinez		
			rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
			cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

		# montrer le cadre et l'image binaire
		cv2.imshow("Tracking", frame)
		cv2.imshow("hsv", coloR1)

		
		time.sleep(0.025)

		# si la touche 'q' est enfoncée, arrête la boucle
		if cv2.waitKey(10) & 0xFF == ord("q"):
			break

	# cleanup the camera and close any open windows
	camera.release()
	cv2.destroyAllWindows()

