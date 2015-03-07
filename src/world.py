#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame

from const import *
from helper import *
import player
import dungeon
import mapgen

## Static World Class
class World(object):
	"""Holds complete Game Logic State"""

	RUN = True
	dungeons = [] # list of instances of Dungeon (see below) objects
	cur_level = -float('inf')
	player = player.Player # overwrite module with Player class (!)
	tick = 0
	cam_x, cam_y = 0, 0 # world offset
	cam = 3

	@classmethod
	def init(cls, world_size):
		cls.cur_level = cls.gen_new_level(world_size)
		cls.player.init(cls, None) # generate random start position in player

		## LOAD pre-made TEST DUNGEON
		#import test_dungeon
		#cls.dungeons.append(dungeon.Dungeon(50, 50, test_dungeon.bsp_example))
		#cls.cur_level = 0

	@classmethod
	def gen_new_level(cls, (x, y)):
		gen = mapgen.GenerateMap(x,y)
		dung = dungeon.Dungeon(x, y, gen.map)
		cls.dungeons.append(dung)
		return len(cls.dungeons) - 1 # should be obvious that this is NOT thread safe

	@classmethod
	def cur_dungeon(cls):
		return cls.dungeons[cls.cur_level]
