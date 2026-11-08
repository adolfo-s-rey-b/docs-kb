[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.ndcg_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.ndcg_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.ndcg_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.ndcg_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.ndcg_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.ndcg_score.html)

Collapse Sidebar Expand Sidebar

ndcg\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html#ndcg-score "Link to this heading")

====================================================================================================================================

sklearn.metrics.ndcg\_score(_y\_true_, _y\_score_, _\*_, _k\=None_, _sample\_weight\=None_, _ignore\_ties\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L1949)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html#sklearn.metrics.ndcg_score "Link to this definition")

Compute Normalized Discounted Cumulative Gain.

Sum the true scores ranked in the order induced by the predicted scores, after applying a logarithmic discount. Then divide by the best possible score (Ideal DCG, obtained for a perfect ranking) to obtain a score between 0 and 1.

This ranking metric returns a high value if true labels are ranked high by `y_score`.

Parameters:

**y\_true**array-like of shape (n\_samples, n\_labels)

True targets of multilabel classification, or true scores of entities to be ranked. Negative values in `y_true` may result in an output that is not between 0 and 1.

**y\_score**array-like of shape (n\_samples, n\_labels)

Target scores, can either be probability estimates of the positive class or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers).

**k**int, default=None

Only consider the highest k scores in the ranking. If `None`, use all outputs.

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights. If `None`, all samples are given the same weight.

**ignore\_ties**bool, default=False

Assume that there are no ties in y\_score (which is likely to be the case if y\_score is continuous) for efficiency gains.

Returns:

**normalized\_discounted\_cumulative\_gain**float in \[0., 1.\]

The averaged NDCG scores for all samples.

See also

[`dcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.dcg_score.html#sklearn.metrics.dcg_score "sklearn.metrics.dcg_score")

Discounted Cumulative Gain (not normalized).

References

[Wikipedia entry for Discounted Cumulative Gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)

Jarvelin, K., & Kekalainen, J. (2002). Cumulated gain-based evaluation of IR techniques. ACM Transactions on Information Systems (TOIS), 20(4), 422-446.

Wang, Y., Wang, L., Li, Y., He, D., Chen, W., & Liu, T. Y. (2013, May). A theoretical analysis of NDCG ranking measures. In Proceedings of the 26th Annual Conference on Learning Theory (COLT 2013)

McSherry, F., & Najork, M. (2008, March). Computing information retrieval performance measures efficiently in the presence of tied scores. In European conference on information retrieval (pp. 414-421). Springer, Berlin, Heidelberg.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import ndcg\_score
\>>> \# we have ground-truth relevance of some answers to a query:
\>>> true\_relevance \= np.asarray(\[\[10, 0, 0, 1, 5\]\])
\>>> \# we predict some scores (relevance) for the answers
\>>> scores \= np.asarray(\[\[.1, .2, .3, 4, 70\]\])
\>>> ndcg\_score(true\_relevance, scores)
0.69
\>>> scores \= np.asarray(\[\[.05, 1.1, 1., .5, .0\]\])
\>>> ndcg\_score(true\_relevance, scores)
0.49
\>>> \# we can set k to truncate the sum; only top k answers contribute.
\>>> ndcg\_score(true\_relevance, scores, k\=4)
0.35
\>>> \# the normalization takes k into account so a perfect answer
\>>> \# would still get 1.0
\>>> ndcg\_score(true\_relevance, true\_relevance, k\=4)
1.0...
\>>> \# now we have some ties in our prediction
\>>> scores \= np.asarray(\[\[1, 0, 0, 0, 1\]\])
\>>> \# by default ties are averaged, so here we get the average (normalized)
\>>> \# true relevance of our top predictions: (10 / 10 + 5 / 10) / 2 = .75
\>>> ndcg\_score(true\_relevance, scores, k\=1)
0.75
\>>> \# we can choose to ignore ties for faster results, but only
\>>> \# if we know there aren't ties in our scores, otherwise we get
\>>> \# wrong results:
\>>> ndcg\_score(true\_relevance,
...           scores, k\=1, ignore\_ties\=True)
0.5...

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)