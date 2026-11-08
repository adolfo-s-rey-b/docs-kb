[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.column_or_1d.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.validation.column_or_1d.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.column_or_1d.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.validation.column_or_1d.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.validation.column_or_1d.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.validation.column_or_1d.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.validation.column_or_1d.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.validation.column_or_1d.html)

Collapse Sidebar Expand Sidebar

column\_or\_1d[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.column_or_1d.html#column-or-1d "Link to this heading")

====================================================================================================================================================

sklearn.utils.validation.column\_or\_1d(_y_, _\*_, _dtype\=None_, _input\_name\='y'_, _warn\=False_, _device\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L1377)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.column_or_1d.html#sklearn.utils.validation.column_or_1d "Link to this definition")

Ravel column or 1d numpy array, else raises an error.

Parameters:

**y**array-like

Input data.

**dtype**data-type, default=None

Data type for `y`.

Added in version 1.2.

**input\_name**str, default=”y”

The data name used to construct the error message.

Added in version 1.8.

**warn**bool, default=False

To control display of warnings.

**device**device, default=None

`device` object. See the [Array API User Guide](https://scikit-learn.org/stable/modules/array_api.html#array-api)
 for more details.

Added in version 1.6.

Returns:

**y**ndarray

Output data.

Raises:

ValueError

If `y` is not a 1D array or a 2D array with a single row or column.

Examples

\>>> from sklearn.utils.validation import column\_or\_1d
\>>> column\_or\_1d(\[1, 1\])
array(\[1, 1\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)