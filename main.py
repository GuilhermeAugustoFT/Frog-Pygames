from typing import Type
import pygame
import time

class Player:

    def __init__(self):
        self.xPlayer = w / 2 - 20
        self.yPlayer = 570 - 20

    def move(self, pressed):
        global points
        if pressed[pygame.K_UP]:
            self.yPlayer -= 0.7

            points = int(points + 1 / 10)

        elif pressed[pygame.K_DOWN]:
            self.yPlayer += 0.7

            points = int(points + 1 / 10)

        elif pressed[pygame.K_RIGHT]:
            self.xPlayer += 0.7

        elif pressed[pygame.K_LEFT]:
            self.xPlayer -= 0.7

        screen.blit(imgPlayer, (self.xPlayer, self.yPlayer))


class Car:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.5

    def move(self):

        if self.y > h:
            self.y -= h

        self.y += 0.2
        if self.x == 490:
            self.x = -self.x + 470

        self.x += self.speed
        screen.blit(imgCar, (self.x, self.y))

    def move_simple(self):
        if self.x == 490:
            self.x = -self.x + 470

        self.x += self.speed
        screen.blit(imgCar, (self.x, self.y))

    def intersects(self, x_player, y_player):
        if (y_player <= self.y + 20) and (y_player >= self.y - 20):
            if (x_player >= self.x - 20) and (x_player <= self.x + 20):
                return True


class Wood:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.5

    def move(self):
        if self.y > h:
            self.y -= h

        self.y += 0.2
        if self.x == 490:
            self.x = -self.x + 470

        self.x += self.speed
        screen.blit(imgWood, (self.x, self.y))

    def move_simple(self):
        if self.x == 490:
            self.x = -self.x + 470

        self.x += self.speed
        screen.blit(imgWood, (self.x, self.y))




## Background
background = pygame.image.load("background.png")
background_size = background.get_size()
w, h = background_size
screen = pygame.display.set_mode((w, h))
yB = 0
yB2 = 0 - h

## Window
done = False
pygame.init()
music_menu = 'music_menu.mp3'
music_game = 'music_game.mp3'
music_game_over = 'music_game_over.mp3'
music_paused = 'music_paused.mp3'
pygame.init()
pygame.display.set_caption("Frogger Game")
pygame.display.update()

## Player
imgPlayer = pygame.image.load("frog.png")
player = Player()
pygame.mixer.init()
points = 0

## Car
imgCar = pygame.image.load("car.png")
cars = []

## Wood
imgWood = pygame.image.load("wood.png")
woods = []

state = 0


def play_music(music, loops):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops)


def show_points():
    global points
    black = (0, 0, 0)
    font = pygame.font.Font('machine_gunk.ttf', 20)
    title = font.render(str(points), True, black)
    screen.blit(title, (20, 20))


def initialize_woods():
    global woods
    woods_aux = []

    x = 100

    ## Linha 1
    for i in range(0, 16):
        x += 100
        woods_aux.append(Wood(x, 255))

    x = 0

    ## Linha 2
    for i in range(0, 16):
        x += 100
        woods_aux.append(Wood(x, 235))

    x = 200

    ## Linha 3
    for i in range(0, 16):
        x += 100
        woods_aux.append(Wood(x, 215))

    x = 300

    ## Linha 4
    for i in range(0, 16):
        x += 100
        woods_aux.append(Wood(x, 195))

    x = 150

    ## Linha 5
    for i in range(0, 16):
        x += 100
        woods_aux.append(Wood(x, 175))

    x = 70

    ## Linha 6
    for i in range(0, 16):
        x += 120
        woods_aux.append(Wood(x, 155))

    x = 120

    ## Linha 7
    for i in range(0, 16):
        x += 80
        woods_aux.append(Wood(x, 135))

    x = 180

    ## Linha 8
    for i in range(0, 16):
        x += 120
        woods_aux.append(Wood(x, 115))

    x = 140

    ## Linha 9
    for i in range(0, 16):
        x += 110
        woods_aux.append(Wood(x, 95))

    x = 150

    ## Linha 10
    for i in range(0, 16):
        x += 100
    woods_aux.append(Wood(x, 75))

    ## Linha 11
    for i in range(0, 16):
        x += 100
    woods_aux.append(Wood(x, 20))

    woods = woods_aux


