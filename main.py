import pygame, sys
import pyganim
import math
from pygame.locals import *

pygame.init()
window = width, height = (320, 240)
windowSurface = pygame.display.set_mode(window)
clock = pygame.time.Clock()

walkLeftAnim = pyganim.PygAnimation(
        [('resources/duderunleft/duderunleft0.tiff', 0.1),
         ('resources/duderunleft/duderunleft1.tiff', 0.1),
         ('resources/duderunleft/duderunleft2.tiff', 0.1),
         ('resources/duderunleft/duderunleft3.tiff', 0.1),
         ('resources/duderunleft/duderunleft4.tiff', 0.1),
         ('resources/duderunleft/duderunleft5.tiff', 0.1),
         ('resources/duderunleft/duderunleft6.tiff', 0.1),
         ('resources/duderunleft/duderunleft7.tiff', 0.1)])

walkRightAnim = pyganim.PygAnimation(
        [('resources/duderunright/duderunright0.tiff', 0.1),
         ('resources/duderunright/duderunright1.tiff', 0.1),
         ('resources/duderunright/duderunright2.tiff', 0.1),
         ('resources/duderunright/duderunright3.tiff', 0.1),
         ('resources/duderunright/duderunright4.tiff', 0.1),
         ('resources/duderunright/duderunright5.tiff', 0.1),
         ('resources/duderunright/duderunright6.tiff', 0.1),
         ('resources/duderunright/duderunright7.tiff', 0.1)])

walkFrontAnim = pyganim.PygAnimation(
        [('resources/duderunfront/duderunfront0.tiff', 0.1),
         ('resources/duderunfront/duderunfront1.tiff', 0.1),
         ('resources/duderunfront/duderunfront2.tiff', 0.1),
         ('resources/duderunfront/duderunfront3.tiff', 0.1),
         ('resources/duderunfront/duderunfront4.tiff', 0.1),
         ('resources/duderunfront/duderunfront5.tiff', 0.1),
         ('resources/duderunfront/duderunfront6.tiff', 0.1),
         ('resources/duderunfront/duderunfront7.tiff', 0.1)])

walkBackAnim = pyganim.PygAnimation(
        [('resources/duderunback/duderunback0.tiff', 0.1),
         ('resources/duderunback/duderunback1.tiff', 0.1),
         ('resources/duderunback/duderunback2.tiff', 0.1),
         ('resources/duderunback/duderunback3.tiff', 0.1),
         ('resources/duderunback/duderunback4.tiff', 0.1),
         ('resources/duderunback/duderunback5.tiff', 0.1),
         ('resources/duderunback/duderunback6.tiff', 0.1),
         ('resources/duderunback/duderunback7.tiff', 0.1)])

walkLeftAnim.play()
walkRightAnim.play()
walkFrontAnim.play()
walkBackAnim.play()

target = [0, 0]
current = [0, 0]
anim = walkFrontAnim

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            target = event.pos

    # Clear screen 
    windowSurface.fill((0, 0, 0))
 
    # Perform character movement
    if math.fabs(current[0] - target[0]) > 5 or math.fabs(current[1] - target[1]) > 5:
        sqrtdist = math.sqrt(((target[0] - current[0]) ** 2) + ((target[1] - current[1]) ** 2))
        moveX = (target[0] - current[0]) / sqrtdist
        moveY = (target[1] - current[1]) / sqrtdist
        if math.fabs(moveX) > math.fabs(moveY):
            if moveX > 0:
                anim = walkRightAnim
            else:
                anim = walkLeftAnim
        else:
            if moveY > 0:
                anim = walkFrontAnim
            else:
               anim = walkBackAnim
        current[0] += moveX
        current[1] += moveY
        anim.blit(windowSurface, current)
    # If no movment, idle the animation at the first frame
    else:
        anim.blitFrameNum(0, windowSurface, current)

    # Swap the buffers
    pygame.display.flip()
    # Wait until 1/60 of a second has passed before updating again
    clock.tick(60)
