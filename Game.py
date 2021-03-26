"""
The point of this exercise is to use the data structure pile to create a pile of card
"""


import random as r
from time import sleep
import pygame
import sys

def jeudecarte():
    """
    Create a 52 card game and shuffle it.
    """
    jeu = []
    for x in range(1,14):
        if x == 1:#1 is replace by A for AS
            n = "A"
        elif x == 11:#11 is replace by V for Valet
            n = "V"
        elif x == 12:#11 is replace by Q for Queen
            n = "Q"
        elif x == 13:#13 is replace by K for King
            n = "K"
        else:#Else, the value stay the same
            n = x
        for y in range(0,4):#Create 12 card for every color
            if y == 0:
                c = "♠"
            elif y == 1:
                c = "♦"
            elif y == 2:
                c = "♣"
            else:
                c = "♥"
            carte = str(n),c
            jeu.append(carte)
            
    r.shuffle(jeu)
    return jeu

def valor(x):
    """
    This function change head with a value and a value-1 so it can compare 2 card later. (Because you can't compare str and int.)
    """
    if x == "A":
        return 13
    elif x == "K":
        return 12
    elif x == "Q":
        return 11
    elif x == "V":
        return 10
    else:
        return int(x)-1
    
def color(card):
    """
    return the color of a card depending of his symbol
    """
    if card[1] == "♥" or card[1] == "♦":
        return "red"
    elif card[1] == "♣" or card[1] == "♠":
        return "black"
        
def win(liste1,liste2) :
    """
    Compare 2 the value of 2 cards, the highest win and if it's equal return "egalite". We don't comapre the color of the card, just the Value
    """
    if valor(liste1[0])>valor(liste2[0]):
        return "p1"
    
    elif valor(liste1[0]) < valor(liste2[0]):
        return "p2"
    
    else:
        return "egalite"
    
def loose(player, compteur, mode):
    """
    When a player wins, it plays a song to celebrate your victory.
    For the war game, show which player wins
    For the rob, show in how many trys you win.
    """
    clap.play()
    fenetre.blit(fond, (0,0))
    if mode == 1:
        fin = font.render(f'You win in {compteur} try !',True, (0,0,0))
        fenetre. blit(fin, (75,300))
    else:
        won = font.render(f'{player} Win !',True, (0,0,0))
        fenetre.blit(won, (150,300))
    
    
def load(carte):
    """
    with the value and the color of the card, we search into a folder the picture of the card that correspond and load it so we can show it with pygame
    """
    x = str(carte[0])
    if carte[1] == "♠":#replace this symbole by "pique" to find the good picture
        y="pique"
    elif carte[1] == "♦":
        y="carreau"
    elif carte[1] == "♥":
        y="coeur"
    else:
        y="trefle"
    x = "cartes/"+x+"_"+y+".gif"
    return pygame.image.load(x)

def b_starting(main1, main2):
    """
    Show information about the war game
    """
    fenetre.blit(p1, (100,10))#Show player1
    fenetre.blit(p2, (300,10))
    nb_card1 = font.render(str(len(main1))+'Cartes',True, (0,0,0))#load and show the number of card of each players
    fenetre.blit(nb_card1, (100,270))
    nb_card2 = font.render(str(len(main2))+'Cartes',True, (0,0,0))
    fenetre.blit(nb_card2, (300,270))
    #create a deck of card for each players
    for i in range(len(main1)):
        fenetre.blit(dos_carte, (100-i,300))
    for y in range(len(main2)):
        fenetre.blit(dos_carte, (300-y,300))
 
def detect(mode):
    """
    This program is used to create a pause in the programm, if it is the war game, you can press any buttons to skip it
    If it is the red or black game, you must press r or b
    """
    epic = True
    while epic == True:
        for event in pygame.event.get():#Detect an input/event
            if event.type == pygame.KEYDOWN:#If a key is pressed
                if mode == 1:#if it is rob game
                    if event.key == pygame.K_b:#if the b ket is pressed
                        return "black"
                    if event.key == pygame.K_r:#if the r ket is pressed
                        return "red"
                else:
                    return None

def rob():
    """
    This is the second game of this programm, the point is to choose between 2 colors of card and o finish the deck with the least try.
    If your guess is right, you win a point and +1 to your attemps and get rid of the card
    If your guess is wrong, the card goes to the end of the deck and +1 ti you attemps
    """
    shuffle.play()#play a shuffle sound
    #loading screen at the begining
    fenetre.blit(shuffling, (175,250))
    pygame.display.flip()
    sleep(1)
    fenetre.blit(fond, (0,0))
    pygame.display.flip()
    
    jeu = jeudecarte()#create a deck of card and shuffke it
    #create variable
    play = True
    point = 0 #gains 1 for each good guess
    compteur_coup = 0 #gains 1 for every trys
    
    while play == True:
        main = []
        #show important indication
        fenetre.blit(fond, (0,0))
        fenetre.blit(color_q, (15,10))
        fenetre.blit(tuto, (20,100))
        
        if compteur_coup == 0:
            #Show the number of cards
            nb_card = font.render(str(len(jeu))+' Cards',True, (0,0,0))
            fenetre.blit(nb_card, (175,400))
            
            #Show the number of try
            compteur = font.render(str(compteur_coup) +' Trys',True, (0,0,0))
            fenetre.blit(compteur, (350,465))
            
            #Show your points
            points =  font.render(str(point)+' Points',True, (0,0,0))
            fenetre.blit(points, (5,465))
            
            #Show your deck of card
            for i in range(len(jeu)): 
                fenetre.blit(dos_carte, (100-(i/2),200))
            pygame.display.flip()
            
        #take the last card of the deck and show it
        main = jeu.pop()
        fenetre.blit(load(main), (300,200))
        
        #if the color of the card is what you guessed, you win
        if color(main) == detect(1):
            fenetre.blit(bravo, (150,150))
            point += 1
        else:#Else, you loose and the card goes at the back of the deck
            fenetre.blit(dommage,(170,150))
            liste = [main]
            jeu = liste + jeu
        
        #Show the number of cards
        nb_card = font.render(str(len(jeu))+' Cards',True, (0,0,0))
        fenetre.blit(nb_card, (175,400))
        
        #Show the number of try
        compteur = font.render(str(compteur_coup) +' Trys',True, (0,0,0))
        fenetre.blit(compteur, (350,465))
        
        #Show your points
        points =  font.render(str(point)+' Points',True, (0,0,0))
        fenetre.blit(points, (5,465))
        
        #Show your deck of card
        for i in range(len(jeu)): 
            fenetre.blit(dos_carte, (100-(i/2),200))
        pygame.display.flip()
        
        compteur_coup += 1
        #If the deck of card is empty, wou win !
        if len(jeu) == 0:
            sleep(1)
            loose(0, compteur_coup, 1)
            break
            
