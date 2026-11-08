[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.as_float_array.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.as_float_array.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.as_float_array.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.as_float_array.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.as_float_array.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.as_float_array.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.as_float_array.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.as_float_array.html)

Collapse Sidebar Expand Sidebar

as\_float\_array[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.as_float_array.html#as-float-array "Link to this heading")

===============================================================================================================================================

sklearn.utils.as\_float\_array(_X_, _\*_, _copy\=True_, _ensure\_all\_finite\=True_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L235)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.as_float_array.html#sklearn.utils.as_float_array "Link to this definition")

Convert an array-like to an array of floats.

The new dtype will be np.float32 or np.float64, depending on the original type. The function can create a copy or modify the argument depending on the argument copy.

Parameters:

**X**{array-like, sparse matrix}

The input data.

**copy**bool, default=True

If True, a copy of X will be created. If False, a copy may still be returned if X’s dtype is not a floating point type.

**ensure\_all\_finite**bool or ‘allow-nan’, default=True

Whether to raise an error on np.inf, np.nan, pd.NA in X. The possibilities are:

*   True: Force all values of X to be finite.
    
*   False: accepts np.inf, np.nan, pd.NA in X.
    
*   ‘allow-nan’: accepts only np.nan and pd.NA values in X. Values cannot be infinite.
    

Added in version 1.6: `force_all_finite` was renamed to `ensure_all_finite`.

Returns:

**XT**{ndarray, sparse matrix}

An array of type float.

Examples

\>>> from sklearn.utils import as\_float\_array
\>>> import numpy as np
\>>> array \= np.array(\[0, 0, 1, 2, 2\], dtype\=np.int64)
\>>> as\_float\_array(array)
array(\[0., 0., 1., 2., 2.\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)