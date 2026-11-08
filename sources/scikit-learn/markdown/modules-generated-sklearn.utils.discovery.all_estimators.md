[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_estimators.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Collapse Sidebar Expand Sidebar

all\_estimators[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_estimators.html#all-estimators "Link to this heading")

========================================================================================================================================================

sklearn.utils.discovery.all\_estimators(_type\_filter\=None_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/discovery.py#L22)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.discovery.all_estimators.html#sklearn.utils.discovery.all_estimators "Link to this definition")

Get a list of all estimators from `sklearn`.

This function crawls the module and gets all classes that inherit from BaseEstimator. Classes that are defined in test-modules are not included.

Parameters:

**type\_filter**{“classifier”, “regressor”, “cluster”, “transformer”} or list of such str, default=None

Which kind of estimators should be returned. If None, no filter is applied and all estimators are returned. Possible values are ‘classifier’, ‘regressor’, ‘cluster’ and ‘transformer’ to get estimators only of these specific types, or a list of these to get the estimators that fit at least one of the types.

Returns:

**estimators**list of tuples

List of (name, class), where `name` is the class name as string and `class` is the actual type of the class.

Examples

\>>> from sklearn.utils.discovery import all\_estimators
\>>> estimators \= all\_estimators()
\>>> type(estimators)
<class 'list'>
\>>> type(estimators\[0\])
<class 'tuple'>
\>>> estimators\[:2\]
\[('ARDRegression', <class 'sklearn.linear\_model.\_bayes.ARDRegression'>),\
 ('AdaBoostClassifier',\
  <class 'sklearn.ensemble.\_weight\_boosting.AdaBoostClassifier'>)\]
\>>> classifiers \= all\_estimators(type\_filter\="classifier")
\>>> classifiers\[:2\]
\[('AdaBoostClassifier',\
  <class 'sklearn.ensemble.\_weight\_boosting.AdaBoostClassifier'>),\
 ('BaggingClassifier', <class 'sklearn.ensemble.\_bagging.BaggingClassifier'>)\]
\>>> regressors \= all\_estimators(type\_filter\="regressor")
\>>> regressors\[:2\]
\[('ARDRegression', <class 'sklearn.linear\_model.\_bayes.ARDRegression'>),\
 ('AdaBoostRegressor',\
  <class 'sklearn.ensemble.\_weight\_boosting.AdaBoostRegressor'>)\]
\>>> both \= all\_estimators(type\_filter\=\["classifier", "regressor"\])
\>>> both\[:2\]
\[('ARDRegression', <class 'sklearn.linear\_model.\_bayes.ARDRegression'>),\
 ('AdaBoostClassifier',\
  <class 'sklearn.ensemble.\_weight\_boosting.AdaBoostClassifier'>)\]

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)