# """
# cs5001
# project memory_game
# Jian Zhang
# """
# import turtle
# import random
# from card import Card
# from leaderboard import LeaderBoard
# from area import *
# import json  # 用于读取配置文件
#
# # constants
# # Memory Match Game class
# class MemoryMatchGame:
#     def __init__(self):
#         self.cards = []
#         self.guess_count = 0
#         self.matches = 0
#         self.leaderboard = LeaderBoard()
#         self.player_name = "Anonymous"
#         self.num_cards = 8  # 默认值，稍后从用户获取
#         self.front_group = 0  # 默认值
#         self.card_group = "config_poker_cards.txt"
#         self.config = self.load_config("config.json")  #
#
#
#         # 初始化常量
#         self.HALF_SCREEN_WIDTH = self.config["HALF_SCREEN_WIDTH"]
#         self.HALF_SCREEN_HEIGHT = self.config["HALF_SCREEN_HEIGHT"]
#         self.CARD_AREA_WIDTH = int(self.config["CARD_AREA_WIDTH_RATIO"] * self.HALF_SCREEN_WIDTH)
#         self.CARD_AREA_HEIGHT = int(self.config["CARD_AREA_HEIGHT_RATIO"] * self.HALF_SCREEN_HEIGHT)
#         self.LEADBOARD_WIDTH = int(self.config["LEADBOARD_WIDTH_RATIO"] * self.HALF_SCREEN_WIDTH)
#         self.STATUS_HEIGHT = int(self.config["STATUS_HEIGHT_RATIO"] * self.HALF_SCREEN_HEIGHT)
#         self.LEAVE_BLANK_W = int(self.config["LEAVE_BLANK_W_RATIO"] * self.HALF_SCREEN_WIDTH)
#         self.LEAVE_BLANK_H = int(self.config["LEAVE_BLANK_H_RATIO"] * self.HALF_SCREEN_HEIGHT)
#         self.CARD_WIDTH = self.config["CARD_WIDTH"]
#         self.CARD_HEIGHT = self.config["CARD_HEIGHT"]
#         self.QUIT_IMAGE = self.config["QUIT_IMAGE"]
#         self.WARNING_IMAGE = self.config["WARNING_IMAGE"]
#         self.IMAGE_PATH = self.config["IMAGE_PATH"]
#
#         # Set up the screen
#         self.setup_screen()
#
#
#         self.setup_screen_for_play()
#
#         # Start the game
#         self.setup_game()
#
#     def odd_warning(self):
#         '''show warning pic and modify number_cards'''
#         screen = turtle.Screen()
#
#         # Register the custom quit button image
#         screen.register_shape(WARNING_IMAGE)
#
#
#     def setup_screen(self):
#         # """Set up the game screen."""
#         # screen = turtle.Screen()
#         # screen.setup(800, 800)
#         # screen.bgcolor("white")
#         # # Set the window title
#         # screen.title("CS5001 Memory Games")
#         screen = turtle.Screen()
#         screen.title("Memory Game")
#         screen.setup(width=HALF_SCREEN_WIDTH * 2, height=HALF_SCREEN_HEIGHT * 2)
#         screen.bgcolor("white")
#         # Ask for player's name
#         self.get_player_name()
#
#         # Ask for number of cards
#         self.get_num_cards()
#
#         # 创建各区域对象
#         card_area = CardArea()
#         leaderboard_area = LeaderboardArea()
#         status_area = StatusArea()
#         self.create_quit_button()
#         screen.mainloop()
#         # prepare cards
#
#
#
#     def get_player_name(self):
#         """Get player's name via turtle's text input"""
#         turtle.clear()
#         self.player_name = turtle.textinput("CS5001 Memory Games", "your name:")
#         if not self.player_name:
#             self.player_name = "Anonymous"
#
#     def get_num_cards(self):
#         """Get num_cards via turtle's text input"""
#         turtle.clear()
#         self.num_cards = turtle.textinput("CS5001 Memory Games", "#of cards to play:(8,10 or 12)")
#
#         if not self.num_cards:
#             self.num_cards = 8
#
#     def create_quit_button(self):
#         """Create a quit button using an image."""
#         screen = turtle.Screen()
#
#         # Register the custom quit button image
#         screen.register_shape(self.QUIT_IMAGE)
#
#         # Create the quit button turtle
#         self.quit_button = turtle.Turtle()
#         self.quit_button.shape(self.QUIT_IMAGE)
#         self.quit_button.penup()
#         self.quit_button.goto(-HALF_SCREEN_WIDTH + 2 * LEAVE_BLANK_W + CARD_AREA_WIDTH + 50
#                               , HALF_SCREEN_HEIGHT - 2 *LEAVE_BLANK_H - CARD_AREA_HEIGHT - 30)  # Adjust position as
#         # needed
#         self.quit_button.onclick(self.quit_game)
#
#     def load_config(self, filepath):
#         """从 JSON 文件加载配置"""
#         try:
#             with open(filepath, 'r') as f:
#                 config = json.load(f)
#             return config
#         except Exception as e:
#             print(f"加载配置文件失败: {e}")
#             return {}
#
#     def setup_game(self):
#         """Initialize the game grid and shuffle cards.
#         1. draw the 3 different areas setup screen for play
#         2. choose cards
#         3. place cards"""
#
#
#         # self.cards = [Card(row, col) for row in range(GRID_SIZE[1])\
#         #               for col, value in enumerate(
#         #     random.sample(CARD_IMAGES[0], len(CARD_IMAGES[0])))]
#         #
#         # random.shuffle(self.cards)
#         #
#         # # Draw all the cards (facing down initially)
#         # for card in self.cards:
#         #     card.draw()
#         #
#         # # Set up mouse click event
#         # turtle.onscreenclick(self.on_click)
#
#
#         # # 创建卡片对象
#         # image_path = "memory_game_2024/cards_front/"
#         # # prepare cards
#         # config_file = "config_dog_cards.txt"
#         # with open(config_file, "r") as f:
#         #     card_images = f.readlines()
#         #     card_images = [image.strip() for image in card_images]
#         # back_image = "memory_game_2024/card_back.gif"
#         #
#         # card_images = 2 * card_images
#         # random.shuffle(card_images)
#         # card_x = -HALF_SCREEN_WIDTH + LEAVE_BLANK_W
#         # card_y = HALF_SCREEN_HEIGHT - LEAVE_BLANK_H
#         # BLANK_CARD_W = int((CARD_AREA_WIDTH - 2 * LEAVE_BLANK_W - 4 * CARD_WIDTH) / 3)
#         # card_list = []
#         # for ind_img, image in enumerate(card_images):
#         #     row = ind_img // 4
#         #     col = ind_img % 4
#         #
#         #     card = Card(card_x + LEAVE_BLANK_W + (BLANK_CARD_W + CARD_WIDTH) * col + CARD_WIDTH / 2,
#         #                 card_y - int(LEAVE_BLANK_H / 2) - (BLANK_CARD_W + CARD_HEIGHT) * row - CARD_HEIGHT / 2,
#         #                 image_path + image, back_image)
#         #     card_list.append(card)
#         # card_area.get_cards(card_list)
#         #
#         # screen.mainloop()
#
#     def setup_screen_for_play(self):
#         '''set 3 areas: cards, current infor, leaderboard'''
#         # Create a turtle object
#         pen = turtle.Turtle()
#
#         pen.width(5)
#
#
#
#     # def on_click(self, x, y):
#     #     """Handle card click event."""
#     #     col = (x + 150) // (CARD_SIZE[0] + 10)
#     #     row = (150 - y) // (CARD_SIZE[1] + 10)
#     #
#     #     # Find the card based on click position
#     #     clicked_card = self.get_card_by_position(row, col)
#     #     if clicked_card and not clicked_card.is_face_up:
#     #         self.flip_card(clicked_card)
#
#     def get_card_by_position(self, row, col):
#         """Find the card at the specified row and column."""
#         for card in self.cards:
#             if card.row == row and card.col == col:
#                 return card
#         return None
#
#     def flip_card(self, card):
#         """Flip the selected card and check for a match."""
#         self.guess_count += 1
#         card.flip()
#         card.draw()
#         self.flipped_cards.append(card)
#
#         # Check if two cards are flipped
#         if len(self.flipped_cards) == 2:
#             self.check_for_match()
#
#     def check_for_match(self):
#         """Check if the two flipped cards match."""
#         card1, card2 = self.flipped_cards
#         if card1.value == card2.value:
#             self.matches += 1
#             self.flipped_cards = []  # Reset flipped cards
#             if self.matches == len(self.cards) // 2:  # All pairs matched
#                 self.win_game()
#         else:
#             # Flip them back after a short delay
#             turtle.ontimer(self.flip_back, 500)
#
#     def flip_back(self):
#         """Flip the cards back down."""
#         for card in self.flipped_cards:
#             card.flip()
#             card.draw()
#         self.flipped_cards = []
#
#     def win_game(self):
#         """Handle game win."""
#         self.leaderboard.update_leaderboard(self.player_name, self.guess_count)
#         turtle.clear()
#         turtle.penup()
#         turtle.goto(-150, 0)
#         turtle.write(f"Congratulations {self.player_name}!\nYou won with {self.guess_count} guesses.",
#         font=("Arial", 18, "normal"))
#         turtle.onscreenclick(None)  # Disable further clicks
#
#     def quit_game(self,x=None, y=None):
#         """Quit the game."""
#         turtle.bye()
#
#
# if __name__ == "__main__":
#     game = MemoryMatchGame()
#     #game.setup_game()


