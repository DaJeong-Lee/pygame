#coding=utf-8
import sys, pygame
import math
from pygame.locals import *

BRIGHTBLUE = (0,50,255)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BGCOLOR = WHITE

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
WIN_CENTER_X = int(WINDOWWIDTH/2)
WIN_CENTER_Y = int(WINDOWHEIGHT/2)

AMPLITUDE = 100 # y축의 가중치

#초당 프레임 수(클수록 빠름)
FPS = 60

#기본 셋업
pygame.init()
FPSCLOCK = pygame.time.Clock()
displaywin = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
step = 0

#main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
            pygame.quit()
            sys.exit()

    #배경을 칠합니다.
    displaywin.fill(BGCOLOR)

    #black rect
    #화면은 y축 숫자가 커질수록 밑으로 내려감
    #그래서 아래쪽 yPos에 -1을 곱해서 숫자가 커질수록 위로 올라가도록 한거임
    pygame.draw.rect(displaywin, BLACK, pygame.Rect(0,10,5,5))
    pygame.draw.rect(displaywin, BLACK, pygame.Rect(5,30,5,5))

    #움직이는 공 그리기
    yPos = -1 * math.sin(step) * AMPLITUDE

    #파란색 공 그리기
    pygame.draw.circle(displaywin, BRIGHTBLUE, (int(WINDOWWIDTH*0.333),int(yPos)+WIN_CENTER_Y ), 40)

    #red 공 그리기
    yPos = -1 * abs(math.sin(step)) * AMPLITUDE
    pygame.draw.circle(displaywin, RED, (int(WINDOWWIDTH*0.666),int(yPos)+WIN_CENTER_Y ), 40)

    #dispaly update
    pygame.display.flip()

    step += 0.02

    FPSCLOCK.tick(FPS)

