import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent

# class pour le jeu
from sounds import SoundManager


class Game():
    def __init__(self):
        # definir si le jeu a commence ou non
        self.is_playing = False
        self.player = Player(self)  # Generer joueur
        self.all_player = pygame.sprite.Group()
        self.all_player.add(self.player)
        self.all_monster = pygame.sprite.Group() # groupe de monstre
        self.sound_manager = SoundManager()
        self.comet_event = CometFallEvent(self)
        self.font = pygame.font.Font("./assets/PottaOne.ttf", 20)
        self.score = 0
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def spawn_monster(self, monster_name):
        self.all_monster.add(monster_name.__call__(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def add_score(self, points=10):
        # ajouter le nbr ptn au score
        self.score += points

    def game_over(self):
        # remettre le jeu a neuf et en attente
        self.all_monster = pygame.sprite.Group()
        self.comet_event.all_comet = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        # jouer le son
        self.sound_manager.play("game_over")

    def update(self, screen):
        # afficher le score sur l'ecran
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # Afficher l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Acualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Actualiser l'animation du joueur
        self.player.update_animation()

        # Actualiser la barre d'event du jeu
        self.comet_event.update_bar(screen)

        # recuperer les projectile du joueur
        for projectile in self.player.all_projectile:
            projectile.move()

        # Recuperer les monstres du jeu
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # Recuperer les comets de notre jeu
        for comet in self.comet_event.all_comet:
            comet.fall()

        # appliquer les images du groupe projectile
        self.player.all_projectile.draw(screen)

        # appliquer les images du groupe monstre
        self.all_monster.draw(screen)

        # appliquer le groupe des comets
        self.comet_event.all_comet.draw(screen)

        # mouvement du joueur a droite ou gauche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()