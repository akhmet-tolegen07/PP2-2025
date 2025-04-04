import pygame as pg
import random

# initialize pygame
pg.init()

# screen settings
w, h, fps = 400, 600, 60
is_running, lose = True, False
screen = pg.display.set_mode((w, h))
pg.display.set_caption('racer')
clock = pg.time.Clock()

y = 0
ry = 2 

# game variables
step, enemy_step, score, score_coin = 5, 5, 0, 0
N = 5  
speed_increase_amount = 1 

# load images
game_over = pg.image.load("C:\\Users\\Asus\\Desktop\\PP2-2025\\lab8\\race\\gameover.jpg")
bg = pg.image.load("C:\\Users\\Asus\\Desktop\\PP2-2025\\lab8\\race\\track.png")
game_over = pg.transform.scale(game_over, (w, h))

# load fonts
score_font = pg.font.SysFont("Verdana", 20)
score_coins = pg.font.SysFont("Verdana", 20)

# enemy class
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("C:\\Users\\Asus\\Desktop\\PP2-2025\\lab8\\race\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)

    def update(self):
        global score
        self.rect.move_ip(0, enemy_step)
        if self.rect.bottom > h + 90:
            score += 1
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# player class
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("C:\\Users\\Asus\\Desktop\\PP2-2025\\lab8\\race\\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pg.K_a]:
            self.rect.move_ip(-step, 0)
        if self.rect.right < w and pressed_keys[pg.K_d]:
            self.rect.move_ip(step, 0)
        if self.rect.top > 0 and pressed_keys[pg.K_w]:
            self.rect.move_ip(0, -step)
        if self.rect.bottom < h and pressed_keys[pg.K_s]:
            self.rect.move_ip(0, step)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# coin class with random weight
class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("C:\\Users\\Asus\\Desktop\\PP2-2025\\lab8\\race\\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, w - 30), random.randint(30, h - 130))
        self.weight = random.choice([1, 2, 3])

    def draw(self):
        screen.blit(self.image, self.rect)

p = Player()
e = Enemy()
c = Coin()

enemies = pg.sprite.Group()
enemies.add(e)

coins = pg.sprite.Group()
coins.add(c)

# game loop
while is_running:
    clock.tick(fps)
    
    # quit event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    # scrolling background
    screen.blit(pg.transform.scale(bg, (w, h)), (0, y % h))
    screen.blit(pg.transform.scale(bg, (w, h)), (0, -h + (y % h)))
    y += ry

    # update player and enemy
    p.update()
    e.update()

    # player hits enemy
    if pg.sprite.spritecollideany(p, enemies):
        lose = True

    # coin drawing and collision
    for c in coins:
        c.draw()
        if pg.sprite.collide_rect(p, c):
            c.kill()
            score_coin += c.weight  # add coin weight to score
            new = Coin()
            coins.add(new)

            # increase enemy speed every N coins
            if score_coin % N == 0:
                enemy_step += speed_increase_amount

    # draw player and enemy
    e.draw(screen)
    p.draw(screen)

    # game over
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        screen.blit(game_over, (0, 0))
        pg.display.flip()

    # coin score
    counter = score_coins.render(f'Coins: {score_coin}', True, 'white')
    screen.blit(counter, (300, 10))

    pg.display.flip()

pg.quit()
