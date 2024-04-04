import pygame
import sys
import random as rd

#initialisation
pygame.init()

#parameters
size_x = 600
size_y = 450
x = size_x//2
y = size_y//2
r = 10
vel = 10
cell_size =20
rect_x = size_x//2-90
rect_y = size_y//2+10
rect_width = 180
rect_height = 50
#colors
black = (0, 0, 0)
sky_blue = (68, 142, 228)
red_fruity = (255, 26, 64)
greeny = (71, 71, 0)
brown = (157, 78, 21)
green_blue = (0, 255, 200)
red=(255,0,0)
light_blue = (191,207,255)

keys = pygame.key.get_pressed()
win = pygame.display.set_mode((500, 400))

#creation window
clock = pygame.time.Clock()
screen = pygame.display.set_mode((size_x, size_y), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
#writing title and score
pygame.display.set_caption("Snake Game")
font=pygame.font.SysFont(None,40)
font1=pygame.font.SysFont(None,20)
def draw_score(score):
    score_txt = "score: " + str(score)
    score_img=font.render(score_txt,True,black)
    win.blit(score_img,(10,10))

#characters
snake_character = [[int(x*(1-1/4)), int(y*(1-1/4))]]
snake_character.append([int(x*(1-1/4)), int(y*(1-1/4))+cell_size])
snake_character.append([int(x*(1-1/4)), int(y*(1-1/4))+cell_size*2])
snake_character.append([int(x*(1-1/4)), int(y*(1-1/4))+cell_size*3])
#variables
run = True
timer = 0
point = (x, y)
game_over=False
food=[0,0]
new_food=True
new_snake=[0,0]
clicked = False
pause = False
#events
score = 0
direction = 1
while run:
    win.fill(brown)
    draw_score(score)
    #movments
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP and direction != 3:
                direction = 1
            if events.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if events.key == pygame.K_DOWN and direction!=1:
                direction = 3
            if events.key == pygame.K_LEFT and direction!=2:
                direction = 4
            if events.key == pygame.K_SPACE:
                if not game_over:
                    pause = not pause  # Toggle pause
    #cheking some conditions
    
    if new_food==True:
        new_food=False
        food = [rd.randint(0, (size_x//cell_size)-1)*cell_size , rd.randint(0, (size_y//cell_size)-2)*cell_size]
    #draw the food
    pygame.draw.circle(win, red_fruity, (food[0]+r, food[1]+r), r, 0)
    
    epsilon=15
    if (abs(snake_character[0][0] - food[0])<epsilon) and (abs(snake_character[0][1] - food[1])<epsilon):
        new_food=True
        score += 1
        new_snake=list(snake_character[-1])
        if direction==1: #up 
            new_snake[1]-=cell_size
        elif direction==2: #right
            new_snake[0]+=cell_size
        elif direction==3: #down
            new_snake[1]+=cell_size
        elif direction == 4: #left
            new_snake[0] -= cell_size
        #the growth of the snake
        snake_character.append(new_snake)
    #the game over condition
    for pos in range(1, len(snake_character)):
        if snake_character[pos] == snake_character[0]:
            game_over = True
    #outside border condition
    if snake_character[0][0] < 0 or snake_character[0][0] > size_x or snake_character[0][1] < 0 or snake_character[0][1] > size_y:
        game_over = True
    #movments
    if pause:
        pygame.draw.rect(win, light_blue, (size_x//2-90, size_y//2-65, 200, 100))
        over_img = font.render("Game Paused", True, black)
        win.blit(over_img, (size_x//2-80, size_y//2-60))
        over_img = font1.render("click space bar to resume", True, black)
        win.blit(over_img, (size_x//2-80+2, size_y//2+10))
    elif game_over == False and pause == False:
        if timer>300:
            timer = 0
            snake_character=snake_character[-1:]+snake_character[:-1]
            if direction==1: #up
                snake_character[0][0]=snake_character[1][0]
                snake_character[0][1] = snake_character[1][1]-cell_size
            elif direction==2: #right
                snake_character[0][0] = snake_character[1][0]+cell_size
                snake_character[0][1] = snake_character[1][1]
            elif direction==3: #down
                snake_character[0][0] = snake_character[1][0]
                snake_character[0][1] = snake_character[1][1]+cell_size
            elif direction==4: #left
                snake_character[0][0] = snake_character[1][0]-cell_size
                snake_character[0][1] = snake_character[1][1]
    else:
        #drawing the game over
        pygame.draw.rect(win, light_blue, (size_x//2-90, size_y//2-65, 180, 50))
        over_img = font.render("Game Over!!", True, black)
        win.blit(over_img, (size_x//2-80, size_y//2-60))
        
        pygame.draw.rect(win, light_blue, (rect_x, rect_y, rect_width, rect_height))
        again_img = font.render("Play Again?", True, black)
        win.blit(again_img, (size_x//2-80, size_y//2+15))
        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if events.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked=True
        if events.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            if rect_x <= mouse_x <= rect_x + rect_width and rect_y <= mouse_y <= rect_y + rect_height:
                pygame.draw.rect(win, sky_blue, (rect_x, rect_y, rect_width, rect_height))
                #reset var
                #characters
                snake_character = [[int(x*(1-1/4)), int(y*(1-1/4))]]
                snake_character.append([int(x*(1-1/4)), int(y*(1-1/4))+cell_size])
                snake_character.append([int(x*(1-1/4)), int(y*(1-1/4))+cell_size*2])
                snake_character.append([int(x*(1-1/4)), int(y*(1-1/4))+cell_size*3])
                #variables
                run = True
                timer = 0
                point = (x, y)
                game_over = False
                food = [0, 0]
                new_food = True
                new_snake = [0, 0]
                clicked = False
                #events
                score = 0
                direction = 1
        if rect_x <= mouse_x <= rect_x + rect_width and rect_y <= mouse_y <= rect_y + rect_height:
            pygame.draw.rect(win, sky_blue, (rect_x, rect_y, rect_width, rect_height))
            again_img = font.render("Play Again?", True, black)
            win.blit(again_img, (size_x//2-80, size_y//2+15))
                                

    #draw the snake
    head = 1
    for body in snake_character:
        if head==0:
            pygame.draw.rect(win, greeny, (body[0], body[1], cell_size, cell_size))
        if head == 1:
            pygame.draw.rect(win, green_blue, (body[0], body[1], cell_size, cell_size))
            head=0
    
    #draw the score
    #pygame.draw.rect(win, sky_blue, (0, 0, size_x, 40), 0)
    #update the display
    pygame.display.update()
    
    timer+=1

# Close the window and exit
pygame.quit()
