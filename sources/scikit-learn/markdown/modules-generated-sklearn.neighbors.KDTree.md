[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.KDTree.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.neighbors.KDTree.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.neighbors.KDTree.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.neighbors.KDTree.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.KDTree.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.neighbors.KDTree.html)

Collapse Sidebar Expand Sidebar

KDTree[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#kdtree "Link to this heading")

=========================================================================================================================

class sklearn.neighbors.KDTree[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree "Link to this definition")

KDTree for fast generalized N-point problems

Read more in the [User Guide](https://scikit-learn.org/stable/modules/neighbors.html#unsupervised-neighbors)
.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

n\_samples is the number of points in the data set, and n\_features is the dimension of the parameter space. Note: if X is a C-contiguous array of doubles then data will not be copied. Otherwise, an internal copy will be made.

**leaf\_size**positive int, default=40

Number of points at which to switch to brute-force. Changing leaf\_size will not affect the results of a query, but can significantly impact the speed of a query and the memory required to store the constructed tree. The amount of memory needed to store the tree scales as approximately n\_samples / leaf\_size. For a specified `leaf_size`, a leaf node is guaranteed to satisfy `leaf_size <= n_points <= 2 * leaf_size`, except in the case that `n_samples < leaf_size`.

**metric**str or DistanceMetric64 object, default=’minkowski’

Metric to use for distance computation. Default is “minkowski”, which results in the standard Euclidean distance when p = 2. A [list of valid metrics](https://scikit-learn.org/stable/modules/neighbors.html#kdtree-and-balltree-classes)
 for KDTree is given by the attribute `valid_metrics`. See the documentation of [scipy.spatial.distance](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
 and the metrics listed in [`distance_metrics`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.distance_metrics.html#sklearn.metrics.pairwise.distance_metrics "sklearn.metrics.pairwise.distance_metrics")
 for more information on any distance metric.

**Additional keywords are passed to the distance metric class.**

**Note: Callable functions in the metric parameter are NOT supported for KDTree**

**and Ball Tree. Function call overhead will result in very poor performance.**

Attributes:

**data**memory view

The training data

**valid\_metrics: list of str**

List of valid distance metrics.

Examples

Query for k-nearest neighbors

\>>> import numpy as np
\>>> from sklearn.neighbors import KDTree
\>>> rng \= np.random.RandomState(0)
\>>> X \= rng.random\_sample((10, 3))  \# 10 points in 3 dimensions
\>>> tree \= KDTree(X, leaf\_size\=2)
\>>> dist, ind \= tree.query(X\[:1\], k\=3)
\>>> print(ind)  \# indices of 3 closest neighbors
\[0 3 1\]
\>>> print(dist)  \# distances to 3 closest neighbors
\[ 0.          0.19662693  0.29473397\]

Copy to clipboard

Pickle and Unpickle a tree. Note that the state of the tree is saved in the pickle operation: the tree needs not be rebuilt upon unpickling.

\>>> import numpy as np
\>>> import pickle
\>>> rng \= np.random.RandomState(0)
\>>> X \= rng.random\_sample((10, 3))  \# 10 points in 3 dimensions
\>>> tree \= KDTree(X, leaf\_size\=2)
\>>> s \= pickle.dumps(tree)
\>>> tree\_copy \= pickle.loads(s)
\>>> dist, ind \= tree\_copy.query(X\[:1\], k\=3)
\>>> print(ind)  \# indices of 3 closest neighbors
\[0 3 1\]
\>>> print(dist)  \# distances to 3 closest neighbors
\[ 0.          0.19662693  0.29473397\]

Copy to clipboard

Query for neighbors within a given radius

\>>> import numpy as np
\>>> rng \= np.random.RandomState(0)
\>>> X \= rng.random\_sample((10, 3))  \# 10 points in 3 dimensions
\>>> tree \= KDTree(X, leaf\_size\=2)
\>>> print(tree.query\_radius(X\[:1\], r\=0.3, count\_only\=True))
3
\>>> ind \= tree.query\_radius(X\[:1\], r\=0.3)
\>>> print(ind)  \# indices of neighbors within distance 0.3
\[3 0 1\]

Copy to clipboard

Compute a gaussian kernel density estimate:

\>>> import numpy as np
\>>> rng \= np.random.RandomState(42)
\>>> X \= rng.random\_sample((100, 3))
\>>> tree \= KDTree(X)
\>>> tree.kernel\_density(X\[:3\], h\=0.1, kernel\='gaussian')
array(\[ 6.94114649,  7.83281226,  7.2071716 \])

Copy to clipboard

Compute a two-point auto-correlation function

\>>> import numpy as np
\>>> rng \= np.random.RandomState(0)
\>>> X \= rng.random\_sample((30, 3))
\>>> r \= np.linspace(0, 1, 5)
\>>> tree \= KDTree(X)
\>>> tree.two\_point\_correlation(X, r)
array(\[ 30,  62, 278, 580, 820\])

Copy to clipboard

get\_arrays()[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree.get_arrays "Link to this definition")

Get data and node arrays.

Returns:

arrays: tuple of array

Arrays for storing tree data, index, node data and node bounds.

get\_n\_calls()[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree.get_n_calls "Link to this definition")

Get number of calls.

Returns:

n\_calls: int

number of distance computation calls

get\_tree\_stats()[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree.get_tree_stats "Link to this definition")

Get tree status.

Returns:

tree\_stats: tuple of int

(number of trims, number of leaves, number of splits)

kernel\_density(_X_, _h_, _kernel\='gaussian'_, _atol\=0_, _rtol\=1E-8_, _breadth\_first\=True_, _return\_log\=False_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree.kernel_density "Link to this definition")

Compute the kernel density estimate at points X with the given kernel, using the distance metric specified at tree creation.

Parameters:

**X**array-like of shape (n\_samples, n\_features)

An array of points to query. Last dimension should match dimension of training data.

**h**float

the bandwidth of the kernel

**kernel**str, default=”gaussian”

specify the kernel to use. Options are - ‘gaussian’ - ‘tophat’ - ‘epanechnikov’ - ‘exponential’ - ‘linear’ - ‘cosine’ Default is kernel = ‘gaussian’

**atol**float, default=0

Specify the desired absolute tolerance of the result. If the true result is `K_true`, then the returned result `K_ret` satisfies `abs(K_true - K_ret) < atol + rtol * K_ret` The default is zero (i.e. machine precision).

**rtol**float, default=1e-8

Specify the desired relative tolerance of the result. If the true result is `K_true`, then the returned result `K_ret` satisfies `abs(K_true - K_ret) < atol + rtol * K_ret` The default is `1e-8` (i.e. machine precision).

**breadth\_first**bool, default=False

If True, use a breadth-first search. If False (default) use a depth-first search. Breadth-first is generally faster for compact kernels and/or high tolerances.

**return\_log**bool, default=False

Return the logarithm of the result. This can be more accurate than returning the result itself for narrow kernels.

Returns:

**density**ndarray of shape X.shape\[:-1\]

The array of (log)-density evaluations

query(_X_, _k\=1_, _return\_distance\=True_, _dualtree\=False_, _breadth\_first\=False_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree.query "Link to this definition")

query the tree for the k nearest neighbors

Parameters:

**X**array-like of shape (n\_samples, n\_features)

An array of points to query

**k**int, default=1

The number of nearest neighbors to return

**return\_distance**bool, default=True

if True, return a tuple (d, i) of distances and indices if False, return array i

**dualtree**bool, default=False

if True, use the dual tree formalism for the query: a tree is built for the query points, and the pair of trees is used to efficiently search this space. This can lead to better performance as the number of points grows large.

**breadth\_first**bool, default=False

if True, then query the nodes in a breadth-first manner. Otherwise, query the nodes in a depth-first manner.

**sort\_results**bool, default=True

if True, then distances and indices of each point are sorted on return, so that the first column contains the closest points. Otherwise, neighbors are returned in an arbitrary order.

Returns:

**i**if return\_distance == False

**(d,i)**if return\_distance == True

**d**ndarray of shape X.shape\[:-1\] + (k,), dtype=double

Each entry gives the list of distances to the neighbors of the corresponding point.

**i**ndarray of shape X.shape\[:-1\] + (k,), dtype=int

Each entry gives the list of indices of neighbors of the corresponding point.

query\_radius(_X_, _r_, _return\_distance\=False_, _count\_only\=False_, _sort\_results\=False_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree.query_radius "Link to this definition")

query the tree for neighbors within a radius r

Parameters:

**X**array-like of shape (n\_samples, n\_features)

An array of points to query

**r**distance within which neighbors are returned

r can be a single value, or an array of values of shape x.shape\[:-1\] if different radii are desired for each point.

**return\_distance**bool, default=False

if True, return distances to neighbors of each point if False, return only neighbors Note that unlike the query() method, setting return\_distance=True here adds to the computation time. Not all distances need to be calculated explicitly for return\_distance=False. Results are not sorted by default: see `sort_results` keyword.

**count\_only**bool, default=False

if True, return only the count of points within distance r if False, return the indices of all points within distance r If return\_distance==True, setting count\_only=True will result in an error.

**sort\_results**bool, default=False

if True, the distances and indices will be sorted before being returned. If False, the results will not be sorted. If return\_distance == False, setting sort\_results = True will result in an error.

Returns:

**count**if count\_only == True

**ind**if count\_only == False and return\_distance == False

**(ind, dist)**if count\_only == False and return\_distance == True

**count**ndarray of shape X.shape\[:-1\], dtype=int

Each entry gives the number of neighbors within a distance r of the corresponding point.

**ind**ndarray of shape X.shape\[:-1\], dtype=object

Each element is a numpy integer array listing the indices of neighbors of the corresponding point. Note that unlike the results of a k-neighbors query, the returned neighbors are not sorted by distance by default.

**dist**ndarray of shape X.shape\[:-1\], dtype=object

Each element is a numpy double array listing the distances corresponding to indices in i.

reset\_n\_calls()[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree.reset_n_calls "Link to this definition")

Reset number of calls to 0.

two\_point\_correlation(_X_, _r_, _dualtree\=False_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KDTree.html#sklearn.neighbors.KDTree.two_point_correlation "Link to this definition")

Compute the two-point correlation function

Parameters:

**X**array-like of shape (n\_samples, n\_features)

An array of points to query. Last dimension should match dimension of training data.

**r**array-like

A one-dimensional array of distances

**dualtree**bool, default=False

If True, use a dualtree algorithm. Otherwise, use a single-tree algorithm. Dual tree algorithms can have better scaling for large N.

Returns:

**counts**ndarray

counts\[i\] contains the number of pairs of points with distance less than or equal to r\[i\]

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)