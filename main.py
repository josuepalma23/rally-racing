import settings 
import pygame
import sys

def main():
    pygame.init() 

    pantalla = pygame.display.set_mode((settings.Ventana.ANCHO, settings.Ventana.ALTO))
    pygame.display.set_caption(settings.Ventana.TITULO)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()

    