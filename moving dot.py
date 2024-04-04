import pygame


pygame.init()
win = pygame.display.set_mode((500,400))
win.fill((100, 100, 100))
run = True
#parameters
sky_blue = (68, 142, 228)
red = (255, 0, 0)
green = (0, 255, 0)
x = 50
y = 50
r = 20
vel = 10
#game
while run:
    pygame.time.delay(100)

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < 400:
        y += vel
    win.fill((100, 100, 100))
    pygame.draw.circle(win, (0, 255, 255), (x, y), r, 0)
    pygame.display.update()
