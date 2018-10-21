# -*- coding: utf-8 -*-
import pygame

# pygame.mixer.init()
pygame.init()

def mandioca():
    pygame.mixer.music.load('/Users/moisesabraao/Documents/Project/PyliticaMemes/src/pyliticamemes/sounds/saudando-a-mandioca.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()

def bola():
    pygame.mixer.music.load('/Users/moisesabraao/Documents/Project/PyliticaMemes/src/pyliticamemes/sounds/mulhersapiens.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()