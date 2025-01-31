import pygame
import random

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("./assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comet.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play("meteorite")

        # verifier si le nbr de comet et de 0
        if len(self.comet_event.all_comet) == 0:
            # remettre la bar à 0
            self.comet_event.reset_percent()
            # faire apparaitre les monstre
            self.comet_event.game.start()
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity
        # ne tombe pas au sol
        if self.rect.y >= 500:
            self.remove()

            if len(self.comet_event.all_comet) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verif si la boule touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_player):
            self.remove()
            self.comet_event.game.player.damage(20)
