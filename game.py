import pygame
import random

pygame.init()

screen_width = 400
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
#title
pygame.display.set_caption("Mountain Rush")
clock = pygame.time.Clock()

#background image
bg = pygame.image.load('asset/bg.png')
bg = pygame.transform.scale(bg,(screen_width,screen_height))

#player
list_player = [20]
player_x = 200
player_y = 0
player_width = 40
player_height = 20
#first enemy
enemy = pygame.image.load("asset/rock3.png")
enemy_img = pygame.transform.scale(enemy, (40, 20))
enemy = enemy_img.get_rect(topleft=(200, 0))
###new enemie
new_x = 200
new_y = 0
new_width = 40
new_height = 20
#new_enemy = pygame.Rect(new_x,new_y,new_width,new_height)
new_enemy = pygame.image.load("asset/rock3.png")
new_enemy_img = pygame.transform.scale(new_enemy, (40, 20))
new_enemy = new_enemy_img.get_rect(topleft=(200, 0))
#car

car = pygame.image.load("asset/player_.png")
car_img = pygame.transform.scale(car, (50, 80))
car = car_img.get_rect(topleft=(180, 410))
#food
food = pygame.image.load('asset/image2.jpg')
food_img = pygame.transform.scale(food,(40,20))
food = food_img.get_rect(topleft=(200,0))
#score and health
score = 0
health = 1000
font = pygame.font.SysFont('arial',25)
high = open('score/high_score.txt','r')
high = high.read()

running = True
while running:
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #game loop
    screen.blit(bg,(0,0))
    #always put player on the screen player
    if enemy.y <0:
        enemy.y = 0
        
    if enemy.y + player_height > screen_height:
        enemy.y = 0 
        enemy.x = random.randrange(0,400-player_width)
        score += 1

    # enemy
    #always put player on the screen player
    if new_enemy.y <0:
        new_enemy.y = 0
        
    if new_enemy.y + new_height > screen_height:
        new_enemy.y = 0 
        new_enemy.x = random.randrange(0,400-new_width)
        score += 1 

    #food
    if food.y < 0:
        food.y = 0
    if food.y + 20 > screen_height:
        food.y = 0
        food.x = random.randrange(0,400-20)
    #food appear
    state = random.randrange(0,20)
    if score > 100 and state < 5:
        food.y += 5
        new_enemy.y += 5
        enemy.y += 5
        screen.blit(food_img, food)

    if score <= 20:
        #keys
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            car.x -= 10
        if key[pygame.K_RIGHT]:
            car.x += 10    

    #handle car to the edge
    if car.x + 50 > screen_width:
        car.x = screen_width - 50
        
    if car.x  < 0 :
        car.x = 0    
           
    #enemy player    
    enemy.y += 10
    #collision
    if car.colliderect(food):
        health += 100
        food.y=0
    
    if car.colliderect(enemy) or car.colliderect(new_enemy):
        health -= 10
        #score = score - 1
    else:
        
        print('no collision')

    #end game if life = 0 
    if health == 0:
        running = False   
                

    #screen and draw
    #screen.fill('white')
    screen.blit(enemy_img, enemy)
    screen.blit(car_img, car)
    #bring in new enemies
    if score >= 10:
        new_enemy.y += 10
        enemy.y += 5
        screen.blit(new_enemy_img, new_enemy)
    
    if score >= 20:
        new_enemy.y += 5
        enemy.y += 10
    
    if score >= 20:
        #keys
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            car.x -= 13
        if key[pygame.K_RIGHT]:
            car.x += 13              
          

    #text on screen
    write_score = font.render(f'Score: {score}',True,(0,0,0))
    write_health = font.render(f"Health +{health}",True,(0,100,0))
    write_high_score = font.render(f"High Score: {high}",True,(0,0,0))
    #put health on the screen
    screen.blit(write_score,[0,0])
    screen.blit(write_health,[280,0])
    screen.blit(write_high_score,[0,30])
    
    #pygame.draw.rect(screen, (255, 0, 0), car, 2)
    #pygame.draw.rect(screen, (0, 255, 0), enemy, 2) 
    #pygame.draw.rect(screen, (0, 0, 255), new_enemy, 2)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()    

old_score = open('score/high_score.txt','r')
old_score = int(old_score.read())
new_score = score

if int(new_score) > int(old_score):
    write_new_score = open('score/high_score.txt','w')
    write_new_score.write(str(new_score))
    write_new_score.close()


