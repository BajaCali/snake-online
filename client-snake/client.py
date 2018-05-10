import sys, os.path, traceback
import pygame
sys.path.append(os.path.join(*(3 * ['..'])))

from Communication.tcp import Client


tcp = Client('localhost', 11111, timeout = 2, encoding = 'utf8', decoding = None)

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
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            tcp.write('w')
        elif event.key == pygame.K_a:
            tcp.write('a')
        elif event.key == pygame.K_s:
            tcp.write('s')
        elif event.key == pygame.K_d:
            tcp.write('d')
    print (tcp.read())
tcp.close()
print('\n\nclosed')
