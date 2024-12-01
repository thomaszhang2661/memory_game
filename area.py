"""
CS5001 - Memory Game
Project by Jian Zhang

This script serves for the front part of a simple memory matching game using the turtle graphics library.
It includes multiple screen areas, such as the card area, leaderboard area, and status area, which are used to
display and manage the game interface.

Classes:
    - BaseArea: A base class for creating rectangular areas on the screen, with methods to draw and label
      the area.
    - CardArea: A subclass of BaseArea that handles displaying and managing the cards.
    - LeaderboardArea: A subclass of BaseArea that displays and updates the leaderboard with scores.
    - StatusArea: A subclass of BaseArea that displays the current game status (e.g., moves, matches).

Constants:
    - HALF_SCREEN_WIDTH: Half the width of the screen.
    - HALF_SCREEN_HEIGHT: Half the height of the screen.
    - CARD_AREA_WIDTH: Width of the area that will hold the cards.
    - CARD_AREA_HEIGHT: Height of the area that will hold the cards.
    - LEADBORAD_WIDTH: Width of the leaderboard area.
    - STATUS_HEIGHT: Height of the status area.
    - LEAVE_BLANK_W: Blank space on the left side of the screen.
    - LEAVE_BLANK_H: Blank space on the top side of the screen.
    - CARD_WIDTH: Width of each individual card.
    - CARD_HEIGHT: Height of each individual card.

Main Function:
    The `main` function initializes the game screen, creates the areas (card area, leaderboard area, and
    status area), loads the card images, shuffles the cards, and sets up the initial leaderboard and status
    information. It then starts the turtle graphics main loop to allow user interaction.

    This part only have the click flip function, game logic and other functions are not included.

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


class BaseArea:
    """
    A base class for creating and managing rectangular areas on the game screen.

    Attributes:
        x (int): The x-coordinate of the bottom-left corner of the area.
        y (int): The y-coordinate of the bottom-left corner of the area.
        width (int): The width of the area.
        height (int): The height of the area.
        color (str): The color of the area.
        drawer (turtle.Turtle): A turtle object used to draw the area.
        label (str): A label to display on the area.

    Methods:
        draw_area: Draws the rectangular area on the screen.
        display_label: Displays the label on the area.
    """
    def __init__(self, x, y, width, height, color="black", label="",speed=0):
        """
        Initializes the BaseArea object.

        Args:
            x (int): The x-coordinate of the bottom-left corner of the area.
            y (int): The y-coordinate of the bottom-left corner of the area.
            width (int): The width of the area.
            height (int): The height of the area.
            color (str): The color of the area. Defaults to "black".
            label (str): A label to display on the area. Defaults to an empty string.
            speed (int): The drawing speed of the turtle. Defaults to 0.
        """
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


class CardArea(BaseArea):
    """
    A subclass of BaseArea that handles displaying and managing game cards.

    Attributes:
        cards_list (list): A list to store Card objects.

    Methods:
        draw_cards: Draws all the cards in the area.
        get_cards: Assigns a list of Card objects to the cards_list.
    """
    def __init__(self, x, y, width, height, color="black", label="Card Area", speed=0):
        """
        Initializes the CardArea object.

        Args:
            x (int): The x-coordinate of the bottom-left corner of the area.
            y (int): The y-coordinate of the bottom-left corner of the area.
            width (int): The width of the area.
            height (int): The height of the area.
            color (str): The color of the area. Defaults to "black".
            label (str): A label for the area. Defaults to "Card Area".
            speed (int): The drawing speed of the turtle. Defaults to 0.
        """

        super().__init__(x, y, width, height, color, label,speed)
        self.cards_list = []  # 可以存储卡片对象
        self.draw_cards()

    def draw_cards(self):
        # 在此处绘制卡片
        for card in self.cards_list:
            card.draw()

    def get_cards(self, card_list):
        self.cards_list = card_list


class LeaderboardArea(BaseArea):
    """
    A subclass of BaseArea that displays and updates the leaderboard.

    Attributes:
        scores (list): A list of leaderboard scores to display.
        draw_board (turtle.Turtle): A turtle object used to draw the leaderboard.

    Methods:
        update_leaderboard: Updates the leaderboard display with a list of scores.
    """
    def __init__(self, x, y, width, height, color="blue", label="Card Leaderboard", speed=0):
        """
        Initializes the LeaderboardArea object.

        Args:
            x (int): The x-coordinate of the bottom-left corner of the area.
            y (int): The y-coordinate of the bottom-left corner of the area.
            width (int): The width of the area.
            height (int): The height of the area.
            color (str): The color of the area. Defaults to "blue".
            label (str): A label for the area. Defaults to "Leaderboard".
            speed (int): The drawing speed of the turtle. Defaults to 0.
        """

        super().__init__(x, y, width, height, color, label, speed)
        self.scores = []
        self.draw_board = turtle.Turtle()
        self.draw_board.speed(0)

    def update_leaderboard(self, scores):
        """Updates the leaderboard with a new list of scores.

        Args:
            scores (list): A list of score strings to display on the leaderboard.
        """
        self.scores = scores
        self.draw_board.clear()
        y_offset = -40
        for score in self.scores:
            self.draw_board.penup()
            self.draw_board.goto(self.x + 10, self.y + y_offset)
            self.draw_board.write(score, font=("Arial", 16, "normal"))
            y_offset -= 40

# 状态区域类
class StatusArea(BaseArea):
    """
    A subclass of BaseArea that displays the current game status (e.g., moves and matches).

    Attributes:
        status (str): The current game status as a string.
        draw_status (turtle.Turtle): A turtle object used to display the status.

    Methods:
        update_status: Updates the displayed status text.
    """
    def __init__(self, x, y, width, height, color="blue", label="Card Leaderboard",speed=0):
        """
        Initializes the StatusArea object.

        Args:
            x (int): The x-coordinate of the bottom-left corner of the area.
            y (int): The y-coordinate of the bottom-left corner of the area.
            width (int): The width of the area.
            height (int): The height of the area.
            color (str): The color of the area. Defaults to "blue".
            label (str): A label for the area. Defaults to "Status".
            speed (int): The drawing speed of the turtle. Defaults to 0.
        """
        super().__init__(x, y, width, height, color, label,speed)
        self.status = "0 moves, 0 matches"
        self.draw_status = turtle.Turtle()
        self.update_status(self.status)

    def update_status(self, status_text):
        """Updates the status text displayed on the screen.

        Args:
            status_text (str): The new status text to display.
        """
        self.status = status_text
        self.draw_status.clear()
        self.draw_status.speed(0)

        #self.draw_area()
        self.draw_status.penup()
        self.draw_status.goto(self.x + 10, self.y - 30)
        self.draw_status.write(self.status, font=("Arial", 16, "normal"))

def main():
    screen = turtle.Screen()
    screen.title("Memory Game")
    screen.setup(width=HALF_SCREEN_WIDTH * 2, height=HALF_SCREEN_HEIGHT * 2)
    screen.bgcolor("white")


    # create areas
    card_area = CardArea()
    leaderboard_area = LeaderboardArea()
    status_area = StatusArea()

    # create cards
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

    # update leaderboard
    leaderboard_area.update_leaderboard(["8 : Bobbie", "9 : Keith", "14 : Keith"])

    # update status
    status_area.update_status("Status:Guess: 2, Matches: 1")

    screen.mainloop()

if __name__ == "__main__":
    main()
