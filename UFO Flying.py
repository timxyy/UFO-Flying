import pygame as pg
from random import randint
import time

pg.init()
screen = pg.display.set_mode((700, 700))
clock = pg.time.Clock()
display_width, display_height = screen.get_size()
play_list = ['main-menu.mp3', 'overworld.mp3', 'boss-battle.mp3']
for i in enumerate(play_list):
    play_list[i[0]] = 'Files for Code/UFO Files/' + i[1]
pg.mixer.music.load(play_list.pop(0))
pg.mixer.music.play(loops=-1)
pg.display.set_caption("UFO Landing")
sprites = ("space.png", "ufo.png", "lava.png", "win_portal.png",
           "lava2.png", "lava3.png", "lava4.png", "lava5.png",
           "lava6.png", "portal.png", "laser.png", "enemy.png",
           "ammo.png", "laser2.png", "lava7.png", "b0ss.png",
           "lava8.png", "lava9.png", "cool_lava.png", "title_screen.png",
           "death1.png", "credits.png", "cool_lava2.png")
sprite = ["Files for Code/UFO Files/" + i for i in sprites]
running = True
x = 100
y = display_height / 2
bullet_x = x
bullet_y = y
object_y2 = 600
object_x2 = 600
x_change, accel_x, y_change, accel_y, object_y, object_x = 0, 0, 0, 0, 0, 0
timer = 120
direction = 5
max_speed = 6
level = 1
boss_lives = 3
r = False
hiy = -700
hiy2 = 0
count = 1800
rain_loc = [randint(0, 850), 0]
rain_list = [rain_loc]
loaded = False
dead = False
fired = False
title_screen = True


def drop_rain(rain_list):
    delay = randint(0, 20)
    if len(rain_list) < 10 and delay < 2:
        x_pos = randint(0, 850)
        y_pos = 0
        rain_list.append([x_pos, y_pos])


def draw_rain(rain_list):
    for rain_loc in rain_list:
        screen.blit(pg.image.load(sprite[18]), (rain_loc[0], rain_loc[1]))


def update_rain(rain_list):
    for index, rain_loc in enumerate(rain_list):
        if 0 <= rain_loc[1] < 700:
            rain_loc[1] += 5
        else:
            rain_list.pop(index)


def rain_col(rain_loc):
    ex = rain_loc[0]
    ey = rain_loc[1]
    if x - 50 < ex < x + 32:
        if y - 50 < ey < y + 30:
            return True
    return False


def bullet_col(rain_loc):
    ex = rain_loc[0]
    ey = rain_loc[1]
    if bullet_x - 50 < ex < bullet_x + 20:
        if bullet_y - 50 < ey < bullet_y + 30:
            return True
    return False


def bullet_collision_detection(rain_list):
    for rain_loc in rain_list:
        if bullet_col(rain_loc):
            return True
    return False


def collision_detection(rain_list):
    for rain_loc in rain_list:
        if rain_col(rain_loc):
            return True
    return False


def cycle():
    global hiy
    global hiy2
    screen.blit(pg.image.load(sprite[16]), (-25, hiy))
    screen.blit(pg.image.load(sprite[17]), (200, hiy))
    screen.blit(pg.image.load(sprite[16]), (550, hiy2))
    screen.blit(pg.image.load(sprite[17]), (-125, hiy2))
    hiy += 5
    hiy2 += 5
    if hiy > 700:
        hiy = -700
    if hiy2 > 700:
        hiy2 = -700


def level_begin(xx):
    global x
    global y
    global accel_x
    global accel_y
    global level
    global loaded
    global dead
    global fired
    x = xx
    y = display_height / 2
    accel_x = 0
    accel_y = 0
    level += 1
    loaded = False
    dead = False
    fired = False


def level_failed(xx):
    global x
    global y
    global accel_x
    global accel_y
    global bullet_x
    global bullet_y
    global level
    global loaded
    global fired
    global dead
    global boss_lives
    screen.blit(pg.image.load(sprite[20]), (x, y))
    boss_lives = 3
    x = xx
    y = display_height / 2
    accel_x = 0
    accel_y = 0
    bullet_x = 0
    bullet_y = 0
    loaded = False
    fired = False
    dead = False


