import pygame
import math
from game import Game
pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 60

# Generer la fenetre de jeu + bg
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('./assets/bg.jpg')
# Importation de la banniere
banner = pygame.image.load("./assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4) # permet d'arrondir a l'entier suviant

btn_play = pygame.image.load("./assets/button.png")
btn_play = pygame.transform.scale(btn_play, (400, 150))
btn_play_rect = btn_play.get_rect()
btn_play_rect.x = math.ceil(screen.get_width() / 3.33) # permet d'arrondir a l'entier suviant
btn_play_rect.y = math.ceil(screen.get_height() / 2) # permet d'arrondir a l'entier suviant

# Charger le jeu
game = Game()
running = True

while running:
    # appliquer l'arrière plan du jeu
    screen.blit(background, (0, -200))

    # verifier si le jeu a commencer ou non
    if game.is_playing:
        #declencher les instruc de la partie
        game.update(screen)
    else:
        screen.blit(btn_play, btn_play_rect)
        screen.blit(banner, banner_rect)


    # maj de l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detecter si un joueur lache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # dectecter la touche espace pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verife pour savoir si la souris et en collision avec le btn
            if btn_play_rect.collidepoint(event.pos):
                # lancer le jeu
                game.start()

    #fixer le nbr de FPS
    clock.tick(FPS)