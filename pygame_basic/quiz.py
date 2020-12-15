import pygame
from random import *

pygame.init()

#화면

screen_width = 520
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))

#FPS

clock = pygame.time.Clock()


#백그라운드 

background = pygame.image.load("C:/Users/나/Desktop/파이썬 게임/pygame_basic/background.png")

#타이틀

pygame.display.set_caption("escape dung")

#캐릭터

character = pygame.image.load("C:/Users/나/Desktop/파이썬 게임/pygame_basic/character.png")

character_size = character.get_rect().size

character_width = character_size[0]
character_height = character_size[1]

character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

# ㄸㅗㅇ이 내려온다

enemy = pygame.image.load("C:/Users/나/Desktop/파이썬 게임/pygame_basic/enemy.png")

enemy_size = enemy.get_rect().size

enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

enemy_x_pos= randrange(0, (screen_width- enemy_width))
enemy_y_pos = 0
enemy_speed = 10

#이동
to_x = 0

#캐릭터 스피드

character_speed = 0.3

#이벤트

running = True

while running:
    dt = clock.tick(30)
    print(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #키보드 누름
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        #키보드 뗌
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    character_x_pos += to_x * dt
    enemy_y_pos += enemy_speed

    # 캐릭터 가로 제한

    if character_x_pos < 0:
        character_x_pos = 0 
    elif character_x_pos + character_width > screen_width:
        character_x_pos = screen_width - character_width 

    #적 제한 및 재생성
    
    if enemy_y_pos > screen_height:   
        enemy_x_pos = randrange(0, (screen_width- enemy_width))
        enemy_y_pos = 0 - enemy_height


    #충돌처리

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("다이")
        running = False

    screen.blit(background, (0,0))
    screen.blit(character,(character_x_pos, character_y_pos))
    
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    
    pygame.display.update()

#종료

pygame.quit()