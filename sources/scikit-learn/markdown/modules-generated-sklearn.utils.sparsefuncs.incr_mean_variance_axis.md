[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.incr_mean_variance_axis.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

incr\_mean\_variance\_axis[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.incr_mean_variance_axis.html#incr-mean-variance-axis "Link to this heading")

=======================================================================================================================================================================================

sklearn.utils.sparsefuncs.incr\_mean\_variance\_axis(_X_, _\*_, _axis_, _last\_mean_, _last\_var_, _last\_n_, _weights\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/sparsefuncs.py#L179)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.incr_mean_variance_axis.html#sklearn.utils.sparsefuncs.incr_mean_variance_axis "Link to this definition")

Compute incremental mean and variance along an axis on a CSR or CSC matrix.

last\_mean, last\_var are the statistics computed at the last step by this function. Both must be initialized to 0-arrays of the proper size, i.e. the number of features in X. last\_n is the number of samples encountered until now.

Parameters:

**X**CSR or CSC sparse matrix of shape (n\_samples, n\_features)

Input data.

**axis**{0, 1}

Axis along which the axis should be computed.

**last\_mean**ndarray of shape (n\_features,) or (n\_samples,), dtype=floating

Array of means to update with the new data X. Should be of shape (n\_features,) if axis=0 or (n\_samples,) if axis=1.

**last\_var**ndarray of shape (n\_features,) or (n\_samples,), dtype=floating

Array of variances to update with the new data X. Should be of shape (n\_features,) if axis=0 or (n\_samples,) if axis=1.

**last\_n**float or ndarray of shape (n\_features,) or (n\_samples,), dtype=floating

Sum of the weights seen so far, excluding the current weights If not float, it should be of shape (n\_features,) if axis=0 or (n\_samples,) if axis=1. If float it corresponds to having same weights for all samples (or features).

**weights**ndarray of shape (n\_samples,) or (n\_features,), default=None

If axis is set to 0 shape is (n\_samples,) or if axis is set to 1 shape is (n\_features,). If it is set to None, then samples are equally weighted.

Added in version 0.24.

Returns:

**means**ndarray of shape (n\_features,) or (n\_samples,), dtype=floating

Updated feature-wise means if axis = 0 or sample-wise means if axis = 1.

**variances**ndarray of shape (n\_features,) or (n\_samples,), dtype=floating

Updated feature-wise variances if axis = 0 or sample-wise variances if axis = 1.

**n**ndarray of shape (n\_features,) or (n\_samples,), dtype=integral

Updated number of seen samples per feature if axis=0 or number of seen features per sample if axis=1.

If weights is not None, n is a sum of the weights of the seen samples or features instead of the actual number of seen samples or features.

Notes

NaNs are ignored in the algorithm.

Examples

\>>> from sklearn.utils import sparsefuncs
\>>> from scipy import sparse
\>>> import numpy as np
\>>> indptr \= np.array(\[0, 3, 4, 4, 4\])
\>>> indices \= np.array(\[0, 1, 2, 2\])
\>>> data \= np.array(\[8, 1, 2, 5\])
\>>> scale \= np.array(\[2, 3, 2\])
\>>> csr \= sparse.csr\_array((data, indices, indptr))
\>>> csr.todense()
array(\[\[8, 1, 2\],\
       \[0, 0, 5\],\
       \[0, 0, 0\],\
       \[0, 0, 0\]\])
\>>> sparsefuncs.incr\_mean\_variance\_axis(
...     csr, axis\=0, last\_mean\=np.zeros(3), last\_var\=np.zeros(3), last\_n\=2
... )
(array(\[1.33, 0.167, 1.17\]), array(\[8.88, 0.139, 3.47\]),
array(\[6., 6., 6.\]))

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)