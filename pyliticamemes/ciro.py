# -*- coding: utf-8 -*-
import pygame

pygame.mixer.init()

def aidentu():
    pygame.mixer.music.load('/Users/moisesabraao/Documents/Project/PyliticaMemes/src/pyliticamemes/sounds/aidentu.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()