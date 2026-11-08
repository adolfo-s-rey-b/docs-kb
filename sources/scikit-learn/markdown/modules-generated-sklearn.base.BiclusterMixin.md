[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.base.BiclusterMixin.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.base.BiclusterMixin.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.base.BiclusterMixin.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.base.BiclusterMixin.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.base.BiclusterMixin.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.base.BiclusterMixin.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.base.BiclusterMixin.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.base.BiclusterMixin.html)

Collapse Sidebar Expand Sidebar

BiclusterMixin[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.BiclusterMixin.html#biclustermixin "Link to this heading")

============================================================================================================================================

class sklearn.base.BiclusterMixin[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L773)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.BiclusterMixin.html#sklearn.base.BiclusterMixin "Link to this definition")

Mixin class for all bicluster estimators in scikit-learn.

This mixin defines the following functionality:

*   `biclusters_` property that returns the row and column indicators;
    
*   `get_indices` method that returns the row and column indices of a bicluster;
    
*   `get_shape` method that returns the shape of a bicluster;
    
*   `get_submatrix` method that returns the submatrix corresponding to a bicluster.
    

Examples

\>>> import numpy as np
\>>> from sklearn.base import BaseEstimator, BiclusterMixin
\>>> class DummyBiClustering(BiclusterMixin, BaseEstimator):
...     def fit(self, X, y\=None):
...         self.rows\_ \= np.ones(shape\=(1, X.shape\[0\]), dtype\=bool)
...         self.columns\_ \= np.ones(shape\=(1, X.shape\[1\]), dtype\=bool)
...         return self
\>>> X \= np.array(\[\[1, 1\], \[2, 1\], \[1, 0\],\
...               \[4, 7\], \[3, 5\], \[3, 6\]\])
\>>> bicluster \= DummyBiClustering().fit(X)
\>>> hasattr(bicluster, "biclusters\_")
True
\>>> bicluster.get\_indices(0)
(array(\[0, 1, 2, 3, 4, 5\]), array(\[0, 1\]))

Copy to clipboard

get\_indices(_i_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L809)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.BiclusterMixin.html#sklearn.base.BiclusterMixin.get_indices "Link to this definition")

Row and column indices of the `i`’th bicluster.

Only works if `rows_` and `columns_` attributes exist.

Parameters:

**i**int

The index of the cluster.

Returns:

**row\_ind**ndarray, dtype=np.intp

Indices of rows in the dataset that belong to the bicluster.

**col\_ind**ndarray, dtype=np.intp

Indices of columns in the dataset that belong to the bicluster.

get\_shape(_i_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L830)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.BiclusterMixin.html#sklearn.base.BiclusterMixin.get_shape "Link to this definition")

Shape of the `i`’th bicluster.

Parameters:

**i**int

The index of the cluster.

Returns:

**n\_rows**int

Number of rows in the bicluster.

**n\_cols**int

Number of columns in the bicluster.

get\_submatrix(_i_, _data_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/base.py#L849)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.base.BiclusterMixin.html#sklearn.base.BiclusterMixin.get_submatrix "Link to this definition")

Return the submatrix corresponding to bicluster `i`.

Parameters:

**i**int

The index of the cluster.

**data**array-like of shape (n\_samples, n\_features)

The data.

Returns:

**submatrix**ndarray of shape (n\_rows, n\_cols)

The submatrix corresponding to bicluster `i`.

Notes

Works with sparse matrices. Only works if `rows_` and `columns_` attributes exist.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)