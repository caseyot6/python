import pygame
import pickle

def conway():

    pygame.init()
    pygame.font.init()

    x = 600
    y = 600
    ui_width = 300
    running = True
    offset = (0,0)
    step = 10
    world = pygame.display.set_mode(size = (x+ui_width,y))
    current_rules = 0
    map = dict()
    line_color = (0,0,0)
    box_color = [0,255,255]
    current_color = box_color
    box_positions = dict()
    box_colors = {0:(255,0,0), 1:(0,255,0),2:(0,0,255)}
    current_map = dict()
    pause = True
    current_num = 1
    time = False
    last_frame = 0
    period = 50
    shape_num = 1
    #initialize dictionary containing each possible position
    for i in range(0, x//step):
        for j in range(0, y//step):
            if (i,j) not in current_map:
                current_map[(i,j)] = [0, box_colors[current_num]]


    while running:

        world.fill((255,255,255))

        if time:
            if pygame.time.get_ticks()-last_frame > period:
                last_frame = pygame.time.get_ticks()
                if current_rules == 0:
                    current_map = run_conway(current_map, step, x//step, y//step)

        draw_ui(world, ui_width)
        draw_lines(world, offset, step, line_color, x, y)
        draw_squares(world, current_map, offset, step)

        pygame.display.update()
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            new_coord = (mouse_pos[0]//step, mouse_pos[1]//step)

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if current_map[new_coord][0] == 0:
                    current_map[new_coord] = [current_num, box_colors[current_num]]
                else:
                    current_map[new_coord] = [0, box_colors[current_num]]

            elif event.type == pygame.KEYDOWN:
                if(event.key == 99):
                    for i in range(0, x//step):
                        for j in range(0, y//step):
                            if (i,j) in current_map:
                                current_map[(i,j)] = [0, box_colors[current_num]]

                elif(event.key == 112):
                    if time == True:
                        time = False
                    else:
                        time = True
                elif (event.key == 48):
                    for i in range(0, x//step):
                        for j in range(0, y//step):
                            current_map[(i,j)] = [0, box_colors[current_num]]

                elif (event.key == 49):
                    shape_num = 0
                    add_conway_shape(shape_num, current_map, new_coord,
                    x//step, y//step)
                elif (event.key == 50):
                    shape_num = 1
                    add_conway_shape(shape_num, current_map, new_coord,
                    x//step, y//step)
                elif (event.key == 51):
                    shape_num = 2
                    add_conway_shape(shape_num, current_map, new_coord,
                    x//step, y//step)

def draw_ui(world, ui_width):

    x = 10
    y = 10

    font_type = pygame.font.SysFont('Comic Sans MS', 15)
    title = font_type.render("Conway's Game of Life", True, (0,0,0))
    world.blit(title,(world.get_width()-ui_width+x, y))


    instructions = font_type.render("Instructions:", True, (0,0,0))
    world.blit(instructions,(world.get_width()-ui_width+x, y+20))

    instructions = font_type.render("Point & click to draw on grid.", True, (0,0,0))
    world.blit(instructions,(world.get_width()-ui_width+x, y+40))

    instructions = font_type.render("Press 1-3 to add unique shapes", True, (0,0,0))
    world.blit(instructions,(world.get_width()-ui_width+x, y+70))

    instructions = font_type.render("Press 0 to erase current view", True, (0,0,0))
    world.blit(instructions,(world.get_width()-ui_width+x, y+100))

    instructions = font_type.render("Press P to pause & play simulation", True, (0,0,0))
    world.blit(instructions,(world.get_width()-ui_width+x, y+130))


    return world

def draw_lines(world, offset, step, line_color, x, y):

    height = x
    width = y

    for i in range(0, height, step):
        pygame.draw.line(world, line_color, (0, i), (width, i),1)

    for i in range(0, width, step):
        pygame.draw.line(world, line_color, (i, 0), (i,height),1)

def draw_squares(world, current_map, offset, step):

    for key in current_map:
        if current_map[key][0] != 0:
            x = key[0]
            y = key[1]
            pygame.draw.rect(world, current_map[key][1],
             (x*step, y*step, step,step))

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
                        sum += current_map[x_y][0]

        if current_map[coord][0] == 0:
            if sum == 3:
                new_map[coord] = [1, current_map[coord][1]]

            else:
                new_map[coord] = [0, current_map[coord][1]]
        elif current_map[coord][0] == 1:
            if (sum == 2) or (sum == 3):
                new_map[coord] = [1, current_map[coord][1]]
            else:
                new_map[coord] = [0, current_map[coord][1]]
        else:
            new_map[coord] = current_map[coord]

    return new_map

def add_conway_shape(index, current_map, new_coord, width, height):

    if index == 0:
        glider = [(0,0), (-1,1),(1,0),(0,-1),(-1,-1)]
        for i in glider:
            x = i[0]+new_coord[0]
            y = i[1]+new_coord[1]

            if (x >= width):
                x = 0
            elif(x < 0):
                x = width-1

            if (y >= height):
                y = 0
            elif(y < 0):
                y = height-1

            current_map[(x,y)][0] = 1
    elif index == 1:

        hwss = [(0,1,0,0), (1,1,1,0), (1,0,1,1), (0,1,1,1), (0,1,1,1), (0,1,1,1), (0,1,1,0)]
        for i in range(0,len(hwss)):
            k = 0
            for j in hwss[i]:
                x = i + new_coord[0]
                y = k + new_coord[1]

                if (x >= width):
                    x = 0
                elif(x < 0):
                    x = width-1

                if (y >= height):
                    y = 0
                elif(y < 0):
                    y = height-1

                current_map[(x,y)][0] = j
                k += 1




    elif index == 2:

        mwss = [(0,1,0,0), (1,1,1,0), (1,0,1,1), (0,1,1,1), (0,1,1,1), (0,1,1,0)]
        for i in range(0,len(mwss)):
            k = 0
            for j in mwss[i]:
                x = i + new_coord[0]
                y = k + new_coord[1]

                if (x >= width):
                    x = 0
                elif(x < 0):
                    x = width-1

                if (y >= height):
                    y = 0
                elif(y < 0):
                    y = height-1

                current_map[(x,y)][0] = j
                k += 1
    elif index == 3:

        lwss = [(0,1,1,0), (0,1,1,1), (1,0,1,1), (1,1,1,0), (0,1,0,0)]
        for i in range(0,len(lwss)):
            k = 0
            for j in lwss[i]:
                x = i + new_coord[0]
                y = k + new_coord[1]

                if (x >= width):
                    x = 0
                elif(x < 0):
                    x = width-1

                if (y >= height):
                    y = 0
                elif(y < 0):
                    y = height-1

                current_map[(x,y)][0] = j
                k += 1

    return current_map


conway()
