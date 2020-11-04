import pygame
import os
import random
import pyautogui
player='gallery\sprites\player.png' #
background='gallery\sprites\\background.png' #
screen = pygame.display.set_mode((720, 480))
FPS = 30
GAME_SPRITES={}
pip=True
def welcome_screen(): #
    image=pygame.image.load(player)
    rect = image.get_rect()
    rect.center =(200,300)
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
                screen.blit(image, rect)
                pygame.display.update()

def main_game():
    image=pygame.image.load(player)#
    rect = image.get_rect()#
    rect.center =(200,300)#
    # rect = pygame.Rect((350, 220), (32, 32))  # Often used to track the position of an object in pygame.
    # image = pygame.Surface((32, 32))  # Images are Surfaces, so here I create an 'image' from scratch since I don't have your image.
    # image.fill(pygame.Color('white'))  # I fill the image with a white color.
    # ballVellY=-10
    # ballxy={'x':random.randrange(10,15),'y':-5}
    # velocity = [0, 0]  # This is the current velocity.
    # speed = 200  # This is the speed the player will move in (pixels per second).
    # dx = []  # This will be our queue. It'll keep track of the horizontal movement.
    while True:
        
        dt = clock.tick(FPS) / 1000.0  # This will give me the time in seconds between each loop.

        for event in pygame.event.get():#
            if event.type == pygame.QUIT:#
                raise SystemExit#
            elif event.type == pygame.KEYDOWN:#
                if event.key == pygame.K_LEFT:#
                    dx.insert(0, -speed)#
                elif event.key == pygame.K_RIGHT:#
                    dx.insert(0, speed) #
            # elif event.type == pygame.KEYUP:
                # if event.key == pygame.K_LEFT:
                    # dx.remove(-speed)
                # elif event.key == pygame.K_RIGHT:
                    # dx.remove(speed)

        if dx:  # If there are elements in the list.
            rect.x += dx[0] * dt


        # balls motion in y axis
        # p=balls()
        # current_ball=p[random.randrange(0,4)]
        

        # Add a new ball when the first is about to cross the leftmost part of the screen
        # if 0<bally_x<5:
        #     new_ballx,new_bally=random.randrange(100,150),-5 
        #     ballx.append(new_ballx)
        #     bally.append(new_bally)    

        # if the ball is out of the screen, remove it
        # if ballx['x'] < - GAME_SPRITES['pipe'][0].get_width():
            # upperPipes.pop(0)
            # lowerPipes.pop(0)        
        


        screen.fill((0, 0, 0))
        screen.blit(bck_image, (0,0))
        screen.blit(image, rect)
        pygame.display.update()

        # print dx  # Uncomment to see what's happening.

        

