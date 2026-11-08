[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.tensordot.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.tensordot.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.tensordot.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.tensordot.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.tensordot.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.tensordot.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.tensordot.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.tensordot.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.tensordot.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.tensordot.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.tensordot.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.tensordot.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.tensordot.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.tensordot.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.tensordot.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.tensordot.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.tensordot.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.tensordot.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.tensordot.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.tensordot.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.tensordot[#](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy-tensordot "Link to this heading")

=================================================================================================================================

numpy.tensordot(_a_, _b_, _axes\=2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L996-L1218)
[#](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot "Link to this definition")

Compute tensor dot product along specified axes.

Given two tensors, _a_ and _b_, and an array\_like object containing two array\_like objects, `(a_axes, b_axes)`, sum the products of _a_’s and _b_’s elements (components) over the axes specified by `a_axes` and `b_axes`. The third argument can be a single non-negative integer\_like scalar, `N`; if it is such, then the last `N` dimensions of _a_ and the first `N` dimensions of _b_ are summed over.

Parameters:

**a, b**array\_like

Tensors to “dot”.

**axes**int or (2,) array\_like

*   integer\_like If an int N, sum over the last N axes of _a_ and the first N axes of _b_ in order. The sizes of the corresponding axes must match.
    
*   (2,) array\_like Or, a list of axes to be summed over, first sequence applying to _a_, second to _b_. Both elements array\_like must be of the same length. Each axis may appear at most once; repeated axes are not allowed. For example, `axes=([1, 1], [0, 0])` is invalid.
    

**Returns**

**——-**

**output**ndarray

The tensor dot product of the input.

See also

[`dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
, [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")

Notes

Three common use cases are:

*   `axes = 0` : tensor product \\(a\\otimes b\\)
    
*   `axes = 1` : tensor dot product \\(a\\cdot b\\)
    
*   `axes = 2` : (default) tensor double contraction \\(a:b\\)
    

When _axes_ is integer\_like, the sequence of axes for evaluation will be: from the -Nth axis to the -1th axis in _a_, and from the 0th axis to (N-1)th axis in _b_. For example, `axes = 2` is the equal to `axes = [[-2, -1], [0, 1]]`. When N-1 is smaller than 0, or when -N is larger than -1, the element of _a_ and _b_ are defined as the _axes_.

When there is more than one axis to sum over - and they are not the last (first) axes of _a_ (_b_) - the argument _axes_ should consist of two sequences of the same length, with the first axis to sum over given first in both sequences, the second axis second, and so forth. The calculation can be referred to `numpy.einsum`.

For example, if `a.shape == (2, 3, 4)` and `b.shape == (3, 4, 5)`, then `axes=([1, 2], [0, 1])` sums over the `(3, 4)` dimensions of both arrays and produces an output of shape `(2, 5)`.

Each summation axis corresponds to a distinct contraction index; repeating an axis (for example `axes=([1, 1], [0, 0])`) is invalid.

The shape of the result consists of the non-contracted axes of the first tensor, followed by the non-contracted axes of the second.

Examples

Try it in your browser!

An example on integer\_like:

\>>> a\_0 \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> b\_0 \= np.array(\[\[5, 6\], \[7, 8\]\])
\>>> c\_0 \= np.tensordot(a\_0, b\_0, axes\=0)
\>>> c\_0.shape
(2, 2, 2, 2)
\>>> c\_0
array(\[\[\[\[ 5,  6\],\
         \[ 7,  8\]\],\
        \[\[10, 12\],\
         \[14, 16\]\]\],\
       \[\[\[15, 18\],\
         \[21, 24\]\],\
        \[\[20, 24\],\
         \[28, 32\]\]\]\])

Copy to clipboard

An example on array\_like:

\>>> a \= np.arange(60.).reshape(3,4,5)
\>>> b \= np.arange(24.).reshape(4,3,2)
\>>> c \= np.tensordot(a,b, axes\=(\[1,0\],\[0,1\]))
\>>> c.shape
(5, 2)
\>>> c
array(\[\[4400., 4730.\],\
       \[4532., 4874.\],\
       \[4664., 5018.\],\
       \[4796., 5162.\],\
       \[4928., 5306.\]\])

Copy to clipboard

A slower but equivalent way of computing the same…

\>>> d \= np.zeros((5,2))
\>>> for i in range(5):
...   for j in range(2):
...     for k in range(3):
...       for n in range(4):
...         d\[i,j\] += a\[k,n,i\] \* b\[n,k,j\]
\>>> c \== d
array(\[\[ True,  True\],\
       \[ True,  True\],\
       \[ True,  True\],\
       \[ True,  True\],\
       \[ True,  True\]\])

Copy to clipboard

An extended example taking advantage of the overloading of + and \*:

\>>> a \= np.array(range(1, 9)).reshape((2, 2, 2))
\>>> A \= np.array(('a', 'b', 'c', 'd'), dtype\=np.object\_)
\>>> A \= A.reshape((2, 2))
\>>> a; A
array(\[\[\[1, 2\],\
        \[3, 4\]\],\
       \[\[5, 6\],\
        \[7, 8\]\]\])
array(\[\['a', 'b'\],\
       \['c', 'd'\]\], dtype=object)

Copy to clipboard

\>>> np.tensordot(a, A) \# third argument default is 2 for double-contraction
array(\['abbcccdddd', 'aaaaabbbbbbcccccccdddddddd'\], dtype=object)

Copy to clipboard

\>>> np.tensordot(a, A, 1)
array(\[\[\['acc', 'bdd'\],\
        \['aaacccc', 'bbbdddd'\]\],\
       \[\['aaaaacccccc', 'bbbbbdddddd'\],\
        \['aaaaaaacccccccc', 'bbbbbbbdddddddd'\]\]\], dtype=object)

Copy to clipboard

\>>> np.tensordot(a, A, 0) \# tensor product (result too long to incl.)
array(\[\[\[\[\['a', 'b'\],\
          \['c', 'd'\]\],\
          ...\
\
Copy to clipboard\
\
\>>> np.tensordot(a, A, (0, 1))\
array(\[\[\['abbbbb', 'cddddd'\],\
        \['aabbbbbb', 'ccdddddd'\]\],\
       \[\['aaabbbbbbb', 'cccddddddd'\],\
        \['aaaabbbbbbbb', 'ccccdddddddd'\]\]\], dtype=object)\
\
Copy to clipboard\
\
\>>> np.tensordot(a, A, (2, 1))\
array(\[\[\['abb', 'cdd'\],\
        \['aaabbbb', 'cccdddd'\]\],\
       \[\['aaaaabbbbbb', 'cccccdddddd'\],\
        \['aaaaaaabbbbbbbb', 'cccccccdddddddd'\]\]\], dtype=object)\
\
Copy to clipboard\
\
\>>> np.tensordot(a, A, ((0, 1), (0, 1)))\
array(\['abbbcccccddddddd', 'aabbbbccccccdddddddd'\], dtype=object)\
\
Copy to clipboard\
\
\>>> np.tensordot(a, A, ((2, 1), (1, 0)))\
array(\['acccbbdddd', 'aaaaacccccccbbbbbbdddddddd'\], dtype=object)\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page