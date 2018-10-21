# -*- coding: utf-8 -*-
import pygame
from os import path

pygame.init()

def risada():
    pygame.mixer.music.load(path.join(path.abspath('pyliticamemes/sounds'), 'risada.mp3'))
    pygame.mixer.music.play()
    input()

def daqueeutedououtra():
    pygame.mixer.music.load(path.join(path.abspath('pyliticamemes/sounds'), 'daqueeutedououtra.mp3'))
    pygame.mixer.music.play()
    input()