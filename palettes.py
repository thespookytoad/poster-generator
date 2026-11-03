palette_options = {}

# Color palette for person 1 here
sela_palette = {
        "bg": (19, 18, 20),
        "primary": (255, 119, 46),
        "secondary": (105, 50, 168),
        "accent": (255, 242, 140)
    }
palette_options["halloween palette"] = sela_palette

# Color palette for person 2 here
alexander_palette = {
        "bg": (120, 185, 145),
        "primary": (225, 105, 75),
        "secondary": (48, 206, 198),
        "accent": (225, 165, 200)
    }
palette_options["dull easter"] = alexander_palette

# Color palette for person 3 here
rui_palette = {
        "bg": (104, 166, 145),
        "primary": (191, 211, 193),
        "secondary": (255, 229, 212),
        "accent": (239, 199, 194)
    }
palette_options["teal pallete"] = rui_palette

# Color palette for person 4 here
carolina_palette = {
    "bg": (25, 20, 40),
    "primary": (130, 85, 190),
    "secondary": (255, 165, 100),
    "accent": (255, 220, 120)
}
palette_options["purple palette"] = carolina_palette

# Run this cell to look at all the names.
palette_names = list(palette_options)
palette_names.append("random")
print(f"The available color palettes are: {palette_names}")
