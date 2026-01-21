import pygame
import math

#ini
pygame.init()
screen = pygame.display.set_mode((1900, 1000))
background = pygame.image.load("assets/background.jpg")
clock = pygame.time.Clock()
running = True

facteur_zoom = 1
zoom = 0.1

data = {
    "Soleil":{
        "size":50,
        "distance_sol":0,
        "mass":2*10E30,
        "color":"yellow",
        "pos":[950, 500],
        "vel":[0, 0]
    },
    "Mercure":{
        "size":10, #2 439,7 km
        "distance_sol":58*10E6,
        "mass":3.3*10E23,
        "color":"grey",
        "pos":[775, 650],
        "vel":[10, 25]
    },
    "Venus":{
        "size":30,
        "distance_sol":108*10E6,
        "mass":4.8*10e24,
        "color":"brown",
        "pos":[675, 650],
        "vel":[10, 20]
    },
    "Terre":{
        "size":30,
        "distance_sol":150*10E6,
        "mass":6*10E24,
        "color":"blue",
        "pos":[600, 650],
        "vel":[10, 20]
    },
    "Mars":{
        "size":25,
        "distance_sol":230*10E6,
        "mass":6.4*10E23,
        "color":"red",
        "pos":[500, 650],
        "vel":[10, 20]
    },
    "Jupiter":{
        "size":45,
        "distance_sol":778*10E6,
        "mass":1.9*10E27,
        "color":"beige",
        "pos":[400, 650],
        "vel":[10, 20]
    },
    "Saturne":{
        "size":40,
        "distance_sol":1400*10E6,
        "mass":5.7*10E26,
        "color":"beige",
        "pos":[300, 650],
        "vel":[10, 20]
    },
    "Uranus":{
        "size":35,
        "distance_sol":2800*10E6,
        "mass":8.7*10E25,
        "color":"light blue",
        "pos":[200, 650],
        "vel":[10, 20]
    },
    "Neptune":{
        "size":35,
        "distance_sol":4500*10E6,
        "mass":1*10E26,
        "color":"cyan",
        "pos":[100, 650],
        "vel":[10, 20]
    }
}

def draw():
    for planet in data:
        if planet == "Saturne":
            pygame.draw.circle(screen, data[planet]["color"], data[planet]["pos"], data[planet]["size"]/2)
            pygame.draw.line(screen, "beige", (data[planet]["pos"][0], data[planet]["pos"][1]), (data[planet]["pos"][0], data[planet]["pos"][1]), 70)
        else:
            pygame.draw.circle(screen, data[planet]["color"], data[planet]["pos"], data[planet]["size"]/2)


def force_grav():

    fplanet = []

    for planet in data:

        som_forcex = 0
        som_forcey = 0

        for other in data:

            distancex = (data[other]["pos"][0] - data[planet]["pos"][0])
            distancey = (data[other]["pos"][1] - data[planet]["pos"][1])
            vec = [distancex, distancey]

            distance = math.sqrt(distancex**2 + distancey**2)


            if other == planet: # or planet == "Soleil":

                continue

            else:

                vec[0] /= distance
                vec[1] /= distance
                F = -6.67*10E-11*(data[planet]["mass"]*data[other]["mass"])/distance**2

                Fx = vec[0] * F * 2
                Fy = vec[1] * F * 2

                som_forcex += Fx
                som_forcey += Fy

        lforce = [som_forcex, som_forcey]
        fplanet.append(lforce)

    return fplanet


def rotation():

    i = 0

    for planet in data:

        Fx, Fy = force_grav()[i]
        data[planet]["vel"][0] += Fx / data[planet]["mass"] * -0.00000000000000001  # F = ma donc a = F/m (equation de l'accélération)
        data[planet]["vel"][1] += Fy / data[planet]["mass"] * -0.00000000000000001

        data[planet]["pos"][0] += data[planet]["vel"][0]
        data[planet]["pos"][1] += data[planet]["vel"][1]

        i += 1

fps = 30

#run
while running:

    #screen.fill("black")
    screen.blit(background, (0, 0))

    draw()

    rotation()

    clock.tick(fps)

    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                fps -= 10
            if event.key == pygame.K_UP:
                fps += 10
            if event.key == pygame.K_RIGHT:
                print(f"FPS = {fps}")
                print(f"zoom = {facteur_zoom}")

pygame.quit()
