# 1 - Import library
import pygame
from pygame.locals import *

gramado = pygame.image.load("gramado.png")
pedra = pygame.image.load("pedra.png") ## altura = 48
rio = pygame.image.load("rio.png") ## altura = 245
rua = pygame.image.load("rua.png") ## altura = 250
frog = pygame.image.load("frog.png")

images = [gramado, pedra, rio, rua]

done = False

x = 300
y = 580

# 2 - Initialize the game
pygame.init()
width, height = 650, 650
screen = pygame.display.set_mode((width, height))

# 3 - Load images
player = pygame.image.load("background.png")
pygame.display.set_caption("Frogger game")


pygame.display.update()

# 4 - keep looping through
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.QUIT]:
        # if it is quit the game
        pygame.quit()
        exit(0)
    if pressed[pygame.K_UP]:
        y -= 2

    if (y < -2):
        y = 623

    if pressed[pygame.K_DOWN]:
        y += 2

        if (y > 623):
            y = 623

    if pressed[pygame.K_RIGHT]:
        x += 2

    if x > 614:
        x = 614

    if pressed[pygame.K_LEFT]:
        x -= 2

        if (x < -4):
            x = -4

    screen.fill(0)
    # 6 - draw the screen elements

    print("x: " + str(x) + " y: " + str(y))
    screen.blit(pedra, (0, 600))
    screen.blit(rua, (0, 351))
    screen.blit(pedra, (0, 300))
    screen.blit(rio, (0, 60))
    screen.blit(gramado, (0, 0))
    screen.blit(frog, (x, y))
    pygame.display.flip()
    ##pygame.display.update()

