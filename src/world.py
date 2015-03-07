#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
import mapgen
from helper import Mode, Dir, field2coor

## GLOBAL CONSTANTS
X = 1000
Y = 600
FPS = 30
SCALE = 10
Title = 'Flaming Octo Geezus'

## Static World Class
class World(object):
	"""Holds complete Game Logic State"""

	class Player(object):
		"""inner class for player; everything static as well"""
		x = None
		y = None

		@classmethod
		def move(cls, dir):
			"""Takes a Dir enum and moves the player (if possible)"""
			pass


	RUN = True
	dungeons = [] # list of instances of Dungeon (see below) objects
	player = Player
	tick = 0

	@classmethod
	def init(cls):
		cls.cur_level = cls.gen_new_level(100, 60)

		## TEST CODE
		#import test_dungeon
		#cls.dungeons.append(Dungeon(50, 50, test_dungeon.bsp_example, SCALE))
		#cls.cur_level = 0
		cls.player.x = 8
		cls.player.y = 8

	@classmethod
	def gen_new_level(cls, x, y):
		gen = mapgen.GenerateMap(x,y)
		#import pprint; pprint.pprint(gen.map)
		dung = Dungeon(gen.x, gen.y, gen.map, SCALE)
		cls.dungeons.append(dung)
		return len(cls.dungeons) - 1 # should be obvious that this is NOT thread safe


# Static Visualization Class
class Visualization(object):
	"""Contains surfaces and everything that is important for visualization"""

	# maybe some global class values here...

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
		cls.MAIN.blit(World.dungeons[World.cur_level].surf, (0,0))
		pygame.draw.circle(World.dungeons[World.cur_level].surf, (255,0,0), field2coor(World.player.x, World.player.y, SCALE), SCALE/2-1)
		cls.draw_text("Test", cls.FONTS['HUD'], (500,300), (200,200,100))

		pygame.display.update()

	@classmethod
	def render_map(cls, i):
		m = World.maps[i]


class Dungeon(object):
	def __init__(self, x, y, m, s):
		"""Generate a Surface for the dungeon.
		x and y are the dimensions,
		m is the 2-dimensional array with {0,1}
		s is the scale for a field, this should not be less than 3"""
		self.level = m # 2 dimensional int array {0,1}
		# A Dungeon surface only needs to be initialized ONCE

		self.surf = pygame.Surface((x*s,y*s))

		self.pxarr = pygame.PixelArray(self.surf)

		for xx in range(x):
			for yy in range(y):
				self.pxarr[yy*s : yy*s+s-1, xx*s : xx*s+s-1] = (255,255,255) if self.level[xx][yy] > 0 else (0,0,0)
		del self.pxarr