def player():
    screen.blit(pg.image.load(sprite[1]), (x, y))


def level_draw():
    global x
    global y
    global bullet_x
    global bullet_y
    global accel_x
    global accel_y
    global object_x
    global object_y
    global object_y2
    global object_x2
    global hiy
    global hiy2
    global direction
    global loaded
    global fired
    global dead
    global boss_lives
    global r
    global timer
    global level

    if level == 1:
        screen.blit(pg.image.load(sprite[3]), (650, 350))
        if 618 < x < 680 and 380 > y > 318:
            level_begin(100)
            pg.mixer.music.load('Files for Code/UFO Files/warn.mp3')
            pg.mixer.music.play()
            time.sleep(2)
            pg.mixer.music.load(play_list.pop(0))
            pg.mixer.music.play(loops=-1)
    if level == 2:
        screen.blit(pg.image.load(sprite[3]), (650, 350))
        screen.blit(pg.image.load(sprite[2]), (200, 200))
        screen.blit(pg.image.load(sprite[2]), (450, 0))
        if 168 < x < 300 and y > 168:
            level_failed(100)
        if 418 < x < 550 and y < 500:
            level_failed(100)
        if 618 < x < 680 and 380 > y > 318:
            level_begin(100)

    if level == 3:
        screen.blit(pg.image.load(sprite[3]), (650, 350))
        screen.blit(pg.image.load(sprite[5]), (200, 0))
        screen.blit(pg.image.load(sprite[4]), (200, 500))
        screen.blit(pg.image.load(sprite[5]), (450, 0))
        screen.blit(pg.image.load(sprite[4]), (450, 500))
        if 168 < x < 250:
            if y > 468 or y < 400:
                level_failed(100)
        if 418 < x < 500:
            if y > 468 or y < 400:
                level_failed(100)
        if 618 < x < 680 and 380 > y > 318:
            level_begin(100)
            direction = -7

    if level == 4:
        if object_y > 550:
            direction = -7
        if object_y < 0:
            direction = 7
        object_y += direction
        object_y2 -= direction
        screen.blit(pg.image.load(sprite[6]), (200, object_y))
        screen.blit(pg.image.load(sprite[6]), (400, object_y))
        screen.blit(pg.image.load(sprite[6]), (200, object_y2))
        screen.blit(pg.image.load(sprite[6]), (400, object_y2))
        screen.blit(pg.image.load(sprite[3]), (650, 350))
        if 168 < x < 250 or 368 < x < 450:
            if object_y - 32 < y < object_y + 100 or object_y2 - 32 < y < object_y2 + 100:
                level_failed(100)
        if 618 < x < 680 and 380 > y > 318:
            level_begin(100)
            direction = 5

    if level == 5:
        if object_y > 550:
            direction = -5
        if object_y < 200:
            direction = 5
        object_y += direction
        screen.blit(pg.image.load(sprite[3]), (650, 350))
        screen.blit(pg.image.load(sprite[5]), (200, 0))
        screen.blit(pg.image.load(sprite[4]), (200, 500))
        screen.blit(pg.image.load(sprite[5]), (450, 0))
        screen.blit(pg.image.load(sprite[4]), (450, 500))
        screen.blit(pg.image.load(sprite[7]), (200, object_y))
        screen.blit(pg.image.load(sprite[7]), (450, object_y))
        if 168 < x < 250 or 418 < x < 500:
            if not 400 < y < 468 or object_y - 32 < y < object_y + 50:
                level_failed(100)
        if 618 < x < 680 and 380 > y > 318:
            level_begin(400)

    if level == 6:
        screen.blit(pg.image.load(sprite[9]), (550, 350))
        screen.blit(pg.image.load(sprite[9]), (100, 100))
        screen.blit(pg.image.load(sprite[8]), (200, 0))
        screen.blit(pg.image.load(sprite[3]), (100, 350))
        if 68 < x < 130 and 380 > y > 318:
            level_begin(100)
            direction = 10
            object_y2 = 250
        if 168 < x < 250:
            level_failed(display_width/2)
        if 518 < x < 600 and 318 < y < 400:
            x = 100
            y = 100
            accel_x = 0
            accel_y = 0

    if level == 7:
        screen.blit(pg.image.load(sprite[3]), (650, 350))
        screen.blit(pg.image.load(sprite[5]), (400, 0))
        screen.blit(pg.image.load(sprite[4]), (400, 500))
        if not loaded and not fired:
            screen.blit(pg.image.load(sprite[12]), (300, 150))
        if loaded and not fired:
            bullet_x = x
            bullet_y = y
        if fired:
            screen.blit(pg.image.load(sprite[10]), (bullet_x + 32, bullet_y))
            bullet_x += 5
        if not dead:
            screen.blit(pg.image.load(sprite[11]), (275, 400))
            if 243 < x and 368 < y < 552:
                level_failed(100)
            if 380 < bullet_y < 500 and bullet_x > 245:
                dead = True
                fired = False
        if bullet_x > 700:
            fired = False
        if 368 < x < 450:
            if y < 400 or y > 468:
                level_failed(100)
        if 618 < x < 680 and 380 > y > 318:
            level_begin(0)
            object_x = 400
            object_y = 351
        if 268 < x < 350 and 118 < y < 200:
            loaded = True

    if level == 8:
        if not loaded and not fired:
            screen.blit(pg.image.load(sprite[12]), (500, 350))
        if loaded and not fired:
            bullet_x = x
            bullet_y = y
        if fired:
            screen.blit(pg.image.load(sprite[10]), (bullet_x + 32, bullet_y))
            bullet_x += 5
        if not dead:
            object_x -= (object_x - x) / ((abs(object_x - x) + 0.1) / 2)
            object_y -= (object_y - y) / ((abs(object_y - y) + 0.1) / 2)
            screen.blit(pg.image.load(sprite[11]), (object_x, object_y))
            if object_y - 20 < bullet_y < object_y + 100 and object_x - 30 < bullet_x < object_x + 120 and fired:
                dead = True
                fired = False
            if object_y - 32 < y < object_y + 100 and object_x - 32 < x < object_x + 120:
                level_failed(0)
                object_x = 400
                object_y = 351
        if dead:
            screen.blit(pg.image.load(sprite[3]), (650, 350))
            if 618 < x < 680 and 380 > y > 318:
                level_begin(250)
                object_x = randint(0, 650)
                object_y = randint(350, 650)
                y = 600
                direction = 5
        if bullet_x > 700:
            fired = False
        if 462 < x < 550 and 380 > y > 318:
            loaded = True

    if level == 9:
        if not loaded and not fired:
            screen.blit(pg.image.load(sprite[12]), (75, 25))
        if loaded and not fired:
            bullet_x = x
            bullet_y = y
        if fired:
            screen.blit(pg.image.load(sprite[10]), (bullet_x + 32, bullet_y))
            bullet_x += 5
        if not dead:
            object_y2 += direction
            screen.blit(pg.image.load(sprite[11]), (580, object_y2))
            screen.blit(pg.image.load(sprite[14]), (200, 0))
            if object_y2 > 580:
                direction = -5
            if object_y2 < 0:
                direction = 5
            if x > 168:
                level_failed(100)
            if object_y2 - 20 < bullet_y < object_y2 + 100 and 700 > bullet_x > 550:
                dead = True
                fired = False
        if dead:
            screen.blit(pg.image.load(sprite[3]), (650, 350))
            if 618 < x < 680 and 380 > y > 318:
                level_begin(100)
                y = 350
                loaded = False
                fired = False
        if bullet_x > 700:
            fired = False
        if 618 < x < 680 and 380 > y > 318:
            level_begin(100)
        if 42 < x < 125 and y < 75:
            loaded = True

    if level == 10:
        screen.blit(pg.image.load(sprite[22]), (400, 0))
        screen.blit(pg.image.load(sprite[9]), (300, 100))
        screen.blit(pg.image.load(sprite[9]), (300, 318))
        screen.blit(pg.image.load(sprite[9]), (300, 568))
        screen.blit(pg.image.load(sprite[9]), (470, 100))
        screen.blit(pg.image.load(sprite[9]), (470, 318))
        screen.blit(pg.image.load(sprite[9]), (470, 568))
        if 268 < x < 330:
            if 68 < y < 130:
                x = 470
                y = 318
            elif 286 < y < 350:
                x = 470
                y = 100
            elif 536 < y < 600:
                x = 470
                y = 568
        if not loaded and not fired:
            screen.blit(pg.image.load(sprite[12]), (50, 50))
            if 12 < x < 100 and 12 < y < 82:
                loaded = True
        if loaded and not fired:
            bullet_x = x
            bullet_y = y
        if fired:
            screen.blit(pg.image.load(sprite[10]), (bullet_x + 32, bullet_y))
            bullet_x += 5
            if bullet_x > 700:
                fired = False
            if 270 < bullet_x < 330:
                if 70 < bullet_y < 130:
                    bullet_x = 470
                    bullet_y = 318
                elif 288 < bullet_y < 350:
                    bullet_x = 470
                    bullet_y = 100
                elif 538 < bullet_y < 600:
                    bullet_x = 470
                    bullet_y = 568
            if 340 < bullet_x < 450:
                fired = False
        if not dead:
            object_y2 += direction
            screen.blit(pg.image.load(sprite[11]), (580, object_y2))
            if object_y2 > 580:
                direction = -5
            if object_y2 < 0:
                direction = 5
            if fired:
                if object_y2 - 20 < bullet_y < object_y2 + 100 and 700 > bullet_x > 550:
                    dead = True
                    fired = False
            if object_y2 + 100 < y < object_y2 - 32 and x > 548:
                level_failed(100)
        if dead:
            screen.blit(pg.image.load(sprite[3]), (650, 350))
            if 618 < x < 680 and 380 > y > 318:
                level_begin(display_width / 2)
                object_x = randint(0, 650)
                object_y = randint(350, 650)
                y = 600
                direction = 5
                object_y2 = 25
                pg.mixer.music.load('Files for Code/UFO Files/bossmono.mp3')
                pg.mixer.music.play()
                time.sleep(11)
                pg.mixer.music.load(play_list.pop(0))
                pg.mixer.music.play(loops=-1)
        if 368 < x < 450:
            level_failed(100)
    if level == 11:
        if boss_lives == 3:
            drop_rain(rain_list)
            update_rain(rain_list)
            draw_rain(rain_list)
            if timer == 0:
                if collision_detection(rain_list) and not dead:
                    level_failed(350)
                    drop_rain(rain_list)
                    y = 600
                    object_x = randint(0, 650)
                    object_y = randint(350, 650)
                    direction = 5
                    object_y2 = 25
                    boss_lives = 3
                    pg.mixer.music.play(loops=-1)
                    timer = 120
            else:
                timer -= 1
            if bullet_collision_detection(rain_list):
                fired = False
        if boss_lives == 2:
            cycle()
            if hiy - 32 < y < hiy + 50:
                if x > 168 or x < 125:
                    level_failed(350)
                    y = 600
            if hiy2 - 32 < y < hiy2 + 50:
                if x > 518 or x < 475:
                    level_failed(350)
                    y = 600
                    object_x = randint(0, 650)
                    object_y = randint(350, 650)
                    direction = 5
                    object_y2 = 25
                    boss_lives = 3
                    hiy = -700
                    hiy2 = 0
                    pg.mixer.music.play(loops=-1)
            if fired:
                if hiy - 3 < bullet_y < hiy + 80:
                    if x > 180 or x < 125:
                        fired = False
                if hiy2 - 20 < bullet_y < hiy2 + 80:
                    if x > 530 or x < 475:
                        fired = False
        if boss_lives == 1:
            object_x2 -= (object_x2 - x) / ((abs(object_x2 - x) + 0.1) / 2.3)
            object_y2 -= (object_y2 - y) / ((abs(object_y2 - y) + 0.1) / 2.3)
            if fired:
                if object_y2 - 20 < bullet_y < object_y2 + 100:
                    if object_x2 + 100 > x > object_x2 - 20:
                        boss_lives -= 1
                        dead = True
                        object_y2 = 700
        if dead:
            pg.mixer.music.unload()
            pg.mixer.music.load('Files for Code/UFO Files/bossdie.mp3')
            pg.mixer.music.play()
            time.sleep(15)
            pg.mixer.music.load('Files for Code/UFO Files/credits.mp3')
            pg.mixer.music.play()
            level += 1
        if not dead:
            if boss_lives > 1:
                object_x2 += direction
            screen.blit(pg.image.load(sprite[15]), (object_x2, object_y2))
            if object_y2 - 32 < y < object_y2 + 120 and object_x2 - 32 < x < object_x2 + 100:
                level_failed(350)
                y = 600
                object_x = randint(0, 650)
                object_y = randint(350, 650)
                direction = 5
                object_y2 = 25
                boss_lives = 3
                pg.mixer.music.play(loops=-1)
                if boss_lives == 1:
                    boss_lives -= 1
        if object_x2 > 550:
            direction = -5
        if object_x2 < 200:
            direction = 5
        if loaded and not fired:
            bullet_x = x
            bullet_y = y
        if not loaded and not fired:
            screen.blit(pg.image.load(sprite[12]), (object_x, object_y))
            if object_x - 32 < x < object_x + 50 and object_y - 32 < y < object_y + 50:
                loaded = True
        if fired:
            screen.blit(pg.image.load(sprite[13]), (bullet_x + 8, bullet_y - 30))
            bullet_y -= 5
            if bullet_y < -30:
                fired = False
            if object_x2 - 20 < bullet_x < object_x2 + 100 and bullet_y < 145:
                fired = False
                boss_lives -= 1
                if boss_lives <= 0:
                    dead = True
                    timer = 120
        if loaded:
            object_x = randint(0, 650)
            object_y = randint(350, 650)

    if level == 12:
        screen.blit(pg.image.load(sprite[21]), (0, object_y2))
        object_y2 -= 1.5
        timer -= 1
        if not timer:
            level = 1


