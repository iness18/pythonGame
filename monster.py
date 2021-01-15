import pygame
import random

# creer la class monstre
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.velocity = random.randint(1, 3)
        self.image = pygame.image.load("./assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.game = game

    def damage(self, amount):
        # Infliger les dégats
        self.health -= amount

        # verifier le nombre de pts de vie
        if self.health <= 0:
            # reapparaitre le monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 3)

    def update_health_bar(self, surface):
        # Dessiner les barres de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        else:
            # Infliger des degats aux joueurs
            self.game.player.damage(self.attack)