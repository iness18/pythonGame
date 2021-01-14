import pygame
from player import Player

# class pour le jeu
class Game():
    def __init__(self):
        #Generer joueur
        self.player = Player()
        self.pressed = {}