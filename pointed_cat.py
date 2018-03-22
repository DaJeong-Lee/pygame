import sys, pygame, math
from pygame.locals import *

WHITE = (255,255,255)
BLACK = (0,0,0)
BGCOLOR = WHITE
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

#기본적인 파이게임 셋업
pygame.init()
DISPALYSUF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

#주인공 이미지 만들기
CATSURF = pygame.image.load("resources/images/cat.png")
CATSURF = pygame.transform.scale(CATSURF, (int(CATSURF.get_size()[0]*0.3), int(CATSURF.get_size()[1]*0.3)))

#각도 구하기
def catch_angle(x1, y1, x2, y2):
    y = y1-y2
    x = x1-x2
    angle = math.atan2(x,y) #result is radian
    angle = angle*180/math.pi #레디안을 60분법으로 바꿈
    angle = (angle+90) % 360 #봐가면서 각도 조절
    return angle

#main game loop
while True:
    #이벤트 핸들링 루프
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    #배경색 칠하기
    DISPALYSUF.fill(BGCOLOR)

    #고양이가 마우스포인트 방향으로 움직임
    mousex , mousey = pygame.mouse.get_pos()
    for catx, caty in ((200,150),(50,300),(50,50),(200,300),(350,400),(400,200),(450,300)):
        degrees = catch_angle(catx, caty, mousex, mousey)
        #고양이 회전시키기
        rotateSurf = pygame.transform.rotate(CATSURF, degrees)

        #rotateSurf는 고양이그림의 사각형 면적
        rotatedRect = rotateSurf.get_rect()
        rotatedRect.center = (catx, caty)

        #blit 함수는 이미지를 화면에 그려주는 함수
        DISPALYSUF.blit(rotateSurf, rotatedRect)

    #마우스 움직일 때 목표물 화살표 그려주기
    pygame.draw.line(DISPALYSUF, BLACK, (mousex-10, mousey), (mousex+10, mousey))
    pygame.draw.line(DISPALYSUF, BLACK, (mousex, mousey-10), (mousex, mousey+10))

    pygame.display.update()
