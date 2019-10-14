# -*- coding: utf-8 -*-
from os import path

from pydub import AudioSegment
from pydub.playback import play


def risada():
    sound = AudioSegment.from_mp3(
        path.join(path.dirname(__file__), 'sounds', 'bolsonaro', 'risada.mp3'))
    play(sound)

def daqueeutedououtra():
    sound = AudioSegment.from_mp3(
        path.join(path.dirname(__file__), 'sounds', 'bolsonaro', 'daqueeutedououtra.mp3'))
    play(sound)
