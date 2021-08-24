from line import Line


def line_between_points(p1: tuple, p2: tuple):
    """
    :param p1: p1 is the first point (x1, y1)
    :param p2: p2 is the second point (x2, y2)
    :return: line object representing f(n) line which spans p1->p2
    """

    a = p2[1]-p1[1]
    b = p1[0]-p2[0]
    c = a*p1[0] + b*p1[1]
    f_n = Line(a, b, c)

    return f_n


class PointSet:

    def __init__(self, points):
        self.points = points
        self.points_d = {}
        self.size = len(points)

        # Init points in point dictionary
        for p in points:
            self.points_d[p] = None

    def print_points(self):
        print(self.points_d)
