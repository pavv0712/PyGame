import pygame
import os
pygame.init()


#화면

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))

#제목

pygame.display.set_caption("crash balloon")


#FPS
clock = pygame.time.Clock()


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

character_speed = 10


#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#한번에 여러발 발사

weapons = []


#무기 발사 속도

weapon_speed = 10

#공 만들기 (4개 크기에 대해 따로 처리)

ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png")),
]

# 공 크기에 따른 최초 스피드

ball_speed_y = [-18, -15, -12, -9] #index 0, 1, 2, 3에 해당하는 값

#공들

balls = []

#최초 발생 큰공 추가

balls.append({
    "pos_x":50, #공의 x좌표
    "pos_y":50, #공의 y좌표
    "img_idx": 0, #공의 이미지 인덱스
    "to_x": 3, #공의 x축 이동방향 
    "to_y": -6, #y축 이동방향
    "init_spd_y": ball_speed_y[0] #y의 최초 속도
})



#이벤트처리

running = True

while running:
    dt = clock.tick(30)
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

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #가로벽에 닿았을 때 공 이동 위치 변경 (튕겨나오는 효과)

        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            
            ball_val["to_x"] = ball_val["to_x"] * -1 


        # 세로 위치
        #스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: #그 외의 모든 경우에는 속도를 증가
            ball_val["to_y"] += 0.5

        
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]



    #무기 위치 조정
    # 100, 200 -> 180, 160 x값 유지 y값만 변경

    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    #천장에 닿은 무기 없애기
    
    weapons = [[w[0],w[1]] for w in weapons if w[1] > 0]


    screen.blit(background, (0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    
    
    
    pygame.display.update()



#끝
pygame.quit()