def bataille():
    """
    Classical war card game but in python. The objective is to win all Cards !
    If the value of a player's card is higher than his ennemy, he wins his card and the card of his enemy
    but if the value is the same, you both are putting a reverse card on top of ht one you played and another one on top. Then you compare the Value
    if a player win, he wins all cards but if it's equal, the card are share
    """
    shuffle.play()#shuffle sound
    #Show a "loading screen"
    fenetre.blit(shuffling, (175,250))
    pygame.display.flip()
    sleep(1)
    
    jeu = jeudecarte()#create a deck of card 
    main1 = jeu[:len(jeu)//2]#Cut the deck in half and give it to each player
    main2 = jeu[len(jeu)//2:]
    reserve = []
    play = True
    while play == True:
        jeu1 = main1.pop()#Take the last card to each player's deck
        jeu2 = main2.pop()
        
        fenetre.blit(fond, (0,0))
        b_starting(main1, main2)
        fenetre.blit(load(jeu1), (100,50))#Show the card of each players
        fenetre.blit(load(jeu2), (300,50))
        pygame.display.flip()
        
        detect(0)#Wait for the player to pressa key
        
        partie = win(jeu1,jeu2)#See which player win withe the value of the card
        
        if partie == "p1":#The Value of the player's 1 car his higher than the the player 2
            liste = [jeu2,jeu1] #Add every card played into the deck of player 1
            main1 = liste+main1
            
            
        elif partie == "p2":
            liste = [jeu1,jeu2]
            main2 = liste+main2
        
        else:#Value are the same
            #I use try except methode because if a player has 1 card remaining, he loose. Because he can't pick a card from an empty deck
            try:
                rancon1 = main1.pop() #The card that is reverse 
                attaque1 = main1.pop() #The card on top
            except:#If a player can't pick a card from his deck
                main1 = []
                loose("player2", 0,0)
                break
            
            try:
                rancon2 = main2.pop()
                attaque2 = main2.pop()
            except:
                main2=[]
                loose("player1", 0,0)
                break
            
            #show the back of a card, to represent the reverse card
            fenetre.blit(dos_carte, (100,50))
            fenetre.blit(dos_carte, (300,50))
            pygame.display.flip()
            detect(0)
            #Show the card that each player put on top
            fenetre.blit(load(attaque1), (100,50))
            fenetre.blit(load(attaque2), (300,50))
            pygame.display.flip()
            detect(0)
            reserve = [rancon1,rancon2,attaque1,attaque2,jeu1,jeu2] #Put every card played into a "bank"
            bataille = win(attaque1,attaque2)#see which player has the highest value with the card on top
            #The player who wins, win every card
            if bataille == "p1":
                main1= reserve + main1
                
            elif bataille == "p2":
                main2= reserve + main2
            #If the value is the same, the bank is split 
            else:
                main1 = reserve[:len(reserve)//2] + main1
                main2 = reserve[len(reserve)//2:] + main2
            reserve = []
        #See if a player's deck is empty 
        if main1 == []:
            play=loose("player2", 0,0)#Tell that player 2 win
        
        if main2 == []:
            play=loose("player1", 0,0)
        
        
#Create a pygame window
pygame.init()
fenetre = pygame.display.set_mode((500, 500))
#The background :
fond = pygame.image.load("cartes/background.png").convert()
fenetre.blit(fond, (0,0))
pygame.display.flip()
#Define image or text used later
dos_carte = pygame.image.load('cartes/dos.png')#Back_card
font = pygame.font.Font('freesansbold.ttf', 32)#font of text
batailles = font.render('War Game : Press space',True, (0,0,0))
robs = font.render('Red or black : Press 0',True, (0,0,0))
p1 = font.render('Player 1',True, (0,0,0))
p2 = font.render('Player 2',True, (0,0,0))
shuffling = font.render('Shuffling... ',True, (0,0,0))
color_q = font.render("What's the next card color ? ",True, (0,0,0))
tuto = font.render('Press b for black or r for red ! ',True, (250,250,250))
bravo = font.render('Well played ! ',True, (255, 255, 0))
dommage = font.render('Too bad...',True, (255, 255, 0))
#Musics
shuffle = pygame.mixer.Sound("Son/shuffle.wav")
clap = pygame.mixer.Sound("Son/clap.wav")
pygame.mixer.music.load('Son/casino.mp3')
pygame.mixer.music.play(-1)

continuer = 1
while True:
    fenetre.blit(batailles, (5,10))#Show the text to know how to start
    fenetre.blit(robs, (5,50))
    for event in pygame.event.get():#Detect an input/event
        if event.type == pygame.QUIT:#If the user click the exit button of the window, quit the program
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:#If a key is pressed
            if event.key == pygame.K_SPACE:#if this key is space
                fenetre.blit(fond, (0,0))#Show the background
                bataille()#Launch the war card game
            if event.key == pygame.K_0:
                fenetre.blit(fond, (0,0))
                rob()#Lauche red or black game
    pygame.display.flip()#Refresh the window




