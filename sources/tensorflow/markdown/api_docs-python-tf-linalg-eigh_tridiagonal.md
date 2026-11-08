[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh_tridiagonal#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh_tridiagonal)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh_tridiagonal?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh_tridiagonal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh_tridiagonal#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh_tridiagonal#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.linalg.eigh\_tridiagonal Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh_tridiagonal#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh_tridiagonal#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh_tridiagonal#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/linalg/linalg_impl.py#L1232-L1588)

Computes the eigenvalues of a Hermitian tridiagonal matrix.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.linalg.eigh_tridiagonal`](https://www.tensorflow.org/api_docs/python/tf/linalg/eigh_tridiagonal)

tf.linalg.eigh_tridiagonal(
        alpha,
        beta,
        eigvals_only=True,
        select='a',
        select_range=None,
        tol=None,
        name=None
    )

|     |     |
| --- | --- |
| Args<br>---- |     |
| `alpha` | A real or complex tensor of shape (n), the diagonal elements of the matrix. NOTE: If alpha is complex, the imaginary part is ignored (assumed zero) to satisfy the requirement that the matrix be Hermitian. |
| `beta` | A real or complex tensor of shape (n-1), containing the elements of the first super-diagonal of the matrix. If beta is complex, the first sub-diagonal of the matrix is assumed to be the conjugate of beta to satisfy the requirement that the matrix be Hermitian |
| `eigvals_only` | If False, both eigenvalues and corresponding eigenvectors are computed. If True, only eigenvalues are computed. Default is True. |
| `select` | Optional string with values in {‘a’, ‘v’, ‘i’} (default is 'a') that determines which eigenvalues to calculate: 'a': all eigenvalues. ‘v’: eigenvalues in the interval (min, max\] given by `select_range`. 'i’: eigenvalues with indices min <= i <= max. |
| `select_range` | Size 2 tuple or list or tensor specifying the range of eigenvalues to compute together with select. If select is 'a', select\_range is ignored. |
| `tol` | Optional scalar. The absolute tolerance to which each eigenvalue is required. An eigenvalue (or cluster) is considered to have converged if it lies in an interval of this width. If tol is None (default), the value eps\*\|T\|\_2 is used where eps is the machine precision, and \|T\|\_2 is the 2-norm of the matrix T. |
| `name` | Optional name of the op. |

|     |     |
| --- | --- |
| Returns<br>------- |     |
| `eig_vals` | The eigenvalues of the matrix in non-decreasing order. |
| `eig_vectors` | If `eigvals_only` is False the eigenvectors are returned in the second output argument. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If input values are invalid. |
| `NotImplemented` | Computing eigenvectors for `eigvals_only` = False is not implemented yet. |

This op implements a subset of the functionality of scipy.linalg.eigh\_tridiagonal.

Add support for outer batch dimensions.

#### Examples

import numpy
    eigvals = tf.linalg.eigh_tridiagonal([0.0, 0.0, 0.0], [1.0, 1.0])
    eigvals_expected = [-numpy.sqrt(2.0), 0.0, numpy.sqrt(2.0)]
    tf.assert_near(eigvals_expected, eigvals)
    # ==> True

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.