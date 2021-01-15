import pygame
from projectile import Projectile

# class pour le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 5 # vitesse de déplacement
        self.all_projectile = pygame.sprite.Group() # groupe de projectile
        self.image = pygame.image.load('./assets/player.png')
        self.rect = self.image.get_rect() # récupérer le mouve du joueur
        self.rect.x = 400 # largeur
        self.rect.y = 500 # hauteur
        self.game = game

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # Si le joueur n'as plus de pts de vie
            self.game.game_over()

    def update_health_bar(self, surface):
        # Dessiner les barres de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def launch_projectile(self):
        # nouvelle instance de la class Projectile
        self.all_projectile.add(Projectile(self)) # ajout du projectile dans le groupe

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity