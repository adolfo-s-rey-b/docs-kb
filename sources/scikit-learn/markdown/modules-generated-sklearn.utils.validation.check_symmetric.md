[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_symmetric.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.validation.check_symmetric.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_symmetric.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.validation.check_symmetric.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.validation.check_symmetric.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.validation.check_symmetric.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.validation.check_symmetric.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.validation.check_symmetric.html)

Collapse Sidebar Expand Sidebar

check\_symmetric[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_symmetric.html#check-symmetric "Link to this heading")

============================================================================================================================================================

sklearn.utils.validation.check\_symmetric(_array_, _\*_, _tol\=1e-10_, _raise\_warning\=True_, _raise\_exception\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L1521)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_symmetric.html#sklearn.utils.validation.check_symmetric "Link to this definition")

Make sure that array is 2D, square and symmetric.

If the array is not symmetric, then a symmetrized version is returned. Optionally, a warning or exception is raised if the matrix is not symmetric.

Parameters:

**array**{ndarray, sparse matrix}

Input object to check / convert. Must be two-dimensional and square, otherwise a ValueError will be raised.

**tol**float, default=1e-10

Absolute tolerance for equivalence of arrays. Default = 1E-10.

**raise\_warning**bool, default=True

If True then raise a warning if conversion is required.

**raise\_exception**bool, default=False

If True then raise an exception if array is not symmetric.

Returns:

**array\_sym**{ndarray, sparse matrix}

Symmetrized version of the input array, i.e. the average of array and array.transpose(). If sparse, then duplicate entries are first summed and zeros are eliminated.

Examples

\>>> import numpy as np
\>>> from sklearn.utils.validation import check\_symmetric
\>>> symmetric\_array \= np.array(\[\[0, 1, 2\], \[1, 0, 1\], \[2, 1, 0\]\])
\>>> check\_symmetric(symmetric\_array)
array(\[\[0, 1, 2\],\
       \[1, 0, 1\],\
       \[2, 1, 0\]\])
\>>> from scipy.sparse import csr\_array
\>>> sparse\_symmetric\_array \= csr\_array(symmetric\_array)
\>>> check\_symmetric(sparse\_symmetric\_array)
<Compressed Sparse Row sparse array of dtype 'int64'
    with 6 stored elements and shape (3, 3)>

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)