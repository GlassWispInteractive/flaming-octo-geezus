#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
from numpy import sin, cos, array
from math import pi


## GLOBAL CONSTANTS
X = 1000
Y = 600
FPS = 30
Title = 'Flaming Octo Geezus'

# possible modes (menu, game, highscore?)
def enum(*seq, **named): return type('Enum', (), dict(zip(seq, range(len(seq))), **named)) ## dont even ask
Mode = enum('Start', 'Menu', 'InGame', 'InGameDetail', 'GameOver')


## Static World Class
class World(object):
	"""Holds complete Game Logic State"""
	RUN = True
	maps = None
	player = None
	tick = 0


# Static Visualization Class
class Visualization(object):
	"""Contains surfaces and everything that is important for visualization"""

	@classmethod
	def init(cls):
		pygame.display.set_caption(Title)
		cls.MAIN = pygame.display.set_mode((X, Y))
		cls.GRAPHICS = None
		cls.SOUNDS = None
		cls.FONTS = {
						'HUD' : pygame.font.Font("../resources/pixel.ttf", 20)
					}

	@classmethod
	def class_foo(cls,x):
		print "executing class_foo(%s,%s)"%(cls,x)

	@classmethod
	def draw_text(cls, text, font, pos, color):
		"""render some text. pos is the _middle_ of the boundary box"""
		label = font.render(text, 1, color)
		posi = label.get_rect(centerx = pos[0], centery = pos[1])
		cls.MAIN.blit(label, posi)

	@classmethod
	def render_main(cls):
		cls.MAIN.fill((0,0,0))

		# HERE BE RENDERING CODE

		# Test...
		cls.draw_text("Test", cls.FONTS['HUD'], (500,300), (200,200,100))

		pygame.display.update()
