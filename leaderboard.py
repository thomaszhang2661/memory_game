"""
cs5001
project memory_game
Jian Zhang
"""
import json
import os
import tkinter.messagebox


class LeaderBoard:
    def __init__(self):
        self.leaderboard = []
        self.load_leaderboard()

    def load_leaderboard(self):
        """Load leaderboard from a file."""
        if os.path.exists("leaderboard.json"):
            with open("leaderboard.json", "r") as f:
                self.leaderboard = json.load(f)

    def save_leaderboard(self):
        """Save leaderboard to a file."""
        with open("leaderboard.json", "w") as f:
            json.dump(self.leaderboard, f)

    def update_leaderboard(self, player_name, guess_count):
        """Update the leaderboard with the current player score."""
        self.leaderboard.append((player_name, guess_count))
        self.leaderboard = sorted(self.leaderboard, key=lambda x: x[1])[:8]  # Keep top 8 players
        self.save_leaderboard()

    def show_leaderboard(self):
        """Display the leaderboard."""
        leaderboard_text = "Leaderboard\n"
        for i, (name, score) in enumerate(self.leaderboard):
            leaderboard_text += f"{i + 1}. {name}: {score} guesses\n"
        tkinter.messagebox.showinfo("Leaderboard", leaderboard_text)
