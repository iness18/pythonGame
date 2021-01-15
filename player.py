import pygame
from projectile import Projectile

# class pour le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5 # vitesse de déplacement
        self.all_projectile = pygame.sprite.Group() # groupe de projectile
        self.image = pygame.image.load('./assets/player.png')
        self.rect = self.image.get_rect() # récupérer le mouve du joueur
        self.rect.x = 400 # largeur
        self.rect.y = 500 # hauteur

    def launch_projectile(self):
        # nouvelle instance de la class Projectile
        self.all_projectile.add(Projectile(self)) # ajout du projectile dans le groupe

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity