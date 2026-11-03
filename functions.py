# Function definition for person 1 here
def draw_sela_tile(t, x, y, size, rotation, palette, tile_type="center"):

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  half = size / 2
  quarter = size / 4
  eigth = size / 8

  # ==========================================
  # BASE BACKGROUND
  # ==========================================
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(4)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  t.jumpto(x, y)
  t.setheading(rotation)

  # ==========================================
  # CONDITIONAL GEOMETRY
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------
  if tile_type == "corner":

      t.pencolor(palette["accent"])
      angle = 90

      for n in range(4):
        t.penup()
        t.right(angle)
        t.forward(eigth)
        t.pendown()
        t.forward(quarter)
        t.left(90)
        t.forward(quarter)
        angle += 180

      t.penup()
      t.forward(quarter)
      t.left(90)
      t.forward(quarter)
      t.pendown()

      for i in range(5):
        t.left(144)
        t.forward(half * 0.2)

      t.jumpto(x, y)
      t.pencolor(palette["secondary"])
      angle = 45

      t.penup()
      t.left(180)
      t.forward(quarter * 1.5)
      t.right(180)
      t.pendown()

      for n in range(3):
        t.penup()
        t.left(90)
        t.forward(quarter)
        t.left(180)
        t.forward(eigth)
        t.pendown()
        for i in range(5):
          t.left(144)
          t.forward(half * 0.2)
        angle += 180

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":

      t.color(palette["primary"])
      t.forward(-half)
      t.left(90)
      t.forward(quarter)
      t.right(90)

      t.pendown()
      t.begin_fill()
      for n in range(2):
          t.forward(size)
          t.left(90)
          t.forward(quarter - half)
          t.left(90)
      t.end_fill()
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(3)
      t.forward(-half)
      t.pendown()
      t.forward(size)
      t.penup()

      t.forward(-half)
      t.left(90)
      t.forward(-half)
      t.right(90)
      t.pendown()

      for n in range(8):
        t.pendown()
        t.forward(quarter * 0.9)
        t.penup()
        t.jumpto(x, y)
        t.right(45)

      t.pencolor(palette["secondary"])
      for n in range(8):
        t.penup()
        t.right(45)
        t.pendown()
        t.forward(quarter * 0.9)
        t.penup()
        t.jumpto(x, y)
        t.right(45)

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:

      t.forward(half * 0.9)

      a = 4

      t.color(palette["primary"], palette["primary"])
      t.setheading(rotation + 60)
      for i in range(4):
        t.jumpto(x, y)
        t.pendown()
        t.begin_fill()
        for j in range(a):
            t.forward(quarter * 1.4)
            t.left(360 / a)
        t.end_fill()
        t.penup()
        t.left(90)

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(8)

      t.pendown()
      for i in range(5):
        t.left(144)
        t.forward(half * 0.2)
      t.penup()

      t.pencolor(palette["secondary"])
      t.jumpto(x, y)
      t.setheading(rotation + 45)
      t.forward(quarter * 1.2)
      t.left(90)
      t.forward(quarter * 1.2)
      t.pendown()
      for i in range(5):
          t.left(72)
          t.forward(half)
      t.left(45)
      t.penup()

  # ==========================================
  # DRAW BORDER
  # ==========================================

  t.pencolor(palette["primary"])
  t.pensize(4)

  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pendown()
  for n in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  # ==========================================
  # TURTLE TEARDOWN
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))

