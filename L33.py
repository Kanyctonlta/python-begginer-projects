import random

import pygame

pygame.init()

WIDTH = 700
HEIGHT = 400

clock = pygame.time.Clock()
pygame.display.set_caption('Google Dino')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

score = 0
sprite = 0
running_sprites = [pygame.image.load("pic/dino2.png"),
                   pygame.image.load("pic/dino3.png")]
jump_count = 6
y_dino = HEIGHT - 100

ground_pic = pygame.image.load("pic/ground.png")
ground_rect = ground_pic.get_rect()
ground_rect.x = 0
ground_rect.centery = HEIGHT - 80
ground_speed = 2

cactus_sprites = [pygame.image.load("pic/cactus/LargeCactus1.png"),
                 pygame.image.load("pic/cactus/LargeCactus2.png"),
                 pygame.image.load("pic/cactus/LargeCactus3.png"),
                 pygame.image.load("pic/cactus/SmallCactus1.png"),
                 pygame.image.load("pic/cactus/SmallCactus2.png"),
                 pygame.image.load("pic/cactus/SmallCactus3.png")]
c_sprite = 0
cactus_x = WIDTH
cactus_y = HEIGHT - 80
cactus_pic = cactus_sprites[random.randint(0, 5)]

font = pygame.font.Font(None, 20)
text_end = basic_font.render(f'Конец игры', True, 'white')

def animate():
    global jump, jump_count, y_dino
    global sprite
    sprite += 0.05
    if sprite >= 2:
        sprite = 0
    image = running_sprites[int(sprite)]
    dino_rect = image.get_rect()
    dino_rect.centery = y_dino
    dino_rect.centerx = 50
    screen.blit(image, dino_rect)
    if jump:
        if jump_count >= -6:
            jump_count -= 0.2
            if jump_count <= 0:
                y_dino += jump_count ** 2 / 2
            else:
                y_dino -= jump_count ** 2 / 2
        else:
            jump = False
            jump_count = 6
            y_dino = HEIGHT - 100
        screen.blit(image, dino_rect)
    return dino_rect


def move_ground():
    global score, ground_speed
    if score > 500:
        ground_speed = 3
    elif score > 1000:
        ground_speed = 4
    ground_rect.x -= ground_speed
    if ground_rect.x <= -500:
        ground_rect.x = 0
    screen.blit(ground_pic, ground_rect)
    return ground_speed


def dance_cactus():
    global cactus_sprites, c_sprite
    c_sprite += 0.02
    if c_sprite > 6:
        c_sprite = 0
    cactus = cactus_sprites[int(c_sprite)]
    cactus_rect = cactus.get_rect()
    cactus_rect.bottomleft = 10, HEIGHT - 80
    screen.blit(cactus, cactus_rect)


def move_cactus():
    global cactus_x, cactus_y, cactus_pic
    cactus_x -= ground_speed
    if cactus_x < -100:
        cactus_x = WIDTH
        cactus_pic = cactus_sprites[random.randint(0, 5)]
    cactus_pic_rect = cactus_pic.get_rect()
    cactus_pic_rect.bottomleft = cactus_x, cactus_y
    screen.blit(cactus_pic, cactus_pic_rect)
    cactus_pic_rect.cola
    return сactus_pic_rect


def count_score():
    global score
    score += 1
    font = pygame.font.Font(None, 20)
    #text_score = font.render('Счёт: ' +str(score), True, 'black')
    text_score = font.render(f'Счёт: {score}', True, 'black')
    screen.blit(text_score, (10, 30))


def move_ptero():
    global ptero_sprite, x_ptero, y_ptero, ground_speed
    if score > 500:
        x_ptero -= ptero_speed
        if x_ptero < random.randint(-500, -200):
            x_ptero = WIDTH
            y_ptero = random.choice(ptero_height)
        ptero_sprite += 0.06
        if ptero_sprite >= 2:
            ptero_sprite = 0
        image = ptero_sprites[int(ptero_sprite)]
        rect = image.get_rect()
        rect.center = x_ptero, y_ptero
        screen.blit(image, rect)
        return rect


right_button = False
left_button = False
start = False
jump = False

GO = True
while GO:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GO = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = True
            if event.button == 1:
                left_button = True
                jump = True
                print('нажата ЛКМ')
            if event.button == 3:
                right_button = True
                print('нажата ПКМ')
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_button = False
            if event.button == 3:
                right_button = False

    screen.fill("white")
    if start:
        if animate().colliderect(move_cactus()):
            screen.fill('black')
            GO = False
        if score > 500:
            move_ptero()
        #animate()
        move_ground()
        # dance_cactus()
        #move_cactus()
        count_score()
    pygame.display.flip()
    clock.tick(100)

pygame.quit()

