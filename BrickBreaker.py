# -*- coding: utf-8 -*-
from visual import *
scene.range=18
scene.autoscale=False


#used for collision between bullet and brick
def collisionSpheres(sphere1,box1):
    dist = abs(box1.pos.x - sphere1.pos.x)
    dist2 = abs(box1.pos.y - sphere1.pos.y)
    if (dist < sphere1.radius + (box1.length/2)) and (dist2 < sphere1.radius + (box1.height/2)):
        return True
    else:
        return False


# variables to replace the width,length, and height of colored bricks
ww = .5
wl = 3
wh = 1


# x coordinates for bricks

x1 = -11 # first column starting from the left
x2 = -7
x3 = -3
x4 = 1
x5 = 5
x6 = 9



#y coordinates for bricks

y1 = 10 # y coordinate for top row
y2 = 8
y3 = 6
y4 = 4
y5 = 2


#z coordinate for all bricks

z=2

#variable for material type in bricks

m = materials.emissive

#varying colors for bricks

color1 = color.red #toprow
color2 = color.magenta #second row
color3 = color.yellow #third row
color4 = color.green #fourth row
color5 = color.cyan #fifth row
color6 = color.white #wall around the screen

shooter = box(
    pos = (-2,-8,0),
    width = 0,
    length = 5,
    height = 1,
    color=color.white,
    material = materials.chrome
    )

#topleft

brick1 = box(
    pos = (x1,y1,z),
    width = ww,
    length = wl,
    height = wh,
    color = color1,
    material = m
    )

brick2 = box(
    pos = (x2,y1,z),
    width = ww,
    length = wl,
    height = wh,
    color = color1,
    material = m
    )

brick3 = box(
    pos = (x3,y1,z),
    width = ww,
    length = wl,
    height = wh,
    color = color1,
    material = m
    )

brick4 = box(
    pos = (x4,y1,z),
    width = ww,
    length = wl,
    height = wh,
    color = color1,
    material = m
    )

brick5 = box(
    pos = (x5,y1,z),
    width = ww,
    length = wl,
    height = wh,
    color = color1,
    material = m
    )

brick6 = box(
    pos = (x6,y1,z),
    width = ww,
    length = wl,
    height = wh,
    color = color1,
    material = m
    )

#second row

brick7 = box(
    pos = (x1,y2,z),
    width = ww,
    length = wl,
    height = wh,
    color = color2,
    material = m
    )

brick8 = box(
    pos = (x2,y2,z),
    width = ww,
    length = wl,
    height = wh,
    color = color2,
    material = m
    )

brick9 = box(
    pos = (x3,y2,z),
    width = ww,
    length = wl,
    height = wh,
    color = color2,
    material = m
    )

brick10 = box(
    pos = (x4,y2,z),
    width = ww,
    length = wl,
    height = wh,
    color = color2,
    material = m
    )

brick11 = box(
    pos = (x5,y2,z),
    width = ww,
    length = wl,
    height = wh,
    color = color2,
    material = m
    )

brick12 = box(
    pos = (x6,y2,z),
    width = ww,
    length = wl,
    height = wh,
    color = color2,
    material = m
    )

#thirdrow

brick13 = box(
    pos = (x1,y3,z),
    width = ww,
    length = wl,
    height = wh,
    color = color3,
    material = m
    )

brick14 = box(
    pos = (x2,y3,z),
    width = ww,
    length = wl,
    height = wh,
    color = color3,
    material = m
    )

brick15 = box(
    pos = (x3,y3,z),
    width = ww,
    length = wl,
    height = wh,
    color = color3,
    material = m
    )

brick16 = box(
    pos = (x4,y3,z),
    width = ww,
    length = wl,
    height =wh,
    color = color3,
    material = m
    )
brick17 = box(
    pos = (x5,y3,z),
    width = ww,
    length = wl,
    height = wh,
    color = color3,
    material = m
    )

brick18 = box(
    pos = (x6,y3,z),
    width = ww,
    length = wl,
    height = wh,
    color = color3,
    material = m
    )

#fourthrow

brick19 = box(
    pos = (x1,y4,z),
    width = ww,
    length = wl,
    height = wh,
    color = color4,
    material = m
    )

brick20 = box(
    pos = (x2,y4,z),
    width = ww,
    length = wl,
    height = wh,
    color = color4,
    material = m
    )

brick21 = box(
    pos = (x3,y4,z),
    width = ww,
    length = wl,
    height = wh,
    color = color4,
    material = m
    )

brick22 = box(
    pos = (x4,y4,z),
    width = ww,
    length = wl,
    height = wh,
    color = color4,
    material = m
    )

brick23 = box(
    pos = (x5,y4,z),
    width = ww,
    length = wl,
    height = wh,
    color = color4,
    material = m
    )

brick24 = box(
    pos = (x6,y4,z),
    width = ww,
    length = wl,
    height = wh,
    color = color4,
    material = m
    )

#fifthrow

brick25 = box(
    pos = (x1,y5,z),
    width = ww,
    length = wl,
    height = wh,
    color = color5,
    material = m
    )

brick26 = box(
    pos = (x2,y5,z),
    width = ww,
    length = wl,
    height = wh,
    color = color5,
    material = m
    )

