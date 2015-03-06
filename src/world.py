#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
import mapgen

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
	dungeons = [] # list of instances of Dungeon (see below) objects
	player = None
	tick = 0

	@classmethod
	def init(cls):
		cls.cur_level = cls.gen_new_level(400, 400)

	@classmethod
	def gen_new_level(cls, x, y):
		gen = mapgen.GenerateMap(x,y)
		#import pprint; pprint.pprint(gen.map)
		dung = Dungeon(x, y, gen.map)
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
		cls.MAIN.blit(World.dungeons[World.cur_level].surf, (300,100))
		cls.draw_text("Test", cls.FONTS['HUD'], (500,300), (200,200,100))


		pygame.display.update()

	@classmethod
	def render_map(cls, i):
		m = World.maps[i]


class Dungeon(object):
	def __init__(self, x, y, m):
		self.level = m # 2 dimensional int array {0,1}
		# A Dungeon surface only needs to be initialized ONCE

		self.surf = pygame.Surface((x,y))

		self.pxarr = pygame.PixelArray(self.surf)

		for xx in range(x):
			for yy in range(y):
				self.pxarr[xx,yy] = (127,127,127) if self.pxarr[xx,yy] > 0 else (50,50,50)
		del self.pxarr
