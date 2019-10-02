# -*- coding: utf-8 -*-
from os import path

from pydub import AudioSegment
from pydub.playback import play


def mandioca():
    sound = AudioSegment.from_mp3(
        path.join(path.dirname(__file__), 'sounds', 'saudando-a-mandioca.mp3'))
    play(sound)

def bola():
    sound = AudioSegment.from_mp3(
        path.join(path.dirname(__file__), 'sounds', 'mulhersapiens.mp3'))
    play(sound)
