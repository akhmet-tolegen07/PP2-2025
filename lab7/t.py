import pygame

pygame.init()
screen = pygame.display.set_mode((400,400))
done = False

pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(30,30,100,100))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
