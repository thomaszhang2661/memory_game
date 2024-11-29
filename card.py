"""
cs5001
project memory_game
Jian Zhang
"""
import turtle

# Constant settings
CARD_SIZE = (100, 150)  # Card size (width, height)
GRID_GAP = 10  # Gap between cards

class Card(turtle.Turtle):
    def __init__(self, x, y, front_image, back_image, game=None):
        super().__init__()
        # self.value = value  # The value of the card
        self.x = x  # X coordinate
        self.y = y  # Y coordinate
        self.is_face_up = False  # Initially the card is face-down
        self.front_image = front_image  # Front image of the card
        self.back_image = back_image  # Back image of the card

        # Register images as shapes
        turtle.register_shape(self.front_image)  # Register front image as shape
        turtle.register_shape(self.back_image)  # Register back image as shape

        self.shape(self.back_image)  # Default to showing the back image
        self.penup()  # Do not draw any lines
        self.setposition(self.x, self.y)  # Directly set the position to (x, y)
        self.onclick(self.flip)  # Bind the click event to flip the card
        self.game = game
        #self.display_coordinates()

    def flip(self, x, y):
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
        """处理点击事件"""
        self.game.flip_card(self)  # 调用 MemoryMatchGame 中的 flip_card 方法

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