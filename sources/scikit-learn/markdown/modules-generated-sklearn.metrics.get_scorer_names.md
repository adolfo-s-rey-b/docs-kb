[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer_names.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.get_scorer_names.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer_names.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.get_scorer_names.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.get_scorer_names.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.get_scorer_names.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.get_scorer_names.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.get_scorer_names.html)

Collapse Sidebar Expand Sidebar

get\_scorer\_names[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer_names.html#get-scorer-names "Link to this heading")

=======================================================================================================================================================

sklearn.metrics.get\_scorer\_names()[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_scorer.py#L893)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer_names.html#sklearn.metrics.get_scorer_names "Link to this definition")

Get the names of all available scorers.

These names can be passed to [`get_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#sklearn.metrics.get_scorer "sklearn.metrics.get_scorer")
 to retrieve the scorer object.

Returns:

list of str

Names of all available scorers.

Examples

\>>> from sklearn.metrics import get\_scorer\_names
\>>> all\_scorers \= get\_scorer\_names()
\>>> type(all\_scorers)
<class 'list'>
\>>> all\_scorers\[:3\]
\['accuracy', 'adjusted\_mutual\_info\_score', 'adjusted\_rand\_score'\]
\>>> "roc\_auc" in all\_scorers
True

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)