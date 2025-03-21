import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)

BALL_SIZE = 50
BALL_RADIUS = BALL_SIZE // 2
ball_x = (SCREEN_WIDTH - BALL_SIZE) // 2
ball_y = (SCREEN_HEIGHT - BALL_SIZE) // 2

BALL_SPEED = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ball")

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        ball_y -= BALL_SPEED
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        ball_y += BALL_SPEED
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        ball_x -= BALL_SPEED
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        ball_x += BALL_SPEED


    ball_x = max(0, min(SCREEN_WIDTH - BALL_SIZE, ball_x))
    ball_y = max(0, min(SCREEN_HEIGHT - BALL_SIZE, ball_y))

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x + BALL_RADIUS, ball_y + BALL_RADIUS), BALL_RADIUS)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()