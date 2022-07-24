"""
Faça um programa em python que abra e
reproduza um arquivo MP3.
"""

"""
import pygame

# iniciar o pygame
pygame.init()
# iniciar o mixer

pygame.mixer.music.load('brinks.mp3')
pygame.mixer.music.play()
input()
pygame.event.mixer.wait()
"""

import pygame

ouvir = str(input('\033[31mDeseja ouvir:[S/N] ')).upper()
if 'S' in ouvir:
    # Iniciando o Mixer Pygame
    pygame.mixer.init()

    # Iniciando o Pygame
    pygame.init()

    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play(loops=1, start=0.0)
    print("\033[34mexecutando a musica BRINK'S NO SAKE ")
    pygame.event.wait()
    print('\033[35m--fim--')
else:
    print('\033[36mOk')
    print('\033[32m<<<Até Mais>>>')
