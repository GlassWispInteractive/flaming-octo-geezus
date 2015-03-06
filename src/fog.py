#!/usr/bin/env python
# -*- coding: utf-8 *-*
import pygame
from pygame.locals import K_ESCAPE, KEYUP, KEYDOWN, QUIT, K_LEFT, K_RIGHT, K_SPACE, K_a, K_d, K_w, K_s, K_f, K_UP, K_DOWN
import world
import events

pygame.init()
TIMER = pygame.time.Clock()


wor = world.World
vis = world.Visualization
vis.init()

while wor.RUN:

	ev = events.filter_keydown()

	vis.render_main()

	TIMER.tick(world.FPS)
	world.World.tick = (world.World.tick % (world.FPS*100)) + 1

pygame.quit()
