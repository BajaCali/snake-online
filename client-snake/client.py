import sys, os.path, traceback
import pygame
sys.path.append(os.path.join(*(3 * ['..'])))

UP    = '1'
DOWN  = '3'
LEFT  = '2'
RIGHT = '4'

from Communication.tcp import Client

tcp = Client('localhost', 11111, timeout = 2, encoding = 'utf8', decoding = 'ASCII')

if not tcp.connected:
    print ('Connection failed. err: {}'.format(tcp.error))
    exit()

tcp.timeout = 0

print('Connected')

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('client')

tcp.write('ahoj')

while 1:
    event = pygame.event.poll()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            tcp.write('w')
            tcp.write(UP)
        elif event.key == pygame.K_a:
            tcp.write('a')
            tcp.write(LEFT)
        elif event.key == pygame.K_s:
            tcp.write('s')
            tcp.write(DOWN)
        elif event.key == pygame.K_d:
            tcp.write('d')
            tcp.write(RIGHT)
    r = tcp.read()
    if r:
        print(r)
tcp.close()
print('\n\nclosed')
