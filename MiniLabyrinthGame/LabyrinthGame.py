import pygame
import sys


pygame.init()


width, height = 700, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Labyrinth game")


cell_size = 50
#textures
wall_texture = pygame.image.load("Images/grass.jpeg")
path_texture = pygame.image.load("Images/water.jpeg")
player_texture = pygame.image.load("Images/goofyfish.jpeg")
goal_texture = pygame.image.load("Images/alga.jpeg")
trap_texture= pygame.image.load("Images/shark.jpeg")

wall_texture = pygame.transform.scale(wall_texture, (cell_size, cell_size))
path_texture = pygame.transform.scale(path_texture, (cell_size, cell_size))
player_texture = pygame.transform.scale(player_texture, (cell_size, cell_size))
goal_texture = pygame.transform.scale(goal_texture, (cell_size, cell_size))
trap_texture= pygame.transform.scale(trap_texture,(cell_size,cell_size))

#Labyrinth
Labyrinth = [
    ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
    ["|", "A", ".", ".", "|", ".", ".", ".", ".", "|", ".", ".", ".", "|"],
    ["|", "|", "|", ".", "|", "|", "|", ".", "|", "|", ".", "|", "|", "|"],
    ["|", ".", "*", ".", ".", ".", ".", "|", ".", ".", ".", ".", ".", "|"],
    ["|", ".", "|", "|", "|", ".", "|", "|", "|", "|", ".", "|", "|", "|"],
    ["|", ".", "|", ".", ".", ".", ".", ".", ".", "|", ".", ".", ".", "|"],
    ["|", "|", "|", "|", "|", "|", "|", ".", "|", "|", "|", "|", ".", "|"],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "|"],
    ["|", ".", "|", "|", "|", "|", ".", "|", "|", ".", "|", "|", ".", "|"],
    ["|", ".", ".", ".", ".", "|", ".", "*", ".", ".", "|", ".", ".", "|"],
    ["|", "|", ".", "|", ".", "|", "|", "|", ".", "|", "*", ".", ".", "|"],
    ["|", ".", ".", "|", ".", ".", ".", ".", ".", "|", ".", "|", "|", "|"],
    ["|", ".", "|", "|", "|", "|", "|", "|", ".", "|", ".", ".", ".", "|"],
    ["|", ".", ".", ".", ".", ".", ".", "|", ".", ".", ".", ".", "B", "|"],
    ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"]
]

Player_x, Player_y = 1, 1

def draw_labyrinth():
    for i in range(len(Labyrinth)):
        for j in range(len(Labyrinth[i])):
            if Labyrinth[i][j] == "|":
                screen.blit(wall_texture, (j * cell_size, i * cell_size))
            elif Labyrinth[i][j] == ".":
                screen.blit(path_texture, (j * cell_size, i * cell_size))
            elif Labyrinth[i][j] == "A":
                screen.blit(player_texture, (j * cell_size, i * cell_size))
            elif Labyrinth[i][j] == "B":
                screen.blit(goal_texture, (j * cell_size, i * cell_size))
            elif Labyrinth[i][j]=="*":
                screen.blit(trap_texture,(j*cell_size,i*cell_size))

def movement(x, y):
    global Player_x, Player_y
    new_x = Player_x + x
    new_y = Player_y + y

    if Labyrinth[new_x][new_y] == "|":
        return 0

    if Labyrinth[new_x][new_y] == "*":
        print("Try again")
        pygame.quit()
        sys.exit()

    if Labyrinth[new_x][new_y] == "B":
        print("Congrats!")
        pygame.quit()
        sys.exit()

    Labyrinth[Player_x][Player_y] = "."
    Player_x = new_x
    Player_y = new_y
    Labyrinth[Player_x][Player_y] = "A"

Commands = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
while True:
    screen.fill((255, 255, 255))
    draw_labyrinth()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movement(*Commands["w"])
            elif event.key == pygame.K_s:
                movement(*Commands["s"])
            elif event.key == pygame.K_a:
                movement(*Commands["a"])
            elif event.key == pygame.K_d:
                movement(*Commands["d"])

    pygame.display.update()
    pygame.time.Clock().tick(144)
