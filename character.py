import pygame
from setting import *
from screen import Screen
from block import Block
from obstacle import Obstacle

class Character:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.speed = 6
        self.jump_speed = 20
        self.gravity = 1.4
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - self.height * 2
        self.vertical_momentum = 0
        self.is_on_ground = True
        self.space_pressed = False
        self.life = 3
        self.game_over = False
        self.game_clear = False

    def set_initial_position(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - self.height * 2
        self.life = 3

    def update_game_state(self):
        current_time = pygame.time.get_ticks()
        print("스페이스 바 눌림 여부:", self.space_pressed)

        if self.space_pressed and self.is_on_ground:
            print('점프 중')
            self.vertical_momentum = -self.jump_speed
            self.is_on_ground = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print('왼쪽키 눌림')
            self.x = max(LEFT_EDGE, self.x - self.speed)
        if keys[pygame.K_RIGHT]:
            print('오른쪽키 눌림')
            self.x = min(RIGHT_EDGE, self.x + self.speed)

        if self.x > SCREEN_WIDTH // 2:
            dx = self.x - SCREEN_WIDTH // 2
            Screen.move_screen(dx)

        self.x = max(0, min(SCREEN_WIDTH - self.width, self.x))
        self.vertical_momentum += self.gravity
        self.y += self.vertical_momentum
        self.y = min(self.y, floor_y - self.height)

        if self.y >= floor_y - self.height:
            self.y = floor_y - self.height
            self.vertical_momentum = 0
            self.is_on_ground = True

        block_collided = Block.check_collision(self.x, self.y, self.width, self.height)
        obstacle_collided = Block.check_collision(self.x, self.y, self.width, self.height)
        if block_collided:
            if self.vertical_momentum > 0:
                self.y = block_collided.y - self.height
                self.vertical_momentum = 0
                self.is_on_ground = True
                
        if obstacle_collided:
            print("장애물과 충돌 여부:", obstacle_collided)
            self.life -= 1
            if self.life == 0:
                self.game_over = True
            else:
                self.set_initial_position()
                self.vertical_momentum = 0
                self.is_on_ground = True

        if Screen.portal and pygame.Rect(self.x, self.y, self.width, self.height).colliderect(Screen.portal.rect):
            self.game_clear = True

    def draw_game_elements(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.x, self.y, self.width, self.height))
