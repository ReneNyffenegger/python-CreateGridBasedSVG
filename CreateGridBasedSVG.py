
class GridLine(object):
    # A GridLine is an indefinitismal thin line that is
    # either horizontal or vertical and runs from one end
    # of a Grid to the other.
    pass

class GridTrack(object):
    # A GridTrak is the space between two adjacent
    # GridLines. Usually, they are referred to as
    # rows or columns.
    pass

class GridCell(object):
    # The GridCell is the intersection of two
    # orthogonal GridTracks. It is the smallest
    # unit with size in a Grid.
    # Note, different GridCells don't necessarly have
    # to have the same rendered size.
    pass

class GridArea(object):
    # A GridArea is bound by 2 different horizontal GridLines
    # and 2 different vertical GridLines.
    # Thus, it's size it at least one GridCell and an exact
    # integer multiple of a GridCell.
    pass


class Grid(object):
    grid_lines_x = [] # Array of GridLine
    grid_lines_y = [] # Array of GridLine
    def __init__(self):
        pass

