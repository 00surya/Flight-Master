import pygame
import random

player='gallery\sprites\player.png'
background='gallery\sprites\\background.jpg'
dino='gallery\sprites\dino.png'
# pygame.init()

screen = pygame.display.set_mode((400, 480))
# clock = pygame.time.Clock()
FPS = 30
velocity = [0, 0]  
speed = 300  
dx = []  
xx=-2
back_Y=-700
ball_no=-9
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
    imagee=pygame.image.load(player).convert_alpha()  ####>>>>>>>>>>>> plane image
    rectt = imagee.get_rect()
    rectt.center =(200,300)
    
    yyy=20
    ballx=random.randrange(12,350)
    px=-12
    while True:
        # print(cv)
        global xx
        global back_Y
        dt = clock.tick(FPS) / 1000.0  # This will give me the time in seconds between each loop.
        
        
        ball=get_ball()
        print(ball)
        image=pygame.image.load(ball).convert_alpha()  ####################### >>  ball image
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
            rectt.x+=dx[0] * dt
            if rectt.x>345 or rectt.x<-3:
                lost()
            
        

        f = getupdate()
        
        bck_motion=bck_update()
        screen.fill((0, 0, 0))
        bally=yyy+f   
        if bally> 500:
            xx=-2
            yyy=20
            ballx=random.randrange(11,350) 

        # what if i lost
        if (300+imagee.get_height()>=bally+image.get_height()>=300) and (rectt.x+imagee.get_width()>=ballx+image.get_width()>=rectt.x or rectt.x+imagee.get_width()>=ballx>=rectt.x):
            lost()    

        screen.fill((0, 0, 0))
        screen.blit(bck_image, (0,bck_motion))
        screen.blit(bck_image, (0,(bck_motion-1300)))
        if bck_motion > 860:
            back_Y=-700
            
        screen.blit(imagee, rectt)
        screen.blit(image,(ballx,bally))

        pygame.display.update()
def lost():
    hdhdhihdikdjkskjdkj
    
        
      
def getupdate():
    global xx
    xx+=15
    return xx
def bck_update():    
    global back_Y
    back_Y+=1
    return back_Y
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
    pygame.display.set_caption('Snehillerious Flight Master')
    bck_image=pygame.image.load(background)
    while True:
        welcome_screen()
        main_game()
            