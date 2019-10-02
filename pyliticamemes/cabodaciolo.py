# -*- coding: utf-8 -*-
from os import path

from pydub import AudioSegment
from pydub.playback import play


def gloriadeux():
    sound = AudioSegment.from_mp3(
        path.join(path.dirname(__file__), 'sounds', 'cabo-daciolo-gloria-a-deus-xUQDkBNqgNE.mp3'))
    play(sound)

def fundopartidario():
    sound = AudioSegment.from_mp3(
        path.join(path.dirname(__file__), 'sounds', 'fundopartidario.mp3'))
    play(sound)
