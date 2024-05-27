import pygame
import sys
from setting import *
from obstacle import Obstacle
from block import Block
from portal import Portal

class ScreenManager:
    def __init__(self):
        pass

    @staticmethod
    def show_start_screen(screen):
        print('show_start_screen 함수 호출')

        screen.fill(WHITE)
        font = pygame.font.Font(None, 64)
        text = font.render("Press SPACE to Start", True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        ScreenManager.wait_for_space()

    @staticmethod
    def wait_for_space():
        print('wait_for_space 함수 호출')
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False

    @staticmethod
    def show_clear_screen(screen):
        print('show_clear_screen 함수 호출')

        screen.fill(WHITE)
        font = pygame.font.Font(None, 64)
        text = font.render("Game Clear!", True, GREEN)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)

    @staticmethod
    def show_game_over_screen(screen):
        print('show_game_over_screen 함수 호출')

        screen.fill(WHITE)
        font = pygame.font.Font(None, 64)
        text = font.render("Game Over", True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)

    @staticmethod
    def draw_game_elements(screen, character_rect):
        print('draw_game_elements 함수 호출')

        pygame.draw.rect(screen, RED, character_rect)
        for block in Block:
            pygame.draw.rect(screen, platform_color, pygame.Rect(block.x, block.y, platform_width, platform_height))
        for obstacle in Obstacle:
            pygame.draw.rect(screen, obstacle_color, pygame.Rect(obstacle.x, obstacle.y, obstacle_width, obstacle_height))
        if Portal:
            pygame.draw.rect(screen, PORTAL_COLOR, Portal.rect)
