import pygame
from setting import *

# obstacle.py

class Obstacle:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def update_position(self):
        self.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, obstacle_color, pygame.Rect(self.x, self.y, obstacle_width, obstacle_height))

    @staticmethod
    def check_collision(character_x, character_y, character_width, character_height, obstacles):  
        for obstacle in obstacles:
            if pygame.Rect(character_x, character_y, character_width, character_height).colliderect(pygame.Rect(obstacle.x, obstacle.y, platform_width, platform_height)):
                return obstacle
        return None
