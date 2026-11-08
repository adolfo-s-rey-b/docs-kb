[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.img_to_graph.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.image.img_to_graph.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.img_to_graph.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.feature_extraction.image.img_to_graph.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.feature_extraction.image.img_to_graph.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.feature_extraction.image.img_to_graph.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.image.img_to_graph.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.feature_extraction.image.img_to_graph.html)

Collapse Sidebar Expand Sidebar

img\_to\_graph[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.img_to_graph.html#img-to-graph "Link to this heading")

============================================================================================================================================================

sklearn.feature\_extraction.image.img\_to\_graph(_img_, _\*_, _mask\=None_, _return\_as\=<class 'scipy.sparse.\_coo.coo\_array'>_, _dtype\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/feature_extraction/image.py#L143)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.image.img_to_graph.html#sklearn.feature_extraction.image.img_to_graph "Link to this definition")

Graph of the pixel-to-pixel gradient connections.

Edges are weighted with the gradient values.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/feature_extraction.html#image-feature-extraction)
.

Parameters:

**img**array-like of shape (height, width) or (height, width, channel)

2D or 3D image.

**mask**ndarray of shape (height, width) or (height, width, channel), dtype=bool, default=None

An optional mask of the image, to consider only part of the pixels.

**return\_as**np.ndarray or a sparse matrix class, default=sparse.coo\_array

The class to use to build the returned adjacency matrix.

**dtype**dtype, default=None

The data of the returned sparse matrix. By default it is the dtype of img.

Returns:

**graph**ndarray or a sparse matrix class

The computed adjacency matrix.

Examples

\>>> import numpy as np
\>>> from sklearn.feature\_extraction.image import img\_to\_graph
\>>> img \= np.array(\[\[0, 0\], \[0, 1\]\])
\>>> img\_to\_graph(img, return\_as\=np.ndarray)
array(\[\[0, 0, 0, 0\],\
       \[0, 0, 0, 1\],\
       \[0, 0, 0, 1\],\
       \[0, 1, 1, 1\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)