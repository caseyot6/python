import pygame

def conway():
    running = True
    offset = (0,0)
    step = 20
    pygame.init()
    world = pygame.display.set_mode(size = (600,600))
    map = dict()
    line_color = (0,0,0)
    box_color = (255,255,0)
    box_positions = dict()
    current_map = dict()

    while running:

        world.fill((255,255,255))

        current_map = run_conway(current_map)
        draw_lines(world, offset, step, line_color)
        draw_squares(world, current_map, offset, step, box_color)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                new_coord = (mouse_pos[0]//step, mouse_pos[1]//step)

                if new_coord not in current_map:
                    current_map[new_coord] = 1
                elif current_map[new_coord] == 0:
                    current_map[new_coord] = 1
                else:
                    current_map[new_coord] = 0

                break


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

def run_conway(current_map):


    pass

conway()
