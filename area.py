"""
cs5001
project memory_game
Jian Zhang
"""

import turtle
import random
from card import Card

# constants
HALF_SCREEN_WIDTH = 450
HALF_SCREEN_HEIGHT = 350
CARD_AREA_WIDTH = int(1.2 * HALF_SCREEN_WIDTH)
CARD_AREA_HEIGHT = int(1.5 * HALF_SCREEN_HEIGHT)
LEADBORAD_WIDTH = int(0.45 * HALF_SCREEN_WIDTH)
STATUS_HEIGHT = int(0.14 * HALF_SCREEN_HEIGHT)
LEAVE_BLANK_W = int(0.1 * HALF_SCREEN_WIDTH)
LEAVE_BLANK_H = int(0.12 * HALF_SCREEN_HEIGHT)
CARD_WIDTH = 100
CARD_HEIGHT = 150


# 创建一个基础区域类
class BaseArea:
    def __init__(self, x, y, width, height, color="black", label="",speed=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.drawer = turtle.Turtle()
        self.drawer.speed(speed)
        self.label = label
        self.draw_area()

    def draw_area(self):
        self.drawer.penup()
        self.drawer.goto(self.x, self.y)
        self.drawer.pendown()
        self.drawer.pensize(3)
        self.drawer.pencolor(self.color)
        #self.drawer.write(f"({self.drawer.xcor()}, {self.drawer.ycor()})", font=("Arial", 12, "normal"))

        for _ in range(2):
            self.drawer.forward(self.width)
            self.drawer.right(90)
            self.drawer.forward(self.height)
            self.drawer.right(90)
        #self.display_label()
        self.drawer.hideturtle()
        turtle.update()


    def display_label(self):
        self.drawer.penup()
        self.drawer.goto(self.x, self.y)
        self.drawer.write(self.label, font=("Arial", 16, "bold"))

# 游戏卡片区域类
class CardArea(BaseArea):
        #def __init__(self):
        # super().__init__(-HALF_SCREEN_WIDTH + LEAVE_BLANK_W,
        #                  HALF_SCREEN_HEIGHT - LEAVE_BLANK_H,
        #                  CARD_AREA_WIDTH,
        #                  CARD_AREA_HEIGHT, "black", "Card Area")
    def __init__(self, x, y, width, height, color="black", label="Card Area",speed=0):

        super().__init__(x, y, width, height, color, label,speed)
        self.cards_list = []  # 可以存储卡片对象
        self.draw_cards()

    def draw_cards(self):
        # 在此处绘制卡片
        for card in self.cards_list:
            card.draw()

    def get_cards(self, card_list):
        self.cards_list = card_list

# 排行榜区域类
class LeaderboardArea(BaseArea):
    # def __init__(self):
    #     super().__init__(-HALF_SCREEN_WIDTH + 2 * LEAVE_BLANK_W + CARD_AREA_WIDTH,
    #                      HALF_SCREEN_HEIGHT - LEAVE_BLANK_H,
    #                      LEADBORAD_WIDTH,
    #                      CARD_AREA_HEIGHT, "blue", "Leaderboard",)
    def __init__(self, x, y, width, height, color="blue", label="Card Leaderboard",speed=0):

        super().__init__(x, y, width, height, color, label, speed)
        self.scores = []

    def update_leaderboard(self, scores):
        self.scores = scores
        self.drawer.clear()
        self.drawer.speed(0)
        self.draw_area()
        #self.draw_area()
        y_offset = -40
        for score in self.scores:
            self.drawer.penup()
            self.drawer.goto(self.x + 10, self.y + y_offset)
            self.drawer.write(score, font=("Arial", 16, "normal"))
            y_offset -= 40

# 状态区域类
class StatusArea(BaseArea):
    # def __init__(self):
    #     super().__init__(-HALF_SCREEN_WIDTH + LEAVE_BLANK_W,
    #                      HALF_SCREEN_HEIGHT - 2 *LEAVE_BLANK_H - CARD_AREA_HEIGHT,
    #                      CARD_AREA_WIDTH,
    #                      STATUS_HEIGHT,
    #                      "black", "Status")
    def __init__(self, x, y, width, height, color="blue", label="Card Leaderboard",speed=0):

        super().__init__(x, y, width, height, color, label,speed)
        self.status = "0 moves, 0 matches"
        self.update_status(self.status)

    def update_status(self, status_text):
        self.status = status_text
        self.drawer.clear()
        self.drawer.speed(0)
        self.draw_area()
        #self.draw_area()
        self.drawer.penup()
        self.drawer.goto(self.x + 10, self.y - 30)
        self.drawer.write(self.status, font=("Arial", 16, "normal"))

# 主程序
def main():
    screen = turtle.Screen()
    screen.title("Memory Game")
    screen.setup(width=HALF_SCREEN_WIDTH * 2, height=HALF_SCREEN_HEIGHT * 2)
    screen.bgcolor("white")


    # 创建各区域对象
    card_area = CardArea()
    leaderboard_area = LeaderboardArea()
    status_area = StatusArea()

    # 创建卡片对象
    image_path = "memory_game_2024/cards_front/"
    # prepare cards
    config_file = "config_dog_cards.txt"
    with open(config_file, "r") as f:
        card_images = f.readlines()
        card_images = [image.strip() for image in card_images]
    back_image = "memory_game_2024/card_back.gif"

    card_images = 2 * card_images
    random.shuffle(card_images)
    card_x = -HALF_SCREEN_WIDTH + LEAVE_BLANK_W
    card_y = HALF_SCREEN_HEIGHT - LEAVE_BLANK_H
    BLANK_CARD_W = int((CARD_AREA_WIDTH - 2 * LEAVE_BLANK_W - 4 * CARD_WIDTH) / 3)
    card_list = []
    for ind_img, image in enumerate(card_images):
        row = ind_img // 4
        col = ind_img % 4

        card = Card(card_x + LEAVE_BLANK_W + (BLANK_CARD_W +CARD_WIDTH)*col + CARD_WIDTH/2,
                    card_y -int(LEAVE_BLANK_H/2) - (BLANK_CARD_W + CARD_HEIGHT)*row - CARD_HEIGHT/2,
                    image_path+image, back_image)
        card_list.append(card)
    card_area.get_cards(card_list)

    # 更新排行榜内容
    leaderboard_area.update_leaderboard(["8 : Bobbie", "9 : Keith", "14 : Keith"])

    # 更新状态区域
    status_area.update_status("Status:Guess: 2, Matches: 1")

    screen.mainloop()

if __name__ == "__main__":
    main()
