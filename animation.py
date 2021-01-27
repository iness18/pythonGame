import pygame

class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')

# definir une fonction pour charger les images d'un srpite

def load_animation_images(sprite_name):
    # charger les 24 images du sprite
    images = []
    # recuperer le chemin du dossier pour le sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque image du dossier
    for num in range(1, 24):
        image_path = path + num + '.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'image
    return images


# def un dictionnaire pour contenir les images chargées des sprites
animations = {
    'mummy': load_animation_images('mummy')
}