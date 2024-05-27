import pygame
from setting import *
from block import *
from screen import *

def set_character_initial_position():
    global character_x, character_y
    character_x = SCREEN_WIDTH // 2
    character_y = SCREEN_HEIGHT - character_height * 2

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

    # 포털 생성
    if len(blocks) > 0:
        last_block = blocks[-1]
        portal = Portal(last_block.x, last_block.y - 70)
    else:
        portal = None

def handle_game_events(event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if game_over:
            if try_again_button_rect.collidepoint(event.pos):
                reset_game()
            elif exit_button_rect.collidepoint(event.pos):
                running = False

def update_game_state():
    global vertical_momentum, character_y, is_on_ground, character_x, game_clear, game_over, life

    current_time = pygame.time.get_ticks()
    if current_time - last_platform_time > new_platform_interval:
        add_new_platform()
        last_platform_time = current_time

    if space_pressed and is_on_ground:
        vertical_momentum = -jump_speed
        is_on_ground = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x = max(LEFT_EDGE, character_x - character_speed)
    if keys[pygame.K_RIGHT]:
        character_x = min(RIGHT_EDGE, character_x + character_speed)

    if character_x > screen_move_threshold:
        for block in blocks:
            block.x -= screen_move_speed
        for obstacle in obstacles:
            obstacle.x -= screen_move_speed
        character_x -= screen_move_speed

    vertical_momentum += gravity
    character_y += vertical_momentum
    character_y = min(character_y, floor_y - character_height)

    if character_y >= floor_y - character_height:
        character_y = floor_y - character_height
        vertical_momentum = 0
        is_on_ground = True

    block_collided = check_collision(pygame.Rect(character_x, character_y, character_width, character_height), blocks)
    obstacle_collided = check_collision(pygame.Rect(character_x, character_y, character_width, character_height), obstacles)

    if block_collided:
        if vertical_momentum > 0:
            character_y = block_collided.y - character_height
            vertical_momentum = 0
            is_on_ground = True

    if obstacle_collided:
        life -= 1
        collision_message = f"Life: {life}"
        collision_time = pygame.time.get_ticks()
        if life == 0:
            game_over = True
        else:
            set_character_initial_position()
            vertical_momentum = 0
            is_on_ground = True
            blocks = [Block(x, y) for x, y in blocks_positions]
            obstacles = [Block(x, y) for x, y in obstacles_positions]

    if portal and game_clear:
        if character_rect.colliderect(portal.rect):
            game_clear = True
