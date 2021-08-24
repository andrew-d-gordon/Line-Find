from math import gcd


def gcd_abc(a, b, c):
    line_var_gcd = gcd(gcd(a, b), c)
    if line_var_gcd == 0:
        return 1
    return line_var_gcd


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

    def print_line_slope(self):
        print(self.slope)