def main():
    global running
    global level
    global x
    global y
    global accel_x
    global accel_y
    global x_change
    global y_change
    global loaded
    global fired
    global title_screen
    while running:
        if title_screen:
            screen.blit(pg.image.load(sprite[19]), (0, 0))
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    title_screen = False
                    pg.mixer.music.load('Files for Code/UFO Files/synthesize.mp3')
                    pg.mixer.music.play()
                    time.sleep(4)
            pg.display.update()
        else:
            screen.blit(pg.image.load(sprite[0]), (0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP:
                        accel_y = -.25
                    if event.key == pg.K_LEFT:
                        accel_x = -.25
                    if event.key == pg.K_RIGHT:
                        accel_x += .25
                    if loaded:
                        if event.key == pg.K_DOWN:
                            loaded = False
                            fired = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_UP:
                        accel_y = .25
                    if event.key in (pg.K_LEFT, pg.K_RIGHT):
                        accel_x = 0
            y_change += accel_y
            x_change += accel_x
            if abs(y_change) >= max_speed:
                y_change = y_change / abs(y_change) * max_speed
            if accel_y == 0:
                y_change *= 0.92
            if abs(x_change) >= max_speed:
                x_change = x_change / abs(x_change) * max_speed
            if accel_x == 0:
                x_change *= 0.92
            x += x_change
            y += y_change
            if y < -32 or y > 700 or x < -32 or x > 700:
                level_failed(100)
                if level == 11:
                    level_failed(350)
            clock.tick(60)
            level_draw()
            player()
            pg.display.update()


main()
