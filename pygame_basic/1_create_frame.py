import pygame

pygame.init() #초기화 (반드시 필요)


#화면 크기 설정
screen_width = 520 #가로크기
screen_height = 600 #세로크기

screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 선정

pygame.display.set_caption("my game") #게임이름


# 이벤트 루프

running = True #게임 진행 여부
while running:
    for event in pygame.event.get(): #어떤 이벤트 발생?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 여부
            running = False #게임 진행중 아님



# pygame 종료
pygame.quit()