import pygame
# Inicialización de Pygame
pygame.init()
# Inicialización de la superficie de dibujo (display surface)
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 3")
# Crea un objeto imagen, y obtengo su rectángulo
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [4,4]
# Crea un objeto imagen bate, y obtengo su rectángulo
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
# Pongo el bate en el medio de la pantalla
baterect.move_ip(240,450)
# Bucle principal
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-3,0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(3,0)
    # Compruebo si ha colisión
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
    # Muevo la pelota
    ballrect = ballrect.move(speed)
    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
    ventana.fill((255,255,255))
    ventana.blit(ball, ballrect)
    # Dibujo el bate
    ventana.blit(bate, baterect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()

