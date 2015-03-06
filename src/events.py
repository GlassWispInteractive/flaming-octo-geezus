#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
import world
from pygame.locals import QUIT, KEYUP, KEYDOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_RETURN, K_p

MOVEMENT_KEYS = [K_LEFT, K_RIGHT, K_SPACE]
CONTROL_KEYS = [K_RETURN, K_ESCAPE, K_p]
KEYS = MOVEMENT_KEYS + CONTROL_KEYS

def filter_keydown():
	for e in pygame.event.get():
		if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
			world.World.RUN = False
			continue
		elif e.type not in [KEYDOWN, KEYUP] or e.key not in KEYS:
			continue
		if e.type == KEYDOWN:
			filter_keydown.events.append(e.key)
		elif e.key in filter_keydown.events:
			filter_keydown.events.remove(e.key)
	return filter_keydown.events
filter_keydown.events = []


class EventHandler(object):
	pass

