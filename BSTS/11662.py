import sys
import math

def distance(x1,y1,x2,y2) :
    return math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))

Ax,Ay,Bx,By,Cx,Cy,Dx,Dy = map(int,sys.stdin.readline().split())

interval = 1000000

dx1 = (Bx-Ax) / interval
dy1 = (By-Ay) / interval
dx2 = (Dx-Cx) / interval
dy2 = (Dy-Cy) / interval

try :
    i = (-1) * ((Ax-Cx)*(dx1-dx2) + (Ay-Cy)*(dy1-dy2))/(math.pow((dx1-dx2),2)+math.pow((dy1-dy2),2))
    tmp_dist = distance(Ax+i*dx1,Ay+i*dy1,Cx+i*dx2,Cy+i*dy2)
    if 0 < i < interval :
        print(tmp_dist)
    else :
        a = distance(Ax,Ay,Cx,Cy)
        b = distance(Bx,By,Dx,Dy)
        print(min(a,b))
except :
    a = distance(Ax,Ay,Cx,Cy)
    b = distance(Bx,By,Dx,Dy)
    print(min(a,b))
