# -*- coding: utf-8 -*-
import pygame
from os import path

# pygame.mixer.init()
pygame.init()

def mandioca():
    pygame.mixer.music.load(path.join(path.abspath('pyliticamemes/sounds'), 'saudando-a-mandioca.mp3'))
    pygame.mixer.music.play()
    input()

def bola():
    pygame.mixer.music.load(path.join(path.abspath('pyliticamemes/sounds'), 'mulhersapiens.mp3'))
    pygame.mixer.music.play()
    input()