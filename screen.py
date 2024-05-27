import pygame
import sys
from setting import *
from obstacle import *
from block import *
from portal import *

# 시작 화면 보여주기
def show_start_screen(screen):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 64)
    text = font.render("Press SPACE to Start", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    wait_for_space()


def wait_for_space():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# 클리어 화면
def show_clear_screen(screen):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 64)
    text = font.render("Game Clear!", True, GREEN)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)

# 게임 오버 화면
def show_game_over_screen(screen):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 64)
    text = font.render("Game Over", True, RED)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)

# 요소 그리기 
def draw_game_elements(screen, character_rect):
    pygame.draw.rect(screen, RED, character_rect)
    for block in blocks:
        pygame.draw.rect(screen, platform_color, pygame.Rect(block.x, block.y, platform_width, platform_height))
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, pygame.Rect(obstacle.x, obstacle.y, obstacle_width, obstacle_height))
    if portal:
        pygame.draw.rect(screen, PORTAL_COLOR, portal.rect)
