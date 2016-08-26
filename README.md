poly-seuils-notes
=================

One of my first project to learn Python scripting language. Parsing of the grades file for a class in Polytechnique Montreal, to extract the thresholds. For example, the threshold for the A grade is 16.81/20. The entry format is the file containing the grades, in either format used at this school which is *txt* or *pdf*. 

The parsing is done by searching the lowest and highest value for each grade.


Execution
---------
The script takes one argument which is the grade file
    $ python main.py foo1001.txt


Example output:
```
32 notes analysees
A* (4): [19.29 , 19.99]
A (4): [16.81 , 18.64]
B+ (4): [14.29 , 15.80]
B (4): [13.77 , 14.25]
C+ (4): [13.34 , 13.59]
C (3): [12.79 , 13.07]
D+ (3): [11.65 , 12.19]
D (3): [10.72 , 11.38]
F (3): [1.29 , 6.33]
```
As the school is completely french-speaking, I did not translate the informations in the output.

Dependecies
-----------

The script is developed with Python 2.7 and using the following module:
  * [PyPDF2](http://mstamy2.github.io/PyPDF2/)


TODO
----
  * Exception handling if module not available
