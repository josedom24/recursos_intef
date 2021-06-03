import pygame
# Inicialización de Pygame
pygame.init()
# Inicialización de la superficie de dibujo (display surface)
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 2")
# Crea un objeto imagen, y obtengo su rectángulo
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [4,4]
# Bucle principal
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Muevo la pelota
    ballrect = ballrect.move(speed)
    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
            
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
    ventana.fill((255, 255, 255))
    ventana.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()

