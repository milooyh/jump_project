import pygame
import sys
import random
from setting import *
from character import *
from platform import *
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

# 이벤트 처리 함수
def handle_game_events(event):
    global space_pressed, running
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            space_pressed = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            space_pressed = False
            
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

        handle_game_events(event)  # 수정된 부분

    if not game_over:
        update_game_state()
        draw_game_elements(screen, character_rect)  # 추가된 부분

        if game_clear:
            show_clear_screen(screen)
        elif game_over:
            show_game_over_screen(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
