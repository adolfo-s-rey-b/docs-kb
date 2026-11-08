[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.consensus_score.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.consensus_score.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.consensus_score.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.consensus_score.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.consensus_score.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.consensus_score.html)

Collapse Sidebar Expand Sidebar

consensus\_score[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html#consensus-score "Link to this heading")

===================================================================================================================================================

sklearn.metrics.consensus\_score(_a_, _b_, _\*_, _similarity\='jaccard'_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_bicluster.py#L52)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html#sklearn.metrics.consensus_score "Link to this definition")

The similarity of two sets of biclusters.

Similarity between individual biclusters is computed. Then the best matching between sets is found by solving a linear sum assignment problem, using a modified Jonker-Volgenant algorithm. The final score is the sum of similarities divided by the size of the larger set.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/biclustering.html#biclustering)
.

Parameters:

**a**tuple (rows, columns)

Tuple of row and column indicators for a set of biclusters.

**b**tuple (rows, columns)

Another set of biclusters like `a`.

**similarity**‘jaccard’ or callable, default=’jaccard’

May be the string “jaccard” to use the Jaccard coefficient, or any function that takes four arguments, each of which is a 1d indicator vector: (a\_rows, a\_columns, b\_rows, b\_columns).

Returns:

**consensus\_score**float

Consensus score, a non-negative value, sum of similarities divided by size of larger set.

See also

[`scipy.optimize.linear_sum_assignment`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html#scipy.optimize.linear_sum_assignment "(in SciPy v1.18.0)")

Solve the linear sum assignment problem.

References

*   Hochreiter, Bodenhofer, et. al., 2010. [FABIA: factor analysis for bicluster acquisition](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2881408/)
    .
    

Examples

\>>> from sklearn.metrics import consensus\_score
\>>> a \= (\[\[True, False\], \[False, True\]\], \[\[False, True\], \[True, False\]\])
\>>> b \= (\[\[False, True\], \[True, False\]\], \[\[True, False\], \[False, True\]\])
\>>> consensus\_score(a, b, similarity\='jaccard')
1.0

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.consensus_score.html#gallery-examples "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_biclustering_thumb.png)

[A demo of the Spectral Biclustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_biclustering.html)

A demo of the Spectral Biclustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_spectral_coclustering_thumb.png)

[A demo of the Spectral Co-Clustering algorithm](https://scikit-learn.org/stable/auto_examples/bicluster/plot_spectral_coclustering.html)

A demo of the Spectral Co-Clustering algorithm

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)