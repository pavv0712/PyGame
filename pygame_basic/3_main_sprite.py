import pygame

pygame.init() #초기화 (반드시 필요)


#화면 크기 설정

screen_width = 520 #가로크기
screen_height = 600 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 선정

pygame.display.set_caption("my game") #게임이름


#배경이미지 불러오기

background = pygame.image.load("C:/Users/나/Desktop/파이썬 게임/pygame_basic/background.png")


#캐릭터 스프라이트 불러오기

character = pygame.image.load("C:/Users/나/Desktop/파이썬 게임/pygame_basic/character.png")

character_size = character.get_rect().size #이미지 크기를 구해옴

character_width = character_size[0] #캐릭터 가로크기
character_height = character_size[1] #캐릭터 세로크기

character_x_pos = (screen_width / 2) - (character_width / 2) #캐릭터를 중앙에 화면 절반크기
character_y_pos = screen_height - character_height # 캐릭터를 중앙 가장 밑에 세로크기 가장 밑에


# 이벤트 루프

running = True #게임 진행 여부
while running:
    for event in pygame.event.get(): #어떤 이벤트 발생?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 여부
            running = False #게임 진행중 아님


    # screen.fill((0,0,255))

    screen.blit(background,(0,0)) #배경그리기
    
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임화면을 다시 그리기!


# pygame 종료
pygame.quit()