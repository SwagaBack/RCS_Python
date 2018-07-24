import sys, pygame, time
pygame.init()
print("starting game...")

size = width, height = 1000, 700
background = 150, 188, 35

screen = pygame.display.set_mode(size)
ball = pygame.image.load("img/basket.png")
ball = pygame.transform.scale(ball,(37,37))
ballrect = ball.get_rect()
bplayer = pygame.image.load("img/bplayer.png")
bplayer = pygame.transform.scale(bplayer, (120,270))
bplayer = pygame.transform.flip(bplayer, True, False)


rim = pygame.image.load("img/basketrim.png")
rim = pygame.transform.scale(rim,(250,500))
rimrect = rim.get_rect()
# starting screen
screen.fill(background)
bx,by = 108,348
# rimx,rimy = rimrect
print(rimrect)
screen.blit(rim,(730,125))
screen.blit(bplayer,(50,350))
screen.blit(ball,(bx,by))
pygame.display.flip()
vx = 42
vy = -77
g = 9.8
t = 0

while True:
    if t < 15:
        bx = bx + vx
        by = by + vy
        vy = vy + g
        t += 1
        screen.blit(ball,(bx,by))
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
