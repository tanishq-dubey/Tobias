
__author__ = 'Martin'

_world = {}

def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t')) # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)