import pygame

class Comet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = 1

    def fall(self):
        self.rect.y += self.velocity

