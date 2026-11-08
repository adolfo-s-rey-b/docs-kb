[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html)

Collapse Sidebar Expand Sidebar

estimator\_checks\_generator[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html#estimator-checks-generator "Link to this heading")

====================================================================================================================================================================================================

sklearn.utils.estimator\_checks.estimator\_checks\_generator(_estimator_, _\*_, _legacy: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= True_, _expected\_failed\_checks: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")
\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
, [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
\] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _mark: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['xfail', 'skip', None\] \= None_, _xfail\_strict: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/estimator_checks.py#L557)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html#sklearn.utils.estimator_checks.estimator_checks_generator "Link to this definition")

Iteratively yield all check callables for an estimator.

This function is used by [`parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")
 and [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")
 to yield all check callables for an estimator. In most cases, these functions should be used instead. When implementing a custom equivalent, please refer to their source code to understand how `estimator_checks_generator` is intended to be used.

Added in version 1.6.

Parameters:

**estimator**estimator object

Estimator instance for which to generate checks.

**legacy**bool, default=True

Whether to include legacy checks. Over time we remove checks from this category and move them into their specific category.

**expected\_failed\_checks**dict\[str, str\], default=None

Dictionary of the form {check\_name: reason} for checks that are expected to fail.

**mark**{“xfail”, “skip”} or None, default=None

Whether to mark the checks that are expected to fail as xfail(`pytest.mark.xfail`) or skip. Marking a test as “skip” is done via wrapping the check in a function that raises a `SkipTest` exception.

**xfail\_strict**bool, default=None

Whether to run checks in xfail strict mode. This option is ignored unless `mark="xfail"`. If True, checks that are expected to fail but actually pass will lead to a test failure. If False, unexpectedly passing tests will be marked as xpass. If None, the default pytest behavior is used.

Added in version 1.8.

Returns:

**estimator\_checks\_generator**generator

Generator that yields (estimator, check) tuples.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)