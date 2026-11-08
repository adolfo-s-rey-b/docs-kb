[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.tree.export_text.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.tree.export_text.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.tree.export_text.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.tree.export_text.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.tree.export_text.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.tree.export_text.html)

Collapse Sidebar Expand Sidebar

export\_text[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html#export-text "Link to this heading")

====================================================================================================================================

sklearn.tree.export\_text(_decision\_tree_, _\*_, _feature\_names\=None_, _class\_names\=None_, _max\_depth\=10_, _spacing\=3_, _decimals\=2_, _show\_weights\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/tree/_export.py#L987)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html#sklearn.tree.export_text "Link to this definition")

Build a text report showing the rules of a decision tree.

Note that backwards compatibility may not be supported.

Parameters:

**decision\_tree**object

The decision tree estimator to be exported. It can be an instance of DecisionTreeClassifier or DecisionTreeRegressor.

**feature\_names**array-like of shape (n\_features,), default=None

An array containing the feature names. If None generic names will be used (“feature\_0”, “feature\_1”, …).

**class\_names**array-like of shape (n\_classes,), default=None

Names of each of the target classes in ascending numerical order. Only relevant for classification and not supported for multi-output.

*   if `None`, the class names are delegated to `decision_tree.classes_`;
    
*   otherwise, `class_names` will be used as class names instead of `decision_tree.classes_`. The length of `class_names` must match the length of `decision_tree.classes_`.
    

Added in version 1.3.

**max\_depth**int, default=10

Only the first max\_depth levels of the tree are exported. Truncated branches will be marked with “…”.

**spacing**int, default=3

Number of spaces between edges. The higher it is, the wider the result.

**decimals**int, default=2

Number of decimal digits to display.

**show\_weights**bool, default=False

If true the classification weights will be exported on each leaf. The classification weights are the number of samples each class.

Returns:

**report**str

Text summary of all the rules in the decision tree.

Examples

\>>> from sklearn.datasets import load\_iris
\>>> from sklearn.tree import DecisionTreeClassifier
\>>> from sklearn.tree import export\_text
\>>> iris \= load\_iris()
\>>> X \= iris\['data'\]
\>>> y \= iris\['target'\]
\>>> decision\_tree \= DecisionTreeClassifier(random\_state\=0, max\_depth\=2)
\>>> decision\_tree \= decision\_tree.fit(X, y)
\>>> r \= export\_text(decision\_tree, feature\_names\=iris\['feature\_names'\])
\>>> print(r)
|--- petal width (cm) <= 0.80
|   |--- class: 0
|--- petal width (cm) >  0.80
|   |--- petal width (cm) <= 1.75
|   |   |--- class: 1
|   |--- petal width (cm) >  1.75
|   |   |--- class: 2

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)