# Function definition for person 2 here
def draw_alexander_tile(t, x, y, size, rotation, palette, tile_type="center"):

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)

  ######################### YOUR CHANGES START HERE ###########################

  # ==========================================
  # CONDITIONAL GEOMETRY (Based on tile_type)
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------
  if tile_type == "corner":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

    # colorful orbiting triangles

    for angle in [0, 120, 240]:

        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation + angle)

        t.forward(quarter * 0.75)

        t.color(palette["primary"], palette["primary"])

        if angle == 120:
            t.color(palette["accent"], palette["accent"])
        elif angle == 240:
            t.color(palette["secondary"], palette["secondary"])

        t.pendown()
        t.begin_fill()

        for _ in range(3):
            t.forward(quarter * 0.45)
            t.left(120)

        t.end_fill()

    # energetic center burst

    t.pencolor(palette["accent"])
    t.pensize(2)

    for angle in range(0, 360, 30):

        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation + angle)

        t.pendown()
        t.forward(quarter * 0.8)

    # center dot

    t.penup()
    t.jumpto(x, y)
    t.dot(quarter * 0.7, palette["primary"])
  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

    # Large diamond
    t.penup()
    t.jumpto(x, y)
    t.color(palette["primary"], palette["primary"])
    t.setheading(rotation + 45)

    t.forward(quarter/2)

    t.pendown()
    t.begin_fill()

    for _ in range(4):
        t.forward(quarter)
        t.left(90)

    t.end_fill()

    # Four small diamonds around center
    for angle in [0, 90, 180, 270]:

        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation + angle)

        t.forward(quarter)

        t.color(palette["accent"], palette["accent"])

        t.pendown()
        t.begin_fill()

        for _ in range(4):
            t.forward(quarter/3)
            t.left(90)

        t.end_fill()

    # Connecting lines
    t.pencolor(palette["secondary"])
    t.pensize(2)

    for angle in [0, 45, 90, 135]:

        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation + angle)

        t.pendown()
        t.forward(quarter * 1.1)

        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation + angle + 180)

        t.pendown()
        t.forward(quarter * 1.1)

    t.penup()
  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
    # large diamond
    t.pencolor(palette["primary"])
    t.pensize(2)

    t.penup()
    t.jumpto(x, y)
    t.setheading(rotation + 45)

    t.forward(quarter)
    t.left(135)

    t.pendown()

    for _ in range(4):
        t.forward(quarter * 1.4)
        t.left(90)

    # smaller diamond
    t.penup()
    t.jumpto(x, y)
    t.setheading(rotation + 45)

    t.forward(quarter/2)
    t.left(135)

    t.pendown()

    for _ in range(4):
        t.forward(quarter * 0.7)
        t.left(90)

    # radial lines
    t.pencolor(palette["secondary"])

    for angle in range(0, 360, 45):

        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation + angle)

        t.pendown()
        t.forward(quarter * 0.9)

    # center accent square
    t.penup()
    t.jumpto(x - quarter/6, y - quarter/6)

    t.color(palette["accent"], palette["accent"])
    t.setheading(rotation)

    t.pendown()
    t.begin_fill()

    for _ in range(4):
        t.forward(quarter/3)
        t.left(90)

    t.end_fill()

    t.penup()




  # ==========================================
  # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
  # ==========================================

  ############## This part is my own drawing #######################
  ################## Change it to your design ######################
  t.pencolor(palette["secondary"])
  t.pensize(2)

  # Go to the corner
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  # Draw the border
  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  ######################### YOUR CHANGES END HERE #############################

  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state for the next user
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))

