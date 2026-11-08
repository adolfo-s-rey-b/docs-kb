[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.arrayfuncs.min_pos.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.arrayfuncs.min_pos.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.arrayfuncs.min_pos.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.arrayfuncs.min_pos.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.arrayfuncs.min_pos.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.arrayfuncs.min_pos.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.arrayfuncs.min_pos.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.arrayfuncs.min_pos.html)

Collapse Sidebar Expand Sidebar

min\_pos[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.arrayfuncs.min_pos.html#min-pos "Link to this heading")

====================================================================================================================================

sklearn.utils.arrayfuncs.min\_pos(_X_)[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.arrayfuncs.min_pos.html#sklearn.utils.arrayfuncs.min_pos "Link to this definition")

Find the minimum value of an array over positive values.

Returns the maximum representable value of the input dtype if none of the values are positive.

Parameters:

**X**ndarray of shape (n,)

Input array.

Returns:

**min\_val**float

The smallest positive value in the array, or the maximum representable value

of the input dtype if no positive values are found.

Examples

\>>> import numpy as np
\>>> from sklearn.utils.arrayfuncs import min\_pos
\>>> X \= np.array(\[0, \-1, 2, 3, \-4, 5\])
\>>> min\_pos(X)
2.0

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)