brick27 = box(
    pos = (x3,y5,z),
    width = ww,
    length = wl,
    height = wh,
    color = color5,
    material = m
    )

brick28 = box(
    pos = (x4,y5,z),
    width = ww,
    length = wl,
    height = wh,
    color = color5,
    material = m
    )

brick29 = box(
    pos = (x5,y5,z),
    width = ww,
    length = wl,
    height = wh,
    color = color5,
    material = m
    )

brick30 = box(
    pos = (x6,y5,z),
    width = ww,
    length = wl,
    height = wh,
    color = color5,
    material = m
    )

#left screen wall

wall1 = box(
    pos = (-18,-18,0),
    width = 0,
    length = 3,
    height = 70,
    color = color6,
    material = materials.silver
    )

#top screen wall

wall2 = box(
    pos = (18,18,0),
    width = 0,
    length = 75,
    height = 3,
    color = color6,
    material = materials.silver
    )

#right screen wall

wall3 = box(
    pos = (18,-18,0),
    width = 0,
    length = 3,
    height = 70,
    color = color6,
    material = materials.silver
    )


shooter.v = 2*vector(1,0,0)

#ballsList = [ball1,ball2,ball3,ball4]

bricksList = [brick1,brick2,brick3,brick4,brick5,brick6,brick7,brick8,brick9,brick10,brick11,brick12,brick13,brick14,brick15,brick16,brick17,brick18,brick19,brick20,brick21,brick22,brick23,brick24,brick25,brick26,brick27,brick28,brick29,brick30]

bulletsList = []

wallsList = [wall1,wall2,wall3]

#function that makes shooter change colors when colliding with bullet
def random_color():
    rgbl=[250,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

hits = 0
shots = 0
max_shots = 1

s=5 #speed of shooter
b=7 #speed of bullet

t=0
dt=0.01


while 1:
    rate(100)
    if scene.kb.keys:
        k = scene.kb.getkey()
        if k =="right":
            shooter.v = s*vector(1,0,0)
        elif k == "left":
            shooter.v = s*vector(-1,0,0)

        elif k == " " and shots< max_shots:
            bullet = sphere(pos=(shooter.pos.x,shooter.pos.y+shooter.height,shooter.pos.z),radius=0.5,color=color.white)
            shots +=1
            print shots
            bullet.v = b*vector(0,1,0)
            bulletsList.append(bullet)

        elif k == "a":
            bullet = sphere(pos=(shooter.pos.x,shooter.pos.y+shooter.height,shooter.pos.z),radius=0.5,color=color.white)
            shots = 0
            shots +=1
            print shots
            bullet.v = b*vector(0,1,0)
            bulletsList.append(bullet)

        else:
            shooter.v=vector(0,0,0)
    shooter.pos = shooter.pos + shooter.v*dt

    #below:keeps shooter within the walls
    if shooter.pos.x > 14:
        shooter.v = vector(-1,0,0)
    if shooter.pos.x < -14:
        shooter.v = vector(1,0,0)

    for bullet in bulletsList:
        bullet.pos = bullet.pos + bullet.v*dt
        for brick in bricksList:
            if collisionSpheres(bullet,brick):
                brick.visible = False
                bullet.v = b*vector(0,-1,0)
                hits += 1
                print hits
                brick.pos = (-20,8,0)
                if hits == 30:
                    text( text='Winner!', align = 'center', depth = -0.8, width = 8, height = 4, color = color.white, material = materials.emissive)
                    break
        if collisionSpheres(bullet,shooter) and bullet.pos.x > shooter.pos.x:
            bullet.v = b*vector(1,1,0) # makes bullet move to the right
            shooter.color = random_color()

        if collisionSpheres(bullet,shooter) and bullet.pos.x < shooter.pos.x:
            bullet.v = b*vector(-1,1,0) #makes bullet move to the left
            shooter.color = random_color()

        if collisionSpheres(bullet,shooter) and bullet.pos.x == shooter.pos.x:
            bullet.v = b*vector(0,1,0) #makes bullet go straight up
            shooter.color = random_color()

        if bullet.pos.y > 16 and bullet.v == b*vector(-1,1,0):
            bullet.v = b*vector(-1,-1,0)

        if bullet.pos.y > 16 and bullet.v == b*vector(1,1,0):
            bullet.v = b*vector(1,-1,0)

        if bullet.pos.y >16 and bullet.v == b*vector(0,1,0):
            bullet.v = b*vector(0,-1,0)

        if bullet.pos.x > 16 and bullet.v == b*vector(1,-1,0):
            bullet.v = b*vector(-1,-1,0)

        if bullet.pos.x > 16 and bullet.v == b*vector(1,1,0):
            bullet.v = b*vector(-1,1,0)

        if bullet.pos.x < -16 and bullet.v == b*vector(-1,-1,0):
            bullet.v = b*vector(1,-1,0)

        if bullet.pos.x < -16 and bullet.v == b*vector(-1,1,0):
            bullet.v = b*vector(1,1,0)

        if -17.02< bullet.pos.y < -17.0 and hits != 30:
            text( text='Game Over', align = 'center', depth = -0.8, width = 8, height = 4, color = color.white, material = materials.emissive, pos = (0,-5,0))
            break

    t=t+dt
