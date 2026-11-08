[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.EstimatorCheckFailedWarning.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.exceptions.EstimatorCheckFailedWarning.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.EstimatorCheckFailedWarning.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.exceptions.EstimatorCheckFailedWarning.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.exceptions.EstimatorCheckFailedWarning.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.exceptions.EstimatorCheckFailedWarning.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.exceptions.EstimatorCheckFailedWarning.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.exceptions.EstimatorCheckFailedWarning.html)

Collapse Sidebar Expand Sidebar

EstimatorCheckFailedWarning[#](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.EstimatorCheckFailedWarning.html#estimatorcheckfailedwarning "Link to this heading")

=========================================================================================================================================================================================

exception sklearn.exceptions.EstimatorCheckFailedWarning(_\*_, _estimator_, _check\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
_, _exception: [Exception](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)")
_, _status: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
_, _expected\_to\_fail: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
_, _expected\_to\_fail\_reason: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/exceptions.py#L195)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.EstimatorCheckFailedWarning.html#sklearn.exceptions.EstimatorCheckFailedWarning "Link to this definition")

Warning raised when an estimator check from the common tests fails.

Parameters:

**estimator**estimator object

Estimator instance for which the test failed.

**check\_name**str

Name of the check that failed.

**exception**Exception

Exception raised by the failed check.

**status**str

Status of the check.

**expected\_to\_fail**bool

Whether the check was expected to fail.

**expected\_to\_fail\_reason**str

Reason for the expected failure.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)