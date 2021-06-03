import pygame
# Inicialización de Pygame
pygame.init()
# Inicialización de la superficie de dibujo (display surface)
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 1")
# Bucle principal
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    ventana.fill((255, 255, 255))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()

