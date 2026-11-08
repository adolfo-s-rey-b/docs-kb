[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.outer.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.outer.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.outer.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.outer.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.outer.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.outer.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.outer.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.outer.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.outer.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.outer.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.outer.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.outer.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.outer.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.outer.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.outer.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.outer.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.outer.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.outer.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.outer.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.outer.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.outer.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.outer.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.outer[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.outer.html#numpy-linalg-outer "Link to this heading")

==========================================================================================================================================

linalg.outer(_x1_, _x2_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L898-L966)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.outer.html#numpy.linalg.outer "Link to this definition")

Compute the outer product of two vectors.

This function is Array API compatible. Compared to `np.outer` it accepts 1-dimensional inputs only.

Parameters:

**x1**(M,) array\_like

One-dimensional input array of size `N`. Must have a numeric data type.

**x2**(N,) array\_like

One-dimensional input array of size `M`. Must have a numeric data type.

Returns:

**out**(M, N) ndarray

`out[i, j] = a[i] * b[j]`

See also

[`outer`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer")

Examples

Try it in your browser!

Make a (_very_ coarse) grid for computing a Mandelbrot set:

\>>> rl \= np.linalg.outer(np.ones((5,)), np.linspace(\-2, 2, 5))
\>>> rl
array(\[\[-2., -1.,  0.,  1.,  2.\],\
       \[-2., -1.,  0.,  1.,  2.\],\
       \[-2., -1.,  0.,  1.,  2.\],\
       \[-2., -1.,  0.,  1.,  2.\],\
       \[-2., -1.,  0.,  1.,  2.\]\])
\>>> im \= np.linalg.outer(1j\*np.linspace(2, \-2, 5), np.ones((5,)))
\>>> im
array(\[\[0.+2.j, 0.+2.j, 0.+2.j, 0.+2.j, 0.+2.j\],\
       \[0.+1.j, 0.+1.j, 0.+1.j, 0.+1.j, 0.+1.j\],\
       \[0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j\],\
       \[0.-1.j, 0.-1.j, 0.-1.j, 0.-1.j, 0.-1.j\],\
       \[0.-2.j, 0.-2.j, 0.-2.j, 0.-2.j, 0.-2.j\]\])
\>>> grid \= rl + im
\>>> grid
array(\[\[-2.+2.j, -1.+2.j,  0.+2.j,  1.+2.j,  2.+2.j\],\
       \[-2.+1.j, -1.+1.j,  0.+1.j,  1.+1.j,  2.+1.j\],\
       \[-2.+0.j, -1.+0.j,  0.+0.j,  1.+0.j,  2.+0.j\],\
       \[-2.-1.j, -1.-1.j,  0.-1.j,  1.-1.j,  2.-1.j\],\
       \[-2.-2.j, -1.-2.j,  0.-2.j,  1.-2.j,  2.-2.j\]\])

Copy to clipboard

An example using a “vector” of letters:

\>>> x \= np.array(\['a', 'b', 'c'\], dtype\=np.object\_)
\>>> np.linalg.outer(x, \[1, 2, 3\])
array(\[\['a', 'aa', 'aaa'\],\
       \['b', 'bb', 'bbb'\],\
       \['c', 'cc', 'ccc'\]\], dtype=object)

Copy to clipboard

Go BackOpen In Tab

On this page