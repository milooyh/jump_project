import random
import pygame
from setting import *

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

blocks = [Block(x, y) for x, y in blocks_positions]

def check_collision(character, blocks):
    for block in blocks:
        if character.colliderect(pygame.Rect(block.x, block.y, platform_width, platform_height)):
            return block
    return None

def add_new_platform():
    x = random.randint(0, SCREEN_WIDTH - platform_width)
    y = random.randint(0, SCREEN_HEIGHT // 2)
    blocks.append(Block(x, y))
