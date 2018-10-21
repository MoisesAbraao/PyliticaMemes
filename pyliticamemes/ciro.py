# -*- coding: utf-8 -*-
import pygame
from os import path

pygame.mixer.init()

def aidentu():
    pygame.mixer.music.load(path.join(path.abspath('pyliticamemes/sounds'), 'aidentu.mp3'))
    pygame.mixer.music.play()
    pygame.event.wait()