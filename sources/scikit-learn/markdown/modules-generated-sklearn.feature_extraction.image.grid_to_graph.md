[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html)

Collapse Sidebar Expand Sidebar

grid\_to\_graph[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html#grid-to-graph "Link to this heading")

===============================================================================================================================================================

sklearn.feature\_extraction.image.grid\_to\_graph(_n\_x_, _n\_y_, _n\_z\=1_, _\*_, _mask\=None_, _return\_as\=<class 'scipy.sparse.\_coo.coo\_array'>_, _dtype\=<class 'int'>_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/image.py#L195)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.grid_to_graph.html#sklearn.feature_extraction.image.grid_to_graph "Link to this definition")

Graph of the pixel-to-pixel connections.

Edges exist if 2 voxels are connected.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_extraction.html#connectivity-graph-image)
.

Parameters:

**n\_x**int

Dimension in x axis.

**n\_y**int

Dimension in y axis.

**n\_z**int, default=1

Dimension in z axis.

**mask**ndarray of shape (n\_x, n\_y, n\_z), dtype=bool, default=None

An optional mask of the image, to consider only part of the pixels.

**return\_as**np.ndarray or a sparse matrix class, default=sparse.coo\_array

The class to use to build the returned adjacency matrix.

**dtype**dtype, default=int

The data of the returned sparse matrix. By default it is int.

Returns:

**graph**np.ndarray or a sparse matrix class

The computed adjacency matrix.

Examples

\>>> import numpy as np
\>>> from sklearn.feature\_extraction.image import grid\_to\_graph
\>>> shape\_img \= (4, 4, 1)
\>>> mask \= np.zeros(shape\=shape\_img, dtype\=bool)
\>>> mask\[\[1, 2\], \[1, 2\], :\] \= True
\>>> graph \= grid\_to\_graph(\*shape\_img, mask\=mask)
\>>> print(graph)
<COOrdinate sparse matrix of dtype 'int64'
  with 2 stored elements and shape (2, 2)>
  Coords    Values
  (0, 0)    1
  (1, 1)    1

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)