# Function definition for person 3 here
def draw_rui_tile(t, x, y, size, rotation, palette, tile_type="center"):

    # ==========================================
    # TURTLE SETUP
    # ==========================================
    t.penup()
    t.jumpto(x, y)
    t.setheading(rotation)

    # Useful relative dimension constants (derived from size)
    half = size / 2
    quarter = size / 4

    # ==========================================
    # BASE BACKGROUND
    # All tile variations share a clean backdrop
    # ==========================================
    t.forward(-half)
    t.left(90)
    t.forward(-half)
    t.right(90)

    t.pencolor(palette["bg"])
    t.fillcolor(palette["bg"])
    t.pensize(2)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.penup()

    # Return turtle to the true center of the tile
    t.jumpto(x, y)
    t.setheading(rotation)

    ######################### YOUR CHANGES START HERE ###########################

    # ==========================================
    # CONDITIONAL GEOMETRY (Based on tile_type)
    # ==========================================

    # ------------------------------------------
    # OPTION 1: CORNER TILE
    # ------------------------------------------
    if tile_type == "corner":
        t.pensize(3)

        # 1. Inner small wave arc
        t.jumpto(x, y)
        t.setheading(rotation)
        t.forward(-half * 0.5)
        t.left(90)
        t.forward(-half * 0.9)

        t.setheading(rotation)
        t.pencolor(palette["primary"])
        t.pendown()
        t.circle(half * 0.4, 90)
        t.penup()

        # 2. Outer wave arc
        t.jumpto(x, y)
        t.setheading(rotation)
        t.forward(-half + quarter * 0.2)
        t.left(90)
        t.forward(-half + 4)
        t.setheading(rotation)

        t.pencolor(palette["accent"])
        t.pendown()
        t.circle(half * 0.75, 90)
        t.penup()

        # 3. Corner accent dot
        t.jumpto(x, y)
        t.setheading(rotation)
        t.forward(quarter)
        t.left(90)
        t.forward(quarter)
        t.color(palette["primary"])
        t.dot(quarter * 0.4)

    # ------------------------------------------
    # OPTION 2: BORDER TILE
    # ------------------------------------------
    elif tile_type == "border":
        t.pencolor(palette["primary"])
        t.pensize(3)

        t.jumpto(x, y)
        t.setheading(rotation)
        t.forward(-half)

        t.pendown()
        for _ in range(4):
            t.left(60)
            t.forward(quarter * 0.5)
            t.right(120)
            t.forward(quarter * 0.5)
            t.left(60)
        t.penup()

        t.jumpto(x, y)
        t.setheading(rotation)
        t.forward(-half)
        t.left(90)
        t.forward(quarter * 0.5)
        t.right(90)

        t.pencolor(palette["accent"])
        t.pensize(2)
        t.pendown()
        t.forward(size)
        t.penup()

    # ------------------------------------------
    # OPTION 3: CENTER TILE
    # ------------------------------------------
    else:
        t.jumpto(x, y)
        t.setheading(rotation)
        t.forward(-quarter * 0.8)
        t.left(90)
        t.forward(-quarter * 0.3)
        t.right(90)

        star_length = half * 0.8
        t.color(palette["primary"], palette["accent"])
        t.pensize(2)
        t.pendown()
        t.begin_fill()
        for _ in range(5):
            t.forward(star_length)
            t.right(144)
        t.end_fill()
        t.penup()

        t.jumpto(x, y)
        t.color(palette["secondary"])
        t.dot(quarter * 0.3)

    # ==========================================
    # DRAW BORDER (OUTER BOX)
    # ==========================================
    t.pencolor(palette["secondary"])
    t.pensize(2)

    t.penup()
    t.jumpto(x, y)
    t.setheading(rotation)
    t.forward(-half)
    t.left(90)
    t.forward(-half)
    t.right(90)

    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.penup()

    ######################### YOUR CHANGES END HERE #############################

    # ==========================================
    # TURTLE TEARDOWN
    # Reset pen, heading, and state for the next user
    # ==========================================
    t.penup()
    t.setheading(0)
    t.pencolor((0, 0, 0))

