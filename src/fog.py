#!/usr/bin/env python
# -*- coding: utf-8 *-*

import pygame
from pygame.locals import K_ESCAPE, KEYUP, KEYDOWN, QUIT, K_LEFT, K_RIGHT, K_SPACE, K_a, K_d, K_w, K_s, K_f, K_UP, K_DOWN

import world
import player
import visualizer
import events
from const import *
from helper import *
import resources

pygame.init()
TIMER = pygame.time.Clock()

wor = world.World
vis = visualizer.Visualization
evh = events.EventHandler
wor.init((DUNGEON_X,DUNGEON_Y))
vis.init()
resources.init()

while wor.RUN:

	evs = evh.filter_keydown()
	evh.handle_movement(evs)

	vis.render_main()

	TIMER.tick(FPS)
	wor.tick = (wor.tick % (FPS*100)) + 1

pygame.quit()
