import sys, pygame, time
pygame.init()
print("starting game...")

size = width, height = 1000, 700
background = 150, 188, 35

screen = pygame.display.set_mode(size)
ball = pygame.image.load("img/basket.png")
ballrect = ball.get_rect()
rim = pygame.image.load("img/basketrim.png")
rimrect = rim.get_rect()
# starting screen
screen.fill(background)
screen.blit(ball,ballrect)
screen.blit(rim,rimrect)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
