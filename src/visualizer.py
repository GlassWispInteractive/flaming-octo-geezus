#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame
import os.path as path
import glob

from const import *
from helper import *
from resources import GRAPHICS, SOUNDS, FONTS
import world


# Static Visualization Class
class Visualization(object):
	"""Contains surfaces and everything that is important for visualization"""

	# maybe some global class values here...
	W = world.World
	P = W.player
	H = W.happiness

	@classmethod
	def init(cls):
		pygame.display.set_caption(Title)
		cls.MAIN = pygame.display.set_mode((X, Y))
		cls.H.init()

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

		map_surf_edit = cls.W.cur_dungeon().surf.copy() # dont modify the original surface, always draw on a copy
		# cls.render_player2map(map_surf_edit)
		cls.render_playerSprite(map_surf_edit)
		cls.render_map(map_surf_edit, -cls.W.cam_x * SCALE, -cls.W.cam_y * SCALE)

		cls.H.refresh()
		cls.MAIN.blit(cls.H.surf, (X-20,0))

		pygame.display.update()

	@classmethod
	def render_map(cls, surf, x, y):
		cls.MAIN.blit(surf, (x,y))

	@classmethod
	def render_player2map(cls, surf):
		pygame.draw.circle(surf, (255,0,0),
			field2coor(cls.P.x, cls.P.y, SCALE), SCALE/2-1)

	@classmethod
	def render_playerSprite(cls, surf):
		cls.P.sprite.draw2dungeon(cls.P.orientation,0, surf, cls.P.x,cls.P.y)
