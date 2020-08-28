import pygame
import random
import math
import time

pygame.init()



dimx = 256
dimy = 256

casex = 16
casey = 16
gapx = int(dimx/casex)
gapy = int(dimy/casey)



cases = {}
vectors = {}
case=0
pixels = {}

r_pixels = {}
general_pixels = {}

possible_vectors = [(-1,-1),(1,-1),(1,1),(-1,1)]


pygame.display.set_caption('Perlin')
screen = pygame.display.set_mode((dimx, dimy))

def dot_product(x1,x2,y1,y2):
    return((x1*x2)+(y1*y2))

def get_distance(x1, x2, y1, y2):
    sq1 = (x1 - x2) ** 2
    sq2 = (y1 - y2) ** 2
    return math.sqrt(sq1 + sq2)

def get_vector(x1,x2,y1,y2):
    x = x2-x1
    y = y2-y1
    x/=gapx
    y/=gapy
    return(x,y)
def fade(a):
    return float((6 * a ** 5) - (15 * a ** 4) + (10 * a ** 3))
    #return (a)



def create_perlin(rgb):
    for y in range(dimy):
        for x in range(dimx):
            screen.set_at((x, y), (255, 255, 255))
    case = 0
    for y in range(casey):
        for x in range(casex):

            cases[case] = (x, y)
            case += 1


    for y in range(casey + 1):
        for x in range(casex + 1):
            vectors[x, y] = possible_vectors[random.randint(0, 3)]





    for case in cases:
        x, y = cases[case]
        vector1 = vectors[x, y]
        vector2 = vectors[x + 1, y]
        vector3 = vectors[x, y + 1]
        vector4 = vectors[x + 1, y + 1]
        x1, y1 = vector1
        x2, y2 = vector2
        x3, y3 = vector3
        x4, y4 = vector4

        for rx in range(gapy):
            for ry in range(gapx):
                yp = float(ry)
                xp = float(rx)

                vect1x, vect1y = get_vector(0, xp, 0, yp)
                vect2x, vect2y = get_vector((gapx - 1), xp, 0, yp)
                vect3x, vect3y = get_vector(0, xp, (gapx - 1), yp)
                vect4x, vect4y = get_vector((gapx - 1), xp, (gapx - 1), yp)

                dot1 = dot_product(x1, vect1x, y1, vect1y)
                dot2 = dot_product(x2, vect2x, y2, vect2y)
                dot3 = dot_product(x3, vect3x, y3, vect3y)
                dot4 = dot_product(x4, vect4x, y4, vect4y)

                xp = xp / gapx
                yp = yp / gapy

                xp = fade(float(xp))
                yp = fade(float(yp))

                xp = xp * gapx
                yp = yp * gapy

                AB = dot1 + (xp / gapx) * (dot2 - dot1)
                CD = dot3 + (xp / gapx) * (dot4 - dot3)
                color = AB + (yp / gapy) * (CD - AB)

                color += 1
                color /= 2
                color *= 255
                pixels[x * gapx + rx, y * gapy + ry] = color

    for pixel in pixels:
        x, y = pixel
        color = pixels[x, y]
        screen.set_at((x, y), (color, color, color))






create_perlin("r")


running = True

while running == True:


    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()