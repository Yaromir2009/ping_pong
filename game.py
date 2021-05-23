import pygame

WIN_X, WIN_Y = 700, 500

window = pygame.display.set_mode((WIN_X, WIN_Y))

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((0, 0, 100))
    pygame.display.update()
    clock.tick(40)
