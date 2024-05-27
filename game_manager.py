# game_manager.py
import pygame
import sys
from setting import *
from character import Character
from screen import Screen

class GameManager:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("점프 점프")

        self.clock = pygame.time.Clock()

        # 게임 시작 페이지 표시
        Screen.show_start_screen(self.screen)

        # 초기 설정
        self.character = Character()
        self.floor_y = floor_y  # setting.py에서 floor_y 상수 가져오기

    def run_game(self):
        running = True

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

                self.character.draw_game_elements(self.screen)  # 게임 요소 그리기
                print('게임 요소 그리기')

                if self.character.game_clear:
                    Screen.show_clear_screen(self.screen)
                elif self.character.game_over:
                    Screen.show_game_over_screen(self.screen)

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()
