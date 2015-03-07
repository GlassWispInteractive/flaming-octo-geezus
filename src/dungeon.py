#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame
from math import pi

from const import *


"""
Possible values for Entries in a level variable:

0 Void
1 Room Unvisited (fog)
2 Corridor Unvisited (fog as well)
3 Room Visited
4 Corridor Visited

"""


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)


class Dungeon(object):

	idx2color = {
		0 : (209, 230, 232), # baby blue
		1 : (100,100,100),
		2 : (200,200,200),
		3 : (100,100,100),
		4 : (200,200,200)
	}

	def __init__(self, x, y, m, rooms=None, corridors=None):
		"""Generate a Surface for the dungeon.
		x and y are the dimensions,
		m is the 2-dimensional array with {0,1}"""
		self.size_x = x
		self.size_y = y
		self.level = m # 2 dimensional int array {0,1}
		# A Dungeon surface only needs to be initialized ONCE

		s = SCALE

		print "Dungeon Surface SHOULD HAVE DIMENSIONS", x, y
		self.surf = pygame.Surface((x*s,y*s))
		print "Dungeon Surface initialized with size", self.surf.get_size(), 'considering scale', SCALE
		# This Surface holds the complete Dungeon.
		# Dont blit on this Surface, instead
		# copy it, blit on the copy and show that copy to the user.

		self.pxarr = pygame.PixelArray(self.surf)

		for xx in range(x):
			for yy in range(y):
				self.pxarr[xx*s : xx*s+s, yy*s : yy*s+s] = self.idx2color[self.level[xx][yy]]
		del self.pxarr

		print rooms
		print sorted(rooms)

		for room in rooms:
			topleft, topright, bottomleft, bottomright = room

			rect = pygame.Rect(0, 0, 2*s, 2*s)
			rect.topleft = [x*s for x in topleft]
			pygame.draw.arc(self.surf, BLACK, rect, 0, pi/2, 2)

			rect = pygame.Rect(0, 0, 2*s, 2*s)
			rect.topright = [x*s for x in topright]
			pygame.draw.arc(self.surf, GREEN, rect, pi/2, pi, 2)

			rect = pygame.Rect(0, 0, 2*s, 2*s)
			rect.bottomleft = [x*s for x in bottomleft]
			pygame.draw.arc(self.surf, BLUE,  rect, pi,3*pi/2, 2)

			rect = pygame.Rect(0, 0, 2*s, 2*s)
			rect.bottomright = [x*s for x in bottomright]
			pygame.draw.arc(self.surf, RED,   rect, 3*pi/2, 2*pi, 2)
