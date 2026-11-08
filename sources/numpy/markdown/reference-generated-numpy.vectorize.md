[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.vectorize.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.vectorize.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.vectorize.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.vectorize.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.vectorize.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.vectorize.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.vectorize.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.vectorize.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.vectorize.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.vectorize.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.vectorize.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.vectorize.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.vectorize.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.vectorize.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.vectorize.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.vectorize.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.vectorize.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.vectorize.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.vectorize.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.vectorize.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.vectorize[#](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy-vectorize "Link to this heading")

=================================================================================================================================

_class_ numpy.vectorize(_pyfunc\=np.\_NoValue_, _otypes\=None_, _doc\=None_, _excluded\=None_, _cache\=False_, _signature\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L2278-L2679)
[#](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy.vectorize "Link to this definition")

Returns an object that acts like pyfunc, but takes arrays as input.

Define a vectorized function which takes a nested sequence of objects or numpy arrays as inputs and returns a single numpy array or a tuple of numpy arrays. The vectorized function evaluates _pyfunc_ over successive tuples of the input arrays like the python map function, except it uses the broadcasting rules of numpy.

The data type of the output of _vectorized_ is determined by calling the function with the first element of the input. This can be avoided by specifying the _otypes_ argument.

Parameters:

**pyfunc**callable, optional

A python function or method. Can be omitted to produce a decorator with keyword arguments.

**otypes**str or list of dtypes, optional

The output data type. It must be specified as either a string of typecode characters or a list of data type specifiers. There should be one data type specifier for each output.

**doc**str, optional

The docstring for the function. If None, the docstring will be the `pyfunc.__doc__`.

**excluded**set, optional

Set of strings or integers representing the positional or keyword arguments for which the function will not be vectorized. These will be passed directly to _pyfunc_ unmodified.

**cache**bool, optional

If neither _otypes_ nor _signature_ are provided, and _cache_ is `True`, then cache the number of outputs.

**signature**string, optional

Generalized universal function signature, e.g., `(m,n),(n)->(m)` for vectorized matrix-vector multiplication. If provided, `pyfunc` will be called with (and expected to return) arrays with shapes given by the size of corresponding core dimensions. By default, `pyfunc` is assumed to take scalars as input and output.

Methods

|     |     |
| --- | --- |
| [`__call__`](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.__call__.html#numpy.vectorize.__call__ "numpy.vectorize.__call__")<br>(\*args, \*\*kwargs) | Call self as a function. |

Returns:

**out**callable

A vectorized function if `pyfunc` was provided, a decorator otherwise.

See also

[`frompyfunc`](https://numpy.org/doc/stable/reference/generated/numpy.frompyfunc.html#numpy.frompyfunc "numpy.frompyfunc")

Takes an arbitrary Python function and returns a ufunc

Notes

The [`vectorize`](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy.vectorize "numpy.vectorize")
 function is provided primarily for convenience, not for performance. The implementation is essentially a for loop.

If neither _otypes_ nor _signature_ are specified, then a call to the function with the first argument will be used to determine the number of outputs. The results of this call will be cached if _cache_ is _True_ to prevent calling the function twice. However, to implement the cache, the original function must be wrapped which will slow down subsequent calls, so only do this if your function is expensive.

The new keyword argument interface and _excluded_ argument support further degrades performance.

References

\[1\]

[Generalized universal function API](https://numpy.org/doc/stable/reference/c-api/generalized-ufuncs.html)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> def myfunc(a, b):
...     "Return a-b if a>b, otherwise return a+b"
...     if a \> b:
...         return a \- b
...     else:
...         return a + b

Copy to clipboard

\>>> vfunc \= np.vectorize(myfunc)
\>>> vfunc(\[1, 2, 3, 4\], 2)
array(\[3, 4, 1, 2\])

Copy to clipboard

The docstring is taken from the input function to [`vectorize`](https://numpy.org/doc/stable/reference/generated/numpy.vectorize.html#numpy.vectorize "numpy.vectorize")
 unless it is specified:

\>>> vfunc.\_\_doc\_\_
'Return a-b if a>b, otherwise return a+b'
\>>> vfunc \= np.vectorize(myfunc, doc\='Vectorized \`myfunc\`')
\>>> vfunc.\_\_doc\_\_
'Vectorized \`myfunc\`'

Copy to clipboard

The output type is determined by evaluating the first element of the input, unless it is specified:

\>>> out \= vfunc(\[1, 2, 3, 4\], 2)
\>>> type(out\[0\])
<class 'numpy.int64'>
\>>> vfunc \= np.vectorize(myfunc, otypes\=\[float\])
\>>> out \= vfunc(\[1, 2, 3, 4\], 2)
\>>> type(out\[0\])
<class 'numpy.float64'>

Copy to clipboard

The _excluded_ argument can be used to prevent vectorizing over certain arguments. This can be useful for array-like arguments of a fixed length such as the coefficients for a polynomial as in [`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")
:

\>>> def mypolyval(p, x):
...     \_p \= list(p)
...     res \= \_p.pop(0)
...     while \_p:
...         res \= res\*x + \_p.pop(0)
...     return res

Copy to clipboard

Here, we exclude the zeroth argument from vectorization whether it is passed by position or keyword.

\>>> vpolyval \= np.vectorize(mypolyval, excluded\={0, 'p'})
\>>> vpolyval(\[1, 2, 3\], x\=\[0, 1\])
array(\[3, 6\])
\>>> vpolyval(p\=\[1, 2, 3\], x\=\[0, 1\])
array(\[3, 6\])

Copy to clipboard

The _signature_ argument allows for vectorizing functions that act on non-scalar arrays of fixed length. For example, you can use it for a vectorized calculation of Pearson correlation coefficient and its p-value:

\>>> import scipy.stats
\>>> pearsonr \= np.vectorize(scipy.stats.pearsonr,
...                 signature\='(n),(n)->(),()')
\>>> pearsonr(\[\[0, 1, 2, 3\]\], \[\[1, 2, 3, 4\], \[4, 3, 2, 1\]\])
(array(\[ 1., -1.\]), array(\[ 0.,  0.\]))

Copy to clipboard

Or for a vectorized convolution:

\>>> convolve \= np.vectorize(np.convolve, signature\='(n),(m)->(k)')
\>>> convolve(np.eye(4), \[1, 2, 1\])
array(\[\[1., 2., 1., 0., 0., 0.\],\
       \[0., 1., 2., 1., 0., 0.\],\
       \[0., 0., 1., 2., 1., 0.\],\
       \[0., 0., 0., 1., 2., 1.\]\])

Copy to clipboard

Decorator syntax is supported. The decorator can be called as a function to provide keyword arguments:

\>>> @np.vectorize
... def identity(x):
...     return x
...
\>>> identity(\[0, 1, 2\])
array(\[0, 1, 2\])
\>>> @np.vectorize(otypes\=\[float\])
... def as\_float(x):
...     return x
...
\>>> as\_float(\[0, 1, 2\])
array(\[0., 1., 2.\])

Copy to clipboard

Go BackOpen In Tab

On this page