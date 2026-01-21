import pygame
import math

#ini
pygame.init()
screen = pygame.display.set_mode((1900, 1200))
clock = pygame.time.Clock()
running = True

data = {
    "autreboule":{
        "size":30,
        "mass":10,
        "color": "blue",
        "pos":[950, 600],
        "vel":[0, 0]
    },
    "boule":{
        "size":7,
        "mass":2,
        "color": "white",
        "pos":[900, 600],
        "vel":[0, 0]
    }
}

def draw():
    for planet in data:
        pygame.draw.circle(screen, data[planet]["color"], data[planet]["pos"], data[planet]["size"])

def force_grav_test():

    fplanet = []

    for planet in data:

        som_forcex = 0
        som_forcey = 0

        for other in data:

            distancex = (data[other]["pos"][0] - data[planet]["pos"][0])
            distancey = (data[other]["pos"][1] - data[planet]["pos"][1])

            if other == planet:

                continue

            else:

                F = -6.67*10E-11*(data[planet]["mass"]*data[other]["mass"])/math.sqrt(distancex**2+distancey**2)**2
                theta = math.atan2(distancex, distancey)
                Fx = math.cos(theta) * F
                Fy = math.sin(theta) * F

                som_forcex += Fx
                som_forcey += Fy

        lforce = [som_forcex, som_forcey]
        fplanet.append(lforce)

    return fplanet

def rotation():

    i = 0
    for planet in data:
        Fx, Fy = force_grav_test()[i]
        ax = Fx / data[planet]["mass"] * -10e12  # a = F/m (equation de l'accélération)
        ay = Fy / data[planet]["mass"] * 10e12
        data[planet]["pos"][0] += ax
        data[planet]["pos"][1] += ay
        i+=1



#run
while running:

    screen.fill("black")

    draw()

    rotation()

    clock.tick(120)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
