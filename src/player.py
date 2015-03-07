#!/usr/bin/env python
# -*- coding: utf-8 *-*

from const import *
import sprites

class Player(object):
	"""class for player; everything static"""

	@classmethod
	def init(cls, (x, y)):
		cls.x = x
		cls.y = y
		cls.commands = [] # list of commands to execute; EventHandler writes to this
		cls.sprite = sprites.CharSetMultiSprite("graphics/Chara1.png", 24,32, 4,0, 72,128)

	@classmethod
	def move(cls, dir):
		"""Takes a Dir enum and moves the player (if possible)"""
		pass
