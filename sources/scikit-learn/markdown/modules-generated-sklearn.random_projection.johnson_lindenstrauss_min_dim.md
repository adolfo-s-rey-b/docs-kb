[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html)

Collapse Sidebar Expand Sidebar

johnson\_lindenstrauss\_min\_dim[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#johnson-lindenstrauss-min-dim "Link to this heading")

=========================================================================================================================================================================================================

sklearn.random\_projection.johnson\_lindenstrauss\_min\_dim(_n\_samples_, _\*_, _eps\=0.1_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/random_projection.py#L56)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#sklearn.random_projection.johnson_lindenstrauss_min_dim "Link to this definition")

Find a ‘safe’ number of components to randomly project to.

The distortion introduced by a random projection `p` only changes the distance between two points by a factor (1 +- eps) in a euclidean space with good probability. The projection `p` is an eps-embedding as defined by:

(1 - eps) ||u - v||^2 < ||p(u) - p(v)||^2 < (1 + eps) ||u - v||^2

Copy to clipboard

Where u and v are any rows taken from a dataset of shape (n\_samples, n\_features), eps is in \]0, 1\[ and p is a projection by a random Gaussian N(0, 1) matrix of shape (n\_components, n\_features) (or a sparse Achlioptas matrix).\
\
The minimum number of components to guarantee the eps-embedding is given by:\
\
n\_components >= 4 log(n\_samples) / (eps^2 / 2 - eps^3 / 3)\
\
Copy to clipboard\
\
Note that the number of dimensions is independent of the original number of features but instead depends on the size of the dataset: the larger the dataset, the higher is the minimal dimensionality of an eps-embedding.\
\
Read more in the [User Guide](https://scikit-learn.org/stable/modules/random_projection.html#johnson-lindenstrauss)\
.\
\
Parameters:\
\
**n\_samples**int or array-like of int\
\
Number of samples that should be an integer greater than 0. If an array is given, it will compute a safe number of components array-wise.\
\
**eps**float or array-like of shape (n\_components,), dtype=float, default=0.1\
\
Maximum distortion rate in the range (0, 1) as defined by the Johnson-Lindenstrauss lemma. If an array is given, it will compute a safe number of components array-wise.\
\
Returns:\
\
**n\_components**int or ndarray of int\
\
The minimal number of components to guarantee with good probability an eps-embedding with n\_samples.\
\
References\
\
\[1\]\
\
[https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss\_lemma](https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma)\
\
\[2\]\
\
[Sanjoy Dasgupta and Anupam Gupta, 1999, “An elementary proof of the Johnson-Lindenstrauss Lemma.”](https://citeseerx.ist.psu.edu/doc_view/pid/95cd464d27c25c9c8690b378b894d337cdf021f9)\
\
Examples\
\
\>>> from sklearn.random\_projection import johnson\_lindenstrauss\_min\_dim\
\>>> johnson\_lindenstrauss\_min\_dim(1e6, eps\=0.5)\
np.int64(663)\
\
Copy to clipboard\
\
\>>> johnson\_lindenstrauss\_min\_dim(1e6, eps\=\[0.5, 0.1, 0.01\])\
array(\[    663,   11841, 1112658\])\
\
Copy to clipboard\
\
\>>> johnson\_lindenstrauss\_min\_dim(\[1e4, 1e5, 1e6\], eps\=0.1)\
array(\[ 7894,  9868, 11841\])\
\
Copy to clipboard\
\
Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.johnson_lindenstrauss_min_dim.html#gallery-examples "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_thumb.png)\
\
[The Johnson-Lindenstrauss bound for embedding with random projections](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)\
\
The Johnson-Lindenstrauss bound for embedding with random projections\
\
On this page\
\
* * *\
\
scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)\
 by Probabl and other institutions.\
\
[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)