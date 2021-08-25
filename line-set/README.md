# Find Lines Through Points
This project serves as a library of code for the purpose of finding lines that cross through a number of unique points 
from a set of points. The driver code within find_lines.py utilizes the other modules within src/ in order to achieve 
it's functionality. It is run with several flags which can be utilized to specify an input file and the threshold of how
many points a line must cross through.

Here is an example of how to run the program using unit_tests/test_9_set_9 as input. (As run from within src/)

`python find_lines.py -t unit_tests/test_9_set_9 -p 3 -g 1 -b 10`

* -t: specifies the name of the test file to pull point data from
* -p: specifies the point threshold to be reached
* -g: specifies whether or not the results should be plotted (1 for yes, 0 for no)
* -b: specifies the x,y bounds which the output graph should have

units_tests/test_9_set_9: 

`1 1`

`2 2`

`3 3`

`1 4`

`2 5`

`3 6`

`1 7`

`2 8`

`3 9`


![alt_text](https://github.com/andrew-d-gordon/coding-challenges/blob/main/line-set/src/unit_tests/unit_tests_output/unique_set_test_9_set_9_graph.png?raw=true)

