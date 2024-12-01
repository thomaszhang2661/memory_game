"""
CS5001 - Memory Game
Project by Jian Zhang

This script serves as a base class used for a simple memory matching game
using the `turtle` module. The game consists of cards that can be flipped when clicked, showing either the front or back image.
This `Card` class handles the creation, flipping, and interaction with the cards.

Classes:
    Card: Represents a card in the memory game with methods for flipping, drawing, and handling
          user clicks.

Functions:
    test_cards: A test function to create multiple card objects and place them in the turtle screen
                for demonstration. It registers the necessary images, creates four cards, and keeps
                the window open for interaction.
"""

import turtle


class Card(turtle.Turtle):
    """
    A class representing a card in the memory matching game.

    Inherits from turtle.Turtle and represents a card that can be flipped to show either its front
    or back image when clicked. The card's state is tracked by whether it is face up or face down.

    Attributes:
        x (int): The x-coordinate for the card's position.
        y (int): The y-coordinate for the card's position.
        is_face_up (bool): A boolean indicating whether the card is face-up (True) or face-down (False).
        front_image (str): The file path for the front image of the card (GIF format).
        back_image (str): The file path for the back image of the card (GIF format).
        game (object): A reference to the game object that manages the game state (optional).

    Methods:
        flip: Flips the card between face-up and face-down, showing the respective image.
        display_coordinates: Displays the card's coordinates on the screen (for debugging purposes).
        on_click: A handler for mouse clicks that triggers the card flip via the game's flip_card method.
        draw: redraws the card, either with its front or back image based on its state.
    """

    def __init__(self, x, y, front_image, back_image, game=None):
        super().__init__()
        # self.value = value  # The value of the card
        self.x = x  # X coordinate
        self.y = y  # Y coordinate
        self.is_face_up = False  # Initially the card is face-down
        self.front_image = front_image  # Front image of the card
        self.back_image = back_image  # Back image of the card
        self.speed(0)
        # Register images as shapes
        turtle.register_shape(self.front_image)  # Register front image as shape
        turtle.register_shape(self.back_image)  # Register back image as shape

        self.shape(self.back_image)  # Default to showing the back image
        self.penup()  # Do not draw any lines
        self.setposition(self.x, self.y)  # Directly set the position to (x, y)
        self.onclick(self.on_click)  # Bind the click event to flip the card
        self.game = game
        #self.display_coordinates()

    def flip(self, x=0, y=0):
        """Flip the card"""
        if self.is_face_up:
            self.shape(self.back_image)  # Show the back side of the card
        else:
            self.shape(self.front_image)  # Show the front side of the card
        self.is_face_up = not self.is_face_up  # Toggle the card state (face-up or face-down)
        self.draw()

    def display_coordinates(self):
        """Display the coordinates on the card"""
        self.penup()
        self.goto(self.x, self.y + 20)  # Adjust position slightly above the card
        self.write(f"({self.x}, {self.y})", align="center", font=("Arial", 10, "normal"))

    def on_click(self, x, y):
        """Handle the event of clicking on the card."""
        # MemoryMatchGame flip_card method
        self.game.flip_card(self)

    def draw(self):
        """Redraw the card after flipping."""
        self.shape(self.front_image if self.is_face_up else self.back_image)


def test_cards():
    screen = turtle.Screen()
    screen.setup(800, 800)

    # Image paths, make sure these images exist and are valid .gif files
    front_image = "memory_game_2024/cards_front/dog1.gif"  # Front image
    back_image = "memory_game_2024/card_back.gif"    # Back image

    # Create multiple cards and place them at different coordinates
    card1 = Card(-100, 100, front_image, back_image)  # Card 1
    card2 = Card(100, 100, front_image, back_image)  # Card 2
    card3 = Card(-100, -100, front_image, back_image)  # Card 3
    card4 = Card(100, -100, front_image, back_image)  # Card 4

    # Keep the window open and continue listening for events
    turtle.mainloop()  # This keeps the window open and listens for click events


if __name__ == "__main__":
    test_cards()
