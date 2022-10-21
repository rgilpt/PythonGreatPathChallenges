import pygame
import random
import math

# initiate pygame
pygame.init()

# set screen res
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("spaceBackground.jpg")

# title and icon
pygame.display.set_caption("I'll change this later")
icon = pygame.image.load("Eyeball - for project.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("fireModDude(project).png")
playerX = 400
playerY = 538
playerXChange = 0

#lives
lives = 3
#score (when asteroid dodged)
score = 0

# asteroid
asteroidImg = []
asteroidX = []
asteroidY = []
asteroidStartingX = []
asteroidAngle = []
numOfAsteroids = 6

for i in range(numOfAsteroids):
    asteroidImg.append(pygame.image.load("asteroid.png"))
    x = random.randint(0, 768)
    asteroidX.append(x)
    asteroidStartingX.append(x)
    asteroidY.append(-32)
    asteroidAngle.append(random.uniform(0.15, 0.9))


def player(x, y):
    screen.blit(playerImg, (x, y))


def asteroid(x, y, i):
    screen.blit(asteroidImg[i], (x, y))


def isCollision(asteroidX, asteroidY, playerX, playerY):
    distance = math.sqrt((math.pow(asteroidX - playerX, 2)) + (math.pow(asteroidY - playerY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:

    # RGB background
    screen.fill((57, 70, 78))

    # background img
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXChange = -0.3
            if event.key == pygame.K_RIGHT:
                playerXChange = 0.3
            if event.key != pygame.K_LEFT and event.key != pygame.K_LEFT:

                # to make it stop when key released
                # if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #     playerXChange = 0

                # moves when no input is detected
                if event.key == pygame.K_LEFT:
                    playerXChange = -0.3
                if event.key == pygame.K_RIGHT:
                    playerXChange = 0.3

    playerX += playerXChange
    asteroidY += asteroidAngle

    # makes asteroids move diagonally to some extent rather than straight
    if asteroidStartingX[i] <= 384:
        asteroidX[i] += random.uniform(0.05, 0.25)
    elif asteroidStartingX[i] >= 384:
        asteroidX[i] -= random.uniform(0.05, 0.25)

    # respawns asteroid
    for i in range(numOfAsteroids):
        if asteroidY[i] >= 600:
            score += 1
            asteroidX[i] = random.randint(0, 768)
            asteroidStartingX[i] = asteroidX[i]
            asteroidY[i] = -32
            asteroidAngle[i] = random.uniform(0.3, 1)

        # collision
        collision = isCollision(asteroidX[i], asteroidY[i], playerX, playerY)
        if collision:
            asteroidX[i] = random.randint(0, 768)
            asteroidStartingX[i] = asteroidX[i]
            asteroidY[i] = -32
            asteroidAngle[i] = random.uniform(0.3, 1)
            lives -= 1
            print(lives)

        asteroid(asteroidX[i], asteroidY[i], i)


    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768

    player(playerX, playerY)
    pygame.display.update()