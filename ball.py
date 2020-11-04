import pygame
import random

player='gallery\sprites\player.png'
background='gallery\sprites\\background.png'
# pygame.init()

screen = pygame.display.set_mode((400, 480))
# clock = pygame.time.Clock()
FPS = 30
velocity = [0, 0]  
speed = 300  
dx = []  
xx=-2
ball_no=0
def welcome_screen():
    image=pygame.image.load(player)
    rectt = image.get_rect()
    rectt.center =(200,300)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pip=False
                raise SystemExit

            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE):
                return
            else:
                screen.fill((0, 0, 0))
                screen.blit(bck_image, (0,0))
                screen.blit(image, rectt)
                pygame.display.update()


def main_game():
    imagee=pygame.image.load(player).convert_alpha()
    rectt = imagee.get_rect()
    rectt.center =(200,300)
    
    
    yyy=20
    ballx=11
    while True:
        global xx
        dt = clock.tick(FPS) / 1000.0  # This will give me the time in seconds between each loop.
        
        
        ball=get_ball()
        print(ball)
        image=pygame.image.load(ball).convert_alpha()
        rect = image.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx.insert(0, -speed)
                elif event.key == pygame.K_RIGHT:
                    dx.insert(0, speed)
            
        if dx:  
            rectt.x += dx[0] * dt
        f = getupdate()
        screen.fill((0, 0, 0))
        bally=yyy+f
        if bally> 500:
            xx=-2
            yyy=20
            ballx=random.randrange(11,300)
        screen.fill((0, 0, 0))
        screen.blit(bck_image, (0,0))
        screen.blit(imagee, rectt)
        screen.blit(image,(ballx,bally))

        pygame.display.update()
def getupdate():
    global xx
    xx+=15
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
    
if __name__ == "__main__":
    pygame.init()    
    clock = pygame.time.Clock()
    bck_image=pygame.image.load(background)
    while True:
        welcome_screen()
        main_game()
            