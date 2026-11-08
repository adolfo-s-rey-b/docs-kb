[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.check_X_y.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.check_X_y.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.check_X_y.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.check_X_y.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.check_X_y.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.check_X_y.html)

Collapse Sidebar Expand Sidebar

check\_X\_y[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#check-x-y "Link to this heading")

================================================================================================================================

sklearn.utils.check\_X\_y(_X_, _y_, _accept\_sparse\=False_, _\*_, _accept\_large\_sparse\=True_, _dtype\='numeric'_, _order\=None_, _copy\=False_, _force\_writeable\=False_, _ensure\_all\_finite\=True_, _ensure\_2d\=True_, _allow\_nd\=False_, _multi\_output\=False_, _ensure\_min\_samples\=1_, _ensure\_min\_features\=1_, _y\_numeric\=False_, _estimator\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L1186)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "Link to this definition")

Input validation for standard estimators.

Checks X and y for consistent length, enforces X to be 2D and y 1D. By default, X is checked to be non-empty and containing only finite values. Standard input checks are also applied to y, such as checking that y does not have np.nan or np.inf targets. For multi-label y, set multi\_output=True to allow 2D and sparse y. If the dtype of X is object, attempt converting to float, raising on failure.

Parameters:

**X**{ndarray, list, sparse matrix}

Input data.

**y**{ndarray, list, sparse matrix}

Labels.

**accept\_sparse**str, bool or list of str, default=False

String\[s\] representing allowed sparse matrix formats, such as ‘csc’, ‘csr’, etc. If the input is sparse but not in the allowed format, it will be converted to the first listed format. True allows the input to be any format. False means that a sparse matrix input will raise an error.

**accept\_large\_sparse**bool, default=True

If a CSR, CSC, COO or BSR sparse matrix is supplied and accepted by accept\_sparse, accept\_large\_sparse will cause it to be accepted only if its indices are stored with a 32-bit dtype.

Added in version 0.20.

**dtype**‘numeric’, type, list of type or None, default=’numeric’

Data type of result. If None, the dtype of the input is preserved. If “numeric”, dtype is preserved unless array.dtype is object. If dtype is a list of types, conversion on the first type is only performed if the dtype of the input is not in the list.

**order**{‘F’, ‘C’}, default=None

Whether an array will be forced to be fortran or c-style. If `None`, then the input data’s order is preserved when possible.

**copy**bool, default=False

Whether a forced copy will be triggered. If copy=False, a copy might be triggered by a conversion.

**force\_writeable**bool, default=False

Whether to force the output array to be writeable. If True, the returned array is guaranteed to be writeable, which may require a copy. Otherwise the writeability of the input array is preserved.

Added in version 1.6.

**ensure\_all\_finite**bool or ‘allow-nan’, default=True

Whether to raise an error on np.inf, np.nan, pd.NA in array. This parameter does not influence whether y can have np.inf, np.nan, pd.NA values. The possibilities are:

*   True: Force all values of X to be finite.
    
*   False: accepts np.inf, np.nan, pd.NA in X.
    
*   ‘allow-nan’: accepts only np.nan or pd.NA values in X. Values cannot be infinite.
    

Added in version 1.6: `force_all_finite` was renamed to `ensure_all_finite`.

**ensure\_2d**bool, default=True

Whether to raise a value error if X is not 2D.

**allow\_nd**bool, default=False

Whether to allow X.ndim > 2.

**multi\_output**bool, default=False

Whether to allow 2D y (array or sparse matrix). If false, y will be validated as a vector. y cannot have np.nan or np.inf values if multi\_output=True.

**ensure\_min\_samples**int, default=1

Make sure that X has a minimum number of samples in its first axis (rows for a 2D array).

**ensure\_min\_features**int, default=1

Make sure that the 2D array has some minimum number of features (columns). The default value of 1 rejects empty datasets. This check is only enforced when X has effectively 2 dimensions or is originally 1D and `ensure_2d` is True. Setting to 0 disables this check.

**y\_numeric**bool, default=False

Whether to ensure that y has a numeric type. If dtype of y is object, it is converted to float64. Should only be used for regression algorithms.

**estimator**str or estimator instance, default=None

If passed, include the name of the estimator in warning messages.

Returns:

**X\_converted**object

The converted and validated X.

**y\_converted**object

The converted and validated y.

Examples

\>>> from sklearn.utils.validation import check\_X\_y
\>>> X \= \[\[1, 2\], \[3, 4\], \[5, 6\]\]
\>>> y \= \[1, 2, 3\]
\>>> X, y \= check\_X\_y(X, y)
\>>> X
array(\[\[1, 2\],\
      \[3, 4\],\
      \[5, 6\]\])
\>>> y
array(\[1, 2, 3\])

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)