import pygame
import sys

# 화면 크기 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600 # 가로 세로
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("점프 점프")

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FLOOR_COLOR = (144, 228, 144)

# 캐릭터 속성 설정
character_width, character_height = 50, 50
character_x, character_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - character_height * 2
character_speed = 10
jump_speed = 20
gravity = 1

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

clock = pygame.time.Clock() # 게임 프레임 속도 제어

# 충돌 감지
def check_collision(character, blocks):
    for block in blocks:
        if character.colliderect(pygame.Rect(block.x, block.y, platform_width, platform_height)):
            return block
    return None

# 게임 루프
running = True
vertical_momentum = 0 # 수직 이동 속도
is_on_ground = True # 바닥에 있는지 여부
space_pressed = False # 스페이스키 눌림 여부

while running:
    screen.fill(WHITE)
    character_rect = pygame.Rect(character_x, character_y, character_width, character_height)

    # 게임 종료 이벤트, 스페이스 키 눌림 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_pressed = False

    # 스페이스 눌리고 바닥에 있으면 점프
    if space_pressed and is_on_ground:
        vertical_momentum = -jump_speed
        is_on_ground = False

    # 상하좌우 이동키
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed

    character_x = max(0, min(SCREEN_WIDTH - character_width, character_x)) # 화면 밖으로 나가지 않게
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
    if block_collided or obstacle_collided:
        if vertical_momentum > 0:
            character_y = (block_collided.y if block_collided else obstacle_collided.y) - character_height
            vertical_momentum = 0
            is_on_ground = True

    # 블록 처리
    for block in blocks:
        pygame.draw.rect(screen, platform_color, (block.x, block.y, platform_width, platform_height))

    # 캐릭터 처리
    pygame.draw.rect(screen, RED, character_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
