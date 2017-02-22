#!/usr/bin/env python3

import pygame

SIZE = (640, 480)

pygame.init()

display = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Blight')

clock = pygame.time.Clock()

run = True

while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False


  display.fill( (255,255,255) )

  pygame.display.flip()
  
  clock.tick(60)

pygame.quit()

