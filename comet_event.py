import pygame
from comet import Comet


# class pour event comet
class CometFallEvent:
    # creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 30
        self.game = game
        self.fall_mode = False

        # definir un group pour les comets
        self.all_comet = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        self.all_comet.add(Comet(self))

    def attempt_fall(self):
        #si jauge complete
        if self.is_full_loaded() and len(self.game.all_monster) == 0:
            self.meteor_fall()
            self.reset_percent()
            self.fall_mode = True

    def update_bar(self, surface):

        self.add_percent()

        self.attempt_fall()

        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        pygame.draw.rect(surface, (202, 0, 42), [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])

