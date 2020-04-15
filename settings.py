import pygame as pg
from random import randint
vec = pg.math.Vector2
pg.font.init()

# colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (100,100,100)
LGREY = (140,140,140)
bgColour = WHITE
bgText = GREY
bgHoverText = LGREY
fColour = BLACK

# GUI Settings
g_scale = 0.5

# screen Settings
s_screenWidth = 1920//2
s_screenHeight = 1080//2
s_FPS = 120
s_title = "Chi-Squared Calculator and Hypothesis Testing"
s_tileSize = 48
s_font = pg.font.SysFont('arial', 25)
