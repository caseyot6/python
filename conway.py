import pygame

def conway():
    x = 600
    y = 600
    running = True
    offset = (0,0)
    step = 20
    pygame.init()
    world = pygame.display.set_mode(size = (x,y))
    map = dict()
    line_color = (0,0,0)
    box_color = (255,255,0)
    box_positions = dict()
    current_map = dict()
    pause = True

    for i in range(0, x//step):
        for j in range(0, y//step):
            if (i,j) not in current_map:
                current_map[(i,j)] = 0


    while running:

        world.fill((255,255,255))

        if pause == False:
            current_map = run_conway(current_map, step, x//step, y//step)
            pause = True
        draw_lines(world, offset, step, line_color)
        draw_squares(world, current_map, offset, step, box_color)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                new_coord = (mouse_pos[0]//step, mouse_pos[1]//step)

                if current_map[new_coord] == 0:
                    current_map[new_coord] = 1
                else:
                    current_map[new_coord] = 0



                break

            elif event.type == pygame.KEYDOWN:
                if (event.key == 112):
                    if pause == True:
                        pause = False
                    else:
                        pause = True


def draw_lines(world, offset, step, line_color):
    height = world.get_height()
    width = world.get_width()


    for i in range(0, height, step):
        pygame.draw.line(world, line_color, (0, i), (width, i),1)

    for i in range(0, width, step):
        pygame.draw.line(world, line_color, (i, 0), (i,height),1)

def draw_squares(world, current_map, offset, step, box_color):

    for key in current_map:
        if current_map[key] == 1:
            x = key[0]
            y = key[1]
            pygame.draw.rect(world, box_color, (x*step, y*step, step,step))

def run_conway(current_map, step, width, height):

    new_map = dict()

    for coord in current_map:
        sum = 0

        for i in range(-1,2):
            for j in range(-1,2):
                if (i == 0 and j == 0) == False:
                    x = i+coord[0]
                    y = j+coord[1]

                    if (x >= width):
                        x = 0
                    elif(x < 0):
                        x = width-1

                    if (y >= height):
                        y = 0
                    elif(y < 0):
                        y = height-1

                    x_y = (x, y)
                    if x_y in current_map:
                        sum += current_map[x_y]

        if current_map[coord] == 0:
            if sum == 3:
                new_map[coord] = 1

            else:
                new_map[coord] = 0
        else:
            if (sum == 2) or (sum == 3):
                new_map[coord] = 1
            else:
                new_map[coord] = 0

    return new_map

conway()
