#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame

from const import *
from helper import *

class Menu(object):

	@classmethod
	def init(cls):
		cls.LOGO = pygame.image.load('graphics/logo.png').convert_alpha()
		cls.FONT = pygame.font.SysFont("Consolas", 20)
		cls.MENU_FONT = pygame.font.Font("fonts/starcraft.ttf", 22)
		cls.items = ["Start game", "Highscore", "Exit"]
		cls.current = 0

	@classmethod
	def draw_menu(cls, surf):
		logorect = cls.LOGO.get_rect()
		logorect.center = (R(X*0.5), R(Y*0.3))
		surf.blit(cls.LOGO, logorect)
		pygame.draw.rect(surf, (192, 192, 192), (R(X*0.2778), R(Y*0.6), R(X*0.4444), R(Y*0.12)))
		pygame.draw.rect(surf, (80, 80, 80), (R(X*0.2833), R(Y*0.61), R(X*0.4333), R(Y*0.1)))
		label = cls.FONT.render("Press ENTER to start", 1, (200, 200, 200))
		pos = label.get_rect(centerx = R(X*0.5), centery = R(Y*0.66))
		surf.blit(label, pos)
