import pygame

WIN_X, WIN_Y = 700, 500

BLACK = (0,0,0)
GREY = (39, 40, 35)
GREEN = (50, 150, 50)
BLUE = (50, 50, 150)


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, speed, wight, height):
        super().__init__()
        self.image = pygame.Surface((wight, height)) #вместе 55,55 - параметры
        self.image.fill(color=color)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
   def update(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[pygame.K_DOWN] and self.rect.y < WIN_Y - self.rect.height:
           self.rect.y += self.speed
class Player2(GameSprite):
   def update(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[pygame.K_s] and self.rect.y < WIN_Y - self.rect.height:
           self.rect.y += self.speed



window = pygame.display.set_mode((WIN_X, WIN_Y))

#создания мяча и ракетки   
racket2 = Player2(color=GREEN, x=15, y=200, speed=4, wight=25, height=150) 
racket1 = Player1(BLUE, WIN_X - 40, 200, 4, 25, 150)

clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(GREY)
    racket1.update()
    racket2.update()
    racket1.reset()
    racket2.reset()
    pygame.display.update()
    clock.tick(40)
