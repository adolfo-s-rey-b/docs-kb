[Skip to main content](https://numpy.org/doc/stable/reference/arrays.nditer.cython.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/arrays.nditer.cython.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/arrays.nditer.cython.html)
[2.4](https://numpy.org/doc/2.4/reference/arrays.nditer.cython.html)
[2.3](https://numpy.org/doc/2.3/reference/arrays.nditer.cython.html)
[2.2](https://numpy.org/doc/2.2/reference/arrays.nditer.cython.html)
[2.1](https://numpy.org/doc/2.1/reference/arrays.nditer.cython.html)
[2.0](https://numpy.org/doc/2.0/reference/arrays.nditer.cython.html)
[1.26](https://numpy.org/doc/1.26/reference/arrays.nditer.cython.html)
[1.25](https://numpy.org/doc/1.25/reference/arrays.nditer.cython.html)
[1.24](https://numpy.org/doc/1.24/reference/arrays.nditer.cython.html)
[1.23](https://numpy.org/doc/1.23/reference/arrays.nditer.cython.html)
[1.22](https://numpy.org/doc/1.22/reference/arrays.nditer.cython.html)
[1.21](https://numpy.org/doc/1.21/reference/arrays.nditer.cython.html)
[1.20](https://numpy.org/doc/1.20/reference/arrays.nditer.cython.html)
[1.19](https://numpy.org/doc/1.19/reference/arrays.nditer.cython.html)
[1.18](https://numpy.org/doc/1.18/reference/arrays.nditer.cython.html)
[1.17](https://numpy.org/doc/1.17/reference/arrays.nditer.cython.html)
[1.16](https://numpy.org/doc/1.16/reference/arrays.nditer.cython.html)
[1.15](https://numpy.org/doc/1.15/reference/arrays.nditer.cython.html)
[1.14](https://numpy.org/doc/1.14/reference/arrays.nditer.cython.html)
[1.13](https://numpy.org/doc/1.13/reference/arrays.nditer.cython.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Putting the inner loop in Cython[#](https://numpy.org/doc/stable/reference/arrays.nditer.cython.html#putting-the-inner-loop-in-cython "Link to this heading")

==============================================================================================================================================================

Those who want really good performance out of their low level operations should strongly consider directly using the iteration API provided in C, but for those who are not comfortable with C or C++, Cython is a good middle ground with reasonable performance tradeoffs. For the [`nditer`](https://numpy.org/doc/stable/reference/generated/numpy.nditer.html#numpy.nditer "numpy.nditer")
 object, this means letting the iterator take care of broadcasting, dtype conversion, and buffering, while giving the inner loop to Cython.

For our example, we’ll create a sum of squares function. To start, let’s implement this function in straightforward Python. We want to support an ‘axis’ parameter similar to the numpy [`sum`](https://docs.python.org/3/library/functions.html#sum "(in Python v3.14)")
 function, so we will need to construct a list for the _op\_axes_ parameter. Here’s how this looks.

Example

\>>> def axis\_to\_axeslist(axis, ndim):
...     if axis is None:
...         return \[\-1\] \* ndim
...     else:
...         if type(axis) is not tuple:
...             axis \= (axis,)
...         axeslist \= \[1\] \* ndim
...         for i in axis:
...             axeslist\[i\] \= \-1
...         ax \= 0
...         for i in range(ndim):
...             if axeslist\[i\] != \-1:
...                 axeslist\[i\] \= ax
...                 ax += 1
...         return axeslist
...
\>>> def sum\_squares\_py(arr, axis\=None, out\=None):
...     axeslist \= axis\_to\_axeslist(axis, arr.ndim)
...     it \= np.nditer(\[arr, out\], flags\=\['reduce\_ok',\
...                                       'buffered', 'delay\_bufalloc'\],
...                 op\_flags\=\[\['readonly'\], \['readwrite', 'allocate'\]\],
...                 op\_axes\=\[None, axeslist\],
...                 op\_dtypes\=\['float64', 'float64'\])
...     with it:
...         it.operands\[1\]\[...\] \= 0
...         it.reset()
...         for x, y in it:
...             y\[...\] += x\*x
...         return it.operands\[1\]
...
\>>> a \= np.arange(6).reshape(2,3)
\>>> sum\_squares\_py(a)
array(55.)
\>>> sum\_squares\_py(a, axis\=-1)
array(\[  5.,  50.\])

Copy to clipboard

To Cython-ize this function, we replace the inner loop (y\[…\] += x\*x) with Cython code that’s specialized for the float64 dtype. With the ‘external\_loop’ flag enabled, the arrays provided to the inner loop will always be one-dimensional, so very little checking needs to be done.

Here’s the listing of sum\_squares.pyx:

import numpy as np
cimport numpy as np
cimport cython

def axis\_to\_axeslist(axis, ndim):
    if axis is None:
        return \[\-1\] \* ndim
    else:
        if type(axis) is not tuple:
            axis \= (axis,)
        axeslist \= \[1\] \* ndim
        for i in axis:
            axeslist\[i\] \= \-1
        ax \= 0
        for i in range(ndim):
            if axeslist\[i\] != \-1:
                axeslist\[i\] \= ax
                ax += 1
        return axeslist

@cython.boundscheck(False)
def sum\_squares\_cy(arr, axis\=None, out\=None):
    cdef np.ndarray\[double\] x
    cdef np.ndarray\[double\] y
    cdef int size
    cdef double value

    axeslist \= axis\_to\_axeslist(axis, arr.ndim)
    it \= np.nditer(\[arr, out\], flags\=\['reduce\_ok', 'external\_loop',\
                                      'buffered', 'delay\_bufalloc'\],
                op\_flags\=\[\['readonly'\], \['readwrite', 'allocate'\]\],
                op\_axes\=\[None, axeslist\],
                op\_dtypes\=\['float64', 'float64'\])
    with it:
        it.operands\[1\]\[...\] \= 0
        it.reset()
        for xarr, yarr in it:
            x \= xarr
            y \= yarr
            size \= x.shape\[0\]
            for i in range(size):
               value \= x\[i\]
               y\[i\] \= y\[i\] + value \* value
        return it.operands\[1\]

Copy to clipboard

On this machine, building the .pyx file into a module looked like the following, but you may have to find some Cython tutorials to tell you the specifics for your system configuration.:

$ cython sum\_squares.pyx
$ gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -I/usr/include/python2.7 -fno-strict-aliasing -o sum\_squares.so sum\_squares.c

Copy to clipboard

Running this from the Python interpreter produces the same answers as our native Python/NumPy code did.

Example

\>>> from sum\_squares import sum\_squares\_cy 
\>>> a \= np.arange(6).reshape(2,3)
\>>> sum\_squares\_cy(a) 
array(55.0)
\>>> sum\_squares\_cy(a, axis\=-1) 
array(\[  5.,  50.\])

Copy to clipboard

Doing a little timing in IPython shows that the reduced overhead and memory allocation of the Cython inner loop is providing a very nice speedup over both the straightforward Python code and an expression using NumPy’s built-in sum function.:

\>>> a \= np.random.rand(1000,1000)

\>>> timeit sum\_squares\_py(a, axis\=-1)
10 loops, best of 3: 37.1 ms per loop

\>>> timeit np.sum(a\*a, axis\=-1)
10 loops, best of 3: 20.9 ms per loop

\>>> timeit sum\_squares\_cy(a, axis\=-1)
100 loops, best of 3: 11.8 ms per loop

\>>> np.all(sum\_squares\_cy(a, axis\=-1) \== np.sum(a\*a, axis\=-1))
True

\>>> np.all(sum\_squares\_py(a, axis\=-1) \== np.sum(a\*a, axis\=-1))
True

Copy to clipboard