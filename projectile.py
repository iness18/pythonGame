import pygame

# Classe ppur gerer les projectiles
class Projectile(pygame.sprite.Sprite):
    #constructeur
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("./assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50)) # redimensionne l'image du projectile
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80

    def move(self):
        self.rect.x += self.velocity
        # condition pour verifier si le projectile n'est plus present sur l'ecran
        if self.rect.x > 1080:
            # suppr le projectile
            self.player.all_projectile.remove(self)