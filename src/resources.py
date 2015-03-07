#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame
import os.path as path
import glob

GRAPHICS = None
SOUNDS = None
FONTS = None

def init():
	global GRAPHICS
	global SOUNDS
	global FONTS
	GRAPHICS = { path.basename(path.splitext(s)[0])
		: pygame.image.load(s).convert_alpha() for s in glob.glob("graphics/*.png") }
	SOUNDS = None
	FONTS = {
				'HUD' : pygame.font.Font("resources/pixel.ttf", 20)
			}
