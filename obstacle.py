import pygame
from setting import *

class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

obstacles = [Obstacle(x, y) for x, y in obstacles_positions]

def check_collision(character, obstacles):
    for obstacle in obstacles:
        if character.colliderect(pygame.Rect(obstacle.x, obstacle.y, obstacle_width, obstacle_height)):
            return obstacle
    return None
