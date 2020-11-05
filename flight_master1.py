import pygame
pygame.init()

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 30
x=350
rect = pygame.Rect((350, 220), (32, 32))  # Often used to track the position of an object in pygame.
image = pygame.Surface((32, 32))  # Images are Surfaces, so here I create an 'image' from scratch since I don't have your image.
image.fill(pygame.Color('white'))  # I fill the image with a white color.
velocity = [0, 0]  # This is the current velocity.
speed = 200  # This is the speed the player will move in (pixels per second).
dx = []  # This will be our queue. It'll keep track of the horizontal movement.

while True:
    dt = clock.tick(FPS) / 1000.0  # This will give me the time in seconds between each loop.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx.insert(0, -speed)
            elif event.key == pygame.K_RIGHT:
                dx.insert(0, speed)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx.remove(-speed)
            elif event.key == pygame.K_RIGHT:
                dx.remove(speed)

    if dx:  # If there are elements in the list.
        rect.x += dx[0] * dt

    screen.fill((0, 0, 0))
    screen.blit(image, rect)
    pygame.display.update()

    print(dx)  # Uncomment to see what's happening.
    print(x)