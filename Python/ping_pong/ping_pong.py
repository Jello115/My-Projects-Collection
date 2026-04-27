import pygame
import math
import random
import time

# screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
BG_COLOR = (48, 46, 46)
BG_IMAGE = pygame.image.load('ramadan_bg.png')

# Player settings
PLAYER_WIDTH = 75
PLAYER_HEIGHT = 10
player_x = SCREEN_WIDTH//2
player_y = SCREEN_HEIGHT - PLAYER_HEIGHT*5


# display settings
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Ping Pong')
clock = pygame.time.Clock()

# player
player = pygame.Surface((PLAYER_WIDTH,PLAYER_HEIGHT))
player_rect = player.get_rect(center = (player_x,player_y))
player_speed = 7
player.fill((255,255,255))
Time = 0
# Ball
def ball_reset():
    global ball_x,ball_y,ball,ball_speed_x,ball_speed_y,reset_ball
    ball_x = SCREEN_WIDTH//2
    ball_y = SCREEN_HEIGHT//2 -100
    ball_speeds_x = [-7,7,-9,9]
    ball_speeds_y = [-7,7,-9]
    ball_speed_x = random.choice(ball_speeds_x)
    ball_speed_y = random.choice(ball_speeds_y)
    ball = pygame.Rect(ball_x,ball_y,15,15)
    reset_ball = False
ball_reset()

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf',32)


b_l = []

for i in range(10):
    b_l.append((random.randint(20,SCREEN_WIDTH-50),random.randint(20,SCREEN_HEIGHT-250)))
brick = pygame.Surface((40,15))
brick.fill((173, 173, 173))


while True:
    dt = clock.tick()/1000
    if reset_ball == False:
        Time = pygame.time.get_ticks()
    else:
        Time = 0
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN or keys[pygame.K_SPACE] and reset_ball:
            ball_reset()
            
    if keys[pygame.K_LEFT]:
        player_rect.left -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.left += player_speed

    if player_rect.left < 0:
        player_rect.left = 0
    elif player_rect.right > SCREEN_WIDTH:
        player_rect.right = SCREEN_WIDTH

    screen.fill(BG_COLOR)
    # update_image = pygame.transform.scale(BG_IMAGE, (SCREEN_WIDTH,SCREEN_HEIGHT))
    # screen.blit(update_image, (0,0))
    screen.blit(player,player_rect)
    pygame.draw.ellipse(screen, (253, 235, 155), ball)
    ball.centerx += ball_speed_x
    ball.centery += ball_speed_y

    for pos in b_l:
        screen.blit(brick,(pos))

    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if player_rect.colliderect(ball):
        if abs(ball.bottom - player_rect.top) < 10:
            ball_speed_y *= -1
            score += 1
        elif abs(ball.top - player_rect.bottom) < 10:
            ball_speed_y *= -1
        elif abs(ball.left - player_rect.right) < 10 and ball_speed_x < 0:
            ball_speed_x *= -1
            score += 1
        elif abs(ball.right - player_rect.left) < 10 and ball_speed_x > 0:
            ball_speed_x *= -1
            score += 1
    if ball.bottom >= SCREEN_HEIGHT:
        score = 0
        ball_speed_x = 0
        ball_speed_y = 0
        ball.center = (ball_x,ball_y)
        reset_ball = True

        

    player_text = font.render(f"{score}",False,(200,200,200))
    time_text = font.render(f"Time: {Time//1000}",False,(200,200,200))
    screen.blit(player_text,(SCREEN_WIDTH//2 - 10,100))
    screen.blit(time_text,(20,20))
    

    pygame.display.update()
    clock.tick(60)