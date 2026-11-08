[Skip to main content](https://numpy.org/doc/stable/reference/routines.linalg.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.linalg.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.linalg.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.linalg.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.linalg.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.linalg.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.linalg.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.linalg.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.linalg.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.linalg.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.linalg.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.linalg.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.linalg.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.linalg.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.linalg.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.linalg.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.linalg.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.linalg.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.linalg.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.linalg.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.linalg.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.linalg.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Linear algebra[#](https://numpy.org/doc/stable/reference/routines.linalg.html#linear-algebra "Link to this heading")

=====================================================================================================================

The NumPy linear algebra functions rely on BLAS and LAPACK to provide efficient low level implementations of standard linear algebra algorithms. Those libraries may be provided by NumPy itself using C versions of a subset of their reference implementations but, when possible, highly optimized libraries that take advantage of specialized processor functionality are preferred. Examples of such libraries are [OpenBLAS](https://www.openblas.net/)
, MKL (TM), and ATLAS. Because those libraries are multithreaded and processor dependent, environmental variables and external packages such as [threadpoolctl](https://github.com/joblib/threadpoolctl)
 may be needed to control the number of threads or specify the processor architecture.

The SciPy library also contains a [`linalg`](https://docs.scipy.org/doc/scipy/reference/linalg.html#module-scipy.linalg "(in SciPy v1.18.0)")
 submodule, and there is overlap in the functionality provided by the SciPy and NumPy submodules. SciPy contains functions not found in [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
, such as functions related to LU decomposition and the Schur decomposition, multiple ways of calculating the pseudoinverse, and matrix transcendentals such as the matrix logarithm. Some functions that exist in both have augmented functionality in [`scipy.linalg`](https://docs.scipy.org/doc/scipy/reference/linalg.html#module-scipy.linalg "(in SciPy v1.18.0)")
. For example, [`scipy.linalg.eig`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eig.html#scipy.linalg.eig "(in SciPy v1.18.0)")
 can take a second matrix argument for solving generalized eigenvalue problems. Some functions in NumPy, however, have more flexible broadcasting options. For example, [`numpy.linalg.solve`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve "numpy.linalg.solve")
 can handle “stacked” arrays, while [`scipy.linalg.solve`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve.html#scipy.linalg.solve "(in SciPy v1.18.0)")
 accepts only a single square array as its first argument.

Note

The term _matrix_ as it is used on this page indicates a 2d [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
 object, and _not_ a [`numpy.matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 object. The latter is no longer recommended, even for linear algebra. See [the matrix object documentation](https://numpy.org/doc/stable/reference/arrays.classes.html#matrix-objects)
 for more information.

The `@` operator[#](https://numpy.org/doc/stable/reference/routines.linalg.html#the-operator "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

Introduced in NumPy 1.10.0, the `@` operator is preferable to other methods when computing the matrix product between 2d arrays. The [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")
 function implements the `@` operator.

Matrix and vector products[#](https://numpy.org/doc/stable/reference/routines.linalg.html#matrix-and-vector-products "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")<br>(a, b\[, out\]) | Dot product of two arrays. |
| [`linalg.multi_dot`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.multi_dot.html#numpy.linalg.multi_dot "numpy.linalg.multi_dot")<br>(arrays, \*\[, out\]) | Compute the dot product of two or more arrays in a single function call, while automatically selecting the fastest evaluation order. |
| [`vdot`](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot "numpy.vdot")<br>(a, b, /) | Return the dot product of two vectors. |
| [`vecdot`](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html#numpy.vecdot "numpy.vecdot")<br>(x1, x2, /\[, out, casting, order, ...\]) | Vector dot product of two arrays. |
| [`linalg.vecdot`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.vecdot.html#numpy.linalg.vecdot "numpy.linalg.vecdot")<br>(x1, x2, /, \*\[, axis\]) | Computes the vector dot product. |
| [`inner`](https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner "numpy.inner")<br>(a, b, /) | Inner product of two arrays. |
| [`outer`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer")<br>(a, b\[, out\]) | Compute the outer product of two vectors. |
| [`linalg.outer`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.outer.html#numpy.linalg.outer "numpy.linalg.outer")<br>(x1, x2, /) | Compute the outer product of two vectors. |
| [`matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")<br>(x1, x2, /\[, out, casting, order, ...\]) | Matrix product of two arrays. |
| [`linalg.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matmul.html#numpy.linalg.matmul "numpy.linalg.matmul")<br>(x1, x2, /) | Computes the matrix product. |
| [`matvec`](https://numpy.org/doc/stable/reference/generated/numpy.matvec.html#numpy.matvec "numpy.matvec")<br>(x1, x2, /\[, out, casting, order, ...\]) | Matrix-vector dot product of two arrays. |
| [`vecmat`](https://numpy.org/doc/stable/reference/generated/numpy.vecmat.html#numpy.vecmat "numpy.vecmat")<br>(x1, x2, /\[, out, casting, order, ...\]) | Vector-matrix dot product of two arrays. |
| [`tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot "numpy.tensordot")<br>(a, b\[, axes\]) | Compute tensor dot product along specified axes. |
| [`linalg.tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensordot.html#numpy.linalg.tensordot "numpy.linalg.tensordot")<br>(x1, x2, /, \*\[, axes\]) | Compute tensor dot product along specified axes. |
| [`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")<br>(subscripts, \*operands\[, out, dtype, ...\]) | Evaluates the Einstein summation convention on the operands. |
| [`einsum_path`](https://numpy.org/doc/stable/reference/generated/numpy.einsum_path.html#numpy.einsum_path "numpy.einsum_path")<br>(subscripts, \*operands\[, optimize\]) | Evaluates the lowest cost contraction order for an einsum expression by considering the creation of intermediate arrays. |
| [`linalg.matrix_power`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html#numpy.linalg.matrix_power "numpy.linalg.matrix_power")<br>(a, n) | Raise a square matrix to the (integer) power _n_. |
| [`kron`](https://numpy.org/doc/stable/reference/generated/numpy.kron.html#numpy.kron "numpy.kron")<br>(a, b) | Kronecker product of two arrays. |
| [`linalg.cross`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cross.html#numpy.linalg.cross "numpy.linalg.cross")<br>(x1, x2, /, \*\[, axis\]) | Returns the cross product of 3-element vectors. |

Decompositions[#](https://numpy.org/doc/stable/reference/routines.linalg.html#decompositions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`linalg.cholesky`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cholesky.html#numpy.linalg.cholesky "numpy.linalg.cholesky")<br>(a, /, \*\[, upper\]) | Cholesky decomposition. |
| [`linalg.qr`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.qr.html#numpy.linalg.qr "numpy.linalg.qr")<br>(a\[, mode\]) | Compute the qr factorization of a matrix. |
| [`linalg.svd`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd "numpy.linalg.svd")<br>(a\[, full\_matrices, compute\_uv, ...\]) | Singular Value Decomposition. |
| [`linalg.svdvals`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svdvals.html#numpy.linalg.svdvals "numpy.linalg.svdvals")<br>(x, /) | Returns the singular values of a matrix (or a stack of matrices) `x`. |

Matrix eigenvalues[#](https://numpy.org/doc/stable/reference/routines.linalg.html#matrix-eigenvalues "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`linalg.eig`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig "numpy.linalg.eig")<br>(a) | Compute the eigenvalues and right eigenvectors of a square array. |
| [`linalg.eigh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#numpy.linalg.eigh "numpy.linalg.eigh")<br>(a\[, UPLO\]) | Return the eigenvalues and eigenvectors of a complex Hermitian (conjugate symmetric) or a real symmetric matrix. |
| [`linalg.eigvals`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#numpy.linalg.eigvals "numpy.linalg.eigvals")<br>(a) | Compute the eigenvalues of a general matrix. |
| [`linalg.eigvalsh`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html#numpy.linalg.eigvalsh "numpy.linalg.eigvalsh")<br>(a\[, UPLO\]) | Compute the eigenvalues of a complex Hermitian or real symmetric matrix. |

Norms and other numbers[#](https://numpy.org/doc/stable/reference/routines.linalg.html#norms-and-other-numbers "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`linalg.norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm "numpy.linalg.norm")<br>(x\[, ord, axis, keepdims\]) | Matrix or vector norm. |
| [`linalg.matrix_norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_norm.html#numpy.linalg.matrix_norm "numpy.linalg.matrix_norm")<br>(x, /, \*\[, keepdims, ord\]) | Computes the matrix norm of a matrix (or a stack of matrices) `x`. |
| [`linalg.vector_norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.vector_norm.html#numpy.linalg.vector_norm "numpy.linalg.vector_norm")<br>(x, /, \*\[, axis, ...\]) | Computes the vector norm of a vector (or batch of vectors) `x`. |
| [`linalg.cond`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html#numpy.linalg.cond "numpy.linalg.cond")<br>(x\[, p\]) | Compute the condition number of a matrix. |
| [`linalg.det`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html#numpy.linalg.det "numpy.linalg.det")<br>(a) | Compute the determinant of an array. |
| [`linalg.matrix_rank`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html#numpy.linalg.matrix_rank "numpy.linalg.matrix_rank")<br>(A\[, tol, hermitian, rtol\]) | Return matrix rank of array using SVD method |
| [`linalg.slogdet`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.slogdet.html#numpy.linalg.slogdet "numpy.linalg.slogdet")<br>(a) | Compute the sign and (natural) logarithm of the determinant of an array. |
| [`trace`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html#numpy.trace "numpy.trace")<br>(a\[, offset, axis1, axis2, dtype, out\]) | Return the sum along diagonals of the array. |
| [`linalg.trace`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.trace.html#numpy.linalg.trace "numpy.linalg.trace")<br>(x, /, \*\[, offset, dtype\]) | Returns the sum along the specified diagonals of a matrix (or a stack of matrices) `x`. |

Solving equations and inverting matrices[#](https://numpy.org/doc/stable/reference/routines.linalg.html#solving-equations-and-inverting-matrices "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`linalg.solve`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve "numpy.linalg.solve")<br>(a, b) | Solve a linear matrix equation, or system of linear scalar equations. |
| [`linalg.tensorsolve`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorsolve.html#numpy.linalg.tensorsolve "numpy.linalg.tensorsolve")<br>(a, b\[, axes\]) | Solve the tensor equation `a x = b` for x. |
| [`linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")<br>(a, b\[, rcond\]) | Return the least-squares solution to a linear matrix equation. |
| [`linalg.inv`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html#numpy.linalg.inv "numpy.linalg.inv")<br>(a) | Compute the inverse of a matrix. |
| [`linalg.pinv`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html#numpy.linalg.pinv "numpy.linalg.pinv")<br>(a\[, rcond, hermitian, rtol\]) | Compute the (Moore-Penrose) pseudo-inverse of a matrix. |
| [`linalg.tensorinv`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorinv.html#numpy.linalg.tensorinv "numpy.linalg.tensorinv")<br>(a\[, ind\]) | Compute the 'inverse' of an N-dimensional array. |

Other matrix operations[#](https://numpy.org/doc/stable/reference/routines.linalg.html#other-matrix-operations "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal")<br>(a\[, offset, axis1, axis2\]) | Return specified diagonals. |
| [`linalg.diagonal`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.diagonal.html#numpy.linalg.diagonal "numpy.linalg.diagonal")<br>(x, /, \*\[, offset\]) | Returns specified diagonals of a matrix (or a stack of matrices) `x`. |
| [`linalg.matrix_transpose`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_transpose.html#numpy.linalg.matrix_transpose "numpy.linalg.matrix_transpose")<br>(x, /) | Transposes a matrix (or a stack of matrices) `x`. |

Exceptions[#](https://numpy.org/doc/stable/reference/routines.linalg.html#exceptions "Link to this heading")

-------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`linalg.LinAlgError`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.LinAlgError.html#numpy.linalg.LinAlgError "numpy.linalg.LinAlgError") | Generic Python-exception-derived object raised by linalg functions. |

Linear algebra on several matrices at once[#](https://numpy.org/doc/stable/reference/routines.linalg.html#linear-algebra-on-several-matrices-at-once "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Several of the linear algebra routines listed above are able to compute results for several matrices at once, if they are stacked into the same array.

This is indicated in the documentation via input parameter specifications such as `a : (..., M, M) array_like`. This means that if for instance given an input array `a.shape == (N, M, M)`, it is interpreted as a “stack” of N matrices, each of size M-by-M. Similar specification applies to return values, for instance the determinant has `det : (...)` and will in this case return an array of shape `det(a).shape == (N,)`. This generalizes to linear algebra operations on higher-dimensional arrays: the last 1 or 2 dimensions of a multidimensional array are interpreted as vectors or matrices, as appropriate for each operation.

On this page