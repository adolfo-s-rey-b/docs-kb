[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.weighted_mode.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.extmath.weighted_mode.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.weighted_mode.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.extmath.weighted_mode.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.extmath.weighted_mode.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.extmath.weighted_mode.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.extmath.weighted_mode.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.extmath.weighted_mode.html)

Collapse Sidebar Expand Sidebar

weighted\_mode[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.weighted_mode.html#weighted-mode "Link to this heading")

===================================================================================================================================================

sklearn.utils.extmath.weighted\_mode(_a_, _w_, _\*_, _axis\=0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/extmath.py#L791)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.weighted_mode.html#sklearn.utils.extmath.weighted_mode "Link to this definition")

Return an array of the weighted modal (most common) value in the passed array.

If there is more than one such value, only the first is returned. The bin-count for the modal bins is also returned.

This is an extension of the algorithm in scipy.stats.mode.

Parameters:

**a**array-like of shape (n\_samples,)

Array of which values to find mode(s).

**w**array-like of shape (n\_samples,)

Array of weights for each value.

**axis**int, default=0

Axis along which to operate. Default is 0, i.e. the first axis.

Returns:

**vals**ndarray

Array of modal values.

**score**ndarray

Array of weighted counts for each mode.

See also

[`scipy.stats.mode`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mode.html#scipy.stats.mode "(in SciPy v1.18.0)")

Calculates the Modal (most common) value of array elements along specified axis.

Examples

\>>> from sklearn.utils.extmath import weighted\_mode
\>>> x \= \[4, 1, 4, 2, 4, 2\]
\>>> weights \= \[1, 1, 1, 1, 1, 1\]
\>>> weighted\_mode(x, weights)
(array(\[4.\]), array(\[3.\]))

Copy to clipboard

The value 4 appears three times: with uniform weights, the result is simply the mode of the distribution.

\>>> weights \= \[1, 3, 0.5, 1.5, 1, 2\]  \# deweight the 4's
\>>> weighted\_mode(x, weights)
(array(\[2.\]), array(\[3.5\]))

Copy to clipboard

The value 2 has the highest score: it appears twice with weights of 1.5 and 2: the sum of these is 3.5.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)