#!/usr/bin/env python
# -*- coding: utf-8 *-*

import random

from const import *
from helper import *
import sprites

class Player(object):
	"""class for player; everything static"""

	@classmethod
	def init(cls, world, pos):
		cls.W = world
		if pos != None:
			cls.x, cls.y = pos
		else:
			m = cls.W.cur_dungeon()
			x, y = DUNGEON_X/2, DUNGEON_Y/2
			while m.level[x][y] not in list(range(1,3)):
				x, y = random.randint(0, m.size_x-1), random.randint(0, m.size_y-1)
			cls.x = x
			cls.y = y

			cls.W.cam_x = min(cls.x, m.size_x - X / SCALE) - cls.W.cam
			cls.W.cam_y = min(cls.y, m.size_y - Y / SCALE) - cls.W.cam
			# print cls.W.cam_x, m.size_x, X / SCALE, cls.W.cam

		cls.commands = [] # list of commands to execute; EventHandler writes to this; not in use yet
		#cls.sprite = sprites.CharSetMultiSprite("graphics/Chara1.png", 24,32, 4,0, 72,128)
		cls.sprite = sprites.CharSetMultiSprite("graphics/TheRevolverTrans.png", 32,32, 0,0, 0,0)
		cls.orientation = 1


	@classmethod
	def handle_movement(cls):
		dung = cls.W.cur_dungeon()

		#print "called handle_movement"
		for com in cls.commands:
			#print 'got key', k
			if com == Dir.W:
				cls.orientation = 1
				if cls.x > 0 and dung.level[cls.x-1][cls.y] != 0:
					cls.x -= 1
				if cls.x > cls.W.cam - 1 and cls.x - cls.W.cam < cls.W.cam_x:
					cls.W.cam_x -= 1
			if com == Dir.E:
				cls.orientation = 0
				if cls.x < dung.size_x - 1 and dung.level[cls.x+1][cls.y] != 0:
					cls.x += 1
				if cls.x + cls.W.cam - 1 < dung.size_x and cls.x + cls.W.cam > cls.W.cam_x + X / SCALE:
					cls.W.cam_x += 1
			if com == Dir.N:
				if cls.y > 0 and dung.level[cls.x][cls.y-1] != 0:
					cls.y -= 1
				if cls.y > cls.W.cam - 1 and cls.y - cls.W.cam < cls.W.cam_y:
					cls.W.cam_y -= 1
			if com == Dir.S:
				if cls.y < dung.size_y - 1 and dung.level[cls.x][cls.y+1] != 0:
					cls.y += 1
				if cls.y + cls.W.cam - 1 < dung.size_y and cls.y + cls.W.cam > cls.W.cam_y + Y / SCALE:
					cls.W.cam_y += 1
				# print cls.y, cls.W.cam, cls.W.cam_y, Y / SCALE, dung.size_y
		cls.commands = [] # ohne das gibts seltsame glitches ^^


	# not in work
	# @classmethod
	# def move(cls):
	# 	"""Takes a Dir enum and moves the player (if possible)"""
	# 	for c in cls.commands:
	# 		if type(c) == Enum:
	# 			if c == Enum.N:
	# 				try_pos(cls.x, cls.y-1)
	# 			if c == Enum.E:
	# 				try_pos(cls.x+1, cls.y)
	# 			if c == Enum.S:
	# 				try_pos(cls.x, cls.y+1)
	# 			if c == Enum.W:
	# 				try_pos(cls.x-1, cls.y)

	# 	def try_pos(x,y):
	# 		if cls.W.cur_dungeon().level[x][y] != 0: # if movement is allowed
	# 			cls.x, cls.y = x, y # then move
