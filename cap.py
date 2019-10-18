print(__doc__)
#Authors : Zouhir Amrani && Youssef Snoussi
#Contact : youssef.snoussi199@hotmail.com



import cv2
import numpy as np
import time


def CAP(file):
	
	# Création d'un objet VideoCapture
	cap = cv2.VideoCapture(file)

	# Nous donnons un peu de temps à la caméra pour la configuration
	time.sleep(3)
	count = 0
	#background=0

	# Capture et stockage du cadre d'arrière-plan statique
	for i in range(60):
		ret,background = cap.read()

	background = np.flip(background,axis=1)

	while(cap.isOpened()):
		ret, img = cap.read()
		if not ret:
			break
		count+=1
		print(count)
		img = np.flip(img,axis=1)
	
		# Conversion de l'espace colorimétrique de BGR à HSV
		hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

		# Génération de masque pour détecter la couleur
		lower_color = np.array([34,12,61])
		upper_color = np.array([97,87,255])
		mask1 = cv2.inRange(hsv,lower_color,upper_color)

		lower_color = np.array([255,255,255])
		upper_color = np.array([255,255,255])
		mask2 = cv2.inRange(hsv,lower_color,upper_color)

		mask3 = mask1+mask2

		# Affinage du masque correspondant à la couleur détectée
		mask1 = cv2.morphologyEx(mask3, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
		mask1 = cv2.dilate(mask3,np.ones((3,3),np.uint8),iterations = 1)
		mask2 = cv2.bitwise_not(mask3)

		# Générer le résultat final
		res1 = cv2.bitwise_and(background,background,mask=mask3)
		res2 = cv2.bitwise_and(img,img,mask=mask2)
		final_output = cv2.addWeighted(res1,1,res2,1,0)
		# affichage de resultat 
		cv2.imshow('backGround',background)
		cv2.imshow('Cape Magic !!!',final_output)
		cv2.imshow('video orrigine',img)
		

		k = cv2.waitKey(1)
		if k == 27:
			break
	cap.release()
	cv2.destroyAllWindows()



