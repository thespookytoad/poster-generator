from ColabTurtlePlus.Turtle import *
import numpy as np

# Import your own code from TileFunctions.py and PaletteOptions.py
from functions import *
from palettes import *

def generate_poster():
  # Ask user for title
  title = input("What is the title of this poster? ")
  print(f"Your title is '{title}'.\n")
  
  # Choose a palette
  palette = input(f"What color palette do you want to use? The options are: {palette_names}!").lower()

  while palette not in palette_names:
    palette = input(f"That is not a valid palette. Pick from these: {palette_names}. ").lower()
  
  if palette == "random":
    print("Now generating a random color palette...")
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    bg = (r, g, b)
  
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    primary = (r, g, b)
  
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    secondary = (r, g, b)
  
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    accent = (r, g, b)
    print("Palette successfully generated!")
    print(f"{bg}, {primary}, {secondary}, {accent}\n")
  else:
    print(f"Your palette is {palette}.\n")
  
  # Width
  width = int(input("How many tiles wide will the pattern be? "))
  while width < 1 or width > 15:
    width = int(input("Please enter a valid number between 1 and 15: "))
  print(f"The width will be {width}.\n")
  
  # Height
  height = int(input("How many tiles tall will the pattern be? "))
  while height < 1 or height > 15:
    height = int(input("Please enter a valid number between 1 and 15: "))
  print(f"The height will be {height}.\n")

  # Set up the screen
  screen_width = 1000
  screen_height = 500
  
  horizontal_spacing = 20
  vertical_spacing_above = 20
  vertical_spacing_below = 180
  
  size_horiz = (screen_width - horizontal_spacing * 2) / width
  size_vert = (screen_height - vertical_spacing_above - vertical_spacing_below) / height
  size = min(size_horiz, size_vert)
  
  if isinstance(palette, str):
      if palette == "random":
          palette = {
              "bg": bg,
              "primary": primary,
              "secondary": secondary,
              "accent": accent
          }
      else:
          palette = palette_options[palette]
  
  clearscreen()
  
  setup(screen_width, screen_height)
  t = Turtle()
  t.speed(0)
  
  y_offset = screen_height / 2 - 20 - size / 2
  x_offset = -size * (width - 1) / 2
  
  for r_idx in range(height):
    y = y_offset - size * r_idx
  
    for c_idx in range(width):
      x = x_offset + size * c_idx
  
      F = tile_functions[np.random.randint(len(tile_functions))]
  
      # Differentiate corners, borders, and center using height and width
      if r_idx == 0:
        if c_idx == 0:
          tile_type = "corner"
          rotation = 0
        elif c_idx == width - 1:
          tile_type = "corner"
          rotation = 90
        else:
          tile_type = "border"
          rotation = np.random.randint(2) * 180
      elif r_idx == height - 1:
        if c_idx == 0:
          tile_type = "corner"
          rotation = 270
        elif c_idx == width - 1:
          tile_type = "corner"
          rotation = 180
        else:
          tile_type = "border"
          rotation = np.random.randint(2) * 180
      else:
        if c_idx == 0 or c_idx == width - 1:
          tile_type = "border"
          rotation = 90 + np.random.randint(2) * 180
        else:
          tile_type = "center"
          rotation = np.random.randint(4) * 90
  
      F(t, x, y, size, rotation, palette, tile_type)
  
  # Title and credits
  t.jumpto(0, -screen_height / 2 + vertical_spacing_below - 30)
  t.pencolor(palette["primary"])
  t.write(title, align="center", font=(20, "Arial", "bold"))
  t.setheading(270)
  t.forward(30)
  t.write("By Alexander, Carolina, Rui, and Sela", align="center", font=(20, "Arial", "bold"))
  
  # Draw color palette
  t.jumpto(-245, -190)
  for v in palette.values():
    t.color(v, v)
    t.setheading(90)
    t.pendown()
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(100)
    t.end_fill()
    t.penup()
    t.right(180)
    t.forward(50)
    t.right(90)
    t.forward(20)
  
    t.write(v, align="center")
    t.setheading(0)
    t.forward(80)
    t.left(90)
    t.forward(20)
  
  t.hideturtle()
  t.done()
  
  saveSVG("/content/poster.svg")
