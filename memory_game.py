import random
from card import Card
from leaderboard import LeaderBoard
from area import *
import json  # 用于读取配置文件
import math


# Memory Match Game class
class MemoryMatchGame:
    def __init__(self):
        self.cards = []
        self.guess_count = 0
        self.matches = 0
        self.player_name = "Anonymous"
        self.num_cards = 8  # 默认值，稍后从用户获取
        self.front_group = 0  # 默认值

        self.flipped_cards = []
        self.game_start_time = None

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
        self.QUIT_IMAGE = self.config.get("QUIT_IMAGE", "memory_game_2024/quitbutton.gif")
        self.WARNING_IMAGE = self.config.get("WARNING_IMAGE", "memory_game_2024/card_warning.gif")
        self.IMAGE_PATH = self.config.get("IMAGE_PATH", "images/")
        self.BACK_IMAGE = self.config.get("BACK_IMAGE", "memory_game_2024/card_back.gif")
        self.WIN_IMAGE = self.config.get("WIN_IMAGE", "memory_game_2024/winer.gif")
        self.CARD_GROUPS = self.config.get("CARD_GROUPS", ["config_poker_cards.txt"])
        self.group_ind = 0
        self.card_group = self.CARD_GROUPS[self.group_ind][1]
        # Set up the screen
        self.setup_screen()


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
        # Ask for card group
        self.get_card_group()


        # 创建各区域对象
        self.card_area = CardArea(- self.HALF_SCREEN_WIDTH + self.LEAVE_BLANK_W,
                             self.HALF_SCREEN_HEIGHT - self.LEAVE_BLANK_H,
                             self.CARD_AREA_WIDTH,
                             self.CARD_AREA_HEIGHT, "black", "Card Area")

        self.leaderboard_area = LeaderboardArea(-self.HALF_SCREEN_WIDTH + 2 * self.LEAVE_BLANK_W + self.CARD_AREA_WIDTH,
                                           self.HALF_SCREEN_HEIGHT - self.LEAVE_BLANK_H,
                                           self.LEADBOARD_WIDTH,
                                           self.CARD_AREA_HEIGHT, "blue", "Leaderboard")

        self.status_area = StatusArea(-self.HALF_SCREEN_WIDTH + self.LEAVE_BLANK_W,
                                 self.HALF_SCREEN_HEIGHT - 2 * self.LEAVE_BLANK_H - self.CARD_AREA_HEIGHT,
                                 self.CARD_AREA_WIDTH,
                                 self.STATUS_HEIGHT,
                                 "black", "Status")

        self.leaderboard = LeaderBoard(self.leaderboard_area,self.num_cards)

        self.create_quit_button()

        screen.tracer(0)  # Disable automatic updates

        self.place_cards()
        screen.update()
        screen.tracer(1)
        screen.mainloop()

    def get_player_name(self):
        """Get player's name via turtle's text input"""
        turtle.clear()
        self.player_name = turtle.textinput("CS5001 Memory Games", "your name:")
        if not self.player_name:
            self.player_name = "Anonymous"

    def get_card_group(self):
        """Get player's name via turtle's text input"""
        turtle.clear()
        flag = True
        options = ", ".join(
            [f'{ind} for {x[0]}' for ind, x in enumerate(self.CARD_GROUPS)])

        while flag or not self.group_ind.isdigit() or int(self.group_ind) not in range(len(self.CARD_GROUPS)):
            self.group_ind = turtle.textinput("choose card group:",
                                              options +
                                              "\n defalt:0" +
                                              "\n edit \"config.json\" for more option" )
            flag = False
            if not self.group_ind:
                self.group_ind = '0'
        self.group_ind = int(self.group_ind)
        self.card_group = self.CARD_GROUPS[self.group_ind][1]


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

    def get_card_by_position(self, row, col):
        """Find the card at the specified row and column."""
        for card in self.cards:
            if card.row == row and card.col == col:
                return card
        return None

    def flip_card(self, card):
        """Flip the selected card and check for a match."""
        # if not self.game_start_time:
        #     self.game_start_time = time.time()  # Start the timer when the first card is clicked
        if card not in self.flipped_cards and card.is_face_up == False and len(self.flipped_cards) < 2:
            card.flip()
            self.flipped_cards.append(card)
            if len(self.flipped_cards) == 2:
                self.guess_count += 1
                self.check_for_match()
                self.status_area.update_status(f"{self.guess_count} moves, {self.matches} matches")

    def check_for_match(self):
        """Check if the two flipped cards match."""
        card1, card2 = self.flipped_cards
        if card1.front_image == card2.front_image:
            # 让卡片消失
            card1.hideturtle()
            card2.hideturtle()
            self.matches += 1
            self.status_area.update_status(f"{self.guess_count} moves, {self.matches} matches")
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
        # total_time = round(time.time() - self.game_start_time,2)
        screen = turtle.Screen()
        screen.register_shape(self.WIN_IMAGE)
        # Create a turtle to display the warning image
        win_turtle = turtle.Turtle()
        win_turtle.shape(self.WIN_IMAGE)

        self.leaderboard.add_entry(self.player_name, self.guess_count)
        self.leaderboard.save()
        self.leaderboard.update()
        #self.show_leaderboard()

    # def show_leaderboard(self):
    #     """Display the leaderboard."""
    #     leaderboard_text = "Leaderboard:\n"
    #     for entry in self.leaderboard.get_top_entries():
    #         leaderboard_text += f"{entry['guess']}:{entry['name']} \n"
    #     turtle.clear()
    #     turtle.write(leaderboard_text, align="center", font=("Arial", 16, "normal"))


    def quit_game(self, x=None, y=None):
        """Quit the game."""
        turtle.bye()



class LeaderBoard:
    def __init__(self, area, num_card=8,filepath="leader_log.json"):
        self.entries = []
        self.filepath = filepath
        self.load()
        self.num_card = num_card
        self.area = area
        self.update()


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

    def add_entry(self, name, guess):
        """Add a new entry to the leaderboard."""
        self.entries[str(self.num_card)].append({"name": name, "guesses": guess})

        self.entries[str(self.num_card)].sort(key=lambda entry: entry["guesses"])  # Sort by guesses

        # Keep only the top 8 entries
        self.entries[str(self.num_card)] = self.entries[str(self.num_card)][:8]

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

    def update(self):

        list_to_show = [f'{x["guesses"]}:{x["name"]} 'for x in self.entries[str(self.num_card)]]
        self.area.update_leaderboard(list_to_show)


if __name__ == "__main__":
    game = MemoryMatchGame()


