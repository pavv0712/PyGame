import pygame
import os
pygame.init()


#화면

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))

#제목

pygame.display.set_caption("crash balloon")

#배경
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환

image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "background.png"))


#스테이지

stage =pygame.image.load(os.path.join(image_path, "stage.png"))

stage_size = stage.get_rect().size

stage_height = stage_size[1] #스테이지 위에 캐릭터 두기위해

#캐릭터

character = pygame.image.load(os.path.join(image_path, "character.png"))

character_size = character.get_rect().size

charater_width = character_size[0]
charater_height = character_size[1]

character_x_pos = (screen_width/2) - (charater_width/2)
character_y_pos = screen_height - stage_height- charater_height

#캐릭터 이동
to_x = 0

character_speed = 0.6


#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#한번에 여러발 발사

weapons = []


#무기 발사 속도

weapon_speed = 1



#이벤트처리

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed

            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (charater_width/2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos

                weapons.append([weapon_x_pos, weapon_y_pos])


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0



    #캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - charater_width:
        character_x_pos = screen_width - charater_width

    #무기 위치 조정
    # 100, 200 -> 180, 160 x값 유지 y값만 변경

    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    #천장에 닿은 무기 없애기
    
    weapons = [[w[0],w[1]] for w in weapons if w[1] > 0]


    screen.blit(background, (0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    
    
    
    pygame.display.update()



#끝
pygame.quit()

