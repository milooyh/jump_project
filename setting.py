# 화면 크기 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

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
PORTAL_COLOR = (255, 0, 255)

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

# 게임 초기 상태
character_x, character_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - character_height * 2
vertical_momentum = 0
is_on_ground = True
space_pressed = False
life = 3
game_clear = False
game_over = False
collision_message = ""
collision_time = 0
item_effects = {}
effect_start_time = {}
