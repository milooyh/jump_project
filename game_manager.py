import pygame
import sys
from setting import *
from character import Character
from screen import Screen
from block import Block
from obstacle import Obstacle
from portal import Portal
from item import *

class GameManager:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("점프 점프")

        self.clock = pygame.time.Clock()

        Screen.show_start_screen(self.screen)

        self.floor_y = floor_y

        self.blocks = [Block(x, y) for x, y in blocks_positions]
        self.obstacles = [Obstacle(x, y, obstacle_speed) for x, y, obstacle_speed in obstacles_positions]

        highest_block_x = max([block.x for block in self.blocks])
        highest_block_y = max([block.y for block in self.blocks])

        self.portal = Portal(highest_block_x, highest_block_y - 100)

        self.character = Character(self.blocks, self.obstacles, self.portal)

        # 아이템들의 초기 위치 설정
        self.heart_item = HeartItem(100, 550)  # 고정 위치 (x, y) 값으로 변경
        self.speed_item = SpeedItem(300, 450)  # 고정 위치 (x, y) 값으로 변경
        self.invincibility_item = InvincibilityItem(400,450)  # 고정 위치 (x, y) 값으로 변경

        self.game_over = False
        self.game_clear = False

    def reset_game(self):
        self.character.set_initial_position()
        self.character.life = 3
        self.character.game_over = False
        self.character.current_color_index = 0
        self.obstacles = [Obstacle(x, y, obstacle_speed) for x, y, obstacle_speed in obstacles_positions]

    def run_game(self):
        running = True
        font = pygame.font.Font(None, 36)

        while running:
            self.screen.fill(WHITE)
            character_rect = pygame.Rect(self.character.x, self.character.y, self.character.width, self.character.height)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.character.space_pressed = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.character.space_pressed = False

            if not self.character.game_over and not self.character.game_clear:
                self.character.update_game_state()
                self.character.draw_game_elements(self.screen, self.blocks, self.obstacles, self.portal)
                self.character.check_item_collision(self.heart_item, self.speed_item, self.invincibility_item)

                for obstacle in self.obstacles:
                    obstacle.update_position()
                    if obstacle.x < -obstacle_width:
                        obstacle.x = SCREEN_WIDTH

                life_text = font.render(f"Life: {self.character.life}", True, BLACK)
                life_rect = life_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
                self.screen.blit(life_text, life_rect)

                self.heart_item.draw(self.screen)
                self.speed_item.draw(self.screen)
                self.invincibility_item.draw(self.screen)

                if self.character.game_clear:
                    Screen.show_clear_screen(self.screen)

            elif self.character.game_over:
                Screen.show_game_over_screen(self.screen, self)
                
        # 아이템 먹기
            if self.character.check_item_collision(self.heart_item, self.speed_item, self.invincibility_item):
                self.heart_item_eaten = True
                self.speed_item_eaten = True
                self.invincibility_item_eaten = True

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()
