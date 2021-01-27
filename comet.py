import pygame
import random

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("./assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(20, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comet.remove(self)

    def fall(self):
        self.rect.y += self.velocity
        # ne tombe pas au sol
        if self.rect.y >= 500:
            print("test")
            self.remove()

            if len(self.comet_event.all_comet):
                print("test")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verif si la boule touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_player):
            self.remove()
            self.comet_event.game.player.damage(20)
