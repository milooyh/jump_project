import pygame
import sys
import random

# Pygame 초기화
pygame.init()
pygame.font.init()

# 화면 크기 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # 가로 세로
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("점프 점프")

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FLOOR_COLOR = (144, 228, 144)
GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)
LIGHT_RED = (255, 144, 144)

# 캐릭터 속성 설정
character_width, character_height = 20, 20
character_speed = 6
jump_speed = 20
gravity = 1.4

# 상수 정의
LEFT_EDGE = 0
RIGHT_EDGE = SCREEN_WIDTH - character_width

# 바닥 속성 설정
floor_height = 22  # 바닥 두께
floor_y = SCREEN_HEIGHT - floor_height

# 발판 속성 설정
platform_width, platform_height = 100, 20
platform_color = BLUE

# 장애물 속성 설정
obstacle_width, obstacle_height = 80, 30
obstacle_color = BLACK

# 블록 좌표 설정
blocks_positions = [
    (100, 500),
    (300, 400),
    (500, 300),
    (700, 200)
]

# 장애물 좌표 설정
obstacles_positions = [
    (200, 400),
    (400, 300),
    (600, 200),
    (800, 100)
]

# 블록 클래스 정의
class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 블록, 장애물 리스트 초기화
blocks = [Block(x, y) for x, y in blocks_positions]
obstacles = [Block(x, y) for x, y in obstacles_positions]

clock = pygame.time.Clock()  # 게임 프레임 속도 제어

# 충돌 감지
def check_collision(character, blocks):
    for block in blocks:
        if character.colliderect(pygame.Rect(block.x, block.y, platform_width, platform_height)):
            return block
    return None

