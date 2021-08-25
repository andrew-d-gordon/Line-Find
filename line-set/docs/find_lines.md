# find_lines.py documentation

**Overview**

find_lines.py contains the primary driver code and functions to process a set of points and return a set of lines which 
cross through a certain threshold of unique points in the set. Lines are returned in a string and reduced linear
equation from which resembles: `ax + by = c`. The reduced form is a tuple resembling: `(a, b, c)`. The lines returned 
from find_unique_lines guarantees each line crosses through at least point_threshold number of points and the set of
points that it crosses through is unique. Discussion and information regarding the line finding algorithm and alternate 
solutions are available in finding_unique_lines function info below.

# Functions

**plot_points(line: tuple, line_dict: dict, graph: plt):**
* Usage:
    * Serves to plot points on a graph for a specific line.

* Return: N/A

**plot_lines(lines: list, l_d: dict, x_bnd: int, y_bnd: int, g_name: str, p_plt: bool):**
* Usage:
    * Serves to plot lines (and points if p_plt is True) on a graph with the specified bounds.

* Return: N/A

**unique_points(p1: tuple, p2: tuple, points_used: dict, f_n_id: tuple, line_d: dict, point_thresh: int):**
* Usage:
    * Helper function to find_unique_lines. Serves to determine whether or not p1 and p2 should be processed in 
    find_unique_lines. If the line between p1 and p2 is unseen, seen but not satisfying of threshold, or if either p1 or
    
    p2 are unseen, the pair is deemed necessary of processing.
* Return: Boolean representing the uniqueness/necessity of the two points within find_unique_lines main loop.

**find_unique_lines(p_set: PointSet, num_points: int, point_thresh: int):**
* Usage:
    * Serves to return the set of lines which pass through point_thresh number of 'unique' points within a set of points 
    represented in p_set. 'unique' in the sense that the set of points which a given, eligible line passes through is
    
    unique. E.g. the point (1,1) could be utilized in lines passing through (1,1), (2,2), (3,3) and (1,1), (1,2), (1,3).

* Line finding algorithm design and runtime:
    * Overview
        * It is effectively a match finding algorithm. The main loop serves to build a dictionary of every line between a 
        unique pair of points; the key of the dict being the line and it's value being a list of points which that line 
        has crossed in the set. During this loop a check is run to see if that newly computed line between a unique pair of 
        points already exists in the dictionary. If the line is unseen, it adds the line to the dictionary with the value 
        being the list containing the points used to compute it. If the line has been seen before, it adds the previously 
        uncrossed points from the pair to it's value, then checks to see if the length of it's crossed points list has 
        reached the point threshold. If so, this line's equation is added to the output lists, if not, the loop continues.
    
    * Runtime
        * During the run of the double loop, it considers every unique pair of two in the set of points.
        This comes out to **n(n-1)/2** (n choose 2) pairs to consider where n is the number of points in the set. This 
        results in an exponential run of `O((n*n-1)/2)` => `O(n*n)`. 
            * This exponential runtime results in some hefty computational times for point sets with large volume and 
            are densely located. The test set unit_tests/test_10000_random_1000 has 10000 coordinate pairs within the 
            bounds (-1000, -1000), (1000,1000). This large number of points with whole numbered coordinates results in 
            lines which cross many points and the amount of unique pairs is immense. Visual outputs on larger point sets
            can be viewed in the unit_tests/unit_tests_output folder where things can get a bit fuzzy. Thankfully on
            less dense inputs the run is relatively swift; optimizations would certainly be necessary if many large 
            volume inputs are the intended use.
    
    * Alternate approaches
        * Other approaches I thought could be possible include finding the bounds of the point sets area, and once
        calculating a line, attempting to make 'smart' guesses about the whereabouts of collisions it makes with other 
        points in the set. I assume this approach generates a similar O(n*n) but on average runs potentially
        saves computation when significant amounts of points have already been marked as used in a line.
    
    * 'Unique'
        * I contemplated the meaning of unique points and settled for this function to serve the purpose of finding 
        lines which cross through a **unique set of points**, as opposed to a **set of unique points** in regards to 
        the point set. The output of this function could be utilized to achieve the goal of only finding lines which 
        satisfy the uniqueness required by **set of unique points**. To achieve this, one could create a recursive 
        function which incrementally builds a candidate set of lines while iterating through each line in the list of 
        lines returned by finding_unique_lines. At each run, if the currently viewed line utilizes points so far unused
        in the set, a recursive call is made with that line added to the set, and a recursive call is made without that
        line added to the set. This find a set representing each permutation of non conflicting lines (each crossing 
        through entirely unique points in the pt set) as well as allow you to choose the largest set of non conflicting 
        lines. O(2^n) as 2^n subsets are technically possible but many recursive calls should be avoided by only making 
        the recursive call with the new line added to the set when it has only unseen points to the set thus far.
        

* Return: Satisfying set of lines as their linear equation strings `['ax + by + c',...]`, and tuples `[(a, b, c),...]`.

**retrieve_point_list(is_file: bool, input_name: str, points: list):**
* Usage:
    * Can parse points from a test file following format in src/unit_tests. If is_file is True and the file at path 
    input_name can be opened for reading, parsing ensues. The desired structure to parse points from is as follows: 
        * `x1 y1\nx2 y2\nx3 y3\n`
        
    * All x and y in the input file must be numeric as they are cast to integers upon creation of the point list.
    Each point is stored into the point list as a tuple (x, y).
    
* Returns: A list of points with the form: `[(x1, y1), ..., (xn, yn)]`. Errors if desired file cannot be opened. 
Returns points if is_file is False.

**supply_arguments(d_test: str = 'input_file_path', d_pt_thr: int = 3, d_plt_g: bool = False, d_b: int = 20):**
* Usage: 
    * Utilized to parse command line arguments specified by the flags -t, -p, -g, -b.
        * -t: path to input file
        * -p: point threshold to meet (in find_unique_lines)
        * -g: 1 or 0 respectively signifying to graph or not to graph results
        * -b: bounds for graph to abide by (b x b dimensions)
        
    * If arguments not supplied, defaults are set for unspecified attributes. If faulty flags are present, errors risen.
        
* Return: Desired arguments needed to run driver code in main.py.

**main**
* Usage:
    * Driver code to retrieve args from supply_arguments, request point list from input file, create PointSet for said 
    points, runs them through find_unique_lines, prints results and if specified graph results.
* Returns: N/A