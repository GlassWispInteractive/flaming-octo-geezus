#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame

from const import *

class Dungeon(object):
	def __init__(self, x, y, m):
		"""Generate a Surface for the dungeon.
		x and y are the dimensions,
		m is the 2-dimensional array with {0,1}"""
		self.x = x
		self.y = y
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
