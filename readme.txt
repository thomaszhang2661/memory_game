Memory Match Game
A memory matching card game implemented in Python using the turtle graphics library.

Overview
Memory Match Game challenges players to match pairs of cards by flipping them over. The goal is to find all matching pairs with the fewest guesses possible. The game also tracks the leaderboard and displays a win screen when all matches are found.

Features
Choose the number of cards to play with (8, 10, or 12).
Select a card group theme (configurable in config.json).
Track your number of moves and matched pairs.
View the leaderboard with top scores.
Status shows the infor of how many guesses and matches.
Play a new game or quit using graphical buttons.

Advance Features
User can add more themes by adding gif pics in folder "pics",
and create a new text file {pics_file_name} write down the {pics_file_name} in each line,
and then add the {pics_file_name} in config.json "CARD_GROUPS" list.

Requirements
Python 3.x
turtle graphics library (pre-installed with Python)
Installation
Clone the repository:

bash
https://github.com/thomaszhang2661/memory_game.git

Navigate to the project directory:

bash
cd memory-match-game
Ensure you have Python 3 installed and that turtle is available.

Configuration
The game uses a config.json file to define game settings such as screen dimensions, card themes, and image paths. You can edit this file to customize the game’s appearance and behavior.

Example config.json:

json
{
    "HALF_SCREEN_WIDTH": 400,
    "HALF_SCREEN_HEIGHT": 400,
    "CARD_AREA_WIDTH_RATIO": 0.6,
    "CARD_AREA_HEIGHT_RATIO": 0.6,
    "LEADBOARD_WIDTH_RATIO": 0.3,
    "STATUS_HEIGHT_RATIO": 0.2,
    "LEAVE_BLANK_W_RATIO": 0.05,
    "LEAVE_BLANK_H_RATIO": 0.05,
    "CARD_WIDTH": 100,
    "CARD_HEIGHT": 150,
    "QUIT_IMAGE": "memory_game_2024/quitbutton.gif",
    "WARNING_IMAGE": "memory_game_2024/card_warning.gif",
    "IMAGE_PATH": "images/",
    "BACK_IMAGE": "memory_game_2024/card_back.gif",
    "WIN_IMAGE": "memory_game_2024/winer.gif",
    "NEW_GAME_IMAGE": "memory_game_2024/new_game.gif",
    "CARD_GROUPS": ["config_poker_cards.txt"],
    "speed": 10
}
How to Play
When the game starts, enter your player name.
Choose the number of cards (8, 10, or 12).
Select a card group (default is poker cards).
Flip two cards at a time to find matching pairs.
Once all pairs are matched, your score will be recorded in the leaderboard.
Running the Game
To start the game, run the Python script:


python memory_match_game.py
This will open a graphical window where you can play the game and interact with it using the turtle interface.

License
This project is licensed under the MIT License - see the LICENSE file for details.