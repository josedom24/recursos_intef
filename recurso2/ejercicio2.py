import pygame
pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 2")
# Crea el objeto pelota
ball = pygame.image.load("ball.png")
# Obtengo el rectángulo del objeto anterior
ballrect = ball.get_rect()
# Inicializo los valores con los que se van a mover la pelota
speed = [4,4]
# Pongo la pelota en el origen de coordenadas
ballrect.move_ip(0,0)
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
    
    ventana.fill((252, 243, 207))
    # Dibujo la pelota
    ventana.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()

