import random

class Item:
    def __init__(self, x, y, item_type):
        self.x = x
        self.y = y
        self.item_type = item_type

    def apply_effect(self, player):
        if self.item_type == "life_plus_one":
            player.life += 1
        elif self.item_type == "jump_power_plus_ten":
            player.jump_power += 10
        elif self.item_type == "speed_plus_ten":
            player.speed += 10

# 아이템 생성 함수
def generate_item():
    item_type = random.choice(["life_plus_one", "jump_power_plus_ten", "speed_plus_ten"])
    x = random.randint(0, SCREEN_WIDTH - ITEM_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT - ITEM_HEIGHT)
    return Item(x, y, item_type)
