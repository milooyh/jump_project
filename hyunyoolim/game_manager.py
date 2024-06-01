# game_manager.py

import pygame
import sys
from setting import *
from character import Character
from screen import Screen
from block import Block
from obstacle import Obstacle
from portal import Portal

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
        obstacles = [Obstacle(x, y, obstacle_speed) for x, y, obstacle_speed in obstacles_positions]

        while running:
            self.screen.fill(WHITE)
            character_rect = pygame.Rect(self.character.x, self.character.y, self.character.width, self.character.height)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print('게임 강제 종료')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.character.space_pressed = True
                        print('스페이스바 눌림')
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.character.space_pressed = False
                        print('스페이스바 안 눌림')

            if not self.character.game_over and not self.character.game_clear:
                self.character.update_game_state()
                print('게임 상태 업데이트')

                self.character.draw_game_elements(self.screen, self.blocks, self.obstacles, self.portal)
                print('게임 요소 그리기')
          
