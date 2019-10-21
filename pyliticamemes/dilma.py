# -*- coding: utf-8 -*-
from os import path

from pydub import AudioSegment
from pydub.playback import play


def mandioca():
    sound = AudioSegment.from_mp3(
        path.join(path.dirname(__file__), 'sounds', 'dilma', 'saudandoamandioca.mp3'))
    play(sound)

def bola():
    sound = AudioSegment.from_mp3(
        path.join(path.dirname(__file__), 'sounds', 'dilma', 'mulhersapiens.mp3'))
    play(sound)

def vaiperder():
    sound = AudioSegment.from_mp3(
        path.join(path.dirname(__file__), 'sounds', 'dilma', 'vaitodomundoperder.mp3'))
    play(sound)

def saomulheres():
    sound = AudioSegment.from_mp3(
        path.join(path.dirname(__file__), 'sounds', 'dilma', 'saomulheres.mp3'))
    play(sound)
