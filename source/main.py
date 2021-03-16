import pygame

# Configurations

save_in_file = True
save_file_name = "graph"

# To which decimal after the dot the number is rounded
rounding = 3

# Options are "white" and "black"
background_color = "black"

# Options are "red" and "green"
line_color = "green"
line_width = 3

# Whether should the chart have timestamps in it or not (this currentluy does nothing)
use_timestamps = True

window_title = "GraphMaker Alpha 0.1"

window_width = 1280
window_height = 720

# Program start

timestamps = []
amounts = []

# Read data file
with open("data.txt", "r") as data:
    for line in data:
        # Checks if line does contain data or is it an empty space
        if ":" not in line:
            continue
        
        # Splitting the line
        splitted_line = line.split(":")

        amount = splitted_line[1]
        # Storing the line in arrays and removing the \n from the end
        if "." in amount:
            if "\n" in amount:
                amounts.append(float(amount[:-1]))
            else:
                amounts.append(float(amount))
        else:
            if "\n" in amount:
                amounts.append(int(amount[:-1]))
            else:
                amounts.append(int(amount))
        timestamps.append(splitted_line[0])
    print(timestamps)
    print(amounts)

# Open window
screen = pygame.display.set_mode((window_width, window_height))

pygame.init()
pygame.display.set_caption(window_title)
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

if background_color == "black":
    screen.fill((0, 0, 0))
else:
    screen.fill((255, 255, 255))

# Define the font
font = pygame.font.Font("freesansbold.ttf", 10)

# Calculating the "line area's" dimensions
line_area_pixels_width = window_width - (window_width / 14)
line_area_pixels_height = window_height - (window_height / 14)

# Calculating the difference between the "real" window's and the "line area's" dimensions
difference_width = (window_width - line_area_pixels_width) / 2
difference_height = (window_height - line_area_pixels_height) / 2

# Calculating the space between each line
line_spacing_horizontal = round(line_area_pixels_height / 5)

# Calculating the interval between each horizontal line in amounts
interval_between_each_line_in_amounts = (max(amounts) - min(amounts)) / 6

# Drawing the horizontal lines
i = 0
while i < 6:
    pygame.draw.line(screen, (176,176,176), (difference_width, window_height - (line_spacing_horizontal * i + difference_height)), (window_width - difference_width, window_height - (line_spacing_horizontal * i + difference_height)), 1)

    text = font.render(str(round((min(amounts) + i * interval_between_each_line_in_amounts), rounding)), True, (176,176,176))
    screen.blit(text, (5, window_height - (line_spacing_horizontal * i + difference_height) - 5))

    i = i + 1

# Calculate line start and end points and also draw them on the screen (its duplicated so the colors can be different might make it better later)
if line_color == "red":
    # Calculating the space between each line "turnpoint"
    line_spacing = round(line_area_pixels_width / (len(amounts) - 1))

    # Drawing loop
    i = 0
    last_starting_height = None
    while i < len(amounts):
        
        # If its the first loop basically
        if last_starting_height != None:
            try:
                pygame.draw.line(screen, (255, 0, 0), (line_spacing * (i - 1) + difference_width, window_height - (last_starting_height + difference_height)), (line_spacing * i + difference_width, window_height - (int(round(line_area_pixels_height / ((max(amounts) - min(amounts)) / (amounts[i] - min(amounts))))) + difference_height)), line_width)
            except ZeroDivisionError:
                pygame.draw.line(screen, (255, 0, 0), (line_spacing * (i - 1) + difference_width, window_height - (last_starting_height + difference_height)), (line_spacing * i + difference_width, window_height - difference_height), line_width)

        try:
            last_starting_height = int(round(line_area_pixels_height / ((max(amounts) - min(amounts)) / (amounts[i] - min(amounts)))))
        except ZeroDivisionError: 
            last_starting_height = 0

        text = font.render((timestamps[i]), True, (176,176,176))
        screen.blit(text, (line_spacing * i + difference_width, window_height - 5))

        i = i + 1
else:
    # Calculating the space between each line "turnpoint"
    line_spacing = round(line_area_pixels_width / (len(amounts) - 1))

    # Drawing loop
    i = 0
    last_starting_height = None
    while i < len(amounts):
        
        # If its the first loop basically
        if last_starting_height != None:
            try:
                pygame.draw.line(screen, (0, 128, 0), (line_spacing * (i - 1) + difference_width, window_height - (last_starting_height + difference_height)), (line_spacing * i + difference_width, window_height - (int(round(line_area_pixels_height / ((max(amounts) - min(amounts)) / (amounts[i] - min(amounts))))) + difference_height)), line_width)
            except ZeroDivisionError:
                pygame.draw.line(screen, (0, 128, 0), (line_spacing * (i - 1) + difference_width, window_height - (last_starting_height + difference_height)), (line_spacing * i + difference_width, window_height - difference_height), line_width)

        try:
            last_starting_height = int(round(line_area_pixels_height / ((max(amounts) - min(amounts)) / (amounts[i] - min(amounts)))))
        except ZeroDivisionError: 
            last_starting_height = 0

        # Write timestamps under ea
        text = font.render((timestamps[i]), True, (176,176,176))
        screen.blit(text, (line_spacing * i + difference_width, window_height - 12))

        i = i + 1

pygame.display.update()

if save_in_file == True:
    pygame.image.save(screen, save_file_name + ".jpg")

# Keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
