#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame
from pygame.locals import K_ESCAPE, KEYUP, KEYDOWN, QUIT, K_LEFT, K_RIGHT, K_SPACE, K_a, K_d, K_w, K_s, K_f, K_UP, K_DOWN

import world
import events
import player
import visualizer
from const import *
from helper import *
import resources

pygame.init()
TIMER = pygame.time.Clock()

#resources.init_resources()
evh = events.EventHandler
wor = world.World
vis = visualizer.Visualization
wor.init((DUNGEON_X,DUNGEON_Y), Mode.Menu)
vis.init(wor)

if MUSIC:
	pygame.mixer.music.load("sounds/Kirby_and_the_Rainbow_Curse_-_Boss_(Kirbys_Dream_Land).ogg")
	pygame.mixer.music.play(-1)

while wor.RUN:

	evs = evh.filter_keydown()
	evh.movement2player(evs)
	wor.P.handle_movement()

	vis.render_main()

	TIMER.tick(FPS)
	wor.tick = (wor.tick % (FPS*100)) + 1

	#print pygame.time.get_ticks(), TIMER.get_fps()

pygame.quit()
