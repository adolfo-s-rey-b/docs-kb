[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.dcg_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.dcg_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.dcg_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.dcg_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.dcg_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.dcg_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.dcg_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.dcg_score.html)

Collapse Sidebar Expand Sidebar

dcg\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.dcg_score.html#dcg-score "Link to this heading")

=================================================================================================================================

sklearn.metrics.dcg\_score(_y\_true_, _y\_score_, _\*_, _k\=None_, _log\_base\=2_, _sample\_weight\=None_, _ignore\_ties\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/_ranking.py#L1778)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.dcg_score.html#sklearn.metrics.dcg_score "Link to this definition")

Compute Discounted Cumulative Gain.

Sum the true scores ranked in the order induced by the predicted scores, after applying a logarithmic discount.

This ranking metric yields a high value if true labels are ranked high by `y_score`.

Usually the Normalized Discounted Cumulative Gain (NDCG, computed by ndcg\_score) is preferred.

Parameters:

**y\_true**array-like of shape (n\_samples, n\_labels)

True targets of multilabel classification, or true scores of entities to be ranked.

**y\_score**array-like of shape (n\_samples, n\_labels)

Target scores, can either be probability estimates of the positive class or non-thresholded decision values (as returned by [decision\_function](https://scikit-learn.org/stable/glossary.html#term-decision_function)
 on some classifiers).

**k**int, default=None

Only consider the highest k scores in the ranking. If None, use all outputs.

**log\_base**float, default=2

Base of the logarithm used for the discount. A low value means a sharper discount (top results are more important).

**sample\_weight**array-like of shape (n\_samples,), default=None

Sample weights. If `None`, all samples are given the same weight.

**ignore\_ties**bool, default=False

Assume that there are no ties in y\_score (which is likely to be the case if y\_score is continuous) for efficiency gains.

Returns:

**discounted\_cumulative\_gain**float

The averaged sample DCG scores.

See also

[`ndcg_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html#sklearn.metrics.ndcg_score "sklearn.metrics.ndcg_score")

The Discounted Cumulative Gain divided by the Ideal Discounted Cumulative Gain (the DCG obtained for a perfect ranking), in order to have a score between 0 and 1.

References

[Wikipedia entry for Discounted Cumulative Gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)
.

Jarvelin, K., & Kekalainen, J. (2002). Cumulated gain-based evaluation of IR techniques. ACM Transactions on Information Systems (TOIS), 20(4), 422-446.

Wang, Y., Wang, L., Li, Y., He, D., Chen, W., & Liu, T. Y. (2013, May). A theoretical analysis of NDCG ranking measures. In Proceedings of the 26th Annual Conference on Learning Theory (COLT 2013).

McSherry, F., & Najork, M. (2008, March). Computing information retrieval performance measures efficiently in the presence of tied scores. In European conference on information retrieval (pp. 414-421). Springer, Berlin, Heidelberg.

Examples

\>>> import numpy as np
\>>> from sklearn.metrics import dcg\_score
\>>> \# we have ground-truth relevance of some answers to a query:
\>>> true\_relevance \= np.asarray(\[\[10, 0, 0, 1, 5\]\])
\>>> \# we predict scores for the answers
\>>> scores \= np.asarray(\[\[.1, .2, .3, 4, 70\]\])
\>>> dcg\_score(true\_relevance, scores)
9.49
\>>> \# we can set k to truncate the sum; only top k answers contribute
\>>> dcg\_score(true\_relevance, scores, k\=2)
5.63
\>>> \# now we have some ties in our prediction
\>>> scores \= np.asarray(\[\[1, 0, 0, 0, 1\]\])
\>>> \# by default ties are averaged, so here we get the average true
\>>> \# relevance of our top predictions: (10 + 5) / 2 = 7.5
\>>> dcg\_score(true\_relevance, scores, k\=1)
7.5
\>>> \# we can choose to ignore ties for faster results, but only
\>>> \# if we know there aren't ties in our scores, otherwise we get
\>>> \# wrong results:
\>>> dcg\_score(true\_relevance,
...           scores, k\=1, ignore\_ties\=True)
5.0

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)