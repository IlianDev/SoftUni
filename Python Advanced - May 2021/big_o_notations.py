"""
https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/

How to calculate in O notation -> O(n)
There are two ways to calculate in O notation:
 1. Space complexity
 2. Time complexity - more important.
 In the Jupyter Notebook, you can use the %timeit literal followed by the
 function call to find the time taken by the function to execute:

 !We should calculate (to bear in mind) the worst scenario!
"""


# O(n) complexity
a = [1, 2, 3, 4]

for el in range(len(a)):
    if el == 2:
        print("Found it")
        break

# O(n^2) complexity
a = [1, 2, 3, 4]

for el in a:
    if isinstance(el, list):
        for inner_el in el:
            pass

