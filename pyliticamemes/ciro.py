# -*- coding: utf-8 -*-
from os import path

from pydub import AudioSegment
from pydub.playback import play


def aidentu():
    sound = AudioSegment.from_mp3(
        path.join(path.dirname(__file__), 'sounds', 'aidentu.mp3'))
    play(sound)
