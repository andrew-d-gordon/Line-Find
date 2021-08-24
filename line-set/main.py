
def retrieve_point_list(is_file: bool, input_name: str = '', points: list = []):
    """
    :param input_name: name of input file (if using unit test)
    :param is_file: boolean for if input should be from input_name file or from points param
    :param points: list of points if testing in code input
    :return: returns list of points of form [(x1,y1), ..., (xn,yn)]
    """

    if not is_file:
        return points

    print("This is input_name:", input_name, points, is_file)

    with open(input_name, 'r') as f:
        content = f.readlines()
        for p_raw in content:
            p_split = p_raw[:-1].split(' ')  # :-1 splice removes \n
            points.append(tuple([int(p_split[0]), int(p_split[1])]))

    return points


if __name__ == '__main__':
    # Unit test files must be labeled for text content to be parsed
    unit_test_file = 'unit_tests/test_3_set_3'
    pts = retrieve_point_list(True, unit_test_file, [])
    print(pts)

    p_s = PointSet(pts)
    for i in range(p_s.size):
        j = i + 1
        p_1 = p_s.points[i]
        while j < p_s.size:
            p_2 = p_s.points[j]
            print(p_s.line_between_points(p_1, p_2))
            j += 1