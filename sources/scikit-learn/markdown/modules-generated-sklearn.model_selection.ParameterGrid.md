[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.model_selection.ParameterGrid.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.model_selection.ParameterGrid.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.model_selection.ParameterGrid.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.model_selection.ParameterGrid.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.ParameterGrid.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.model_selection.ParameterGrid.html)

Collapse Sidebar Expand Sidebar

ParameterGrid[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html#parametergrid "Link to this heading")

====================================================================================================================================================

class sklearn.model\_selection.ParameterGrid(_param\_grid_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/model_selection/_search.py#L70)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html#sklearn.model_selection.ParameterGrid "Link to this definition")

Grid of parameters with a discrete number of values for each.

Can be used to iterate over parameter value combinations with the Python built-in function iter. The order of the generated parameter combinations is deterministic.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)
.

Parameters:

**param\_grid**dict of str to sequence, or sequence of such

The parameter grid to explore, as a dictionary mapping estimator parameters to sequences of allowed values.

An empty dict signifies default parameters.

A sequence of dicts signifies a sequence of grids to search, and is useful to avoid exploring parameter combinations that make no sense or have no effect. See the examples below.

See also

[`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")

Uses [`ParameterGrid`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html#sklearn.model_selection.ParameterGrid "sklearn.model_selection.ParameterGrid")
 to perform a full parallelized parameter search.

Examples

\>>> from sklearn.model\_selection import ParameterGrid
\>>> param\_grid \= {'a': \[1, 2\], 'b': \[True, False\]}
\>>> list(ParameterGrid(param\_grid)) \== (
...    \[{'a': 1, 'b': True}, {'a': 1, 'b': False},\
...     {'a': 2, 'b': True}, {'a': 2, 'b': False}\])
True

Copy to clipboard

\>>> grid \= \[{'kernel': \['linear'\]}, {'kernel': \['rbf'\], 'gamma': \[1, 10\]}\]
\>>> list(ParameterGrid(grid)) \== \[{'kernel': 'linear'},\
...                               {'kernel': 'rbf', 'gamma': 1},\
...                               {'kernel': 'rbf', 'gamma': 10}\]
True
\>>> ParameterGrid(grid)\[1\] \== {'kernel': 'rbf', 'gamma': 1}
True

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)