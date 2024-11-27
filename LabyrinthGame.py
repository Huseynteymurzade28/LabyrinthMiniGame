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
interface_texture = pygame.image.load("Images/background.jpeg")

Blue=(0,0,255)
Green=(0,255,0)
randcolor=(223,123,24)
wall_texture = pygame.transform.scale(wall_texture, (cell_size, cell_size))
path_texture = pygame.transform.scale(path_texture, (cell_size, cell_size))
player_texture = pygame.transform.scale(player_texture, (cell_size, cell_size))
goal_texture = pygame.transform.scale(goal_texture, (cell_size, cell_size))
trap_texture= pygame.transform.scale(trap_texture,(cell_size,cell_size))
interface_texture =pygame.transform.scale(interface_texture,(700,700))

#Labyrinth
levels = {
    1: [
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
    ],
    2: [
    ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
    ["|", "A", ".", ".", "*", ".", ".", ".", "*", "|", ".", ".", ".", "|"],
    ["|", "|", "|", ".", "|", "|", "|", ".", "*", "|", ".", "|", "|", "|"],
    ["|", ".", "*", ".", ".", ".", ".", "|", ".", ".", ".", ".", "*", "|"],
    ["|", ".", "|", "|", "|", ".", "|", "|", "*", "|", ".", "|", "|", "|"],
    ["|", ".", "|", ".", ".", ".", ".", ".", ".", "|", ".", ".", "*", "|"],
    ["|", "|", "|", "|", "|", "|", "|", ".", "|", "|", "|", "|", ".", "|"],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "*", "|"],
    ["|", ".", "|", "|", "|", "|", ".", "|", "|", ".", "|", "|", ".", "|"],
    ["|", ".", ".", ".", ".", "|", ".", "*", ".", ".", "|", ".", ".", "|"],
    ["|", "|", ".", "|", ".", "|", "|", "|", ".", "|", "*", ".", ".", "|"],
    ["|", ".", ".", "|", ".", ".", ".", ".", ".", "|", ".", "|", "|", "|"],
    ["|", ".", "|", "|", "|", "|", "|", "|", ".", "|", ".", ".", ".", "|"],
    ["|", ".", ".", ".", ".", ".", ".", "|", ".", ".", ".", ".", "B", "|"],
    ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"]
],
    3:[
    ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"],
    ["|", "A", ".", ".", ".", ".", ".", ".", ".", "|", ".", ".", ".", "|"],
    ["|", "|", "|", ".", "|", "|", "|", ".", ".", "|", "*", "|", "|", "|"],
    ["|", ".", ".", ".", "*", ".", ".", "|", ".", ".", ".", "*", ".", "|"],
    ["|", ".", "|", "|", "|", ".", "|", "|", ".", "|", ".", "|", "|", "|"],
    ["|", ".", "|", ".", "*", ".", ".", ".", ".", "|", ".", ".", ".", "|"],
    ["|", "|", "|", "|", "|", "|", "|", ".", "|", "|", "|", "|", ".", "|"],
    ["|", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "|"],
    ["|", ".", "|", "|", "|", "|", ".", "|", "|", ".", "|", "|", ".", "|"],
    ["|", ".", ".", ".", "*", "|", ".", "*", ".", ".", "|", ".", ".", "|"],
    ["|", "|", ".", "|", ".", "|", "|", "|", ".", "|", ".", ".", ".", "|"],
    ["|", ".", ".", "|", ".", ".", ".", ".", ".", "|", ".", "|", "|", "|"],
    ["|", ".", "|", "|", "|", "|", "|", "|", ".", "|", ".", ".", ".", "|"],
    ["|", ".", ".", ".", ".", ".", ".", "|", ".", ".", ".", ".", "B", "|"],
    ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"]
]

}
level=None
Labyrinth=None


Player_x, Player_y = 1, 1
def button_drawing(x, y, width, height, text, control=False):

    if control:
        color=Blue
    else:
        color=Green
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.draw.rect(screen,randcolor , (x, y, width, height), 2)
    font = pygame.font.SysFont(None, 40)
    text_surface = font.render(text, True, randcolor)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def main_menu():
    global Player_x,Player_y,level,Labyrinth
    while True:
        screen.blit(interface_texture,(0,0))

        mouse_x,mouse_y=pygame.mouse.get_pos()
        button1_control = 200 <= mouse_x <= 500 and 200 <= mouse_y <= 280
        button2_control = 200 <= mouse_x <= 500 and 300 <= mouse_y <= 380
        button3_control = 200 <= mouse_x <= 500 and 400 <= mouse_y <= 480

        button_drawing(200, 200, 240, 80, "Level 1", button1_control)
        button_drawing(200, 300, 240, 80, "Level 2", button2_control)
        button_drawing(200,400,240,80,"level 3",button3_control)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if i.type == pygame.MOUSEBUTTONDOWN:
                if button1_control:
                    level = 1
                    Labyrinth = levels[level]
                    Player_x, Player_y = 1, 1
                    return 0
                if button2_control:
                    level = 2
                    Labyrinth = levels[level]
                    Player_x, Player_y = 1, 1
                    return 0
                if button3_control:
                    level=3
                    Labyrinth=levels[level]
                    Player_x, Player_y=1, 1
                    return 0

        pygame.display.update()

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
    global Player_x, Player_y,level,Labyrinth
    new_x = Player_x + x
    new_y = Player_y + y
    if Labyrinth[new_x][new_y] == "|":
        return 0

    if Labyrinth[new_x][new_y] == "*":
        print("Try again")
        pygame.quit()
        sys.exit()

    if Labyrinth[new_x][new_y] == "B":
        level+=1
        if level>len(levels):
            print("Congrats!")
            pygame.quit()
            sys.exit()
        Labyrinth=levels[level]
        Player_x=1
        Player_y=1
        return 0

    Labyrinth[Player_x][Player_y] = "."
    Player_x = new_x
    Player_y = new_y
    Labyrinth[Player_x][Player_y] = "A"

Commands = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
main_menu()
while True:

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