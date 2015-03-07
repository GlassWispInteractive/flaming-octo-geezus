#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
import mapgen
from helper import Mode, Dir, field2coor

## GLOBAL CONSTANTS
X = 1000
Y = 600
FPS = 30
SCALE = 10 ## Only Change for Testing
## Standard: 32
Title = 'Flaming Octo Geezus'

## Static World Class
class World(object):
	"""Holds complete Game Logic State"""

	class Player(object):
		"""inner class for player; everything static as well"""

		@classmethod
		def init(cls, (x, y)):
			cls.x = x
			cls.y = y
			cls.sprite = CharSetMultiSprite("graphics/Chara1.png", 24,32, 4,0, 72,128)


		"""path = file path of the Multi sprite.
		   res_x and res_y are the X, Y size of each sub sprite.
		   offX and offY can specify an internal offset which are applied inside of a field (used for char sets).
		   gX and gY specify global offsets (used for char sets)."""



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
		cls.player.init((8,8))

		## LOAD pre-made TEST DUNGEON
		#import test_dungeon
		#cls.dungeons.append(Dungeon(50, 50, test_dungeon.bsp_example))
		#cls.cur_level = 0

	@classmethod
	def gen_new_level(cls, x, y):
		gen = mapgen.GenerateMap(x,y)
		dung = Dungeon(x, y, gen.map)
		cls.dungeons.append(dung)
		return len(cls.dungeons) - 1 # should be obvious that this is NOT thread safe


# Static Visualization Class
class Visualization(object):
	"""Contains surfaces and everything that is important for visualization"""

	# maybe some global class values here...
	W = World
	P = World.player

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

		i = World.cur_level

		#pygame.draw.circle(World.dungeons[World.cur_level].surf, (255,0,0), field2coor(World.player.x, World.player.y, SCALE), SCALE/2-1)
		cls.render_player2map(i)
		cls.render_playerSprite(i)

		#cls.MAIN.blit(World.dungeons[World.cur_level].surf, (0,0))
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


class MultiSprite(object):
	def __init__(self, path, res_x, res_y=None, offX=0, offY=0, gX=0, gY=0):
		"""path = file path of the Multi sprite.
		   res_x and res_y are the X, Y size of each sub sprite.
		   offX and offY can specify an internal offset which are applied inside of a field (used for char sets).
		   gX and gY specify global offsets (used for char sets)."""
		self.sprite = pygame.image.load(path)
		self.res_x = res_x
		self.res_y = res_y if res_y else res_x
		self.offX = offX
		self.offY = offY
		self.gX = gX
		self.gY = gY

	def draw2dungeon(self, x, y, target, t_x=SCALE, t_y=SCALE):
		"""x and y are the position of the subsprite in the MultiSprite.
		   target is the target surface and
		   t_x and t_y are the positions to where the subsprite shall be blitted.
		   All coordinates are scaled accordingly inside this funtion."""
		# make this _a little_ more readable ^^
		rx, ry = self.res_x, self.res_y
		offX, offY = self.offX, self.offY
		gX, gY = self.gX, self.gY

		subsprite_rect = (gX+rx*x, gY+ry*y, rx, ry) # square around the sub sprite we want to draw
		topleft = (t_x*SCALE+offX, t_y*SCALE+offY) # topleft target coordinates; here goes the subsprite
		#print subsprite_rect, topleft
		target.blit(self.sprite, topleft, subsprite_rect)

class TileSetMultiSprite(MultiSprite):
	def __init__(self, path, res_x, res_y=None):
		super(TileSetMultiSprite, self).__init__(path, res_x, res_y)

class CharSetMultiSprite(MultiSprite):
	def __init__(self, path, res_x, res_y=None, offX=0, offY=0, gX=0, gY=0):
		super(CharSetMultiSprite, self).__init__(path, res_x, res_y, offX, offY, gX, gY)


class Dungeon(object):
	def __init__(self, x, y, m):
		"""Generate a Surface for the dungeon.
		x and y are the dimensions,
		m is the 2-dimensional array with {0,1}"""
		self.level = m # 2 dimensional int array {0,1}
		# A Dungeon surface only needs to be initialized ONCE

		s = SCALE

		print "Dungeon Surface SHOULD HAVE DIMENSIONS", x, y
		self.surf = pygame.Surface((x*s,y*s))
		print "Dungeon Surface initialized with size", self.surf.get_size()
		# This Surface holds the complete Dungeon.
		# Dont blit on this Surface, instead
		# copy it, blit on the copy and show that copy to the user.

		self.pxarr = pygame.PixelArray(self.surf)

		for xx in range(x):
			for yy in range(y):
				val = 100*self.level[xx][yy]
				self.pxarr[xx*s : xx*s+s-1, yy*s : yy*s+s-1] = (val, val, val)
		del self.pxarr
