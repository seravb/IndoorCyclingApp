#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cairo
import pycha
import json
import pycha.line
from pprint import pprint
# from lines import lines

# ###############
# class Song(object):
#     def __init__(self, artist, track):
#         self.artist = artist
#         self.track = track
#     def jdefault(o):
#     	return o.__dict__

# songs=open('session_example.json')
# data_songs=json.load(songs)
# songs.close()

# for song in data_songs:
# 	data_song=json.loads(song)
# print "Artist: ", song['artist']
# print "Dimension: ", data['cubes'][cube]['dim']
# print "Measures:  ", data['cubes'][cube]['meas']
################
class Split():
    """ A split it's part of a track, this represents data to create part of the session graphic.
    """

    def __init__(self, split_json_data):
        self.time = split_data['time']
        self.type = split_data['type']
        self.position = split_data['position']
        self.level = split_data['level']
        self.gear = split_data['gear']


class Track():
    """ A track it's part of a session, this represents general data of a session.
    """

    def __init__(self, track_json_data):
        self.artist = track_json_data['artist']
        self.track = track_json_data['track']
        self.type = track_json_data['type']
        self.level = track_json_data['level']
        self.splits = json.load(Split(track_json_data['splits']))  # track_json_data['splits']


class Session():
    """ A Session have the meta data of a session defined in json format.
    """

    def __init__(self, session_json_file):
        self.data_session = json.load(open(session_json_file))
        self.title = data_session['title']
        self.session_time = data_session['session_time']
        self.type = data_session['type']
        self.tracks = json.load(Track(data_session['tracks']))

################



width, height = (800, 800)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

ctx = cairo.Context(surface)
pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba(1, 0.7, 0, 0, 1)  # First stop, 50% opacity
pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity
ctx.set_source(pat)
ctx.fill()

# Nivel - x  -> [[x, y], [x', y'], [x'', y'']]
# x, x', x'' means the splits for draw the levels. This must be the same number as total tracks splits that a session have.
# y, y', y'' means the level as a draw level. For "Level - 1" then y, y'... must be 1, for "Level - 2" then y, y'... must be 2
# Grafica x -> [[z, t], [z', t'], [z'', t'']]
# z, z', z'' represents the level of the track
# t, t', t'' represents the level of the split inside the track 'z'. To draw the track this number will be z+(t/10)
dataSet = (
    ('Nivel - 5', [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5]]),
    ('Nivel - 4', [[0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4]]),
    ('Nivel - 3', [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3]]),
    ('Nivel - 2', [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2]]),
    ('Nivel - 1', [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1]]),
    ('Grafica 1', [[0, 1], [1, 4.25], [2, 0.5], [3, 4], [4, 1], [5, 4.75], [6, 5]]),
)

# dataSet = (
#         ('myFirstDataset', [[0, 3], [1, 2], [2, 1.414], [3, 2.3]]),
#         ('mySecondDataset', [[0, 1.4], [1, 2.67], [2, 1.34], [3, 1.2]]),
#         ('myThirdDataset', [[0, 0.46], [1, 1.45], [2, 1.0], [3, 1.6]]),
#         ('myFourthDataset', [[0, 0.3], [1, 0.83], [2, 0.7], [3, 0.2]]),
#     )
colors = ('#8e450a', '#ea2c2c', '#d7d94b', '#82d064', '#b9dcac', '#0000ff')
colors = ('#9d4c0b', '#cb2626', '#c9cb26', '#55cb26', '#acdcd0', '#67a44f')

# colors = ('#b9dcac', '#0000ff')
options = {
    'legend': {'hide': False},
    'background': {'color': '#000000'},
    'padding': {'left': 0, 'right': 0, 'top': 0, 'bottom': 0},
    'colorScheme': {'name': 'fixed', 'args': {'colors': colors}},
}

chart = pycha.line.LineChart(surface, options)
chart.addDataset(dataSet)
chart.render()
surface.write_to_png('output.png')
