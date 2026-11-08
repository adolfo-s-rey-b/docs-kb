[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html)

Collapse Sidebar Expand Sidebar

homogeneity\_completeness\_v\_measure[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html#homogeneity-completeness-v-measure "Link to this heading")

==============================================================================================================================================================================================================

sklearn.metrics.homogeneity\_completeness\_v\_measure(_labels\_true_, _labels\_pred_, _\*_, _beta\=1.0_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/metrics/cluster/_supervised.py#L465)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_completeness_v_measure.html#sklearn.metrics.homogeneity_completeness_v_measure "Link to this definition")

Compute the homogeneity and completeness and V-Measure scores at once.

Those metrics are based on normalized conditional entropy measures of the clustering labeling to evaluate given the knowledge of a Ground Truth class labels of the same samples.

A clustering result satisfies homogeneity if all of its clusters contain only data points which are members of a single class.

A clustering result satisfies completeness if all the data points that are members of a given class are elements of the same cluster.

Both scores have positive values between 0.0 and 1.0, larger values being desirable.

Those 3 metrics are independent of the absolute values of the labels: a permutation of the class or cluster label values won’t change the score values in any way.

V-Measure is furthermore symmetric: swapping `labels_true` and `label_pred` will give the same score. This does not hold for homogeneity and completeness. V-Measure is identical to [`normalized_mutual_info_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.normalized_mutual_info_score.html#sklearn.metrics.normalized_mutual_info_score "sklearn.metrics.normalized_mutual_info_score")
 with the arithmetic averaging method.

Read more in the [User Guide](https://scikit-learn.org/stable/modules/clustering.html#homogeneity-completeness)
.

Parameters:

**labels\_true**array-like of shape (n\_samples,)

Ground truth class labels to be used as a reference.

**labels\_pred**array-like of shape (n\_samples,)

Cluster labels to evaluate.

**beta**float, default=1.0

Ratio of weight attributed to `homogeneity` vs `completeness`. If `beta` is greater than 1, `completeness` is weighted more strongly in the calculation. If `beta` is less than 1, `homogeneity` is weighted more strongly.

Returns:

**homogeneity**float

Score between 0.0 and 1.0. 1.0 stands for perfectly homogeneous labeling.

**completeness**float

Score between 0.0 and 1.0. 1.0 stands for perfectly complete labeling.

**v\_measure**float

Harmonic mean of the first two.

See also

[`homogeneity_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.homogeneity_score.html#sklearn.metrics.homogeneity_score "sklearn.metrics.homogeneity_score")

Homogeneity metric of cluster labeling.

[`completeness_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.completeness_score.html#sklearn.metrics.completeness_score "sklearn.metrics.completeness_score")

Completeness metric of cluster labeling.

[`v_measure_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html#sklearn.metrics.v_measure_score "sklearn.metrics.v_measure_score")

V-Measure (NMI with arithmetic mean option).

Examples

\>>> from sklearn.metrics import homogeneity\_completeness\_v\_measure
\>>> y\_true, y\_pred \= \[0, 0, 1, 1, 2, 2\], \[0, 0, 1, 2, 2, 2\]
\>>> homogeneity\_completeness\_v\_measure(y\_true, y\_pred)
(0.71, 0.771, 0.74)

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)