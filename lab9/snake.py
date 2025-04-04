import pygame
import time
import random

# snake speed
snake_speed = 15

# window size
window_x = 720
window_y = 480

# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# initialize pygame
pygame.init()
pygame.display.set_caption('snake')
game_window = pygame.display.set_mode((window_x, window_y))

# frame controller
fps = pygame.time.Clock()

# snake position and body
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# function to spawn food using only basic variables
def spawn_food():
    x = random.randrange(1, (window_x // 10)) * 10
    y = random.randrange(1, (window_y // 10)) * 10
    value = random.choice([5, 10, 15])
    spawn_time = time.time()
    return x, y, value, spawn_time

# initial food
food_x, food_y, food_value, food_time = spawn_food()
food_spawn = True

# initial direction and score
direction = 'RIGHT'
change_to = direction
score = 0

# show score function
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('your score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# main game loop
while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_to = 'RIGHT'

    # prevent snake from reversing
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # move the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # insert new head to snake body
    snake_body.insert(0, list(snake_position))

    # snake eats food
    if snake_position == [food_x, food_y]:
        score += food_value
        food_spawn = False
    else:
        snake_body.pop()

    # food respawn or timeout
    if not food_spawn:
        food_x, food_y, food_value, food_time = spawn_food()
        food_spawn = True
    elif time.time() - food_time > 8:
        food_x, food_y, food_value, food_time = spawn_food()

    # fill background
    game_window.fill(black)

    # draw snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # draw food
    pygame.draw.rect(game_window, blue, pygame.Rect(food_x, food_y, 10, 10))

    # check boundaries
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # check collision with self
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # increase speed based on score
    snake_speed = 15 + (score // 20)

    # show score
    show_score(1, white, 'times new roman', 20)

    pygame.display.update()
    fps.tick(snake_speed)
