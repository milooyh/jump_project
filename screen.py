import pygame
from setting import *
from obstacle import *
from block import *
from portal import *

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

def show_game_over_screen(screen):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 64)
    text = font.render("Game Over", True, RED)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(text, text_rect)
    try_again_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
    exit_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 60, 200, 50)
    pygame.draw.rect(screen, GREEN, try_again_button_rect)
    pygame.draw.rect(screen, RED, exit_button_rect)
    font = pygame.font.Font(None, 36)
    try_again_text = font.render("Try Again", True, BLACK)
    exit_text = font.render("Exit", True, BLACK)
    screen.blit(try_again_text, try_again_text.get_rect(center=try_again_button_rect.center))
    screen.blit(exit_text, exit_text.get_rect(center=exit_button_rect.center))
    pygame.display.update()

def show_clear_screen(screen):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 64)
    text = font.render("Game Clear!", True, GREEN)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()

def draw_game_elements(screen, character_rect):
    pygame.draw.rect(screen, LIGHT_RED, character_rect)
    pygame.draw.rect(screen, FLOOR_COLOR, (LEFT_EDGE, floor_y, SCREEN_WIDTH, floor_height))
    for block in blocks:
        pygame.draw.rect(screen, LIGHT_GREEN, (block.x, block.y, platform_width, platform_height))
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, (obstacle.x, obstacle.y, obstacle_width, obstacle_height))
    if portal:
        pygame.draw.rect(screen, PORTAL_COLOR, portal.rect)

    if collision_message:
        font = pygame.font.Font(None, 36)
        collision_text = font.render(collision_message, True, RED)
        screen.blit(collision_text, (20, 20))