import turtle
import random
from card import Card
from leaderboard import LeaderBoard
from area import *
import json  # 用于读取配置文件
import math
import time


# Memory Match Game class
class MemoryMatchGame:
    def __init__(self):
        self.cards = []
        self.guess_count = 0
        self.matches = 0
        self.leaderboard = LeaderBoard()
        self.player_name = "Anonymous"
        self.num_cards = 8  # 默认值，稍后从用户获取
        self.front_group = 0  # 默认值
        self.card_group = "config_poker_cards.txt"
        self.flipped_cards = []

        # Load the config from the file
        self.config = self.load_config("config.json")

        # Initialize constants from the config file
        self.HALF_SCREEN_WIDTH = self.config.get("HALF_SCREEN_WIDTH", 400)  # Default to 400 if not found
        self.HALF_SCREEN_HEIGHT = self.config.get("HALF_SCREEN_HEIGHT", 400)  # Default to 400 if not found
        self.CARD_AREA_WIDTH = int(self.config.get("CARD_AREA_WIDTH_RATIO", 0.6) * self.HALF_SCREEN_WIDTH)
        self.CARD_AREA_HEIGHT = int(self.config.get("CARD_AREA_HEIGHT_RATIO", 0.6) * self.HALF_SCREEN_HEIGHT)
        self.LEADBOARD_WIDTH = int(self.config.get("LEADBOARD_WIDTH_RATIO", 0.3) * self.HALF_SCREEN_WIDTH)
        self.STATUS_HEIGHT = int(self.config.get("STATUS_HEIGHT_RATIO", 0.2) * self.HALF_SCREEN_HEIGHT)
        self.LEAVE_BLANK_W = int(self.config.get("LEAVE_BLANK_W_RATIO", 0.05) * self.HALF_SCREEN_WIDTH)
        self.LEAVE_BLANK_H = int(self.config.get("LEAVE_BLANK_H_RATIO", 0.05) * self.HALF_SCREEN_HEIGHT)
        self.CARD_WIDTH = self.config.get("CARD_WIDTH", 100)
        self.CARD_HEIGHT = self.config.get("CARD_HEIGHT", 150)
        self.QUIT_IMAGE = self.config.get("QUIT_IMAGE", "quit_button.gif")
        self.WARNING_IMAGE = self.config.get("WARNING_IMAGE", "warning.gif")
        self.IMAGE_PATH = self.config.get("IMAGE_PATH", "images/")
        self.BACK_IMAGE = self.config.get("BACK_IMAGE", "card_back.gif")

        # Set up the screen
        self.setup_screen()

        self.setup_screen_for_play()

        # Start the game
        self.setup_game()

    def odd_warning(self):
        '''Show warning picture, block execution, and modify number of cards'''
        screen = turtle.Screen()

        # Register the warning image
        screen.register_shape(self.WARNING_IMAGE)

        # Create a turtle to display the warning image
        warning_turtle = turtle.Turtle()
        warning_turtle.shape(self.WARNING_IMAGE)
        warning_turtle.penup()
        warning_turtle.goto(0, 0)



        # Wait for a short time to let the user see the warning
        # Use `turtle.textinput` to wait for user acknowledgment
        # Use `turtle.textinput` to wait for user acknowledgment
        turtle.ontimer(lambda: warning_turtle.hideturtle(), 2000)  # Hide after 2 seconds

        # Adjust the number of cards to the nearest valid value
        if self.num_cards < 8:
            self.num_cards = 8
        elif self.num_cards < 10:
            self.num_cards = 10
        else:
            self.num_cards = 12

    def load_card_images(self):
        """Load the card images from the disk."""
        card_images = []
        with open(self.card_group, "r") as f:
            card_images = f.readlines()
            card_images = [image.strip() for image in card_images]
        return card_images[:self.num_cards // 2] * 2

    def place_cards(self):
        """Place the cards on the screen."""
        # Create the cards
        card_images = self.load_card_images()
        num_image = len(card_images)
        random.shuffle(card_images)
        card_x = -self.HALF_SCREEN_WIDTH + self.LEAVE_BLANK_W
        card_y = self.HALF_SCREEN_HEIGHT - self.LEAVE_BLANK_H

        row_max = math.ceil(num_image / 4)

        BLANK_CARD_W = int((self.CARD_AREA_WIDTH - 2 * self.LEAVE_BLANK_W - 4 * self.CARD_WIDTH) / 3)
        BLANK_CARD_H = int((self.CARD_AREA_HEIGHT - 2 * self.LEAVE_BLANK_H - row_max * self.CARD_HEIGHT) / row_max)

        for ind_image, image in enumerate(card_images):
            row = ind_image // 4
            col = ind_image % 4

            card = Card(card_x + self.LEAVE_BLANK_W + (BLANK_CARD_W + self.CARD_WIDTH) * col + self.CARD_WIDTH / 2,
                        card_y - self.LEAVE_BLANK_H - (BLANK_CARD_H + self.CARD_HEIGHT) * row - self.CARD_HEIGHT / 2,
                        self.IMAGE_PATH + image, self.BACK_IMAGE, self)
            self.cards.append(card)

    def setup_screen(self):
        screen = turtle.Screen()
        screen.title("Memory Game")
        screen.setup(width=self.HALF_SCREEN_WIDTH * 2, height=self.HALF_SCREEN_HEIGHT * 2)
        screen.bgcolor("white")

        # Ask for player's name
        self.get_player_name()

        # Ask for number of cards
        self.get_num_cards()
        if self.num_cards % 2 != 0:
            self.odd_warning()

        # 创建各区域对象
        card_area = CardArea(- self.HALF_SCREEN_WIDTH + self.LEAVE_BLANK_W,
                             self.HALF_SCREEN_HEIGHT - self.LEAVE_BLANK_H,
                             self.CARD_AREA_WIDTH,
                             self.CARD_AREA_HEIGHT, "black", "Card Area")

        leaderboard_area = LeaderboardArea(-self.HALF_SCREEN_WIDTH + 2 * self.LEAVE_BLANK_W + self.CARD_AREA_WIDTH,
                                           self.HALF_SCREEN_HEIGHT - self.LEAVE_BLANK_H,
                                           self.LEADBOARD_WIDTH,
                                           self.CARD_AREA_HEIGHT, "blue", "Leaderboard")

        status_area = StatusArea(-self.HALF_SCREEN_WIDTH + self.LEAVE_BLANK_W,
                                 self.HALF_SCREEN_HEIGHT - 2 * self.LEAVE_BLANK_H - self.CARD_AREA_HEIGHT,
                                 self.CARD_AREA_WIDTH,
                                 self.STATUS_HEIGHT,
                                 "black", "Status")

        self.create_quit_button()

        self.place_cards()

        screen.mainloop()

    def get_player_name(self):
        """Get player's name via turtle's text input"""
        turtle.clear()
        self.player_name = turtle.textinput("CS5001 Memory Games", "your name:")
        if not self.player_name:
            self.player_name = "Anonymous"

    def get_num_cards(self):
        """Get num_cards via turtle's text input"""
        turtle.clear()
        self.num_cards = turtle.textinput("CS5001 Memory Games", "#of cards to play:(8,10 or 12)")

        if not self.num_cards:
            self.num_cards = 8
        self.num_cards = int(self.num_cards)

    def create_quit_button(self):
        """Create a quit button using an image."""
        screen = turtle.Screen()

        # Register the custom quit button image
        screen.register_shape(self.QUIT_IMAGE)

        # Create the quit button turtle
        self.quit_button = turtle.Turtle()
        self.quit_button.shape(self.QUIT_IMAGE)
        self.quit_button.penup()
        self.quit_button.goto(-self.HALF_SCREEN_WIDTH + 2 * self.LEAVE_BLANK_W + self.CARD_AREA_WIDTH + 30,
                              self.HALF_SCREEN_HEIGHT - 2 * self.LEAVE_BLANK_H - self.CARD_AREA_HEIGHT - 20)  #
        # Adjust position as needed
        self.quit_button.onclick(self.quit_game)

    def load_config(self, filepath):
        """从 JSON 文件加载配置"""
        try:
            with open(filepath, 'r') as f:
                config = json.load(f)
            return config
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            return {}
    #
    # def setup_game(self):
    #     """Initialize the game grid and shuffle cards."""
    #     pass  # Game setup logic will go here
    #
    # # def setup_screen_for_play(self):
    # #     '''set 3 areas: cards, current infor, leaderboard'''
    # #     # Create a turtle object for drawing areas
    # #     pen = turtle.Turtle()
    # #     pen.width(5)

    def get_card_by_position(self, row, col):
        """Find the card at the specified row and column."""
        for card in self.cards:
            if card.row == row and card.col == col:
                return card
        return None

    def flip_card(self, card):
        """Flip the selected card and check for a match."""
        if not self.game_start_time:
            self.game_start_time = time.time()  # Start the timer when the first card is clicked

        card.flip()
        self.flipped_cards.append(card)
        if len(self.flipped_cards) == 2:
            self.guess_count += 1
            self.check_for_match()

    def check_for_match(self):
        """Check if the two flipped cards match."""
        card1, card2 = self.flipped_cards
        if card1.front_image == card2.front_image:
            self.matches += 1
            self.flipped_cards = []  # Reset flipped cards
            if self.matches == len(self.cards) // 2:  # All pairs matched
                self.win_game()
        else:
            # Flip them back after a short delay
            turtle.ontimer(self.flip_back, 500)

    def flip_back(self):
        """Flip the cards back to their original state."""
        card1, card2 = self.flipped_cards
        card1.flip()
        card2.flip()
        card1.draw()
        card2.draw()
        self.flipped_cards = []  # Reset flipped cards

    def win_game(self):
        """End the game when all matches are found and update the leaderboard."""
        total_time = time.time() - self.game_start_time
        self.leaderboard.add_entry(self.player_name, total_time)
        self.leaderboard.save("leader_log.json")
        self.show_leaderboard()


    def quit_game(self, x=None, y=None):
        """Quit the game."""
        turtle.bye()



class LeaderBoard:
    def __init__(self, filepath="leader_log.json"):
        self.entries = []
        self.filepath = filepath
        self.load()

    def load(self):
        """Load leaderboard entries from a file."""
        try:
            with open(self.filepath, "r") as f:
                # Read the content of the file (either JSON or plain text)
                file_content = f.read().strip()
                if file_content:
                    self.entries = json.loads(file_content)
                else:
                    self.entries = []
        except FileNotFoundError:
            # If the file doesn't exist, just initialize an empty leaderboard
            self.entries = []
        except json.JSONDecodeError:
            # Handle case where file exists but has invalid JSON format
            print(f"Warning: {self.filepath} is corrupted, starting with an empty leaderboard.")
            self.entries = []

    def add_entry(self, name, time):
        """Add a new entry to the leaderboard."""
        self.entries.append({"name": name, "time": time})
        self.entries.sort(key=lambda entry: entry["time"])  # Sort by time

        # Keep only the top 8 entries
        self.entries = self.entries[:8]

    def get_top_entries(self):
        """Get the top 8 entries."""
        return self.entries

    def save(self):
        """Save the leaderboard to a file."""
        try:
            with open(self.filepath, "w") as f:
                json.dump(self.entries, f, indent=4)
        except Exception as e:
            print(f"Failed to save leaderboard: {e}")


if __name__ == "__main__":
    game = MemoryMatchGame()