# 새로운 발판 추가 함수
def add_new_platform():
    x = random.randint(0, SCREEN_WIDTH - platform_width)
    y = random.randint(0, SCREEN_HEIGHT // 2)
    blocks.append(Block(x, y))
    
# 캐릭터 초기 위치 설정 함수
def set_character_initial_position():
    global character_x, character_y
    character_x = SCREEN_WIDTH // 2
    character_y = SCREEN_HEIGHT - character_height * 2
    print("Character Initial Position:", character_x, character_y)


# 게임 초기화 함수
def reset_game():
    global character_x, character_y, vertical_momentum, is_on_ground, space_pressed, life, game_over, collision_message, collision_time
    set_character_initial_position()
    vertical_momentum = 0
    is_on_ground = True
    space_pressed = False
    life = 3
    game_over = False
    collision_message = ""
    collision_time = 0

# 초기 설정
reset_game()
new_platform_interval = 3000  # 3초마다 새로운 발판 추가
last_platform_time = pygame.time.get_ticks()

# 화면 이동 관련 변수 초기화
screen_move_speed = character_speed
screen_move_threshold = SCREEN_WIDTH // 2
screen_move_height = SCREEN_HEIGHT // 4  # 캐릭터가 점프할 때마다 화면을 이동시킬 높이


# 게임 루프
running = True

# 게임 오버 화면에 사용자가 선택할 수 있는 두 가지 버튼을 추가
try_again_button_rect = pygame.Rect(250, 400, 300, 50)
exit_button_rect = pygame.Rect(250, 500, 300, 50)

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 왼쪽 마우스 버튼 클릭
                if game_over:
                    if try_again_button_rect.collidepoint(event.pos):
                        # "Try Again" 버튼 클릭 시 게임 재시작
                        reset_game()
                    elif exit_button_rect.collidepoint(event.pos):
                        # "Exit" 버튼 클릭 시 게임 종료
                        running = False

    if not game_over:
        # 일정 간격으로 새로운 발판 추가
        current_time = pygame.time.get_ticks()
        if current_time - last_platform_time > new_platform_interval:
            add_new_platform()
            last_platform_time = current_time
            
        # 스페이스 눌리고 바닥에 있으면 점프
        if space_pressed and is_on_ground:
            vertical_momentum = -jump_speed
            is_on_ground = False

        # 상하좌우 이동키 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_x = max(LEFT_EDGE, character_x - character_speed)
        if keys[pygame.K_RIGHT]:
            character_x = min(RIGHT_EDGE, character_x + character_speed)

        # 화면 이동 관련 처리
        if character_x > screen_move_threshold:
            for block in blocks:
                block.x -= screen_move_speed
            for obstacle in obstacles:
                obstacle.x -= screen_move_speed
            character_x -= screen_move_speed

        character_x = max(0, min(SCREEN_WIDTH - character_width, character_x))  # 화면 밖으로 나
        character_x = max(0, min(SCREEN_WIDTH - character_width, character_x))  # 화면 밖으로 나가지 않게
        vertical_momentum += gravity
        character_y += vertical_momentum
        character_y = min(character_y, floor_y - character_height)

        # 바닥에 닿으면 수직 속도를 0으로 하고 바닥에 있다고 표시
        if character_y >= floor_y - character_height:
            character_y = floor_y - character_height
            vertical_momentum = 0
            is_on_ground = True

        # 바닥
        pygame.draw.rect(screen, FLOOR_COLOR, (0, floor_y, SCREEN_WIDTH, floor_height))

        # 장애물 이동 및 그리기
        for obstacle in obstacles:
            obstacle.x -= character_speed // 2  # 캐릭터 속도의 절반만 이동하도록 설정
            if obstacle.x + obstacle_width < 0:  # 장애물이 화면을 벗어나면
                obstacle.x = SCREEN_WIDTH  # 오른쪽에서 다시 나타남
            pygame.draw.rect(screen, obstacle_color, (obstacle.x, obstacle.y, obstacle_width, obstacle_height))

        # 충돌 검사 및 처리
        block_collided = check_collision(character_rect, blocks)
        obstacle_collided = check_collision(character_rect, obstacles)
        if block_collided:
            if vertical_momentum > 0:
                character_y = block_collided.y - character_height
                vertical_momentum = 0
                is_on_ground = True
        if obstacle_collided:
            life -= 1
            collision_message = f"Life: {life}"
            collision_time = pygame.time.get_ticks()  # 충돌 시간 기록
            if life <= 0:
                # 게임 완전 리셋
                blocks = [Block(x, y) for x, y in blocks_positions]
                obstacles = [Block(x, y) for x, y in obstacles_positions]
                reset_game()
            else:
                # 충돌 시 캐릭터 위치 초기화
                set_character_initial_position()
                vertical_momentum = 0
                is_on_ground = True
                blocks = [Block(x, y) for x, y in blocks_positions]
                obstacles = [Block(x, y) for x, y in obstacles_positions]
    
        # 블록 처리
        for block in blocks:
            pygame.draw.rect(screen, platform_color, (block.x, block.y, platform_width, platform_height))

        # 목숨에 따라 캐릭터 색상 변경
        if life == 3:
            character_color = RED
        elif life == 2:
            character_color = ORANGE
        elif life == 1:
            character_color = YELLOW

        # 캐릭터 처리
        pygame.draw.rect(screen, character_color, character_rect)

        # 목숨 표시
        font = pygame.font.Font(None, 36)
        life_text = font.render(f'Life: {life}', True, BLACK)
        screen.blit(life_text, (10, 10))

        # 충돌 메시지 표시
        if collision_message:
            current_time = pygame.time.get_ticks()
            if current_time - collision_time < 1000:  # 충돌 메시지 1초 동안 표시
                collision_font = pygame.font.Font(None, 74)
                collision_text = collision_font.render(collision_message, True, BLACK)
                collision_rect = collision_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(collision_text, collision_rect)
            else:
                collision_message = ""

        # 캐릭터의 y 위치가 화면 이동 높이에 도달하면 화면을 위로 이동시킴
        if character_y < screen_move_height:
            for block in blocks:
                block.y += screen_move_speed
            for obstacle in obstacles:
                obstacle.y += screen_move_speed
            character_y += screen_move_speed
            
    else:
        # 게임 오버 메시지 출력
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

        # "Try Again" 버튼 그리기
        pygame.draw.rect(screen, GREEN, try_again_button_rect)
        try_again_font = pygame.font.Font(None, 36)
        try_again_text = try_again_font.render("Try Again", True, BLACK)
        try_again_text_rect = try_again_text.get_rect(center=try_again_button_rect.center)
        screen.blit(try_again_text, try_again_text_rect)

        # "Exit" 버튼 그리기
        pygame.draw.rect(screen, RED, exit_button_rect)
        exit_font = pygame.font.Font(None, 36)
        exit_text = exit_font.render("Exit", True, BLACK)
        exit_text_rect = exit_text.get_rect(center=exit_button_rect.center)
        screen.blit(exit_text, exit_text_rect)

        # 마우스가 버튼 위에 있을 때 색상 변경
        if try_again_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, LIGHT_GREEN, try_again_button_rect, border_radius=10)
        if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, LIGHT_RED, exit_button_rect, border_radius=10)

        # 게임 재시작 또는 종료 버튼 클릭 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 왼쪽 마우스 버튼 클릭
                    if try_again_button_rect.collidepoint(event.pos):
                        reset_game()
                    elif exit_button_rect.collidepoint(event.pos):
                        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
