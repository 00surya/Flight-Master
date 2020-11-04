import pygame
import random
pygame.init()

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 30
velocity = [0, 0]  
speed = 200  
dx = []  
xx=-2
ball_no=0

def main_game():
    yyy=20
    ballx=11
    while True:
        global xx
        ball=get_ball()
        print(ball)
        image=pygame.image.load(ball).convert_alpha()
        rect = image.get_rect()
        dt = clock.tick(FPS) / 1000.0  # This will give me the time in seconds between each loop.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
        
            
        if dx:  
            rect.x += dx[0] * dt
        f = getupdate()
        screen.fill((0, 0, 0))
        bally=yyy+f
        if bally> 500:
            xx=-2
            yyy=20
            ballx=random.randrange(11,700)
        screen.blit(image,(ballx,bally))

        pygame.display.update()
def getupdate():
    global xx
    xx+=10
    return xx
ball_no=0    
def get_ball():
    global ball_no
    Balls=(
        'gallery/sprites/ball1.png',
        'gallery/sprites/ball2.png',
        'gallery/sprites/ball3.png',
        'gallery/sprites/ball4.png',
        'gallery/sprites/ball5.png',
        'gallery/sprites/danger.png'
    )
    if xx==-2:
        ball_no=random.randrange(0,6)    
    d=Balls[ball_no]
    return str(d)

main_game()    
            