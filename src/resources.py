#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame
import os.path as path
import glob

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

BABY_BLUE = (209, 230, 232)
DANNY_PINK = (255, 64, 222) # pink (Dannys idea)

GRAPHICS = None
SOUNDS = None
FONTS = None

def init_resources():
	global GRAPHICS
	global SOUNDS
	global FONTS
	GRAPHICS = { path.basename(path.splitext(s)[0])
		: pygame.image.load(s).convert_alpha() for s in glob.glob("graphics/*.png") }
	SOUNDS = None
	FONTS = {
				'HUD' : pygame.font.Font("fonts/pixel.ttf", 20)
			}
