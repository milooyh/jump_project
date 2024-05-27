import pygame
from setting import *

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, platform_color, pygame.Rect(self.x, self.y, platform_width, platform_height))
        
    # 충돌 감지
    def check_collision(self, character):
        for block in Block:
            if character.colliderect(pygame.Rect(block.x, block.y, platform_width, platform_height)):
                return block
        return None