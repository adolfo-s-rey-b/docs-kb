[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.estimator_checks.check_estimator.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.estimator_checks.check_estimator.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.estimator_checks.check_estimator.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.estimator_checks.check_estimator.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.estimator_checks.check_estimator.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.estimator_checks.check_estimator.html)

Collapse Sidebar Expand Sidebar

check\_estimator[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#check-estimator "Link to this heading")

==================================================================================================================================================================

sklearn.utils.estimator\_checks.check\_estimator(_estimator\=None_, _\*_, _legacy: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= True_, _expected\_failed\_checks: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")
\[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
, [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")\
\] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_, _on\_skip: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['warn'\] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= 'warn'_, _on\_fail: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")
\['raise', 'warn'\] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= 'raise'_, _callback: [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")
 | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 \= None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/estimator_checks.py#L736)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "Link to this definition")

Check if estimator adheres to scikit-learn conventions.

This function will run an extensive test-suite for input validation, shapes, etc, making sure that the estimator complies with `scikit-learn` conventions as detailed in [Rolling your own estimator](https://scikit-learn.org/stable/developers/develop.html#rolling-your-own-estimator)
. Additional tests for classifiers, regressors, clustering or transformers will be run if the Estimator class inherits from the corresponding mixin from sklearn.base.

scikit-learn also provides a pytest specific decorator, [`parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")
, making it easier to test multiple estimators.

Checks are categorised into the following groups:

*   API checks: a set of checks to ensure API compatibility with scikit-learn. Refer to [https://scikit-learn.org/dev/developers/develop.html](https://scikit-learn.org/dev/developers/develop.html)
     a requirement of scikit-learn estimators.
    
*   legacy: a set of checks which gradually will be grouped into other categories.
    

Parameters:

**estimator**estimator object

Estimator instance to check.

**legacy**bool, default=True

Whether to include legacy checks. Over time we remove checks from this category and move them into their specific category.

Added in version 1.6.

**expected\_failed\_checks**dict, default=None

A dictionary of the form:

{
    "check\_name": "this check is expected to fail because ...",
}

Copy to clipboard

Where `"check_name"` is the name of the check, and `"my reason"` is why the check fails.

Added in version 1.6.

**on\_skip**“warn”, None, default=”warn”

This parameter controls what happens when a check is skipped.

*   “warn”: A `SkipTestWarning` is logged and running tests continue.
    
*   None: No warning is logged and running tests continue.
    

Added in version 1.6.

**on\_fail**{“raise”, “warn”}, None, default=”raise”

This parameter controls what happens when a check fails.

*   “raise”: The exception raised by the first failing check is raised and running tests are aborted. This does not included tests that are expected to fail.
    
*   “warn”: A [`EstimatorCheckFailedWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.EstimatorCheckFailedWarning.html#sklearn.exceptions.EstimatorCheckFailedWarning "sklearn.exceptions.EstimatorCheckFailedWarning")
     is logged and running tests continue.
    
*   None: No exception is raised and no warning is logged.
    

Note that if `on_fail != "raise"`, no exception is raised, even if the checks fail. You’d need to inspect the return result of `check_estimator` to check if any checks failed.

Added in version 1.6.

**callback**callable, or None, default=None

This callback will be called with the estimator and the check name, the exception (if any), the status of the check (xfail, failed, skipped, passed), and the reason for the expected failure if the check is expected to fail. The callable’s signature needs to be:

def callback(
    estimator,
    check\_name: str,
    exception: Exception,
    status: Literal\["xfail", "failed", "skipped", "passed"\],
    expected\_to\_fail: bool,
    expected\_to\_fail\_reason: str,
)

Copy to clipboard

`callback` cannot be provided together with `on_fail="raise"`.

Added in version 1.6.

Returns:

**test\_results**list

List of dictionaries with the results of the failing tests, of the form:

{
    "estimator": estimator,
    "check\_name": check\_name,
    "exception": exception,
    "status": status (one of "xfail", "failed", "skipped", "passed"),
    "expected\_to\_fail": expected\_to\_fail,
    "expected\_to\_fail\_reason": expected\_to\_fail\_reason,
}

Copy to clipboard

Raises:

Exception

If `on_fail="raise"`, the exception raised by the first failing check is raised and running tests are aborted.

Note that if `on_fail != "raise"`, no exception is raised, even if the checks fail. You’d need to inspect the return result of `check_estimator` to check if any checks failed.

See also

[`parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks")

Pytest specific decorator for parametrizing estimator checks.

[`estimator_checks_generator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html#sklearn.utils.estimator_checks.estimator_checks_generator "sklearn.utils.estimator_checks.estimator_checks_generator")

Generator that yields (estimator, check) tuples.

Examples

\>>> from sklearn.utils.estimator\_checks import check\_estimator
\>>> from sklearn.linear\_model import LogisticRegression
\>>> check\_estimator(LogisticRegression())
\[...\]

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#gallery-examples "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

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