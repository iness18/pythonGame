import pygame

class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0 # commencer l'anim a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une methode pour demarrer l'anim
    def start_animation(self):
        self.animation = True

    # definir une methode pour animer le sprite
    def animate(self, loop=False):
        # verifier sir l'animation est active
        if self.animation:
            # passer a l'image suivante
            self.current_image += 1
            # verifier si on est arriver a la fin de l'anim
            if self.current_image >= len(self.images):
                # remettre l'anim au depart
                self.current_image = 0

                # verifier si l'anim n'est pas en mode loop
                if loop is False:
                    # desactivation de l'anim
                    self.animation = False
            # modifier l'image précédente par l'image suivante
            self.image = self.images[self.current_image]


# definir une fonction pour charger les images d'un srpite
def load_animation_images(sprite_name):
    # charger les 24 images du sprite
    images = []
    # recuperer le chemin du dossier pour le sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque image du dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'image
    return images


# def un dictionnaire pour contenir les images chargées des sprites
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player')
}