import pygame
import random
from setting import *
from block import *
from obstacle import *

character_width = 20
character_height = 20
character_speed = 6
jump_speed = 20
gravity = 1.4
character_x = SCREEN_WIDTH // 2
character_y = SCREEN_HEIGHT - character_height * 2

vertical_momentum = 0
is_on_ground = True

space_pressed = False
life = 3
game_over = False
game_clear = False

collision_message = ""
collision_time = 0

item_effects = {}
effect_start_time = {}

# 캐릭터 초기 위치 설정
def set_character_initial_position():
    global character_x, character_y, life
    character_x = SCREEN_WIDTH // 2
    character_y = SCREEN_HEIGHT - character_height * 2
    life = 3

# 게임 재설정
def reset_game():
    global character_x, character_y, vertical_momentum, is_on_ground, space_pressed, life, game_clear, game_over, collision_message, collision_time, item_effects, effect_start_time, portal
    set_character_initial_position()
    vertical_momentum = 0
    is_on_ground = True
    space_pressed = False
    life = 3
    game_over = False
    game_clear = False
    collision_message = ""
    collision_time = 0
    item_effects = {}
    effect_start_time = {}
    portal = None

# 게임 상태 업데이트
def update_game_state():
    global character_x, character_y, vertical_momentum, is_on_ground, life, game_over, game_clear, portal
    current_time = pygame.time.get_ticks()

    # 스페이스 입력 + 바닥에 있으면 점프
    if space_pressed and is_on_ground:
        vertical_momentum = -jump_speed
        is_on_ground = False

    # 키 입력에 따라 캐릭터 좌우 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x = max(LEFT_EDGE, character_x - character_speed)
    if keys[pygame.K_RIGHT]:
        character_x = min(RIGHT_EDGE, character_x + character_speed)

    # 캐릭터가 일정 위치 넘어가면 화면 이동
    if character_x > screen_move_threshold:
        dx = character_x - screen_move_threshold
        for block in blocks:
            block.x -= screen_move_speed
        for obstacle in obstacles:
            obstacle.x -= screen_move_speed
        character_x -= screen_move_speed

    # 캐릭터가 화면 안에서 움직이도록 범위 제한
    character_x = max(0, min(SCREEN_WIDTH - character_width, character_x))
    vertical_momentum += gravity
    character_y += vertical_momentum
    character_y = min(character_y, floor_y - character_height)

    # 캐릭터가 바닥에 도달하면 세로 운동량 초기화
    if character_y >= floor_y - character_height:
        character_y = floor_y - character_height
        vertical_momentum = 0
        is_on_ground = True

    # 캐릭터가 발판과 충돌하면 바닥으로 이동
    block_collided = check_collision(pygame.Rect(character_x, character_y, character_width, character_height), blocks)
    obstacle_collided = check_collision(pygame.Rect(character_x, character_y, character_width, character_height), obstacles)
    if block_collided:
        if vertical_momentum > 0:
            character_y = block_collided.y - character_height
            vertical_momentum = 0
            is_on_ground = True
            
    # 장애물과 충돌하면 생명을 감소시키거나 게임 오버 여부 판단
    if obstacle_collided:
        life -= 1
        if life == 0:
            game_over = True
        else:
            set_character_initial_position()
            vertical_momentum = 0
            is_on_ground = True

    # 포털과 충돌하면 게임 클리어 상태로 변경
    if portal and pygame.Rect(character_x, character_y, character_width, character_height).colliderect(portal.rect):
        game_clear = True
