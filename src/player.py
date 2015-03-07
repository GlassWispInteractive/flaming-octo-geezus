#!/usr/bin/env python
# -*- coding: utf-8 *-*

from const import *
from helper import *
import sprites

class Player(object):
	"""class for player; everything static"""

	@classmethod
	def init(cls, (x, y), world):
		cls.x = x
		cls.y = y
		cls.W = world
		cls.commands = [] # list of commands to execute; EventHandler writes to this
		cls.sprite = sprites.CharSetMultiSprite("graphics/Chara1.png", 24,32, 4,0, 72,128)

	@classmethod
	def move(cls):
		"""Takes a Dir enum and moves the player (if possible)"""
		for c in cls.commands:
			if type(c) == Enum:
				if c == Enum.N:
					try_pos(cls.x, cls.y-1)
				if c == Enum.E:
					try_pos(cls.x+1, cls.y)
				if c == Enum.S:
					try_pos(cls.x, cls.y+1)
				if c == Enum.W:
					try_pos(cls.x-1, cls.y)

		def try_pos(x,y):
			if cls.W.cur_dungeon().level[x][y] != 0: # if movement is allowed
				self.x, self.y = x, y # then move
