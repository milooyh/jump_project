# game_manager.py
import pygame
from setting import *
from character import *
from block import *
from obstacle import *
from portal import *
from screen import *

class GameManager:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("점프 점프")

        self.clock = pygame.time.Clock()

        # 게임 시작 페이지 표시
        show_start_screen(self.screen)

        # 초기 설정
        self.reset_game()

        self.character = Character()
        self.platform = Platform()
        self.obstacle = Obstacle()
        self.portal = Portal()

    def reset_game(self):
        self.character = Character()
        self.platform = Platform()
        self.obstacle = Obstacle()
        self.portal = Portal()

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
