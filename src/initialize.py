import pygame
import sys
from .settings import *

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Algorithm Visualizer')
icon=pygame.image.load("icons/3d.png")
pygame.display.set_icon(icon)

#importing icons needed
arrow_right=pygame.image.load("icons/right-arrow.png")
arrow_right=pygame.transform.scale(arrow_right,(82,82))
down_arrow_black= pygame.image.load("icons/down-arrow-black.png")
down_arrow_black= pygame.transform.scale(down_arrow_black,(80,80))
down_arrow_red=pygame.image.load("icons/down-arrow-red.png")
down_arrow_red=pygame.transform.scale(down_arrow_red,(80,80))
up_arrow=pygame.image.load("icons/up-arrow.png")
up_arrow=pygame.transform.scale(up_arrow,(80,80))

# Set up font 
font = pygame.font.SysFont(None, 48)
font_small=pygame.font.SysFont(None,36)
font_title=pygame.font.SysFont(None,72)
# we are using default system font