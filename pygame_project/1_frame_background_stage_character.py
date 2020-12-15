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

#이벤트처리

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()



#끝
pygame.quit()

