# Find Lines Through Points
This project serves as a library of code for finding lines that cross through a number of unique points within a set of 
points. The driver code within find_lines.py utilizes the other modules within src/ in order to achieve it's 
functionality. It is best to set several flags which specify an input file and the threshold of how many points a line 
must cross through. More information on available functions, objects, and the line finding algorithm can be found in the 
[docs](https://github.com/andrew-d-gordon/coding-challenges/tree/main/line-set/docs) folder.

Here is an example of how to run the program using unit_tests/test_9_set_9 as input. (As run from within src/)

`python find_lines.py -t unit_tests/test_9_set_9 -p 3 -g 1 -b 12`

* -t: specifies the name of the test file to pull point data from
* -p: specifies the point threshold to be reached
* -g: specifies whether or not the results should be plotted (1 for yes, 0 for no)
* -b: specifies the bounds which the output graph should have (b x b dimensions)

**Contents of units_tests/test_9_set_9:**

`1 1`

`2 2`

`3 3`

`1 4`

`2 5`

`3 6`

`1 7`

`2 8`

`3 9`

**Output graph and corresponding lines for test_9_set_9:**
![alt_text](https://github.com/andrew-d-gordon/coding-challenges/blob/main/line-set/src/unit_tests/unit_tests_output/unique_set_test_9_set_9_graph.png?raw=true)
 * -1.0x + 1.0y = 0.0

 * 1.0x + 0.0y = 1.0
  
 * -4.0x + 1.0y = -3.0
 
 * 1.0x + 0.0y = 2.0 

 * 2.0x + 1.0y = 9.0
 
 * 1.0x + 0.0y = 3.0 
 
 * -1.0x + 1.0y = 3.0
 
 * -1.0x + 1.0y = 6.0