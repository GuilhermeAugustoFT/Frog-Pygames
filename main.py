import pygame
import time


class Player:

    def __init__(self):
        self.xPlayer = w / 2
        self.yPlayer = 570

    def move(self, pressed):

        if pressed[pygame.K_UP]:
            self.yPlayer -= 1

            if self.yPlayer < -2:
                self.yPlayer = 623

        elif pressed[pygame.K_DOWN]:
            self.yPlayer += 1

            if self.yPlayer > 623:
                self.yPlayer = 623

        elif pressed[pygame.K_RIGHT]:
            self.xPlayer += 1

            if self.xPlayer > 614:
                self.xPlayer = 614

        elif pressed[pygame.K_LEFT]:
            self.xPlayer -= 1

            if self.xPlayer < -4:
                self.xPlayer = -4
                time.sleep(5000)

        screen.blit(imgPlayer, (self.xPlayer, self.yPlayer))


class Car:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.5

    def move(self):
        if self.x == 490:
            self.x = -self.x + 390

        self.x += self.speed
        screen.blit(imgCar, (self.x, self.y))


background = pygame.image.load("background.png")
background_size = background.get_size()
w, h = background_size
screen = pygame.display.set_mode((w, h))

done = False
pygame.init()
pygame.display.set_caption("Frogger game")
pygame.display.update()

## Player
imgPlayer = pygame.image.load("player.png")
player = Player()

## Car
imgCar = pygame.image.load("car.png")
cars = []
x = 0

## Linha 1
for i in range(0, 8):
    x += 120
    cars.append(Car(x, 493))

## Linha 2
for i in range(0, 8):
    x += 100
    cars.append(Car(x, 449))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    key = pygame.key.get_pressed()
    screen.blit(background, (0, 0))
    player.move(key)
    print(player.yPlayer)
    for car in cars:
        car.move()
    pygame.display.update()
