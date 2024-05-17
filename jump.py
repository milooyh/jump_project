import pygame
import sys

# 화면 크기 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("점프 점프")

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
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
obstacle_color = RED

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

# 블록 리스트 초기화
blocks = [Block(x, y) for x, y in blocks_positions]
obstacles = [Block(x, y) for x, y in obstacles_positions]

clock = pygame.time.Clock()

# 충돌 감지
def check_collision(character, blocks):
    for block in blocks:
        if character.colliderect(pygame.Rect(block.x, block.y, platform_width, platform_height)):
            return block
    return None

# 게임 루프
running = True
vertical_momentum = 0
is_on_ground = True
space_pressed = False

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

    if space_pressed and is_on_ground:
        vertical_momentum = -jump_speed
        is_on_ground = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed

    character_x = max(0, min(SCREEN_WIDTH - character_width, character_x))
    vertical_momentum += gravity
    character_y += vertical_momentum
    character_y = min(character_y, floor_y - character_height)

    pygame.draw.rect(screen, FLOOR_COLOR, (0, floor_y, SCREEN_WIDTH, floor_height))

    # 장애물 이동 및 그리기
    for obstacle in obstacles:
        obstacle.x -= character_speed // 2  # 캐릭터 속도의 절반만 이동하도록 설정
        pygame.draw.rect(screen, obstacle_color, (obstacle.x, obstacle.y, obstacle_width, obstacle_height))

    # 충돌 검사 및 처리
    block_collided = check_collision(character_rect, blocks)
    obstacle_collided = check_collision(character_rect, obstacles)
    if block_collided or obstacle_collided:
        if vertical_momentum > 0:
            character_y = max(block_collided.y, obstacle_collided.y) - character_height
            vertical_momentum = 0
            is_on_ground = True

    for block in blocks:
        pygame.draw.rect(screen, platform_color, (block.x, block.y, platform_width, platform_height))

    pygame.draw.rect(screen, RED, character_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
