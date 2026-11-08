[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.is_multilabel.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.multiclass.is_multilabel.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.is_multilabel.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.multiclass.is_multilabel.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.multiclass.is_multilabel.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.multiclass.is_multilabel.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.multiclass.is_multilabel.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.multiclass.is_multilabel.html)

Collapse Sidebar Expand Sidebar

is\_multilabel[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.is_multilabel.html#is-multilabel "Link to this heading")

======================================================================================================================================================

sklearn.utils.multiclass.is\_multilabel(_y_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/multiclass.py#L138)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.is_multilabel.html#sklearn.utils.multiclass.is_multilabel "Link to this definition")

Check if `y` is in a multilabel format.

Parameters:

**y**ndarray of shape (n\_samples,)

Target values.

Returns:

**out**bool

Return `True`, if `y` is in a multilabel format, else `False`.

Examples

\>>> import numpy as np
\>>> from sklearn.utils.multiclass import is\_multilabel
\>>> is\_multilabel(\[0, 1, 0, 1\])
False
\>>> is\_multilabel(\[\[1\], \[0, 2\], \[\]\])
False
\>>> is\_multilabel(np.array(\[\[1, 0\], \[0, 0\]\]))
True
\>>> is\_multilabel(np.array(\[\[1\], \[0\], \[0\]\]))
False
\>>> is\_multilabel(np.array(\[\[1, 0, 0\]\]))
True

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)