def initialize_cars():
    global cars
    cars_aux = []
    x = 0
    ## Linha 1
    for i in range(0, 16):
        x += 120
        cars_aux.append(Car(x, 493))

    x = 0

    ## Linha 2
    for i in range(0, 16):
        x += 150
        cars_aux.append(Car(x, 449))

    x = 0

    ## Linha 3
    for i in range(0, 16):
        x += 180
        cars_aux.append(Car(x, 358))

    x = 0

    ## Linha 4
    for i in range(0, 16):
        x += 140
        cars_aux.append(Car(x, 398))

    cars = cars_aux


def is_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True


def menu():
    initialize_woods()
    initialize_cars()
    global state
    global yB
    global yB2
    while True:
        black = (0, 0, 0)
        if yB2 > 0:
            yB = 0
            yB2 = 0 - h

        screen.blit(background, (0, yB2))

        screen.blit(background, (0, yB))
        yB += 0.2
        yB2 += 0.2

        pygame.init()

        for car in cars:
            car.move()

        for wood in woods:
            wood.move()

        font = pygame.font.Font('machine_gunk.ttf', 70)
        title = font.render('Frogger Game', True, black)
        font = pygame.font.Font('machine_gunk.ttf', 20)
        sub_title = font.render('Press g for play !', True, black)
        '''font = pygame.font.Font('freesansbold.ttf', 18)'''
        '''instructions_txt = font.render('Press i for instructions', True, red)'''
        tr_title = title.get_rect()
        tr_sub_title = sub_title.get_rect()
        '''tr_instructions = instructions_txt.get_rect()'''
        tr_title.center = (w // 2, h // 2 - 50)
        tr_sub_title.center = (w // 2, h // 2)
        '''tr_instructions.center = (w // 2, h // 2 + 150)'''
        screen.blit(title, tr_title)
        screen.blit(sub_title, tr_sub_title)
        '''screen.blit(instructions_txt, tr_instructions)'''

        pressed = pygame.key.get_pressed()

        if is_quit():
            state = 5
            return

        if pressed[pygame.K_g]:
            state = 2
            return

        if pressed[pygame.K_i]:
            state = 1
            return

        if is_quit():
            state = 5
            return

        pygame.display.update()


def instructions():
    global state
    black = (0, 0, 0)
    red = (255, 0, 0)
    screen.fill(black)
    font = pygame.font.Font('freesansbold.ttf', 25)
    text_instructions1 = font.render('-> Use the arrows to move', True, red)
    text_instructions2 = font.render('-> Use p to pause the game', True, red)
    font = pygame.font.Font('freesansbold.ttf', 18)
    text_exit = font.render('Press m to back to menu', True, red)
    tr_text1 = text_instructions1.get_rect()
    tr_text2 = text_instructions2.get_rect()
    tr_exit = text_exit.get_rect()
    tr_text1.center = (w // 2, h // 2 - 50)
    tr_text2.center = (w // 2, h // 2)
    tr_exit.center = (w // 2, h // 2 + 120)
    screen.blit(text_instructions1, tr_text1)
    screen.blit(text_instructions2, tr_text2)
    screen.blit(text_exit, tr_exit)

    pressed = pygame.key.get_pressed()

    if is_quit():
        state = 5
        return

    if pressed[pygame.K_m]:
        state = 0
        return

    pygame.display.update()


def pause():
    red = (255, 0, 0)
    font = pygame.font.Font('machine_gunk.ttf', 18)
    text_back = font.render('Press ESC to resume', True, red)
    white = (255, 255, 255)
    color = white
    while True:
        global state
        black = (0, 0, 0)
        screen.fill(black)
        font = pygame.font.Font('machine_gunk.ttf', 60)
        text_instructions = font.render('Paused', True, white)
        font = pygame.font.Font('machine_gunk.ttf', 18)
        text_menu = font.render('Press M to back to menu', True, color)
        tr_text = text_instructions.get_rect()
        tr_back = text_back.get_rect()
        tr_menu = text_menu.get_rect()
        tr_text.center = (w // 2, h // 2 - 200)
        tr_back.center = (w // 2, h // 2 - 100)
        tr_menu.center = (w // 2, h // 2  - 50)
        screen.blit(text_instructions, tr_text)
        screen.blit(text_back, tr_back)
        screen.blit(text_menu, tr_menu)

        pressed = pygame.key.get_pressed()

        if is_quit():
            state = 5
            return

        if pressed[pygame.K_DOWN]:
            color = red
            play_music(music_paused, 1)
            text_back = font.render('Press ESC to resume', True, white)
            text_menu = font.render('Press M to back to menu', True, color)
            tr_back = text_back.get_rect()
            tr_menu = text_menu.get_rect()
            tr_back.center = (w // 2, h // 2 - 100)
            tr_menu.center = (w // 2, h // 2 - 50)
            screen.blit(text_back, tr_back)
            screen.blit(text_menu, tr_menu)

        if pressed[pygame.K_UP]:
            color = white
            play_music(music_paused, 1)
            text_back = font.render('Press ESC to resume', True, red)
            text_menu = font.render('Press M to back to menu', True, color)
            tr_back = text_back.get_rect()
            tr_menu = text_menu.get_rect()
            tr_back.center = (w // 2, h // 2 - 100)
            tr_menu.center = (w // 2, h // 2 - 50)
            screen.blit(text_back, tr_back)
            screen.blit(text_menu, tr_menu)

        if pressed[pygame.K_m]:
            play_music(music_menu, -1)
            state = 0
            return

        if pressed[pygame.K_ESCAPE]:
            break

        pygame.display.update()


def update_game():
    global state
    global yB
    global yB2
    global points
    points = 0
    yB = 0
    yB2 = 0 - h
    initialize_cars()
    initialize_woods()
    while state == 2:
        if is_quit():
            state = 5
            break

        if yB2 > 0:
            yB = 0
            yB2 = 0 - h

        screen.blit(background, (0, yB2))
        key = pygame.key.get_pressed()
        screen.blit(background, (0, yB))
        player.move(key)
        print(player.yPlayer)
        show_points()
        yB += 0.2
        yB2 += 0.2
        player.yPlayer += 0.2

        if player.yPlayer > h:
            play_music(music_game_over, 1)
            state = 4
            return

        for car in cars:
            car.move()

            if car.intersects(player.xPlayer, player.yPlayer):
                play_music(music_game_over, 1)
                state = 4

        for wood in woods:
            wood.move()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_p]:
            pygame.mixer.music.stop()
            pause()

        pygame.display.update()


def game_over():
    global state
    global player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = 5
            return
    white = (255, 255, 255)
    red = (255, 0, 0)
    screen.fill(white)
    font = pygame.font.Font('machine_gunk.ttf', 50)
    text = font.render('Game Over', True, red)
    font = pygame.font.Font('machine_gunk.ttf', 20)
    text2 = font.render('Press c to play again or m for go to menu', True, red)
    text_rect = text.get_rect()
    text_rect2 = text2.get_rect()
    text_rect.center = (w // 2, h // 2 - 50)
    text_rect2.center = (w // 2, h // 2 + 50)
    screen.blit(text, text_rect)
    screen.blit(text2, text_rect2)
    pressed = pygame.key.get_pressed()

    if is_quit():
        state = 5
        return

    if pressed[pygame.K_c]:
        state = 2
        player = Player()
        return

    if pressed[pygame.K_m]:
        play_music(music_menu, -1)
        state = 0
        return

    pygame.display.update()


def finish():
    global done
    done = True


'''0: menu / 1: instructions / 2: game / 3: pause / 4: game_over / 5: finish'''
'''state = 0'''

play_music(music_menu, -1)
while not done:
    if state == 0:
        menu()
    elif state == 1:
        instructions()
    elif state == 2:
        pygame.mixer.music.stop()
        update_game()
    elif state == 3:
        pause()
    elif state == 4:
        game_over()
    elif state == 5:
        finish()
