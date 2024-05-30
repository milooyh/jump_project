import pygame
from setting import *
from screen import Screen
from block import Block
from obstacle import Obstacle
from portal import Portal

class Character:
    def __init__(self, blocks, obstacles, portal):
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
        self.blocks = blocks
        self.obstacles = obstacles
        self.portal = portal
        self.colors = [RED, ORANGE, YELLOW]
        self.current_color_index = 0
        self.show_life = False
        self.life_counter = 0
        self.invincible = False
        self.invincible_timer = 0

        self.image = pygame.image.load('character.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def set_initial_position(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - self.height * 2

    def update_game_state(self):
        current_time = pygame.time.get_ticks()
        
        if self.space_pressed and self.is_on_ground:
            self.vertical_momentum = -self.jump_speed
            self.is_on_ground = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x = max(LEFT_EDGE, self.x - self.speed)
        if keys[pygame.K_RIGHT]:
            self.x = min(RIGHT_EDGE, self.x + self.speed)

        if self.x > SCREEN_WIDTH // 2:
            dx = self.x - SCREEN_WIDTH // 2

        self.x = max(0, min(SCREEN_WIDTH - self.width, self.x))
        self.vertical_momentum += self.gravity
        self.y += self.vertical_momentum
        self.y = min(self.y, floor_y - self.height)

        if self.y >= floor_y - self.height:
            self.y = floor_y - self.height
            self.vertical_momentum = 0
            self.is_on_ground = True

        block_collided = Block.check_collision(self.x, self.y, self.width, self.height, self.blocks)
        obstacle_collided = Obstacle.check_collision(self.x, self.y, self.width, self.height, self.obstacles)
        if block_collided:
            if self.vertical_momentum > 0:
                self.y = block_collided.y - self.height
                self.vertical_momentum = 0
                self.is_on_ground = True

        if obstacle_collided and not self.invincible:
            self.life -= 1
            self.show_life = True
            self.life_counter = current_time
            if self.life == 0:
                self.game_over = True
            else:
                self.current_color_index = min(len(self.colors) - 1, self.current_color_index + 1)
                self.set_initial_position()
                self.vertical_momentum = 0
                self.is_on_ground = True

        if self.invincible and current_time - self.invincible_timer > 5000:  # 무적 시간 5초
            self.invincible = False

    def draw_game_elements(self, screen, blocks, obstacles, portal):
        screen.blit(self.image, (self.x, self.y))
        for block in blocks:
            block.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)
        
        portal.draw(screen)

        if self.show_life:
            font = pygame.font.Font(None, 36)
            text = font.render(f"life : {self.life}", True, BLACK)
            current_time = pygame.time.get_ticks()
            if current_time - self.life_counter >= 1000:  # 1초 동안만 표시
                self.show_life = False

    def check_item_collision(self, heart_item, speed_item, invincibility_item):
        if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(heart_item.rect):
            self.life += 1
            heart_item.x = -100  # 화면 밖으로 이동
        if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(speed_item.rect):
            for obstacle in self.obstacles:
                obstacle.speed /= 2  # 속도 절반으로 줄이기
            speed_item.x = -100  # 화면 밖으로 이동
        if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(invincibility_item.rect):
            self.invincible = True
            self.invincible_timer = pygame.time.get_ticks()
            invincibility_item.x = -100  # 화면 밖으로 이동
