import pygame
import random


class Player:

    def __init__(self):
        self.xPlayer = w / 2 - 20
        self.yPlayer = 300 - 20
        self.speed = 0.5
        self.move_like_log = False
        self.first_Time = True

    def move(self, pressed):
        global points

        if self.move_like_log:
            self.xPlayer += 0.5

        if pressed[pygame.K_UP]:
            self.yPlayer -= 0.7

            points = points + 1 / 10

        elif pressed[pygame.K_DOWN]:
            self.yPlayer += 0.7

            if points != 0:
                points -= 1 / 10
                if points < 0:
                    points = 0

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
        self.first = False

    def move(self):
        global y_cars
        global cars

        if self.y > h:
            self.y -= h
            self.x = 0 - random.randint(0, 11) * 287

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
            if (x_player >= self.x - 25) and (x_player <= self.x + 30):
                return True


class Wood:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.5

    def move(self):
        if self.y > h:
            self.y -= h
            self.x += random.randint(0, 4) * 10

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

    def intersects(self, x_player, y_player):
        if (y_player <= self.y + 10) and (y_player >= self.y - 25):
            if (x_player >= self.x - 22) and (x_player <= self.x + 50):
                return True


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
y_cars = 493
cars = []

## Wood
imgWood = pygame.image.load("wood.png")
woods = []
previous_position_log = 0

## State
state = 0

## Clock
clock = pygame.time.Clock()


def play_music(music, loops):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops)


def show_points():
    global points
    black = (0, 0, 0)
    font = pygame.font.Font('machine_gunk.ttf', 20)
    title = font.render(str(int(points)), True, black)
    screen.blit(title, (20, 20))


def initialize_woods():
    global woods
    woods_aux = []

    x = 100

    ## Linha 1
    for i in range(0, 16):
        x += 100
        woods_aux.append(Wood(x, 248))

    x = 0

    ## Linha 2
    for i in range(0, 16):
        x += 100
        woods_aux.append(Wood(x, 225))

    x = 200

    ## Linha 3
    for i in range(0, 16):
        x += 100
        woods_aux.append(Wood(x, 200))

    x = 300

    ## Linha 4
    for i in range(0, 16):
        x += 100
        woods_aux.append(Wood(x, 175))

    x = 150

    ## Linha 5
    for i in range(0, 16):
        x += 100
        woods_aux.append(Wood(x, 150))

    x = 70

    ## Linha 6
    for i in range(0, 16):
        x += 120
        woods_aux.append(Wood(x, 125))

    x = 120

    ## Linha 7
    for i in range(0, 16):
        x += 80
        woods_aux.append(Wood(x, 100))

    x = 180

    ## Linha 8
    for i in range(0, 16):
        x += 120
        woods_aux.append(Wood(x, 75))

    x = 140

    ## Linha 9
    for i in range(0, 16):
        x += 110
        woods_aux.append(Wood(x, 45))

    x = 150
    woods = woods_aux


def initialize_cars():
    global cars
    global y_cars
    cars_aux = []
    x = 0

    ## Linha 1
    for i in range(0, 16):
        x += (random.randint(1, 9)) * 57
        cars_aux.append(Car(x, y_cars))

    x = 0

    ## Linha 2
    for i in range(0, 16):
        x += (random.randint(2, 9)) * 57
        cars_aux.append(Car(x, y_cars - 44))

    x = 0

    ## Linha 3
    for i in range(0, 16):
        x += (random.randint(2, 9)) * 57
        cars_aux.append(Car(x, y_cars - 44 * 2))

    x = 0

    ## Linha 4
    for i in range(0, 16):
        x += (random.randint(2, 9)) * 57
        cars_aux.append(Car(x, y_cars - 44 * 3))

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
        tr_title = title.get_rect()
        tr_sub_title = sub_title.get_rect()
        tr_title.center = (w // 2, h // 2 - 50)
        tr_sub_title.center = (w // 2, h // 2)
        screen.blit(title, tr_title)
        screen.blit(sub_title, tr_sub_title)

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
        clock.tick(500)


## Precisamos fazer a tela de help e ajuda
'''def instructions():
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

    pygame.display.update()'''


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
        tr_menu.center = (w // 2, h // 2 - 50)
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


def is_in_log(x, y, position):
    global woods
    if woods[position].intersects(x, y):
        return True
    else:
        return False


def update_game():
    global previous_position_log
    global state
    global yB
    global yB2
    global points
    points = 0
    yB = 0
    yB2 = 0 - h
    initialize_cars()
    initialize_woods()
    far_north = 35
    far_south = 249
    position_log = 0
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

        cont = 0
        for wood in woods:
            wood.move()

            if wood.intersects(player.xPlayer, player.yPlayer):
                position_log = cont
                previous_position_log = position_log
                player.move_like_log = True

            cont += 1

        player.move(key)

        if (player.yPlayer < far_north) and player.first_Time:
            player.yPlayer = far_north - 10
            player.first_Time = False
            far_south = player.yPlayer - 368
            far_north = far_south - 230

        show_points()
        yB += 0.2
        yB2 += 0.2
        far_south += 0.2
        far_north += 0.2
        player.yPlayer += 0.2

        if player.yPlayer > h:
            play_music(music_game_over, 1)
            state = 4
            return

        for car in cars:
            car.move()

            if car.intersects(player.xPlayer, player.yPlayer):
                state = 4

        if not is_in_log(player.xPlayer, player.yPlayer, position_log):
            player.move_like_log = False

        if (player.yPlayer < far_south) and (player.yPlayer > far_north):
            if previous_position_log == position_log:
                if not is_in_log(player.xPlayer, player.yPlayer, position_log):
                    state = 4

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_p]:
            pause()

        if far_north < 0:
            player.first_Time = True

        clock.tick(200)
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
        state = 0
        return

    pygame.display.update()


def finish():
    global done
    done = True


'''0: menu / 1: instructions / 2: game / 3: pause / 4: game_over / 5: finish'''

while not done:
    if state == 0:
        menu()
        '''elif state == 1:
        instructions()'''
    elif state == 2:
        pygame.mixer.music.stop()
        update_game()
    elif state == 3:
        pause()
    elif state == 4:
        game_over()
    elif state == 5:
        finish()
