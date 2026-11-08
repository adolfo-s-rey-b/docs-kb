[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.get_scorer.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.get_scorer.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.get_scorer.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.get_scorer.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.get_scorer.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.get_scorer.html)

Collapse Sidebar Expand Sidebar

get\_scorer[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#get-scorer "Link to this heading")

====================================================================================================================================

sklearn.metrics.get\_scorer(_scoring_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_scorer.py#L472)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#sklearn.metrics.get_scorer "Link to this definition")

Get a scorer from string.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter)
. [`get_scorer_names`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer_names.html#sklearn.metrics.get_scorer_names "sklearn.metrics.get_scorer_names")
 can be used to retrieve the names of all available scorers.

Parameters:

**scoring**str, callable or None

Scoring method as string. If callable it is returned as is. If None, returns None.

Returns:

**scorer**callable

The scorer.

Notes

When passed a string, this function always returns a copy of the scorer object. Calling `get_scorer` twice for the same scorer results in two separate scorer objects.

Examples

\>>> import numpy as np
\>>> from sklearn.dummy import DummyClassifier
\>>> from sklearn.metrics import get\_scorer
\>>> X \= np.reshape(\[0, 1, \-1, \-0.5, 2\], (\-1, 1))
\>>> y \= np.array(\[0, 1, 1, 0, 1\])
\>>> classifier \= DummyClassifier(strategy\="constant", constant\=0).fit(X, y)
\>>> accuracy \= get\_scorer("accuracy")
\>>> accuracy(classifier, X, y)
0.4

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#gallery-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_4_0_thumb.png)

[Release Highlights for scikit-learn 1.4](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_4_0.html)

Release Highlights for scikit-learn 1.4

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)