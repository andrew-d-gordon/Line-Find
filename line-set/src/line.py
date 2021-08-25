from math import gcd


def gcd_abc(a, b, c):
    """
    :param a: number representing a in ax + by = c
    :param b: number representing b in ax + by = c
    :param c: number representing c in ax + by = c
    :return: returns gcd of the three values (returns 1 if a,b,c = 0)
    """
    line_var_gcd = gcd(gcd(a, b), c)
    if line_var_gcd == 0:
        return 1
    return line_var_gcd


def line_between_points(p1: tuple, p2: tuple):
    """
    :param p1: first point (x1, y1)
    :param p2: second point (x2, y2)
    :return: line object representing f(n) line which spans p1->p2
    """

    a = p2[1]-p1[1]
    b = p1[0]-p2[0]
    c = a*p1[0] + b*p1[1]
    f_n = Line(a, b, c)

    return f_n


class Line:

    def __init__(self, a, b, c):
        gcd_vars = gcd_abc(a, b, c)
        self.a = a/gcd_vars
        self.b = b/gcd_vars
        self.c = c/gcd_vars
        self.id = tuple([self.a, self.b, self.c])

        # Lines follow equation by ax1 + by1 = c where a = (y2-y1) and b = (x2-x1)
        self.line_format = '{0}x + {1}y = {2}'
        self.line_str = self.line_format.format(self.a, self.b, self.c)

    def print_line(self):
        print(self.line_str)
