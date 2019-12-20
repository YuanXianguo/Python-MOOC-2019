import sys, pygame

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pygame事件处理函数')
fps = 300
fclock = pygame.time.Clock()
num = 1
while True:
    uevent = pygame.event.Event(pygame.KEYDOWN, {'unicode': 123, 'key': pygame.K_ESCAPE, 'mod': pygame.KMOD_ALT})
    pygame.event.post(uevent)
    num += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == '':
                print('[KEYDOWN{}]:'.format(num), '#', event.key, event.mod)
            else:
                print('[KEYDOWN{}]:'.format(num), event.unicode, event.key, event.mod)
    pygame.display.update()
    fclock.tick(fps)

