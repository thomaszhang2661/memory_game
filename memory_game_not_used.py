"""
cs5001
project memory_game
Jian Zhang
"""

import tkinter as tk
from gameLogic import MemoryMatchGame

if __name__ == "__main__":
    game = MemoryMatchGame()
    game.setup_game()