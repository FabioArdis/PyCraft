import pygame, sys
from pygame.locals import*

#Colori
BLACK 	= (0, 0, 0)
BROWN 	= (153, 76, 0)
GREEN 	= (0, 255, 0)
BLUE 	= (0, 0, 255)
WHITE	= (255, 255, 255)

#Tilemap

DIRT 	= 0
GRASS 	= 1
WATER 	= 2
COAL 	= 3

#Dizionario che collega risorse <-> colori
textures= {
		DIRT 	: pygame.image.load('dirt.png'),
		GRASS 	: pygame.image.load('grass.png'),
		WATER 	: pygame.image.load('water.png'),
		COAL 	: pygame.image.load('coal.png')
	}

#Dizionario che collega risorse <-> oggetto
inventory = {
		DIRT:	0,
		GRASS:	0,
		WATER:	0,
		COAL:	0
	}


#Variabili utili
TILESIZE 	= 40
MAPWIDTH 	= 15
MAPHEIGHT 	= 15



#Lista che rappresenta la tilemap
import random
resources 	= [DIRT, GRASS, WATER, COAL]
tilemap 	= [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

#Loop per riga
for rw in range(MAPHEIGHT):
	#Loop per colonna
	for cl in range(MAPWIDTH):
		#Prendi un numero tra 0 e 15
		randomNumber = random.randint(0, 15)
		#Se è zero allora carbone
		if randomNumber == 0:
			tile = COAL
		#Invece acqua se è 1 o 2
		elif randomNumber == 1 or randomNumber == 2:
			tile = WATER
		elif randomNumber >= 3 and randomNumber <= 7:
			tile = GRASS
		else:
			tile = DIRT
		#Trasforma la posizione nel tilemap in una casuale
		tilemap[rw][cl] = tile


print(tilemap)

#Aziona il display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPWIDTH*TILESIZE + 50))

#Carico l'immagine del giocatore
PLAYER 		= pygame.image.load('player.png').convert_alpha()
#Posizione del giocatore
playerPos	 = [0, 0]

INVFONT = pygame.font.Font('FreeSansBold.fon', 18)

while True:
	#Ricettore eventi
	for event in pygame.event.get():
		#Evento quit
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		#Se viene premuto un tasto
		elif event.type == KEYDOWN:
			#Se viene premuta la freccia destra
			if(event.key == K_RIGHT) and playerPos[0] < MAPWIDTH - 1:
				#Cambia la posizione del giocatore
				playerPos[0] += 1
			#//sinistra
			if(event.key == K_LEFT) and playerPos[0] > 0:
				#Cambia la posizione del giocatore
				playerPos[0] -= 1
			#//sotto
			if(event.key == K_DOWN) and playerPos[1] < MAPHEIGHT - 1:
				#Cambia la posizione del giocatore
				playerPos[1] += 1
			#//sopra
			if(event.key == K_UP) and playerPos[1] > 0:
				#Cambia la posizione del giocatore
				playerPos[1] -= 1
			#//Spazio
			if event.key == K_SPACE:
				#Su che risorsa si trova il personaggio?
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				#Ora il giocatore ha +1 risorsa su cui si trova
				inventory[currentTile] += 1
				#Il giocatore ora si trova su della terra
				tilemap[playerPos[1]][playerPos[0]] = DIRT
			#Piazza la terra
			print(inventory)
			if(event.key == K_1):
				#Su che risorsa è posizionato?
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				#Se abbiamo della terra nell'inventario
				if inventory[DIRT] > 0:
					#Elimina e posiziona la terra
					inventory[DIRT] -= 1
					tilemap[playerPos[1]][playerPos[0]] = DIRT
					#Scambia l'oggetto che c'era prima
					inventory[currentTile] += 1

	#Loop per riga
	for row in range(MAPHEIGHT):
		#Loop per colonna
		for column in range(MAPWIDTH):
			#Disegna la tilemap
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))

	#Disegna il giocatore nella posizione corretta
	DISPLAYSURF.blit(PLAYER, (playerPos[0]*TILESIZE, playerPos[1]*TILESIZE))

	#Visualizza l'inventario dopo 10 px
	placePosition = 10
	for item in resources:
		#Aggiunge l'immagine
		DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT*TILESIZE+5))
		placePosition += 50
		#Aggiunge il testo con l'ammonto dell'oggetto nell'inventario
		textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
		DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT*TILESIZE+20))
		placePosition += 50


	#Aggiorna il display
	pygame.display.update()

