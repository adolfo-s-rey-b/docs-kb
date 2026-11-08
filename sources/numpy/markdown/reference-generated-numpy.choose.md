[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.choose.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.choose.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.choose.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.choose.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.choose.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.choose.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.choose.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.choose.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.choose.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.choose.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.choose.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.choose.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.choose.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.choose.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.choose.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.choose.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.choose.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.choose.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.choose.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.choose.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.choose.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.choose[#](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy-choose "Link to this heading")

========================================================================================================================

numpy.choose(_a_, _choices_, _out\=None_, _mode\='raise'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L308-L430)
[#](https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy.choose "Link to this definition")

Construct an array from an index array and a list of arrays to choose from.

First of all, if confused or uncertain, definitely look at the Examples - in its full generality, this function is less simple than it might seem from the following code description:

np.choose(a,c) \== np.array(\[c\[a\[I\]\]\[I\] for I in np.ndindex(a.shape)\])

Copy to clipboard

But this omits some subtleties. Here is a fully general summary:

Given an “index” array (_a_) of integers and a sequence of `n` arrays (_choices_), _a_ and each choice array are first broadcast, as necessary, to arrays of a common shape; calling these _Ba_ and _Bchoices\[i\], i = 0,…,n-1_ we have that, necessarily, `Ba.shape == Bchoices[i].shape` for each `i`. Then, a new array with shape `Ba.shape` is created as follows:

*   if `mode='raise'` (the default), then, first of all, each element of `a` (and thus `Ba`) must be in the range `[0, n-1]`; now, suppose that `i` (in that range) is the value at the `(j0, j1, ..., jm)` position in `Ba` - then the value at the same position in the new array is the value in `Bchoices[i]` at that same position;
    
*   if `mode='wrap'`, values in _a_ (and thus _Ba_) may be any (signed) integer; modular arithmetic is used to map integers outside the range _\[0, n-1\]_ back into that range; and then the new array is constructed as above;
    
*   if `mode='clip'`, values in _a_ (and thus `Ba`) may be any (signed) integer; negative integers are mapped to 0; values greater than `n-1` are mapped to `n-1`; and then the new array is constructed as above.
    

Parameters:

**a**int array

This array must contain integers in `[0, n-1]`, where `n` is the number of choices, unless `mode=wrap` or `mode=clip`, in which cases any integers are permissible.

**choices**sequence of arrays

Choice arrays. _a_ and all of the choices must be broadcastable to the same shape. If _choices_ is itself an array (not recommended), then its outermost dimension (i.e., the one corresponding to `choices.shape[0]`) is taken as defining the “sequence”.

**out**array, optional

If provided, the result will be inserted into this array. It should be of the appropriate shape and dtype. Note that _out_ is always buffered if `mode='raise'`; use other modes for better performance.

**mode**{‘raise’ (default), ‘wrap’, ‘clip’}, optional

Specifies how indices outside `[0, n-1]` will be treated:

*   ‘raise’ : an exception is raised
    
*   ‘wrap’ : value becomes value mod `n`
    
*   ‘clip’ : values < 0 are mapped to 0, values > n-1 are mapped to n-1
    

Returns:

**merged\_array**array

The merged result.

Raises:

ValueError: shape mismatch

If _a_ and each choice array are not all broadcastable to the same shape.

See also

[`ndarray.choose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.choose.html#numpy.ndarray.choose "numpy.ndarray.choose")

equivalent method

[`numpy.take_along_axis`](https://numpy.org/doc/stable/reference/generated/numpy.take_along_axis.html#numpy.take_along_axis "numpy.take_along_axis")

Preferable if _choices_ is an array

Notes

To reduce the chance of misinterpretation, even though the following “abuse” is nominally supported, _choices_ should neither be, nor be thought of as, a single array, i.e., the outermost sequence-like container should be either a list or a tuple.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> choices \= \[\[0, 1, 2, 3\], \[10, 11, 12, 13\],\
...   \[20, 21, 22, 23\], \[30, 31, 32, 33\]\]
\>>> np.choose(\[2, 3, 1, 0\], choices
... \# the first element of the result will be the first element of the
... \# third (2+1) "array" in choices, namely, 20; the second element
... \# will be the second element of the fourth (3+1) choice array, i.e.,
... \# 31, etc.
... )
array(\[20, 31, 12,  3\])
\>>> np.choose(\[2, 4, 1, 0\], choices, mode\='clip') \# 4 goes to 3 (4-1)
array(\[20, 31, 12,  3\])
\>>> \# because there are 4 choice arrays
\>>> np.choose(\[2, 4, 1, 0\], choices, mode\='wrap') \# 4 goes to (4 mod 4)
array(\[20,  1, 12,  3\])
\>>> \# i.e., 0

Copy to clipboard

A couple examples illustrating how choose broadcasts:

\>>> a \= \[\[1, 0, 1\], \[0, 1, 0\], \[1, 0, 1\]\]
\>>> choices \= \[\-10, 10\]
\>>> np.choose(a, choices)
array(\[\[ 10, -10,  10\],\
       \[-10,  10, -10\],\
       \[ 10, -10,  10\]\])

Copy to clipboard

\>>> \# With thanks to Anne Archibald
\>>> a \= np.array(\[0, 1\]).reshape((2,1,1))
\>>> c1 \= np.array(\[1, 2, 3\]).reshape((1,3,1))
\>>> c2 \= np.array(\[\-1, \-2, \-3, \-4, \-5\]).reshape((1,1,5))
\>>> np.choose(a, (c1, c2)) \# result is 2x3x5, res\[0,:,:\]=c1, res\[1,:,:\]=c2
array(\[\[\[ 1,  1,  1,  1,  1\],\
        \[ 2,  2,  2,  2,  2\],\
        \[ 3,  3,  3,  3,  3\]\],\
       \[\[-1, -2, -3, -4, -5\],\
        \[-1, -2, -3, -4, -5\],\
        \[-1, -2, -3, -4, -5\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page