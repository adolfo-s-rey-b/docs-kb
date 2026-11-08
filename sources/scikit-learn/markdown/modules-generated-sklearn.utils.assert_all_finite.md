[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.assert_all_finite.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.assert_all_finite.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.assert_all_finite.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.assert_all_finite.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.assert_all_finite.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.assert_all_finite.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.assert_all_finite.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.assert_all_finite.html)

Collapse Sidebar Expand Sidebar

assert\_all\_finite[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.assert_all_finite.html#assert-all-finite "Link to this heading")

========================================================================================================================================================

sklearn.utils.assert\_all\_finite(_X_, _\*_, _allow\_nan\=False_, _estimator\_name\=None_, _input\_name\=''_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L189)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.assert_all_finite.html#sklearn.utils.assert_all_finite "Link to this definition")

Throw a ValueError if X contains NaN or infinity.

Parameters:

**X**{ndarray, sparse matrix}

The input data.

**allow\_nan**bool, default=False

If True, do not throw error when `X` contains NaN.

**estimator\_name**str, default=None

The estimator name, used to construct the error message.

**input\_name**str, default=””

The data name used to construct the error message. In particular if `input_name` is “X” and the data has NaN values and allow\_nan is False, the error message will link to the imputer documentation.

Examples

\>>> from sklearn.utils import assert\_all\_finite
\>>> import numpy as np
\>>> array \= np.array(\[1, np.inf, np.nan, 4\])
\>>> try:
...     assert\_all\_finite(array)
...     print("Test passed: Array contains only finite values.")
... except ValueError:
...     print("Test failed: Array contains non-finite values.")
Test failed: Array contains non-finite values.

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)