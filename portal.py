import pygame
from setting import *

class Portal:
    def __init__(self, x, y):
        self.width = 50
        self.height = 50
        self.x = SCREEN_WIDTH - self.width - 20
        self.y = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
portal = None