# Function definition for person 4 here
def draw_carolina_tile(t, x, y, size, rotation, palette, tile_type="center"):

    # ==========================================
    # TURTLE SETUP
    # ==========================================
    t.penup()
    t.jumpto(x, y)
    t.setheading(rotation)

    # Useful relative dimension constants
    half = size / 2
    quarter = size / 4

    # ==========================================
    # BASE BACKGROUND
    # ==========================================
    t.forward(-half)
    t.left(90)
    t.forward(-half)
    t.right(90)

    t.pencolor(palette["bg"])
    t.fillcolor(palette["bg"])
    t.pensize(2)
    t.pendown()
    t.begin_fill()

    for _ in range(4):
        t.forward(size)
        t.left(90)

    t.end_fill()
    t.penup()

    # Return turtle to center
    t.jumpto(x, y)
    t.setheading(rotation)

    ######################### YOUR CHANGES START HERE ###########################

    # ==========================================
    # OPTION 1: CORNER TILE
    # ==========================================
    if tile_type == "corner":

        # Decorative diamond
        t.color(palette["accent"], palette["accent"])
        t.pensize(3)
        t.penup()
        t.setheading(rotation + 45)
        t.forward(quarter)
        t.pendown()

        t.begin_fill()
        for i in range(4):
            t.forward(quarter)
            t.left(90)
        t.end_fill()

        # Decorative circles
        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation)
        t.color(palette["secondary"])
        t.dot(quarter * 0.8)

        t.color(palette["primary"])
        t.dot(quarter * 0.4)

    # ==========================================
    # OPTION 2: BORDER TILE
    # ==========================================
    elif tile_type == "border":

        # Main horizontal rectangle
        t.color(palette["primary"], palette["primary"])
        t.penup()
        t.setheading(rotation)
        t.forward(-half)
        t.left(90)
        t.forward(quarter)
        t.right(90)
        t.pendown()

        t.begin_fill()
        for i in range(2):
            t.forward(size)
            t.left(90)
            t.forward(quarter)
            t.left(90)
        t.end_fill()

        # Repeating diamond pattern
        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation)
        t.pencolor(palette["accent"])
        t.pensize(2)

        for i in range(5):
            t.penup()
            t.jumpto(x, y)
            t.setheading(rotation)
            t.forward(-half + (i * size / 4))
            t.pendown()
            t.left(45)

            for j in range(4):
                t.forward(quarter / 2)
                t.left(90)

            t.penup()

    # ==========================================
    # OPTION 3: CENTER TILE
    # ==========================================
    else:

        # Large flower/star design
        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation)
        t.color(palette["secondary"])
        t.pensize(3)

        for i in range(8):
            t.penup()
            t.jumpto(x, y)
            t.setheading(rotation + i * 45)
            t.forward(quarter / 2)
            t.pendown()

            t.begin_fill()
            t.circle(quarter / 2, 180)
            t.left(90)
            t.forward(quarter)
            t.end_fill()

        # Inner diamond
        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation + 45)
        t.color(palette["accent"], palette["accent"])
        t.pendown()
        t.begin_fill()

        for i in range(4):
            t.forward(quarter / 1.3)
            t.left(90)

        t.end_fill()

        # Center circle
        t.penup()
        t.jumpto(x, y)
        t.color(palette["primary"], palette["primary"])
        t.dot(quarter * 0.65)

        # Small decorative dots around the design
        for i in range(8):
            t.penup()
            t.jumpto(x, y)
            t.setheading(rotation + i * 45)
            t.forward(half * 0.8)
            t.dot(quarter / 5)

    # ==========================================
    # DRAW OUTSIDE BORDER
    # ==========================================
    t.pencolor(palette["secondary"])
    t.pensize(2)

    t.penup()
    t.jumpto(x, y)
    t.setheading(rotation)
    t.forward(-half)
    t.left(90)
    t.forward(-half)
    t.right(90)

    t.pendown()

    for _ in range(4):
        t.forward(size)
        t.left(90)

    t.penup()

    ######################### YOUR CHANGES END HERE #############################

    # ==========================================
    # TURTLE TEARDOWN
    # ==========================================
    t.penup()
    t.setheading(0)
    t.pencolor((0, 0, 0))
    t.fillcolor((255, 255, 255))

tile_functions = [draw_sela_tile, draw_alexander_tile, draw_rui_tile, draw_carolina_tile] # [person1_function, person2_function, person3_function, person4_function]
