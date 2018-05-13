# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.

# Encontrada a biblioteca playsound, que é recente (de 2017)
# https://pypi.org/project/playsound/

import playsound

playsound.playsound(r'F:\musicas\Orion.mp3')

#########################

# Usado na aula: PyGame. Essa biblioteca tem muitas funcionalidades usadas pra criar jogos, relacionadas a imagens, sons, etc.
'''
import pygame

# Iniciamos o pygame
pygame.init()

# Usamos o Mixer pra carregar e tocar o arquivo mp3
pygame.mixer.music.load('nome_do_arquivo.mp3')  # Usa-se só o nome do arquivo quando está na mesma pasta, do contrário colocamos o caminho completo, como feito acima.
pygame.mixer.music.play()
pygame.event.wait() # Usado para que ele espere o arquivo terminar de tocar antes de terminar a execução do programa.
'''