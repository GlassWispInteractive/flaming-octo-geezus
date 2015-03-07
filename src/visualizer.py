#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame

from const import *
from helper import *
import world
import player

# Static Visualization Class
class Visualization(object):
	"""Contains surfaces and everything that is important for visualization"""

	# maybe some global class values here...
	W = world.World
	P = player.Player

	@classmethod
	def init(cls):
		pygame.display.set_caption(Title)
		cls.MAIN = pygame.display.set_mode((X, Y))
		cls.GRAPHICS = None
		cls.SOUNDS = None
		cls.FONTS = {
						'HUD' : pygame.font.Font("resources/pixel.ttf", 20)
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

		i = cls.W.cur_level

		#pygame.draw.circle(cls.W.dungeons[cls.W.cur_level].surf, (255,0,0), field2coor(cls.W.x, cls.W.y, SCALE), SCALE/2-1)
		cls.render_player2map(i)
		cls.render_playerSprite(i)

		#cls.MAIN.blit(cls.W.dungeons[cls.W.cur_level].surf, (0,0))
		cls.render_map(i, 0, 0)
		pygame.draw.circle(cls.MAIN, (255,0,0), cls.W.dungeons[cls.W.cur_level].surf.get_size(), 10)


		# Test...
		# cls.draw_text("Test", cls.FONTS['HUD'], (500,300), (200,200,100))

		pygame.display.update()

	@classmethod
	def render_map(cls, i, x, y):
		m = cls.W.dungeons[i]
		cls.MAIN.blit(m.surf, (x,y))

	@classmethod
	def render_player2map(cls, i):
		pygame.draw.circle(cls.W.dungeons[i].surf, (255,0,0),
			field2coor(cls.P.x, cls.P.y, SCALE), SCALE/2-1)

	@classmethod
	def render_playerSprite(cls, i):
		cls.P.sprite.draw2dungeon(1,2, cls.W.dungeons[i].surf, cls.P.x,cls.P.y)