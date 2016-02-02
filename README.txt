Development of structural and technological scheme of industrial robot

The requirement to run the program:
Python 3 https://www.python.org/downloads/
library NumPy for Python 3 http://sourceforge.net/projects/numpy/files/NumPy/1.9.2/
library Graphviz

The contents of the program:
    gks.py
    gks4.py
    main.py
    matrix.txt
    scheme.py

Example program call for the construction of a square matrix: 
Input data:
Т1 Ф1 Ф2 Т2 С1 С2 Ф3 Т3 Т2 Т4 С1 Ф1 С2 Р2
Т3 Т2 С1 С2 Ф1 Р2 Т1 Т3 Т2 Т4 С2 Р2
Т4 Т3 Т2 С1 С2 Ф1 Т5 Т1 Т3 Т2 Т4
Т2 С1 С2 Ф1 Ф2 Р2 Т1 С2 Т3 Т2 Т4 С1 Ф1
Т2 С1 С2 Т3 Т4 Т1 С2 Р2 Т3 Т2 Т4
Т3 Т4 Ф2 Р2 Т2 С1 С2 Т1 С1 Ф1 Т3 Т2 Т4
Т2 С1 С2 Т4 Т3 Т2 Т4 С2 Р2

Output matrix:
[[ 0  9  7 10  8 10  7]
 [ 9  0  9 10 10 10  9]
 [ 7  9  0  8  8  8  7]
 [10 10  8  0  9 11  8]
 [ 8 10  8  9  0  9 10]
 [10 10  8 11  9  0  8]
 [ 7  9  7  8 10  8  0]]