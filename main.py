import pygame
import sys
import random
from setting import *
from character import *
from block import *
from portal import *
from obstacle import *
from screen import *

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("점프 점프")

clock = pygame.time.Clock()

# 게임 시작 페이지 표시
show_start_screen(screen)

# 초기 설정
reset_game()

# 게임 루프
running = True

while running:
    screen.fill(WHITE)
    character_rect = pygame.Rect(character_x, character_y, character_width, character_height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_pressed = False

    if not game_over:
        handle_game_events(event)
        update_game_state()
        draw_game_elements(screen, character_rect)

        if game_clear:
            show_clear_screen(screen)
        elif game_over:
            show_game_over_screen(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
