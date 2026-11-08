[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_integers.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.random_integers.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_integers.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.random_integers.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.random_integers.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.random_integers.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.random_integers.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.random_integers.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.random_integers.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.random_integers.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.random_integers.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.random_integers.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.random_integers.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.random_integers.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.random_integers.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.random_integers.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.random_integers.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.random_integers.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.random_integers.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.random_integers.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.random_integers.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.random_integers.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.random\_integers[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_integers.html#numpy-random-random-integers "Link to this heading")

================================================================================================================================================================================

random.random\_integers(_low_, _high\=None_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_integers.html#numpy.random.random_integers "Link to this definition")

Random integers of type [`numpy.int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
 between _low_ and _high_, inclusive.

Return random integers of type [`numpy.int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
 from the “discrete uniform” distribution in the closed interval \[_low_, _high_\]. If _high_ is None (the default), then results are from \[1, _low_\]. The [`numpy.int_`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int_ "numpy.int_")
 type translates to the C long integer type and its precision is platform dependent.

This function has been deprecated. Use randint instead.

Deprecated since version 1.11.0.

Parameters:

**low**int

Lowest (signed) integer to be drawn from the distribution (unless `high=None`, in which case this parameter is the _highest_ such integer).

**high**int, optional

If provided, the largest (signed) integer to be drawn from the distribution (see above for behavior if `high=None`).

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. Default is None, in which case a single value is returned.

Returns:

**out**int or ndarray of ints

[`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")
\-shaped array of random integers from the appropriate distribution, or a single such random int if [`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")
 not provided.

See also

[`randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")

Similar to [`random_integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_integers.html#numpy.random.random_integers "numpy.random.random_integers")
, only for the half-open interval \[_low_, _high_), and 0 is the lowest value if _high_ is omitted.\
\
Notes\
\
To sample from N evenly spaced floating-point numbers between a and b, use:\
\
a + (b \- a) \* (np.random.random\_integers(N) \- 1) / (N \- 1.)\
\
Copy to clipboard\
\
Examples\
\
Try it in your browser!\
\
\>>> np.random.random\_integers(5)\
4 # random\
\>>> type(np.random.random\_integers(5))\
<class 'numpy.int64'>\
\>>> np.random.random\_integers(5, size\=(3,2))\
array(\[\[5, 4\], # random\
       \[3, 3\],\
       \[4, 5\]\])\
\
Copy to clipboard\
\
Choose five random numbers from the set of five evenly-spaced numbers between 0 and 2.5, inclusive (_i.e._, from the set \\({0, 5/8, 10/8, 15/8, 20/8}\\)):\
\
\>>> 2.5 \* (np.random.random\_integers(5, size\=(5,)) \- 1) / 4.\
array(\[ 0.625,  1.25 ,  0.625,  0.625,  2.5  \]) # random\
\
Copy to clipboard\
\
Roll two six sided dice 1000 times and sum the results:\
\
\>>> d1 \= np.random.random\_integers(1, 6, 1000)\
\>>> d2 \= np.random.random\_integers(1, 6, 1000)\
\>>> dsums \= d1 + d2\
\
Copy to clipboard\
\
Display results as a histogram:\
\
\>>> import matplotlib.pyplot as plt\
\>>> count, bins, ignored \= plt.hist(dsums, 11, density\=True)\
\>>> plt.show()\
\
Copy to clipboard\
\
![../../../_images/numpy-random-random_integers-1.png](https://numpy.org/doc/stable/_images/numpy-random-random_integers-1.png)\
\
Go BackOpen In Tab\
\
On this page