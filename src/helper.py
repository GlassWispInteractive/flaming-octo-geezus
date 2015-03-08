#!/usr/bin/env python
# -*- coding: utf-8 *-*

from const import *

R = lambda x: int(round(x)) # wrapper for rounding

def enum(*seq, **named): return type('Enum', (), dict(zip(seq, range(len(seq))), **named)) ## dont even ask

# possible modes (menu, game, highscore?)
Mode = enum('Start', 'Menu', 'InGame', 'InGameDetail', 'GameOver')

# possible Directions
Dir = enum('N','E','S','W')

def field2coor(x,y,scale):
	xx = x*scale + scale/2
	yy = y*scale + scale/2
	return xx, yy
