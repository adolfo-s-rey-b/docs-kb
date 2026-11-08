[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.einsum_path.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.einsum_path.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.einsum_path.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.einsum_path.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.einsum_path.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.einsum_path.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.einsum_path.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.einsum_path.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.einsum_path.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.einsum_path.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.einsum_path.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.einsum_path.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.einsum_path.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.einsum_path.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.einsum_path.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.einsum_path.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.einsum_path.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.einsum_path.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.einsum_path.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.einsum_path.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.einsum_path.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.einsum_path.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.einsum\_path[#](https://numpy.org/doc/stable/reference/generated/numpy.einsum_path.html#numpy-einsum-path "Link to this heading")

========================================================================================================================================

numpy.einsum\_path(_subscripts_, _\*operands_, _optimize\='greedy'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/einsumfunc.py#L634-L920)
[#](https://numpy.org/doc/stable/reference/generated/numpy.einsum_path.html#numpy.einsum_path "Link to this definition")

Evaluates the lowest cost contraction order for an einsum expression by considering the creation of intermediate arrays.

Parameters:

**subscripts**str

Specifies the subscripts for summation.

**\*operands**list of array\_like

These are the arrays for the operation.

**optimize**{bool, list, tuple, ‘greedy’, ‘optimal’}

Choose the type of path. If a tuple is provided, the second argument is assumed to be the maximum intermediate size created. If only a single argument is provided the largest input or output array size is used as a maximum intermediate size.

*   if a list is given that starts with `einsum_path`, uses this as the contraction path
    
*   if False no optimization is taken
    
*   if True defaults to the ‘greedy’ algorithm
    
*   ‘optimal’ An algorithm that combinatorially explores all possible ways of contracting the listed tensors and chooses the least costly path. Scales exponentially with the number of terms in the contraction.
    
*   ‘greedy’ An algorithm that chooses the best pair contraction at each step. Effectively, this algorithm searches the largest inner, Hadamard, and then outer products at each step. Scales cubically with the number of terms in the contraction. Equivalent to the ‘optimal’ path for most contractions.
    

Default is ‘greedy’.

Returns:

**path**list of tuples

A list representation of the einsum path.

**string\_repr**str

A printable representation of the einsum path.

See also

[`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
, [`linalg.multi_dot`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#numpy.linalg.multi_dot "numpy.linalg.multi_dot")

Notes

The resulting path indicates which terms of the input contraction should be contracted first, the result of this contraction is then appended to the end of the contraction list. This list can then be iterated over until all intermediate contractions are complete.

Examples

Try it in your browser!

We can begin with a chain dot example. In this case, it is optimal to contract the `b` and `c` tensors first as represented by the first element of the path `(1, 2)`. The resulting tensor is added to the end of the contraction and the remaining contraction `(0, 1)` is then completed.

\>>> np.random.seed(123)
\>>> a \= np.random.rand(2, 2)
\>>> b \= np.random.rand(2, 5)
\>>> c \= np.random.rand(5, 2)
\>>> path\_info \= np.einsum\_path('ij,jk,kl->il', a, b, c, optimize\='greedy')
\>>> print(path\_info\[0\])
\['einsum\_path', (1, 2), (0, 1)\]
\>>> print(path\_info\[1\])
  Complete contraction:  ij,jk,kl->il # may vary
         Naive scaling:  4
     Optimized scaling:  3
      Naive FLOP count:  1.600e+02
  Optimized FLOP count:  5.600e+01
   Theoretical speedup:  2.857
  Largest intermediate:  4.000e+00 elements
\-------------------------------------------------------------------------
scaling                  current                                remaining
\-------------------------------------------------------------------------
   3                   kl,jk->jl                                ij,jl->il
   3                   jl,ij->il                                   il->il

Copy to clipboard

A more complex index transformation example.

\>>> I \= np.random.rand(10, 10, 10, 10)
\>>> C \= np.random.rand(10, 10)
\>>> path\_info \= np.einsum\_path('ea,fb,abcd,gc,hd->efgh', C, C, I, C, C,
...                            optimize\='greedy')

Copy to clipboard

\>>> print(path\_info\[0\])
\['einsum\_path', (0, 2), (0, 3), (0, 2), (0, 1)\]
\>>> print(path\_info\[1\])
  Complete contraction:  ea,fb,abcd,gc,hd->efgh # may vary
         Naive scaling:  8
     Optimized scaling:  5
      Naive FLOP count:  8.000e+08
  Optimized FLOP count:  8.000e+05
   Theoretical speedup:  1000.000
  Largest intermediate:  1.000e+04 elements
\--------------------------------------------------------------------------
scaling                  current                                remaining
\--------------------------------------------------------------------------
   5               abcd,ea->bcde                      fb,gc,hd,bcde->efgh
   5               bcde,fb->cdef                         gc,hd,cdef->efgh
   5               cdef,gc->defg                            hd,defg->efgh
   5               defg,hd->efgh                               efgh->efgh

Copy to clipboard

Go BackOpen In Tab

On this page