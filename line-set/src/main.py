from point_set import *
from find_lines_through_points import *
import sys
import getopt


def supply_arguments(d_test: str = 'unit_tests/test_3_set_3', d_pt_thr: int = 3, d_plt_g: bool = False, d_b: int = 20):
    """
    supply_arguments is able to provide a file name, point threshold, and graphing flags for main.
    It does so by attempting to parse the CLI arguments by these flags:
    -t: test file name
    -p: point threshold (1 for graph desired, 0 for graph not desired)
    -g: plot graph of results boolean
    -b: bounds for said graph

    Example CLI run of this program:
    'python main.py -t unit_tests/test_3_set_3 -p 3 -g 1 -b 100'

    :param d_test: default test file to utilize if none supplied
    :param d_pt_thr: default point threshold if none supplied
    :param d_plt_g: default boolean decision for plotting graph when none supplied
    :param d_b: default bounds for graph to plot on
    :return: returns necessary arguments to find test file, process test data, and optional graph flags to be set
    """

    file_name = pt_thresh = plt_graph = graph_bounds = None

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "t:p:g:b:")
        for opt, arg in opts:
            if opt == '-t':
                file_name = str(arg)
            elif opt == '-p':
                pt_thresh = int(arg)
            elif opt == '-g':
                plt_graph = bool(arg)
            elif opt == '-b':
                graph_bounds = int(arg)
    except getopt.GetoptError:
        print('Error in processing command line arguments.')
        print("Example use: python main.py -t unit_tests/test_3_set_3 -p 3 -g 1 -b 10")
        sys.exit(1)

    if file_name is None:
        file_name = d_test
    if pt_thresh is None:
        pt_thresh = d_pt_thr
    if plt_graph is None:
        plt_graph = d_plt_g
    if graph_bounds is None:
        graph_bounds = d_b

    return file_name, pt_thresh, plt_graph, graph_bounds


if __name__ == '__main__':
    # Retrieve test file name and other vars from CLI/defaults
    test_file, point_threshold, plot_graph, bounds = supply_arguments()
    set_points = []  # Supply own set of points here if desired. [(x1, y1), ..., (xn, yn)]

    # Unit test files be textual to be parsed (.read() specs)
    pts = retrieve_point_list(True, test_file, set_points)

    # Create PointSet object from derived pts list
    ps = PointSet(pts)

    # Find unique lines between three or more points within point set
    pt_lines, pt_str_lines, all_line_dict = find_unique_lines(ps, ps.size, point_threshold)
    print("-------------------\nFinished processing.")
    print("Below are lines which crossed {0} or more points from the test data.".format(point_threshold))
    print("Linear equation form: " + str(pt_str_lines))
    print("Reduced linear equation form: " + str(pt_lines))

    # Graph lines (or points, p_plt=True) in bounded space
    if plot_graph and len(pt_lines) > 0:
        plot_lines(pt_lines, all_line_dict, bounds, bounds, test_file.split('/')[-1], p_plt=True)

    sys.exit(0)
