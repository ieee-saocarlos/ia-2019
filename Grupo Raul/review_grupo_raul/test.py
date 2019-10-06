import math


def p_ang(xi, yi, xf, yf):
    ang = math.atan((yf-yi)/(xf-xi))
    return 180*ang/math.pi


print(p_ang(0,0,2,1))