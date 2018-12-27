#! /usr/bin/python3

def dice(nombre):
	dice = []
	for i in range(nombre) :
		dice.append(math.ceil(random.uniform(0,6)))
	dice.sort(reverse = True)

	return (dice)

import random
import math


while True :

	print("Nombre d'attaquants ?")
	attaquants = int(input())
	print("Nombre de défenseur ?")
	defenseurs = int(input())

	print(str(attaquants) + " vs " + str(defenseurs))
	print("===========")

	while (attaquants != 0 and defenseurs != 0):
		if attaquants >= 3 :
			diceNbrAttaquant = 3
		else :
			diceNbrAttaquant = attaquants

		if defenseurs >= 2 :
			diceNbrDefenseur = 2
		else :
			diceNbrDefenseur = defenseurs

		diceAttaquant = dice(diceNbrAttaquant)
		diceDefenseur = dice(diceNbrDefenseur)

		print("Dés attaquants :")

		for i in range(diceNbrAttaquant) :
			print(diceAttaquant[i])

		print ("Dés défenseurs : ")
		for i in range(diceNbrDefenseur) :
			print(diceDefenseur[i])
		print("------------------------------")

		for i in range (min(diceNbrAttaquant,diceNbrDefenseur)) :
			if diceAttaquant[i] > diceDefenseur[i] :
				defenseurs = defenseurs - 1
			else :
				attaquants = attaquants - 1 

		print(str(attaquants) + " vs " + str(defenseurs))
		print('===================')

	print("=========================")
	print("Résultat :")
	if attaquants == 0:
		vainqueur = "Défenseur"
		survivants = defenseurs
	else:
		vainqueur = "Attaquant"
		survivants = attaquants
	print("Vainqueur : " + vainqueur)
	print(str(survivants) + " régiment(s) ont survécu")

	print("#####################################")