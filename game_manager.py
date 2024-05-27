# game_manager.py
import pygame
import sys
from setting import *
from character import Character
from screen import Screen
from block import Block
from obstacle import Obstacle

class GameManager:
    
    # 게임 초기화 함수
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("점프 점프")

        self.clock = pygame.time.Clock()

        # 게임 시작 페이지 표시
        Screen.show_start_screen(self.screen)

        # 초기 설정
        self.floor_y = floor_y  # setting.py에서 floor_y 상수 가져오기
        
        self.blocks = [Block(x, y) for x, y in blocks_positions]  # 블록 객체 리스트 생성
        self.obstacles = [Obstacle(x, y) for x, y in obstacles_positions]  # 장애물 객체 리스트 생성
        self.character = Character(self.blocks, self.obstacles)  # 블록과 장애물 리스트를 전달

    # 게임 시작 함수
    def run_game(self):
        running = True
        font = pygame.font.Font(None, 36)  # 라이프 개수를 표시할 폰트 설정    
        
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
                self.character.update_game_state()  # 게임 상태 업데이트
                print('게임 상태 업데이트')

                self.character.draw_game_elements(self.screen, self.blocks, self.obstacles)  # 게임 요소 그리기
                print('게임 요소 그리기')
                
                life_text = font.render(f"Life: {self.character.life}", True, BLACK)
                life_rect = life_text.get_rect(center=(SCREEN_WIDTH // 2, 30))
                self.screen.blit(life_text, life_rect)

                if self.character.game_clear:
                    Screen.show_clear_screen(self.screen)
                    print('게임 클리어')
                elif self.character.game_over:
                    Screen.show_game_over_screen(self.screen)
                    print('게임오버')
                    break
                    
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()
