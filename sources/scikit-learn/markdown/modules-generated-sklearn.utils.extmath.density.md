[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.density.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.extmath.density.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.density.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.extmath.density.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.extmath.density.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.extmath.density.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.extmath.density.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.extmath.density.html)

Collapse Sidebar Expand Sidebar

density[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.density.html#density "Link to this heading")

================================================================================================================================

sklearn.utils.extmath.density(_w_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/extmath.py#L138)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.density.html#sklearn.utils.extmath.density "Link to this definition")

Compute density of a sparse vector.

Parameters:

**w**{ndarray, sparse matrix}

The input data can be numpy ndarray or a sparse matrix.

Returns:

float

The density of w, between 0 and 1.

Examples

\>>> from scipy import sparse
\>>> from sklearn.utils.extmath import density
\>>> X \= sparse.random\_array((10, 10), density\=0.25, rng\=0)
\>>> density(X)
0.25

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.density.html#gallery-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_document_classification_20newsgroups_thumb.png)

[Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html)

Classification of text documents using sparse features

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)