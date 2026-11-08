[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.validation.validate_data.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.validation.validate_data.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.validation.validate_data.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.validation.validate_data.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.validation.validate_data.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.validation.validate_data.html)

Collapse Sidebar Expand Sidebar

validate\_data[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html#validate-data "Link to this heading")

======================================================================================================================================================

sklearn.utils.validation.validate\_data(_\_estimator_, _/_, _X\='no\_validation'_, _y\='no\_validation'_, _reset\=True_, _validate\_separately\=False_, _skip\_check\_array\=False_, _\*\*check\_params_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/validation.py#L2932)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html#sklearn.utils.validation.validate_data "Link to this definition")

Validate input data and set or check feature names and counts of the input.

This helper function should be used in an estimator that requires input validation. This mutates the estimator and sets the `n_features_in_` and `feature_names_in_` attributes if `reset=True`.

Added in version 1.6.

Parameters:

**\_estimator**estimator instance

The estimator to validate the input for.

**X**{array-like, sparse matrix, dataframe} of shape (n\_samples, n\_features), default=’no validation’

The input samples. If `'no_validation'`, no validation is performed on `X`. This is useful for meta-estimator which can delegate input validation to their underlying estimator(s). In that case `y` must be passed and the only accepted `check_params` are `multi_output` and `y_numeric`.

**y**array-like of shape (n\_samples,), default=’no\_validation’

The targets.

*   If `None`, [`check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     is called on `X`. If the estimator’s `requires_y` tag is True, then an error will be raised.
    
*   If `'no_validation'`, [`check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     is called on `X` and the estimator’s `requires_y` tag is ignored. This is a default placeholder and is never meant to be explicitly set. In that case `X` must be passed.
    
*   Otherwise, only `y` with `_check_y` or both `X` and `y` are checked with either [`check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
     or [`check_X_y`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "sklearn.utils.check_X_y")
     depending on `validate_separately`.
    

**reset**bool, default=True

Whether to reset the `n_features_in_` attribute. If False, the input will be checked for consistency with data provided when reset was last True.

Note

It is recommended to call `reset=True` in `fit` and in the first call to `partial_fit`. All other methods that validate `X` should set `reset=False`.

**validate\_separately**False or tuple of dicts, default=False

Only used if `y` is not `None`. If `False`, call [`check_X_y`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "sklearn.utils.check_X_y")
. Else, it must be a tuple of kwargs to be used for calling [`check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
 on `X` and `y` respectively.

`estimator=self` is automatically added to these dicts to generate more informative error message in case of invalid input data.

**skip\_check\_array**bool, default=False

If `True`, `X` and `y` are unchanged and only `feature_names_in_` and `n_features_in_` are checked. Otherwise, [`check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
 is called on `X` and `y`.

**\*\*check\_params**kwargs

Parameters passed to [`check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array")
 or [`check_X_y`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "sklearn.utils.check_X_y")
. Ignored if validate\_separately is not False.

`estimator=self` is automatically added to these params to generate more informative error message in case of invalid input data.

Returns:

**out**{ndarray, sparse matrix} or tuple of these

The validated input. A tuple is returned if both `X` and `y` are validated.

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.validate_data.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_callback_support_thumb.png)

[Supporting callbacks in third party estimators](https://scikit-learn.org/stable/auto_examples/callbacks/plot_callback_support.html)

Supporting callbacks in third party estimators

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