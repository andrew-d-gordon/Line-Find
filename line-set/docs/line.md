# line.py documentation

**Overview**

line.py contains the Line class as well as a module functions relating to line creation and solving for lines between 
points. The line object serves to provide several pieces of information regarding to a line in one object, these being:
a line id (reduced equation), a string representation of the line function, and individual a, b, and c values relating
to a lines linear equation (these values are utilized in the id and string representations).


# Functions

**def gcd_abc(a, b, c):**
* Usage:
    * Serves to find the gcd of three numeric values. If all a, b, and c equal 0, 1 is returned.

* Return: The gcd of a, b, and c (or 1 if all equal 0)