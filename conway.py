import pygame

def conway():
    running = True
    offset = (0,0)
    step = 20
    pygame.init()
    world = pygame.display.set_mode(size = (600,600))
    map = dict()

    while running:

        world.fill((255,255,255))
        draw_lines(world, offset, step)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def draw_lines(world, offset, step):
    height = world.get_height()
    width = world.get_width()


    for i in range(0, height, step):
        pygame.draw.line(world, (0,0,0), (0, i), (width, i),1)

    for i in range(0, width, step):
        pygame.draw.line(world, (0,0,0), (i, 0), (i,height),1)

conway()
