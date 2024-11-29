# Author: Zhang Jian (Thomas Zhang)
# Date: 2024/11/14, 19:12
import turtle
import tkinter.simpledialog

# Create the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set the window title
screen.title("CS5001 Memory Games")

# 获取屏幕的宽度和高度
width, height = screen.window_width(), screen.window_height()


# Use tkinter's dialog to get the name
name = turtle.textinput("set up", "Please enter your name:")

# Use tkinter's dialog to get the num_cards
num_cards = turtle.textinput("set up", "#of cards to play:(8,10 or 12)")

# Create a turtle object
pen = turtle.Turtle()

pen.width(5)

leave_blank_w = 10
leave_blank_h = 15

# 抬起画笔，移动到左上角
pen.penup()
pen.goto(-width // 2 + leave_blank_w, height // 2 - leave_blank_h)  # 左上角坐标是 (-width/2, height/2)
pen.pendown()

for _ in range(2):
    pen.forward(int(width * 0.6))  # 绘制长边
    pen.right(90)      # 转 90 度
    pen.forward(height * 0.6 )  # 绘制短边
    pen.right(90)      # 转 90 度


# # Display the name entered by the user
# if name:
#     pen.write(f"Hello, {name}!", font=("Arial", 16, "normal"))
# else:
#     pen.write("Please enter your name", font=("Arial", 16, "normal"))

# Keep the window open
turtle.done()
