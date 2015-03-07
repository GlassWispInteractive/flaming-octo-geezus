#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
import world
from pygame.locals import QUIT, KEYUP, KEYDOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE, K_RETURN, K_p

MOVEMENT_KEYS = [K_LEFT, K_RIGHT, K_UP, K_DOWN]
ACTION_KEYS = [K_SPACE]
CONTROL_KEYS = [K_RETURN, K_ESCAPE, K_p]
KEYS = MOVEMENT_KEYS + ACTION_KEYS + CONTROL_KEYS


class EventHandler(object):
	
	W = world.World
	eventsKD = [] # events where the button is pressed down

	@classmethod
	def filter_keydown(cls):
		for e in pygame.event.get():
			if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
				cls.W.RUN = False
				continue
			elif e.type not in [KEYDOWN, KEYUP] or e.key not in KEYS:
				continue
			if e.type == KEYDOWN:
				cls.eventsKD.append(e.key)
			elif e.key in cls.eventsKD:
				cls.eventsKD.remove(e.key)
		return cls.eventsKD


# if PLAYER[0]-foresight < x and x > 0:
#         x -= 1
#     if PLAYER[0]+foresight > x + 900 / size and PLAYER[0]+foresight < gen.size[0]:
#         x += 1
#     if PLAYER[1]-foresight < y and y > 0:
#         y -= 1
#     if PLAYER[1]+foresight > y + 500 / size and PLAYER[1]+foresight < gen.size[1]:
#         y += 1



	@classmethod
	def handle_movement(cls, keys):
		#print "called handle_movement"
		for k in keys:
			#print 'got key', k
			if k == K_LEFT:
				cls.W.player.x -= 1
				
				if cls.W.player.x - cls.W.cam < cls.W.cam_x and cls.W.cam_x > 0:
					cls.W.cam_x -= 1;
			if k == K_RIGHT:
				cls.W.player.x += 1

				if cls.W.player.x + cls.W.cam > cls.W.cam_x + X / SCALE and cls.W.cam_x > 0:
					cls.W.cam_x += 1;
			if k == K_UP:
				cls.W.player.y -= 1
			if k == K_DOWN:
				cls.W.player.y += 1
