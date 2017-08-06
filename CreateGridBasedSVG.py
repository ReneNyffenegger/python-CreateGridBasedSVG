
class GridLine(object):
    # A GridLine is an indefinitismal thin line that is
    # either horizontal or vertical and runs from one end
    # of a Grid to the other.

    def __init__(self, dist):
        self.dist = dist
        
class GridLines(object):
    # GridLines is an array of GridLine
    def __init__(self):
        self.cur_dist   = 0
        self.grid_lines = []

    def addGridLine(self):
        self.cur_dist += 30
        grid_line = GridLine(self.cur_dist)
        self.grid_lines.append(grid_line)
        return grid_line

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
    grid_lines_x = GridLines()
    grid_lines_y = GridLines()
    def __init__(self):
        pass

    def _addGridLine(self, grid_lines_):
        return grid_lines_.addGridLine()

    def add_x(self):
        return self._addGridLine(self.grid_lines_x)

    def add_y(self):
        return self._addGridLine(self.grid_lines_y)

    def createSVG(self, name):
        f_svg = open(name, "w")

