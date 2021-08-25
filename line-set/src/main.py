from point_set import *
from line import Line
import matplotlib.pyplot as plt


def plot_lines(lines):
    print(max(lines))



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
            p_split = p_raw[:-1].split(' ')  # :-1 splice removes \n
            points.append(tuple([int(p_split[0]), int(p_split[1])]))

    return points


def unique_points(p_1: tuple, p_2: tuple, points_used: dict, f_n_id: tuple, line_d: dict, point_thresh: int):
    """
    :param p_1: the first point of pair in check
    :param p_2: the second point of pair in check
    :param points_used: dictionary of use values for points
    :param f_n_id: id of line made by two points
    :param line_d: dictionary containing all lines found so far
    :param point_thresh: number representing how many points a line must cross through in line_d to be part of output
    :return: boolean True or False (True when p_1, p_2 is unique pair and the line between them has reached threshold)
    """
    try:
        if points_used[p_1] and points_used[p_2] and len(line_d[f_n_id]) >= point_thresh:
            return False
        else:
            return True
    except KeyError:
        return True


def find_unique_lines(p_set: PointSet, point_thresh: int):
    """
    :param p_set: PointSet holding points to process for lines
    :param point_thresh: number of unique points the line must intersect to satisfy
    :return: returns set of lines which intersect satisfiable number of unique points
    """
    line_dict = {}
    points_used = p_set.points_d.copy()
    lines_output = []
    lines_output_str = []

    # Build dict of all lines between unique pairs of points in p_set
    # While computing lines, if: line between new pair == previously found line (and threshold met), add line to output
    for i in range(p_set.size):
        p_1 = p_set.points[i]
        # Look at lines w/points at idx i (p_1) and at idx j=i+1->p_set.size (p_2)
        for j in range(i+1, p_set.size):
            p_2 = p_set.points[j]
            f_n = line_between_points(p_1, p_2)

            if not unique_points(p_1, p_2, points_used, f_n.id, line_dict, point_thresh):
                continue

            # If line exists in dict, append new point to it's val, if len(v)==point_thresh, add line to output
            try:
                pts_crossed = line_dict[f_n.id]
                pts_crossed.append(p_2)
                if len(pts_crossed) == point_thresh:
                    lines_output.append(f_n.id)
                    lines_output_str.append(f_n.line_str)
                    #print("New valid line:", f_n.id, pts_crossed)
            except KeyError:
                # If line not in dict yet, add it,
                line_dict[f_n.id] = [p_1, p_2]

            # Set use of points to True (used)
            points_used[p_1] = True
            points_used[p_2] = True

    # Iterate through all lines
    # print(line_dict)
    print(lines_output)
    return lines_output, lines_output_str


if __name__ == '__main__':
    # Unit test files must be labeled for text content to be parsed
    unit_test_file = 'unit_tests/test_100_random_100'
    pts = retrieve_point_list(True, unit_test_file, [])

    # Create PointSet object from parsed points list
    ps = PointSet(pts)

    # Find unique lines between three or more points within point set
    point_threshold = 3
    three_pt_lines, three_pt_lines_str = find_unique_lines(ps, point_threshold)

    # Graph lines
    plot_lines(three_pt_lines)

