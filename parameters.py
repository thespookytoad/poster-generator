# Ask user for title
title = input("What is the title of this poster? ")
print(f"Your title is '{title}'.")

# Choose a palette
palette = input(f"What color palette do you want to use? The options are: {palette_options} OR random! ").lower()

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
  print(f"{bg}, {primary}, {secondary}, {accent}")
else:
  while palette not in palette_options:
    palette = input(f"That is not a valid palette. Pick from these: {palette_options}. ").lower()
  print(f"Your palette is {palette}.")

# Width
width = int(input("How many tiles wide will the pattern be? "))
while width < 1 or width > 15:
  width = int(input("Please enter a valid number between 1 and 15: "))
print(f"The width will be {width}.")

# Height
height = int(input("How many tiles tall will the pattern be? "))
while height < 1 or height > 15:
  height = int(input("Please enter a valid number between 1 and 15: "))
print(f"The height will be {height}.")
