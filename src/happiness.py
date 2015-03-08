#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame
from const import *

class HappinessScale(object):

	@classmethod
	def init(cls, start_level=25):
		cls.surf = pygame.Surface((20,Y))
		cls.lvl = start_level

	@classmethod
	def refresh(cls):
		# 20 x Y
		cls.surf.fill((200,200,200))
		
		pygame.draw.rect(cls.surf, (227,20,20), pygame.Rect((5,Y-cls.lvl*((Y-20)/100)) , (10,cls.lvl*((Y-20)/100))))
