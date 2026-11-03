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
