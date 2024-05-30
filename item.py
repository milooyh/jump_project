import pygame
from setting import *

class Item:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

class HeartItem(Item):
    def __init__(self, x, y):
        super().__init__(x, y, 'heart.png')

class SpeedItem(Item):
    def __init__(self, x, y):
        super().__init__(x, y, 'slow.png')

class InvincibilityItem(Item):
    def __init__(self, x, y):
        super().__init__(x, y, 'star.png')
