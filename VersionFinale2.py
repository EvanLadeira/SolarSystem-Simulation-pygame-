"""
Version corrigée de VersionFinale.py :
- Le système devrait maintenant être à l'équilibre
- Changement des unités (maintenant elles sont bien plus cohérentes)
- Distances des planètes maintenant à l'échelle (on ne voit plus tout mais tant pis)
- Noms de variables et de fonctions plus cohérents

Code commenté par chatGPT (merci à ce GOAT)
"""


import pygame
import math

# ===================== CONSTANTES =====================
G = 6.67430e-11          # constante gravitationnelle
DT = 3600 * 50           # 5 heures par frame
SCALE = 1 / 1.5e9        # 1 pixel = 1.5 milliard de mètres

WIDTH, HEIGHT = 1900, 1000
CENTER = (WIDTH // 2, HEIGHT // 2)

# ===================== INIT PYGAME =====================
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


# ===================== DONNÉES =====================
data = {
    "Soleil": {
        "mass": 1.989e30,
        "radius": 26,              # rayon VISUEL (pixels)
        "color": "yellow",
        "pos": [0.0, 0.0],         # m
        "vel": [0.0, 0.0]          # m/s
    },

    "Mercure": {
        "mass": 3.30e23,
        "radius": 4,
        "color": "grey",
        "pos": [57.9e9, 0.0],
        "vel": [0.0, 47_400.0]
    },

    "Venus": {
        "mass": 4.87e24,
        "radius": 7,
        "color": (205, 133, 63),
        "pos": [108.2e9, 0.0],
        "vel": [0.0, 35_000.0]
    },

    "Terre": {
        "mass": 5.97e24,
        "radius": 7,
        "color": "blue",
        "pos": [149.6e9, 0.0],
        "vel": [0.0, 29_780.0]
    },

    "Mars": {
        "mass": 6.42e23,
        "radius": 6,
        "color": "red",
        "pos": [227.9e9, 0.0],
        "vel": [0.0, 24_070.0]
    },

    "Jupiter": {
        "mass": 1.898e27,
        "radius": 14,
        "color": (210, 180, 140),
        "pos": [778.5e9, 0.0],
        "vel": [0.0, 13_070.0]
    },

    "Saturne": {
        "mass": 5.683e26,
        "radius": 12,
        "color": (222, 184, 135),
        "pos": [1.433e12, 0.0],
        "vel": [0.0, 9_690.0]
    },

    "Uranus": {
        "mass": 8.681e25,
        "radius": 10,
        "color": (173, 216, 230),
        "pos": [2.872e12, 0.0],
        "vel": [0.0, 6_800.0]
    },

    "Neptune": {
        "mass": 1.024e26,
        "radius": 10,
        "color": (0, 191, 255),
        "pos": [4.495e12, 0.0],
        "vel": [0.0, 5_430.0]
    }
}

# ===================== PHYSIQUE =====================
def compute_forces():
    forces = {name: [0.0, 0.0] for name in data}

    for p1 in data:
        for p2 in data:
            if p1 == p2:
                continue

            dx = data[p2]["pos"][0] - data[p1]["pos"][0]
            dy = data[p2]["pos"][1] - data[p1]["pos"][1]
            r = math.sqrt(dx*dx + dy*dy)

            if r == 0:
                continue

            F = G * data[p1]["mass"] * data[p2]["mass"] / r**2
            fx = F * dx / r
            fy = F * dy / r

            forces[p1][0] += fx
            forces[p1][1] += fy

    return forces


def update():
    forces = compute_forces()

    for planet in data:
        ax = forces[planet][0] / data[planet]["mass"]
        ay = forces[planet][1] / data[planet]["mass"]

        data[planet]["vel"][0] += ax * DT
        data[planet]["vel"][1] += ay * DT

        data[planet]["pos"][0] += data[planet]["vel"][0] * DT
        data[planet]["pos"][1] += data[planet]["vel"][1] * DT


# ===================== AFFICHAGE =====================
def draw():
    screen.fill("black")

    for planet in data:
        x = data[planet]["pos"][0] * SCALE + CENTER[0]
        y = data[planet]["pos"][1] * SCALE + CENTER[1]

        pygame.draw.circle(
            screen,
            data[planet]["color"],
            (int(x), int(y)),
            data[planet]["radius"]
        )


# ===================== BOUCLE PRINCIPALE =====================
FPS = 60

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()
    draw()
    pygame.display.flip()

pygame.quit()
