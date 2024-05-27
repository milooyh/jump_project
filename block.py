import pygame
from setting import *

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, platform_color, pygame.Rect(self.x, self.y, platform_width, platform_height))