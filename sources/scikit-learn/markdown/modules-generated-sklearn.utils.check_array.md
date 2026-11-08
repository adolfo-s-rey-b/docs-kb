[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.check_array.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.check_array.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.check_array.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.check_array.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.check_array.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.check_array.html)

Collapse Sidebar Expand Sidebar

check\_array[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#check-array "Link to this heading")

=====================================================================================================================================

sklearn.utils.check\_array(_array_, _accept\_sparse\=False_, _\*_, _accept\_large\_sparse\=True_, _dtype\='numeric'_, _order\=None_, _copy\=False_, _force\_writeable\=False_, _ensure\_all\_finite\=True_, _ensure\_non\_negative\=False_, _ensure\_2d\=True_, _allow\_nd\=False_, _ensure\_min\_samples\=1_, _ensure\_min\_features\=1_, _estimator\=None_, _input\_name\=''_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L733)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "Link to this definition")

Input validation on an array, list, sparse matrix or similar.

By default, the input is checked to be a non-empty 2D array containing only finite values. If the dtype of the array is object, attempt converting to float, raising on failure.

Parameters:

**array**object

Input object to check / convert.

**accept\_sparse**str, bool or list/tuple of str, default=False

String\[s\] representing allowed sparse matrix formats, such as ‘csc’, ‘csr’, etc. If the input is sparse but not in the allowed format, it will be converted to the first listed format. True allows the input to be any format. False means that a sparse matrix input will raise an error.

**accept\_large\_sparse**bool, default=True

If a CSR, CSC, COO or BSR sparse matrix is supplied and accepted by accept\_sparse, accept\_large\_sparse=False will cause it to be accepted only if its indices are stored with a 32-bit dtype.

Added in version 0.20.

**dtype**‘numeric’, type, list of type or None, default=’numeric’

Data type of result. If None, the dtype of the input is preserved. If “numeric”, dtype is preserved unless array.dtype is object. If dtype is a list of types, conversion on the first type is only performed if the dtype of the input is not in the list.

**order**{‘F’, ‘C’} or None, default=None

Whether an array will be forced to be fortran or c-style. When order is None (default), then if copy=False, nothing is ensured about the memory layout of the output array; otherwise (copy=True) the memory layout of the returned array is kept as close as possible to the original array.

**copy**bool, default=False

Whether a forced copy will be triggered. If copy=False, a copy might be triggered by a conversion.

**force\_writeable**bool, default=False

Whether to force the output array to be writeable. If True, the returned array is guaranteed to be writeable, which may require a copy. Otherwise the writeability of the input array is preserved.

Added in version 1.6.

**ensure\_all\_finite**bool or ‘allow-nan’, default=True

Whether to raise an error on np.inf, np.nan, pd.NA in array. The possibilities are:

*   True: Force all values of array to be finite.
    
*   False: accepts np.inf, np.nan, pd.NA in array.
    
*   ‘allow-nan’: accepts only np.nan and pd.NA values in array. Values cannot be infinite.
    

Added in version 1.6: `force_all_finite` was renamed to `ensure_all_finite`.

**ensure\_non\_negative**bool, default=False

Make sure the array has only non-negative values. If True, an array that contains negative values will raise a ValueError.

Added in version 1.6.

**ensure\_2d**bool, default=True

Whether to raise a value error if array is not 2D.

**allow\_nd**bool, default=False

Whether to allow array.ndim > 2.

**ensure\_min\_samples**int, default=1

Make sure that the array has a minimum number of samples in its first axis (rows for a 2D array). Setting to 0 disables this check.

**ensure\_min\_features**int, default=1

Make sure that the 2D array has some minimum number of features (columns). The default value of 1 rejects empty datasets. This check is only enforced when the input data has effectively 2 dimensions or is originally 1D and `ensure_2d` is True. Setting to 0 disables this check.

**estimator**str or estimator instance, default=None

If passed, include the name of the estimator in warning messages.

**input\_name**str, default=””

The data name used to construct the error message. In particular if `input_name` is “X” and the data has NaN values and allow\_nan is False, the error message will link to the imputer documentation.

Added in version 1.1.0.

Returns:

**array\_converted**object

The converted and validated array: a numpy array, Array API compatible array, sparse array or sparse matrix.

Examples

\>>> from sklearn.utils.validation import check\_array
\>>> X \= \[\[1, 2, 3\], \[4, 5, 6\]\]
\>>> X\_checked \= check\_array(X)
\>>> X\_checked
array(\[\[1, 2, 3\], \[4, 5, 6\]\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_6_0_thumb.png)

[Release Highlights for scikit-learn 1.6](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)

Release Highlights for scikit-learn 1.6

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)