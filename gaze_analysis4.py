import numpy as np
import socket
import time
import ctypes

elementsx = [] #liste pour contenant les 10 premieres valeurs de x
elementsy = []#liste pour récupérer les 10 premières valeurs de y
elementst = []#liste pour récupérer le temps de sejour dans une position donnée (x,y)
nMaxElementx = 1000 #taille de la liste des x
nMaxElementy = 1000 #taille de la liste des y
nMaxElementt = 1000 #taille de la liste des t
etatrobot= 5
decision = 5

#récupère la taille de l'écran en pixels
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
widthScreen = user32.GetSystemMetrics(0)
heightScreen = user32.GetSystemMetrics(1)
float(widthScreen)
float(heightScreen)
print(widthScreen)
print(heightScreen)


while True:
	line = input()

	if line.startswith("Gaze Data:"):
		coord = eval(line[12:line.find(")")])
		x = coord[0]
		y = coord[1]
		t = eval(line[line.find("p ") + 1: line.find("ms")])
		data = [x, y, t]

		#print(data)

		x = float(x)  # conversion des x en float
		y = float(y)  # conversion des y en float
		t = int(t) #conversion des t en entier

		elementsx.append(x)  # ajout des x à la liste des x
		elementsy.append(y)  # ajout des y à la liste des y
		elementst.append(t)  # ajout des t à la liste des t

		# on supprime eventuellement la donnée plus anciennes (les x et les y )

		if ((len(elementsx) >= nMaxElementx) and (len(elementsy) >= nMaxElementy) and (len(elementst) >= nMaxElementt)):
			elementsx.pop(0)
			elementsy.pop(0)
			elementst.pop(0)


		# on calcule la moyenne sur la liste des x et la liste des y séparément
		if (elementst[-1] - elementst[0] > 1750):
			a = (elementst[-1] - elementst[0])
			print(a, len(elementst))
			meanPosx = np.mean(elementsx)
			meanPosy = np.mean(elementsy)
			# on a pris un échantillon de données déjà généré, on a extrait le max sur la liste des x et le max sur la liste des y
			# ce la nous a permis de diviser widthScreen par 5 et heightScreen par 5 et cela nous donne 9 cases de 20% qu'on a délimité par les seuils de division par 5
			# enfin, on intègre notre (meanPosx, meanPosy) dans l'intervalle correspondant à la case

			if ((0.0 <= meanPosx <= widthScreen/5) and (4*heightScreen/5 <= meanPosy <= heightScreen)):
							direction=1
							if (etatrobot==direction):
								pass
							elif ((etatrobot+direction)/2==5):
								decision = 5
								etatrobot = 5
							else:
								decision = 1
								etatrobot = 1
							print(decision)
			elif ((2*widthScreen/5 <= meanPosx <= 3*widthScreen/5) and (4*heightScreen/5 <= meanPosy <= heightScreen)): #en bas
							direction = 2
							if (etatrobot == direction):
								pass
							elif ((etatrobot + direction) / 2 == 5):
								decision = 5
								etatrobot = 5
							else:
								decision = 2
								etatrobot = 2
							print(decision)
			elif ((4*widthScreen/5 <= meanPosx <= widthScreen) and (4*heightScreen/5 <= meanPosy <= heightScreen)): #en bas à droite
							direction = 3
							if (etatrobot == direction):
								pass
							elif ((etatrobot + direction) / 2 == 5):
								decision = 5
								etatrobot = 5
							else:
								decision = 3
								etatrobot = 3
							print(decision)
			elif ((0.0 <= meanPosx <= widthScreen/5) and (2*heightScreen/5 <= meanPosy <= 3*heightScreen/5)): #à gauche
							direction = 4
							if (etatrobot == direction):
								pass
							elif ((etatrobot + direction) / 2 == 5):
								decision = 5
								etatrobot = 5
							else:
								decision = 4
								etatrobot = 4
							print(decision)
			elif ((4*widthScreen/5 <= meanPosx <= widthScreen) and (2*heightScreen/5 <= meanPosy <= 3*heightScreen/5)): #à droite
							direction = 6
							if (etatrobot == direction):
								pass
							elif ((etatrobot + direction) / 2 == 5):
								decision = 5
								etatrobot = 5
							else:
								decision = 6
								etatrobot = 6
							print(decision)
			elif ((0.0 <= meanPosx <= widthScreen/5) and (0.0 <= meanPosy <= heightScreen/5)): #en haut à gauche
							direction = 7
							if (etatrobot == direction):
								pass
							elif ((etatrobot + direction) / 2 == 5):
								decision = 5
								etatrobot = 5
							else:
								decision = 7
								etatrobot = 7
							print(decision)
			elif ((2*widthScreen/5 <= meanPosx <= 3*widthScreen/5) and (0.0 <= meanPosy <= heightScreen/5)): #en haut
							direction = 8
							if (etatrobot == direction):
								pass
							elif ((etatrobot + direction) / 2 == 5):
								decision = 5
								etatrobot = 5
							else:
								decision = 8
								etatrobot = 8
							print(decision)
			elif ((4*widthScreen/5 <= meanPosx <= widthScreen) and (0.0 <= meanPosy <= heightScreen/5)):#en haut à droite
							direction = 9
							if (etatrobot == direction):
								pass
							elif ((etatrobot + direction) / 2 == 5):
								decision = 5
								etatrobot = 5
							else:
								decision = 9
								etatrobot = 9
							print(decision)
						#elif ():
						#	print ("Vous regardez en dehors de l'écran")
						#	pass


			msgFromClient = str(decision)  # on insère la décision récupérée

			bytesToSend = str.encode(msgFromClient)

			serverAddressPort = ("91.168.94.41", 32800)

			bufferSize = 1024

			# Create a UDP socket at client side

			UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

			# Send to server using created UDP socket

			UDPClientSocket.sendto(bytesToSend, serverAddressPort)

			elementsx.clear()
			elementsy.clear()
			elementst.clear()

	if line.startswith("exiting"):
		break
