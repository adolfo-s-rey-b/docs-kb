[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html)

Collapse Sidebar Expand Sidebar

parametrize\_with\_checks[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#parametrize-with-checks "Link to this heading")

===========================================================================================================================================================================================

sklearn.utils.estimator\_checks.parametrize\_with\_checks(_estimators_, _\*_, _legacy: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= True_, _expected\_failed\_checks: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _xfail\_strict: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/estimator_checks.py#L626)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "Link to this definition")

Pytest specific decorator for parametrizing estimator checks.

Checks are categorised into the following groups:

*   API checks: a set of checks to ensure API compatibility with scikit-learn. Refer to [https://scikit-learn.org/dev/developers/develop.html](https://scikit-learn.org/dev/developers/develop.html)
     a requirement of scikit-learn estimators.
    
*   legacy: a set of checks which gradually will be grouped into other categories.
    

The `id` of each check is set to be a pprint version of the estimator and the name of the check with its keyword arguments. This allows to use `pytest -k` to specify which tests to run:

pytest test\_check\_estimators.py \-k check\_estimators\_fit\_returns\_self

Copy to clipboard

Parameters:

**estimators**list of estimators instances

Estimators to generated checks for.

Changed in version 0.24: Passing a class was deprecated in version 0.23, and support for classes was removed in 0.24. Pass an instance instead.

Added in version 0.24.

**legacy**bool, default=True

Whether to include legacy checks. Over time we remove checks from this category and move them into their specific category.

Added in version 1.6.

**expected\_failed\_checks**callable, default=None

A callable that takes an estimator as input and returns a dictionary of the form:

{
    "check\_name": "my reason",
}

Copy to clipboard

Where `"check_name"` is the name of the check, and `"my reason"` is why the check fails. These tests will be marked as xfail if the check fails.

Added in version 1.6.

**xfail\_strict**bool, default=None

Whether to run checks in xfail strict mode. If True, checks that are expected to fail but actually pass will lead to a test failure. If False, unexpectedly passing tests will be marked as xpass. If None, the default pytest behavior is used.

Added in version 1.8.

Returns:

**decorator**`pytest.mark.parametrize`

See also

[`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")

Check if estimator adheres to scikit-learn conventions.

Examples

\>>> from sklearn.utils.estimator\_checks import parametrize\_with\_checks
\>>> from sklearn.linear\_model import LogisticRegression
\>>> from sklearn.tree import DecisionTreeRegressor

Copy to clipboard

\>>> @parametrize\_with\_checks(\[LogisticRegression(),\
...                           DecisionTreeRegressor()\])
... def test\_sklearn\_compatible\_estimator(estimator, check):
...     check(estimator)

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)

[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)

Release Highlights for scikit-learn 0.22

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