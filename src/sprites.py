#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame

from const import *

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
