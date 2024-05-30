import pygame
from setting import *

class Portal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load('portal.png').convert_alpha()  # 이미지 불러오기
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # 이미지 크기 조절
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))  # 이미지 그리기
