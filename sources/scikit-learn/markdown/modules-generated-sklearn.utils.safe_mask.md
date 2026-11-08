[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_mask.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.safe_mask.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_mask.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.safe_mask.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.safe_mask.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.safe_mask.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.safe_mask.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.safe_mask.html)

Collapse Sidebar Expand Sidebar

safe\_mask[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_mask.html#safe-mask "Link to this heading")

===============================================================================================================================

sklearn.utils.safe\_mask(_X_, _mask_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_mask.py#L71)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.safe_mask.html#sklearn.utils.safe_mask "Link to this definition")

Return an indexing mask compatible with X.

Parameters:

**X**{array-like, sparse matrix}

Data on which to apply mask.

**mask**array-like

Mask to be used on X.

Returns:

**mask**ndarray

Array that is safe to use on X.

Examples

\>>> from sklearn.utils import safe\_mask
\>>> from scipy.sparse import csr\_array
\>>> data \= csr\_array(\[\[1\], \[2\], \[3\], \[4\], \[5\]\])
\>>> condition \= \[False, True, True, False, True\]
\>>> mask \= safe\_mask(data, condition)
\>>> data\[mask\].toarray()
array(\[\[2\],\
       \[3\],\
       \[5\]\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)