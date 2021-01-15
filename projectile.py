import pygame

# Classe ppur gerer les projectiles
class Projectile(pygame.sprite.Sprite):
    # constructeur
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load("./assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50)) # redimensionne l'image du projectile
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # Tourner le projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center) # Rotation par rapport au centre de l'image

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # sile projectile entre en collision avec le monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            # Supprimer le projectile
            self.remove()
            # infliger les degats
            monster.damage(self.player.attack)

        # condition pour verifier si le projectile n'est plus present sur l'ecran
        if self.rect.x > 1080:
            # suppr le projectile
            self.remove()