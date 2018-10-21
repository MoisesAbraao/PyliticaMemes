# -*- coding: utf-8 -*-
import pygame
from os import path

pygame.mixer.init()

def gloriadeux():
    pygame.mixer.music.load(path.join(path.abspath('pyliticamemes/sounds'), 'cabo-daciolo-gloria-a-deus-xUQDkBNqgNE.mp3'))
    pygame.mixer.music.play()
    pygame.event.wait()

def fundopartidario():
    pygame.mixer.music.load(path.join(path.abspath('pyliticamemes/sounds'), 'fundopartidario.mp3'))
    pygame.mixer.music.play()
    pygame.event.wait()