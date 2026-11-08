[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg?version=stable#modules_2)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg?version=stable#classes_2)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg?version=stable#functions_2)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.compat.v1.linalg Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Modules](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg?version=stable#modules_2)
    
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg?version=stable#classes_2)
    
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg?version=stable#functions_2)
    

See Stable See Nightly

Public API for tf.\_api.v2.linalg namespace

Modules
-------

[`experimental`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/experimental)
 module: Public API for tf.\_api.v2.linalg.experimental namespace

Classes
-------

[`class LinearOperator`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperator)
: Base class defining a \[batch of\] linear operator\[s\].

[`class LinearOperatorAdjoint`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorAdjoint)
: `LinearOperator` representing the adjoint of another operator.

[`class LinearOperatorBlockDiag`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorBlockDiag)
: Combines one or more `LinearOperators` in to a Block Diagonal matrix.

[`class LinearOperatorBlockLowerTriangular`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorBlockLowerTriangular)
: Combines `LinearOperators` into a blockwise lower-triangular matrix.

[`class LinearOperatorCirculant`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorCirculant)
: `LinearOperator` acting like a circulant matrix.

[`class LinearOperatorCirculant2D`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorCirculant2D)
: `LinearOperator` acting like a block circulant matrix.

[`class LinearOperatorCirculant3D`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorCirculant3D)
: `LinearOperator` acting like a nested block circulant matrix.

[`class LinearOperatorComposition`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorComposition)
: Composes one or more `LinearOperators`.

[`class LinearOperatorDiag`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorDiag)
: `LinearOperator` acting like a \[batch\] square diagonal matrix.

[`class LinearOperatorFullMatrix`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorFullMatrix)
: `LinearOperator` that wraps a \[batch\] matrix.

[`class LinearOperatorHouseholder`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorHouseholder)
: `LinearOperator` acting like a \[batch\] of Householder transformations.

[`class LinearOperatorIdentity`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorIdentity)
: `LinearOperator` acting like a \[batch\] square identity matrix.

[`class LinearOperatorInversion`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorInversion)
: `LinearOperator` representing the inverse of another operator.

[`class LinearOperatorKronecker`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorKronecker)
: Kronecker product between two `LinearOperators`.

[`class LinearOperatorLowRankUpdate`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorLowRankUpdate)
: Perturb a `LinearOperator` with a rank `K` update.

[`class LinearOperatorLowerTriangular`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorLowerTriangular)
: `LinearOperator` acting like a \[batch\] square lower triangular matrix.

[`class LinearOperatorPermutation`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorPermutation)
: `LinearOperator` acting like a \[batch\] of permutation matrices.

[`class LinearOperatorScaledIdentity`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorScaledIdentity)
: `LinearOperator` acting like a scaled \[batch\] identity matrix `A = c I`.

[`class LinearOperatorToeplitz`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorToeplitz)
: `LinearOperator` acting like a \[batch\] of toeplitz matrices.

[`class LinearOperatorTridiag`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorTridiag)
: `LinearOperator` acting like a \[batch\] square tridiagonal matrix.

[`class LinearOperatorZeros`](https://www.tensorflow.org/api_docs/python/tf/linalg/LinearOperatorZeros)
: `LinearOperator` acting like a \[batch\] zero matrix.

Functions
---------

[`adjoint(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/adjoint)
: Transposes the last two dimensions of and conjugates tensor `matrix`.

[`band_part(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/band_part)
: Copy a tensor setting everything outside a central band in each innermost matrix to zero.

[`cholesky(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky)
: Computes the Cholesky decomposition of one or more square matrices.

[`cholesky_solve(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/cholesky_solve)
: Solves systems of linear eqns `A X = RHS`, given Cholesky factorizations.

[`cross(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/cross)
: Compute the pairwise cross product.

[`det(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/det)
: Computes the determinant of one or more square matrices.

[`diag(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/diag)
: Returns a batched diagonal tensor with given batched diagonal values.

[`diag_part(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/diag_part)
: Returns the batched diagonal part of a batched tensor.

[`eigh(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh)
: Computes the eigen decomposition of a batch of self-adjoint matrices.

[`eigh_tridiagonal(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh_tridiagonal)
: Computes the eigenvalues of a Hermitian tridiagonal matrix.

[`eigvalsh(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/eigvalsh)
: Computes the eigenvalues of one or more self-adjoint matrices.

[`einsum(...)`](https://www.tensorflow.org/api_docs/python/tf/einsum)
: Tensor contraction over specified indices and outer product.

[`expm(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/expm)
: Computes the matrix exponential of one or more square matrices.

[`eye(...)`](https://www.tensorflow.org/api_docs/python/tf/eye)
: Construct an identity matrix, or a batch of matrices.

[`global_norm(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/global_norm)
: Computes the global norm of multiple tensors.

[`inv(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/inv)
: Computes the inverse of one or more square invertible matrices or their adjoints (conjugate transposes).

[`l2_normalize(...)`](https://www.tensorflow.org/api_docs/python/tf/math/l2_normalize)
: Normalizes along dimension `axis` using an L2 norm. (deprecated arguments)

[`logdet(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/logdet)
: Computes log of the determinant of a hermitian positive definite matrix.

[`logm(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/logm)
: Computes the matrix logarithm of one or more square matrices:

[`lstsq(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/lstsq)
: Solves one or more linear least-squares problems.

[`lu(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/lu)
: Computes the LU decomposition of one or more square matrices.

[`lu_matrix_inverse(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_matrix_inverse)
: Computes the inverse given the LU decomposition(s) of one or more matrices.

[`lu_reconstruct(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_reconstruct)
: The reconstruct one or more matrices from their LU decomposition(s).

[`lu_solve(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/lu_solve)
: Solves systems of linear eqns `A X = RHS`, given LU factorizations.

[`matmul(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matmul)
: Multiplies matrix `a` by matrix `b`, producing `a` \* `b`.

[`matrix_rank(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/matrix_rank)
: Compute the matrix rank of one or more matrices.

[`matrix_transpose(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose)
: Transposes last two dimensions of tensor `a`.

[`matvec(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/matvec)
: Multiplies matrix `a` by vector `b`, producing `a` \* `b`.

[`norm(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/norm)
: Computes the norm of vectors, matrices, and tensors. (deprecated arguments)

[`normalize(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/normalize)
: Normalizes `tensor` along dimension `axis` using specified norm.

[`pinv(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/pinv)
: Compute the Moore-Penrose pseudo-inverse of one or more matrices.

[`qr(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/qr)
: Computes the QR decompositions of one or more matrices.

[`set_diag(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/set_diag)
: Returns a batched matrix tensor with new batched diagonal values.

[`slogdet(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/slogdet)
: Computes the sign and the log of the absolute value of the determinant of

[`solve(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/solve)
: Solves systems of linear equations.

[`sqrtm(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/sqrtm)
: Computes the matrix square root of one or more square matrices:

[`svd(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/svd)
: Computes the singular value decompositions of one or more matrices.

[`tensor_diag(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/tensor_diag)
: Returns a diagonal tensor with a given diagonal values.

[`tensor_diag_part(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/tensor_diag_part)
: Returns the diagonal part of the tensor.

[`tensordot(...)`](https://www.tensorflow.org/api_docs/python/tf/tensordot)
: Tensor contraction of a and b along specified axes and outer product.

[`trace(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/trace)
: Compute the trace of a tensor `x`.

[`transpose(...)`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/linalg/matrix_transpose)
: Transposes last two dimensions of tensor `a`.

[`triangular_solve(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/triangular_solve)
: Solve systems of linear equations with upper or lower triangular matrices.

[`tridiagonal_matmul(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_matmul)
: Multiplies tridiagonal matrix by matrix.

[`tridiagonal_solve(...)`](https://www.tensorflow.org/api_docs/python/tf/linalg/tridiagonal_solve)
: Solves tridiagonal systems of equations.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.