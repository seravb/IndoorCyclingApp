import cairo
# from pycha import bar
import pycha
import pycha.bar

width, height = (800, 800)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
dataSet = (
    ('dataSet 1', ((0, 1), (1, 3), (2, 2.5))),
    ('', ((1, 2), (2, 0.5))),
    # ('dataSet 2', ((0, 2), (1, 4), (2, 3))),
    # ('dataSet 3', ((0, 5), (1, 1), (2, 0.5))),
)
dataSet2 = (
    ('d1', )
)
options = {
    'legend': {'hide': False},
    'background': {'color': '#f0f0f0'},
    'padding': {'left': 0, 'right': 0, 'top': 5, 'bottom': 5}
}

chart = pycha.bar.VerticalBarChart(surface, options)
chart.addDataset(dataSet)
chart.render()
surface.write_to_png('output.png')