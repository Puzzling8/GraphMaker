import pygame

# Configurations

window_width = 1280
window_height = 720

window_title = "GraphMaker Alpha 0.1"

# Options are "white" and "black"
background_color = "white"

# Options are "red" and "green"
line_color = "red"

# Program start

timestamps = []
amounts = []

# Read data file
with open("data.txt", "r") as data:
    for line in data:
        if ":" not in line:
            continue
        print(line, end="")

# Open window
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption(window_title)
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

if background_color == "black":
    screen.fill((0, 0, 0))
else:
    screen.fill((255, 255, 255))
pygame.display.update()

# Keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False