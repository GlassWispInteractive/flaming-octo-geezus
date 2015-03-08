import pygame
from pygame.locals import *

import time

pygame.init()

pygame.display.set_caption('PyInWoods!')

DISPLAY = pygame.display.set_mode((900, 500))
DISPLAY.fill((209, 230, 232))


LOGO    = pygame.image.load('../graphics/logo.png').convert_alpha()
# BIGFONT = pygame.font.SysFont("Consolas", 56)
FONT    = pygame.font.SysFont("Consolas", 20)


items = ["Start game", "Story", "Cinematics", "Highscore", "Exit"]

current = 0
# current %= len(items)

# logo render
logo = LOGO.get_rect()
logo.center = (450, 100)
DISPLAY.blit(LOGO, logo)

for item, i in zip(items, range(len(items))):
    # button
    fill = (109, 115, 199) if current != i else (141, 146, 214)
    pygame.draw.rect(DISPLAY, (48, 51, 94), (300, 230 + 50*items.index(item), 300, 40))
    pygame.draw.rect(DISPLAY, fill, (310, 235 + 50*items.index(item), 280, 30))
    
    # button text
    label = FONT.render(item, 1, (192, 236, 123))
    pos = label.get_rect(centerx = 450, centery = 250 + 50*items.index(item))
    DISPLAY.blit(label, pos)


pygame.display.update()
time.sleep(5)
pygame.quit()