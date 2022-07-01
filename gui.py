import pygame
from engine import Jeu

WIDTH = 500
HEIGHT = 500
BLANC = (255,255,255)
NOIR = (0,0,0)

pygame.init()

jeu = Jeu()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("morpion")

bg = pygame.Surface((WIDTH,HEIGHT))
bg.fill(BLANC)
pygame.draw.line(bg, NOIR, (0,HEIGHT/3), (WIDTH,HEIGHT/3), 3)
pygame.draw.line(bg, NOIR, (0,2*HEIGHT/3), (WIDTH,2*HEIGHT/3), 3)
pygame.draw.line(bg, NOIR, (WIDTH/3,0), (WIDTH/3,HEIGHT), 3)
pygame.draw.line(bg, NOIR, (2*WIDTH/3,0), (2*WIDTH/3,HEIGHT), 3)

w = WIDTH/3-4
h = HEIGHT/3-4
croix = pygame.Surface((w,h))
croix.fill(BLANC)
pygame.draw.line(croix, NOIR, (w/4, h/4), (3*w/4, 3*h/4), 3)
pygame.draw.line(croix, NOIR, (w/4, 3*h/4), (3*w/4, h/4), 3)

cercle = pygame.Surface((w,h))
cercle.fill(BLANC)
pygame.draw.circle(cercle, NOIR, (int(w//2), int(h//2)), int(3*w//8), 3)

clock = pygame.time.Clock()

continuer = True
while continuer:

  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      continuer = False
    elif e.type == pygame.MOUSEBUTTONUP and not jeu.fin[0]:
      position = e.pos
      colonne = int(position[0]//(WIDTH/3))
      ligne = int(position[1]//(HEIGHT/3))
      jeu.maj(colonne, ligne)
  screen.blit(bg, (0,0))
  for i in range(len(jeu.plateau)):
    for j in range(len(jeu.plateau[i])):
      if jeu.plateau[i][j]==1:
        screen.blit(croix, (j*WIDTH/3+2, i*HEIGHT/3+2))
      elif jeu.plateau[i][j]==2:
        screen.blit(cercle, (j*WIDTH/3+2, i*HEIGHT/3+2))

  if jeu.fin[0]:
    pygame.display.set_caption("Victoire "+str(jeu.fin[1]))

  pygame.display.flip()

  clock.tick(30)

pygame.quit()
quit()
