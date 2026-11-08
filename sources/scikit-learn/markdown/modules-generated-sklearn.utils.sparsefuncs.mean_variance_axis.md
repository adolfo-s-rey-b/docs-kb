[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html)

Collapse Sidebar Expand Sidebar

mean\_variance\_axis[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html#mean-variance-axis "Link to this heading")

=======================================================================================================================================================================

sklearn.utils.sparsefuncs.mean\_variance\_axis(_X_, _axis_, _weights\=None_, _return\_sum\_weights\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/sparsefuncs.py#L101)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.sparsefuncs.mean_variance_axis.html#sklearn.utils.sparsefuncs.mean_variance_axis "Link to this definition")

Compute mean and variance along an axis on a CSR or CSC matrix.

Parameters:

**X**sparse matrix of shape (n\_samples, n\_features)

Input data. It can be of CSR or CSC format.

**axis**{0, 1}

Axis along which the axis should be computed.

**weights**ndarray of shape (n\_samples,) or (n\_features,), default=None

If axis is set to 0 shape is (n\_samples,) or if axis is set to 1 shape is (n\_features,). If it is set to None, then samples are equally weighted.

Added in version 0.24.

**return\_sum\_weights**bool, default=False

If True, returns the sum of weights seen for each feature if `axis=0` or each sample if `axis=1`.

Added in version 0.24.

Returns:

**means**ndarray of shape (n\_features,), dtype=floating

Feature-wise means.

**variances**ndarray of shape (n\_features,), dtype=floating

Feature-wise variances.

**sum\_weights**ndarray of shape (n\_features,), dtype=floating

Returned if `return_sum_weights` is `True`.

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
\>>> sparsefuncs.mean\_variance\_axis(csr, axis\=0)
(array(\[2.  , 0.25, 1.75\]), array(\[12.    ,  0.1875,  4.1875\]))

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)