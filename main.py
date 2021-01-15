import pygame
from game import Game
pygame.init()

# Generer la fenetre de jeu + bg
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('./assets/bg.jpg')

# Charger le jeu
game = Game()

running = True

while running:
    # appliquer l'arrière plan du jeu
    screen.blit(background, (0, -200))

    # Afficher l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # recuperer les projectile du joueur
    for projectile in game.player.all_projectile:
        projectile.move()

    # appliquer les images du groupe projectile
    game.player.all_projectile.draw(screen)

    # mouvement du joueur a droite ou gauche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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