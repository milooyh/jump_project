import pygame
from setting import *

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, obstacle_color, pygame.Rect(self.x, self.y, obstacle_width, obstacle_height))