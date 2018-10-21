# -*- coding: utf-8 -*-
import pygame

pygame.mixer.init()

def gloriadeux():
    pygame.mixer.music.load('sounds/cabo-daciolo-gloria-a-deus-xUQDkBNqgNE.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()

def fundopartidario():
    pygame.mixer.music.load('/Users/moisesabraao/Documents/Project/PyliticaMemes/src/pyliticamemes/sounds/fundopartidario.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()