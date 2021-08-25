from point_set import *
from line import *
import matplotlib.pyplot as plt
import numpy as np


def plot_points(line: tuple, line_dict: dict, graph: plt):
    """
    :param line: line whose points it crosses should be plotted
    :param line_dict: dict with keys as lines and values as points the lines cross through
    :param graph: graph to plot points on
    :return: None, function serves to plot black points on graph
    """

    points = line_dict[line]
    for p in points:
        graph.plot([p[0]], [p[1]], marker='o', markersize=5, markerfacecolor='black', markeredgecolor='black')


def plot_lines(lines: list, l_d: dict, x_bnd: int = 100, y_bnd: int = 100, g_name: str = '', p_plt: bool = False):
    """
    :param lines: set of lines to be plot (2d, each line specified by tuple (a, b, c) for ax + by = c)
    :param l_d: set of lines with corresponding points which they cross through
    :param x_bnd: desired x bounds for graph, default 100
    :param y_bnd: desired y bounds for graph, default 100
    :param g_name: desired name for plot
    :param p_plt: boolean to decide whether to plot points on graph as well as lines
    :return: None, serves to plot lines on graph and show said graph
    """

    graph = plt
    graph.axis([0-x_bnd, x_bnd, 0-y_bnd, y_bnd])

    # For each line in lines, determine f(x) for each x val within the bounds then plot the line
    for line in lines:
        if line[0] == 0:  # Horizontal lines
            graph.axhline(y=line[2], xmin=0, xmax=1)
        elif line[1] == 0:  # Vertical lines
            graph.axvline(x=line[2], ymin=0, ymax=1)
        else:
            x = np.linspace(0-x_bnd, x_bnd, x_bnd)
            y = [(line[2] - line[0] * v) / line[1] for v in x]  # Solving for f(x) at specified x: y = (c-ax)/b
            graph.plot(x, y)

        # If point plotting is desired, plot corresponding points for line
        if p_plt:
            plot_points(line, l_d, graph)

    # Finish setting graph properties and show graph (add x and y axes, grid lines)
    graph.axhline(y=0, color='k')
    graph.axvline(x=0, color='k')
    graph.grid(True, which='both')
    graph.title(g_name)
    graph.show()


def retrieve_point_list(is_file: bool, input_name: str = '', points: list = []):
    """
    :param input_name: name of input file (if using unit test)
    :param is_file: boolean for if input should be from input_name file or from points param
    :param points: list of points if testing in code input
    :return: returns list of points of form [(x1,y1), ..., (xn,yn)]
    """

    if not is_file:
        return points

    with open(input_name, 'r') as f:
        content = f.readlines()
        for p_raw in content:
            p_split = p_raw[:-1].split(' ')  # [:-1) splice removes \n
            if p_split[0] is not None and p_split[1] is not None:
                points.append(tuple([int(p_split[0]), int(p_split[1])]))

    return points


def unique_points(p1: tuple, p2: tuple, points_used: dict, f_n_id: tuple, line_d: dict, point_thresh: int):
    """
    :param p1: the first point of pair in check
    :param p2: the second point of pair in check
    :param points_used: dictionary of use values for points
    :param f_n_id: id of line made by two points
    :param line_d: dictionary containing all lines found so far
    :param point_thresh: number representing how many points a line must cross through in line_d to be part of output
    :return: boolean True or False (True when p_1, p_2 is unique pair and the line between them has reached threshold)
    """
    try:
        if points_used[p1] and points_used[p2] and len(line_d[f_n_id]) >= point_thresh:
            return False
        else:
            return True
    except KeyError:
        return True


def find_unique_lines(p_set: PointSet, num_points: int, point_thresh: int):
    """
    :param p_set: PointSet holding points to process for lines
    :param num_points: number of points to be evaluated (p_set.size)
    :param point_thresh: number of unique points the line must intersect to satisfy
    :return: returns set of lines which intersect satisfiable number (point_thresh) of unique points (UNIQUE SET)
    """
    line_dict = {}
    points_used = p_set.points_d.copy()
    lines_output = []
    str_lines_output = []

    # Build dict of all lines between unique pairs of points in p_set
    # While computing lines, if: line between new pair == previously found line (and threshold met), add line to output
    for i in range(num_points):
        p1 = p_set.points[i]

        # Look at lines between points at idx i (p1) and at idx j=i+1->num_points (p2)
        for j in range(i+1, num_points):
            p2 = p_set.points[j]
            f_n = line_between_points(p1, p2)

            if not unique_points(p1, p2, points_used, f_n.id, line_dict, point_thresh):
                continue

            # If line exists in dict, append new point to crossed point list
            try:
                pts_crossed = line_dict[f_n.id]
                pts_crossed.append(p2)
                if len(pts_crossed) == point_thresh:  # If line crosses through point_thresh points, add to output
                    lines_output.append(f_n.id)
                    str_lines_output.append(f_n.line_str)
            except KeyError:
                # Add line to dict as it is new
                line_dict[f_n.id] = [p1, p2]

            # Set use of points p1 and p2 to True (used)
            points_used[p1] = True
            points_used[p2] = True

    # Iterate through all lines
    return lines_output, str_lines_output, line_dict


if __name__ == '__main__':
    # Unit test files be textual to be parsed (.read() specs)
    unit_test_file = 'unit_tests/test_100_random_100'
    pts = retrieve_point_list(True, unit_test_file, [])

    # Create PointSet object from derived pts list
    ps = PointSet(pts)

    # Find unique lines between three or more points within point set
    point_threshold = 3
    pt_lines, pt_str_lines, all_line_dict = find_unique_lines(ps, ps.size, point_threshold)
    print("Lines which cross three points from input set:\n" + str(pt_lines) + '\n' + str(pt_str_lines))

    # Graph lines (or points, p_plt=True) in bounded space
    bounds = 110
    plot_lines(pt_lines, all_line_dict, bounds, bounds, unit_test_file.split('/')[1], p_plt=True)
