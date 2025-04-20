import pygame
import time
import random
import psycopg2

# === DB CONFIG ===
def connect_db():
    return psycopg2.connect(
        dbname="snake_game",
        user="postgres",
        password="AtuKereK34",
        host="localhost"
    )

def load_user_score(username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT score, level FROM user_data WHERE username = %s ORDER BY id DESC LIMIT 1", (username,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result if result else (0, 1)

def save_user_score(username, score, level):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_data (username, score, level) VALUES (%s, %s, %s)", (username, score, level))
    conn.commit()
    cur.close()
    conn.close()

# === GAME SETTINGS ===
window_x, window_y = 720, 480
black, white, red, green, blue = (0,0,0), (255,255,255), (255,0,0), (0,255,0), (0,0,255)

def get_walls(level):
    if level == 1:
        return []
    elif level == 2:
        return [[i, 200] for i in range(100, 620, 10)]
    elif level == 3:
        return [[100, i] for i in range(100, 400, 10)] + [[600, i] for i in range(100, 400, 10)]
    return []

def spawn_food():
    return random.randrange(1, window_x//10)*10, random.randrange(1, window_y//10)*10, random.choice([5, 10, 15]), time.time()

def show_score(score, level):
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render(f"Score: {score} | Level: {level} (T to save)", True, white)
    game_window.blit(score_surface, (10, 10))

def game_over(score):
    font = pygame.font.SysFont('times new roman', 50)
    over_surface = font.render(f'Game Over! Score: {score}', True, red)
    game_window.blit(over_surface, over_surface.get_rect(center=(window_x/2, window_y/4)))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# === MAIN GAME LOOP ===
username = input("Enter your username: ")
score, level = load_user_score(username)
snake_speed = 15 + (level - 1) * 5
walls = get_walls(level)

pygame.init()
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

food_x, food_y, food_val, food_time = spawn_food()
food_spawn = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over(score)
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_w]:
                change_to = 'UP'
            elif event.key in [pygame.K_DOWN, pygame.K_s]:
                change_to = 'DOWN'
            elif event.key in [pygame.K_LEFT, pygame.K_a]:
                change_to = 'LEFT'
            elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                change_to = 'RIGHT'
            elif event.key == pygame.K_p:
                paused = True
                font = pygame.font.SysFont('times new roman', 30)
                pause_msg = font.render("Paused. Press R to resume", True, white)
                game_window.blit(pause_msg, (window_x // 4, window_y // 2))
                pygame.display.flip()
                while paused:
                    for ev in pygame.event.get():
                        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_r:
                            paused = False
            elif event.key == pygame.K_t:
                save_user_score(username, score, level)

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))

    if snake_pos == [food_x, food_y]:
        score += food_val
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn or time.time() - food_time > 8:
        food_x, food_y, food_val, food_time = spawn_food()
        food_spawn = True

    if score >= level * 50:
        level += 1
        walls = get_walls(level)
        snake_speed = 15 + (level - 1) * 5

    game_window.fill(black)

    for block in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(block[0], block[1], 10, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(food_x, food_y, 10, 10))
    for wall in walls:
        pygame.draw.rect(game_window, red, pygame.Rect(wall[0], wall[1], 10, 10))

    show_score(score, level)

    if (
        snake_pos[0] < 0 or snake_pos[0] >= window_x or
        snake_pos[1] < 0 or snake_pos[1] >= window_y or
        snake_pos in snake_body[1:] or
        snake_pos in walls
    ):
        game_over(score)

    pygame.display.update()
    fps.tick(snake_speed)