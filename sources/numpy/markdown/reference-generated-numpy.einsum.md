[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.einsum.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.einsum.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.einsum.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.einsum.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.einsum.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.einsum.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.einsum.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.einsum.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.einsum.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.einsum.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.einsum.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.einsum.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.einsum.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.einsum.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.einsum.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.einsum.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.einsum.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.einsum.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.einsum.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.einsum.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.einsum[#](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy-einsum "Link to this heading")

========================================================================================================================

numpy.einsum(_subscripts_, _\*operands_, _out\=None_, _dtype\=None_, _order\='K'_, _casting\='safe'_, _optimize\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/einsumfunc.py#L1242-L1647)
[#](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "Link to this definition")

Evaluates the Einstein summation convention on the operands.

Using the Einstein summation convention, many common multi-dimensional, linear algebraic array operations can be represented in a simple fashion. In _implicit_ mode [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
 computes these values.

In _explicit_ mode, [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
 provides further flexibility to compute other array operations that might not be considered classical Einstein summation operations, by disabling, or forcing summation over specified subscript labels.

See the notes and examples for clarification.

Parameters:

**subscripts**str

Specifies the subscripts for summation as comma separated list of subscript labels. An implicit (classical Einstein summation) calculation is performed unless the explicit indicator ‘->’ is included as well as subscript labels of the precise output form.

**operands**list of array\_like

These are the arrays for the operation.

**out**ndarray, optional

If provided, the calculation is done into this array.

**dtype**{data-type, None}, optional

If provided, forces the calculation to use the data type specified. Note that you may have to also give a more liberal _casting_ parameter to allow the conversions. Default is None.

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

Controls the memory layout of the output. ‘C’ means it should be C contiguous. ‘F’ means it should be Fortran contiguous, ‘A’ means it should be ‘F’ if the inputs are all ‘F’, ‘C’ otherwise. ‘K’ means it should be as close to the layout as the inputs as is possible, including arbitrarily permuted axes. Default is ‘K’.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘unsafe’}, optional

Controls what kind of data casting may occur. Setting this to ‘unsafe’ is not recommended, as it can adversely affect accumulations.

*   ‘no’ means the data types should not be cast at all.
    
*   ‘equiv’ means only byte-order changes are allowed.
    
*   ‘safe’ means only casts which can preserve values are allowed.
    
*   ‘same\_kind’ means only safe casts or casts within a kind, like float64 to float32, are allowed.
    
*   ‘unsafe’ means any data conversions may be done.
    

Default is ‘safe’.

**optimize**{False, True, ‘greedy’, ‘optimal’}, optional

Controls if intermediate optimization should occur. No optimization will occur if False and True will default to the ‘greedy’ algorithm. Also accepts an explicit contraction list from the `np.einsum_path` function. See `np.einsum_path` for more details. Defaults to False.

Returns:

**output**ndarray

The calculation based on the Einstein summation convention.

See also

[`einsum_path`](https://numpy.org/doc/stable/reference/generated/numpy.einsum_path.html#numpy.einsum_path "numpy.einsum_path")
, [`dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
, [`inner`](https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner "numpy.inner")
, [`outer`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer")
, [`tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot "numpy.tensordot")
, [`linalg.multi_dot`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#numpy.linalg.multi_dot "numpy.linalg.multi_dot")

[`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")

Similar verbose interface is provided by the [einops](https://github.com/arogozhnikov/einops)
 package to cover additional operations: transpose, reshape/flatten, repeat/tile, squeeze/unsqueeze and reductions. The [opt\_einsum](https://optimized-einsum.readthedocs.io/en/stable/)
 optimizes contraction order for einsum-like expressions in backend-agnostic manner.

Notes

The Einstein summation convention can be used to compute many multi-dimensional, linear algebraic array operations. [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
 provides a succinct way of representing these.

A non-exhaustive list of these operations, which can be computed by [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
, is shown below along with examples:

*   Trace of an array, [`numpy.trace`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "numpy.trace")
    .
    
*   Return a diagonal, [`numpy.diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
    .
    
*   Array axis summations, [`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
    .
    
*   Transpositions and permutations, [`numpy.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")
    .
    
*   Matrix multiplication and dot product, [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")
    
    [`numpy.dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
    .
    
*   Vector inner and outer products, [`numpy.inner`](https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner "numpy.inner")
    
    [`numpy.outer`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer")
    .
    
*   Broadcasting, element-wise and scalar multiplication,
    
    [`numpy.multiply`](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html#numpy.multiply "numpy.multiply")
    .
    
*   Tensor contractions, [`numpy.tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot "numpy.tensordot")
    .
    
*   Chained array operations, in efficient calculation order,
    
    [`numpy.einsum_path`](https://numpy.org/doc/stable/reference/generated/numpy.einsum_path.html#numpy.einsum_path "numpy.einsum_path")
    .
    

The subscripts string is a comma-separated list of subscript labels, where each label refers to a dimension of the corresponding operand. Whenever a label is repeated it is summed, so `np.einsum('i,i', a, b)` is equivalent to [`np.inner(a,b)`](https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner "numpy.inner")
. If a label appears only once, it is not summed, so `np.einsum('i', a)` produces a view of `a` with no changes. A further example `np.einsum('ij,jk', a, b)` describes traditional matrix multiplication and is equivalent to [`np.matmul(a,b)`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")
. Repeated subscript labels in one operand take the diagonal. For example, `np.einsum('ii', a)` is equivalent to [`np.trace(a)`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "numpy.trace")
.

In _implicit mode_, the chosen subscripts are important since the axes of the output are reordered alphabetically. This means that `np.einsum('ij', a)` doesn’t affect a 2D array, while `np.einsum('ji', a)` takes its transpose. Additionally, `np.einsum('ij,jk', a, b)` returns a matrix multiplication, while, `np.einsum('ij,jh', a, b)` returns the transpose of the multiplication since subscript ‘h’ precedes subscript ‘i’.

In _explicit mode_ the output can be directly controlled by specifying output subscript labels. This requires the identifier ‘->’ as well as the list of output subscript labels. This feature increases the flexibility of the function since summing can be disabled or forced when required. The call `np.einsum('i->', a)` is like [`np.sum(a)`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
 if `a` is a 1-D array, and `np.einsum('ii->i', a)` is like [`np.diag(a)`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
 if `a` is a square 2-D array. The difference is that [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
 does not allow broadcasting by default. Additionally `np.einsum('ij,jh->ih', a, b)` directly specifies the order of the output subscript labels and therefore returns matrix multiplication, unlike the example above in implicit mode.

To enable and control broadcasting, use an ellipsis. Default NumPy-style broadcasting is done by adding an ellipsis to the left of each term, like `np.einsum('...ii->...i', a)`. `np.einsum('...i->...', a)` is like [`np.sum(a, axis=-1)`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
 for array `a` of any shape. To take the trace along the first and last axes, you can do `np.einsum('i...i', a)`, or to do a matrix-matrix product with the left-most indices instead of rightmost, one can do `np.einsum('ij...,jk...->ik...', a, b)`.

When there is only one operand, no axes are summed, and no output parameter is provided, a view into the operand is returned instead of a new array. Thus, taking the diagonal as `np.einsum('ii->i', a)` produces a view (changed in version 1.10.0).

[`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
 also provides an alternative way to provide the subscripts and operands as `einsum(op0, sublist0, op1, sublist1, ..., [sublistout])`. If the output shape is not provided in this format [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
 will be calculated in implicit mode, otherwise it will be performed explicitly. The examples below have corresponding [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
 calls with the two parameter methods.

Views returned from einsum are now writeable whenever the input array is writeable. For example, `np.einsum('ijk...->kji...', a)` will now have the same effect as [`np.swapaxes(a, 0, 2)`](https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html#numpy.swapaxes "numpy.swapaxes")
 and `np.einsum('ii->i', a)` will return a writeable view of the diagonal of a 2D array.

Added the `optimize` argument which will optimize the contraction order of an einsum expression. For a contraction with three or more operands this can greatly increase the computational efficiency at the cost of a larger memory footprint during computation.

Typically a ‘greedy’ algorithm is applied which empirical tests have shown returns the optimal path in the majority of cases. In some cases ‘optimal’ will return the superlative path through a more expensive, exhaustive search. For iterative calculations it may be advisable to calculate the optimal path once and reuse that path by supplying it as an argument. An example is given below.

See [`numpy.einsum_path`](https://numpy.org/doc/stable/reference/generated/numpy.einsum_path.html#numpy.einsum_path "numpy.einsum_path")
 for more details.

Examples

Try it in your browser!

\>>> a \= np.arange(25).reshape(5,5)
\>>> b \= np.arange(5)
\>>> c \= np.arange(6).reshape(2,3)

Copy to clipboard

Trace of a matrix:

\>>> np.einsum('ii', a)
60
\>>> np.einsum(a, \[0,0\])
60
\>>> np.trace(a)
60

Copy to clipboard

Extract the diagonal (requires explicit form):

\>>> np.einsum('ii->i', a)
array(\[ 0,  6, 12, 18, 24\])
\>>> np.einsum(a, \[0,0\], \[0\])
array(\[ 0,  6, 12, 18, 24\])
\>>> np.diag(a)
array(\[ 0,  6, 12, 18, 24\])

Copy to clipboard

Sum over an axis (requires explicit form):

\>>> np.einsum('ij->i', a)
array(\[ 10,  35,  60,  85, 110\])
\>>> np.einsum(a, \[0,1\], \[0\])
array(\[ 10,  35,  60,  85, 110\])
\>>> np.sum(a, axis\=1)
array(\[ 10,  35,  60,  85, 110\])

Copy to clipboard

For higher dimensional arrays summing a single axis can be done with ellipsis:

\>>> np.einsum('...j->...', a)
array(\[ 10,  35,  60,  85, 110\])
\>>> np.einsum(a, \[Ellipsis,1\], \[Ellipsis\])
array(\[ 10,  35,  60,  85, 110\])

Copy to clipboard

Compute a matrix transpose, or reorder any number of axes:

\>>> np.einsum('ji', c)
array(\[\[0, 3\],\
       \[1, 4\],\
       \[2, 5\]\])
\>>> np.einsum('ij->ji', c)
array(\[\[0, 3\],\
       \[1, 4\],\
       \[2, 5\]\])
\>>> np.einsum(c, \[1,0\])
array(\[\[0, 3\],\
       \[1, 4\],\
       \[2, 5\]\])
\>>> np.transpose(c)
array(\[\[0, 3\],\
       \[1, 4\],\
       \[2, 5\]\])

Copy to clipboard

Vector inner products:

\>>> np.einsum('i,i', b, b)
30
\>>> np.einsum(b, \[0\], b, \[0\])
30
\>>> np.inner(b,b)
30

Copy to clipboard

Matrix vector multiplication:

\>>> np.einsum('ij,j', a, b)
array(\[ 30,  80, 130, 180, 230\])
\>>> np.einsum(a, \[0,1\], b, \[1\])
array(\[ 30,  80, 130, 180, 230\])
\>>> np.dot(a, b)
array(\[ 30,  80, 130, 180, 230\])
\>>> np.einsum('...j,j', a, b)
array(\[ 30,  80, 130, 180, 230\])

Copy to clipboard

Broadcasting and scalar multiplication:

\>>> np.einsum('..., ...', 3, c)
array(\[\[ 0,  3,  6\],\
       \[ 9, 12, 15\]\])
\>>> np.einsum(',ij', 3, c)
array(\[\[ 0,  3,  6\],\
       \[ 9, 12, 15\]\])
\>>> np.einsum(3, \[Ellipsis\], c, \[Ellipsis\])
array(\[\[ 0,  3,  6\],\
       \[ 9, 12, 15\]\])
\>>> np.multiply(3, c)
array(\[\[ 0,  3,  6\],\
       \[ 9, 12, 15\]\])

Copy to clipboard

Vector outer product:

\>>> np.einsum('i,j', np.arange(2)+1, b)
array(\[\[0, 1, 2, 3, 4\],\
       \[0, 2, 4, 6, 8\]\])
\>>> np.einsum(np.arange(2)+1, \[0\], b, \[1\])
array(\[\[0, 1, 2, 3, 4\],\
       \[0, 2, 4, 6, 8\]\])
\>>> np.outer(np.arange(2)+1, b)
array(\[\[0, 1, 2, 3, 4\],\
       \[0, 2, 4, 6, 8\]\])

Copy to clipboard

Tensor contraction:

\>>> a \= np.arange(60.).reshape(3,4,5)
\>>> b \= np.arange(24.).reshape(4,3,2)
\>>> np.einsum('ijk,jil->kl', a, b)
array(\[\[4400., 4730.\],\
       \[4532., 4874.\],\
       \[4664., 5018.\],\
       \[4796., 5162.\],\
       \[4928., 5306.\]\])
\>>> np.einsum(a, \[0,1,2\], b, \[1,0,3\], \[2,3\])
array(\[\[4400., 4730.\],\
       \[4532., 4874.\],\
       \[4664., 5018.\],\
       \[4796., 5162.\],\
       \[4928., 5306.\]\])
\>>> np.tensordot(a,b, axes\=(\[1,0\],\[0,1\]))
array(\[\[4400., 4730.\],\
       \[4532., 4874.\],\
       \[4664., 5018.\],\
       \[4796., 5162.\],\
       \[4928., 5306.\]\])

Copy to clipboard

Writeable returned arrays (since version 1.10.0):

\>>> a \= np.zeros((3, 3))
\>>> np.einsum('ii->i', a)\[:\] \= 1
\>>> a
array(\[\[1., 0., 0.\],\
       \[0., 1., 0.\],\
       \[0., 0., 1.\]\])

Copy to clipboard

Example of ellipsis use:

\>>> a \= np.arange(6).reshape((3,2))
\>>> b \= np.arange(12).reshape((4,3))
\>>> np.einsum('ki,jk->ij', a, b)
array(\[\[10, 28, 46, 64\],\
       \[13, 40, 67, 94\]\])
\>>> np.einsum('ki,...k->i...', a, b)
array(\[\[10, 28, 46, 64\],\
       \[13, 40, 67, 94\]\])
\>>> np.einsum('k...,jk', a, b)
array(\[\[10, 28, 46, 64\],\
       \[13, 40, 67, 94\]\])

Copy to clipboard

Chained array operations. For more complicated contractions, speed ups might be achieved by repeatedly computing a ‘greedy’ path or pre-computing the ‘optimal’ path and repeatedly applying it, using an [`einsum_path`](https://numpy.org/doc/stable/reference/generated/numpy.einsum_path.html#numpy.einsum_path "numpy.einsum_path")
 insertion (since version 1.12.0). Performance improvements can be particularly significant with larger arrays:

\>>> a \= np.ones(64).reshape(2,4,8)

Copy to clipboard

Basic [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
: ~1520ms (benchmarked on 3.1GHz Intel i5.)

\>>> for iteration in range(500):
...     \_ \= np.einsum('ijk,ilm,njm,nlk,abc->',a,a,a,a,a)

Copy to clipboard

Sub-optimal [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
 (due to repeated path calculation time): ~330ms

\>>> for iteration in range(500):
...     \_ \= np.einsum('ijk,ilm,njm,nlk,abc->',a,a,a,a,a,
...         optimize\='optimal')

Copy to clipboard

Greedy [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
 (faster optimal path approximation): ~160ms

\>>> for iteration in range(500):
...     \_ \= np.einsum('ijk,ilm,njm,nlk,abc->',a,a,a,a,a, optimize\='greedy')

Copy to clipboard

Optimal [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")
 (best usage pattern in some use cases): ~110ms

\>>> path \= np.einsum\_path('ijk,ilm,njm,nlk,abc->',a,a,a,a,a,
...     optimize\='optimal')\[0\]
\>>> for iteration in range(500):
...     \_ \= np.einsum('ijk,ilm,njm,nlk,abc->',a,a,a,a,a, optimize\=path)

Copy to clipboard

Go BackOpen In Tab

On this page