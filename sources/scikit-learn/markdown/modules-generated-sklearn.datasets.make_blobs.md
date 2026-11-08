[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_blobs.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.datasets.make_blobs.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.datasets.make_blobs.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.datasets.make_blobs.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.make_blobs.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.make_blobs.html)

Collapse Sidebar Expand Sidebar

make\_blobs[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#make-blobs "Link to this heading")

=====================================================================================================================================

sklearn.datasets.make\_blobs(_n\_samples\=100_, _n\_features\=2_, _\*_, _centers\=None_, _cluster\_std\=1.0_, _center\_box\=(-10.0, 10.0)_, _shuffle\=True_, _random\_state\=None_, _return\_centers\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/datasets/_samples_generator.py#L989)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "Link to this definition")

Generate isotropic Gaussian blobs for clustering.

Read more in the [User Guide](https://scikit-learn.org/stable/datasets/sample_generators.html#sample-generators)
.

Parameters:

**n\_samples**int or array-like, default=100

If int, it is the total number of points equally divided among clusters. If array-like, each element of the sequence indicates the number of samples per cluster.

Changed in version v0.20: one can now pass an array-like to the `n_samples` parameter

**n\_features**int, default=2

The number of features for each sample.

**centers**int or array-like of shape (n\_centers, n\_features), default=None

The number of centers to generate, or the fixed center locations. If n\_samples is an int and centers is None, 3 centers are generated. If n\_samples is array-like, centers must be either None or an array of length equal to the length of n\_samples.

**cluster\_std**float or array-like of float, default=1.0

The standard deviation of the clusters.

**center\_box**tuple of float (min, max), default=(-10.0, 10.0)

The bounding box for each cluster center when centers are generated at random.

**shuffle**bool, default=True

Shuffle the samples.

**random\_state**int, RandomState instance or None, default=None

Determines random number generation for dataset creation. Pass an int for reproducible output across multiple function calls. See [Glossary](https://scikit-learn.org/stable/glossary.html#term-random_state)
.

**return\_centers**bool, default=False

If True, then return the centers of each cluster.

Added in version 0.23.

Returns:

**X**ndarray of shape (n\_samples, n\_features)

The generated samples.

**y**ndarray of shape (n\_samples,)

The integer labels for cluster membership of each sample.

**centers**ndarray of shape (n\_centers, n\_features)

The centers of each cluster. Only returned if `return_centers=True`.

See also

[`make_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")

A more intricate variant.

Examples

\>>> from sklearn.datasets import make\_blobs
\>>> X, y \= make\_blobs(n\_samples\=10, centers\=3, n\_features\=2,
...                   random\_state\=0)
\>>> print(X.shape)
(10, 2)
\>>> y
array(\[0, 0, 1, 0, 2, 2, 2, 1, 1, 0\])
\>>> X, y \= make\_blobs(n\_samples\=\[3, 3, 4\], centers\=None, n\_features\=2,
...                   random\_state\=0)
\>>> print(X.shape)
(10, 2)
\>>> y
array(\[0, 1, 2, 0, 2, 2, 2, 1, 1, 0\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#gallery-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_thumb.png)

[Probability calibration of classifiers](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration.html)

Probability calibration of classifiers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_calibration_multiclass_thumb.png)

[Probability Calibration for 3-class classification](https://scikit-learn.org/stable/auto_examples/calibration/plot_calibration_multiclass.html)

Probability Calibration for 3-class classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lda_thumb.png)

[Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification](https://scikit-learn.org/stable/auto_examples/classification/plot_lda.html)

Normal, Ledoit-Wolf and OAS Linear Discriminant Analysis for classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_affinity_propagation_thumb.png)

[Demo of affinity propagation clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_affinity_propagation.html)

Demo of affinity propagation clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_birch_vs_minibatchkmeans_thumb.png)

[Compare BIRCH and MiniBatchKMeans](https://scikit-learn.org/stable/auto_examples/cluster/plot_birch_vs_minibatchkmeans.html)

Compare BIRCH and MiniBatchKMeans

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_bisect_kmeans_thumb.png)

[Bisecting K-Means and Regular K-Means Performance Comparison](https://scikit-learn.org/stable/auto_examples/cluster/plot_bisect_kmeans.html)

Bisecting K-Means and Regular K-Means Performance Comparison

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_thumb.png)

[Comparing different clustering algorithms on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

Comparing different clustering algorithms on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dbscan_thumb.png)

[Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)

Demo of DBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_hdbscan_thumb.png)

[Demo of HDBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_hdbscan.html)

Demo of HDBSCAN clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_inductive_clustering_thumb.png)

[Inductive Clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_inductive_clustering.html)

Inductive Clustering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_assumptions_thumb.png)

[Demonstration of k-means assumptions](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html)

Demonstration of k-means assumptions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_plusplus_thumb.png)

[An example of K-Means++ initialization](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_plusplus.html)

An example of K-Means++ initialization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kmeans_silhouette_analysis_thumb.png)

[Selecting the number of clusters with silhouette analysis on KMeans clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)

Selecting the number of clusters with silhouette analysis on KMeans clustering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mean_shift_thumb.png)

[A demo of the mean-shift clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html)

A demo of the mean-shift clustering algorithm

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mini_batch_kmeans_thumb.png)

[Comparison of the K-Means and MiniBatchKMeans clustering algorithms](https://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html)

Comparison of the K-Means and MiniBatchKMeans clustering algorithms

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_multinomial_thumb.png)

[Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html)

Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_separating_hyperplane_thumb.png)

[SGD: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_separating_hyperplane.html)

SGD: Maximum margin separating hyperplane

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_anomaly_comparison_thumb.png)

[Comparing anomaly detection algorithms for outlier detection on toy datasets](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_anomaly_comparison.html)

Comparing anomaly detection algorithms for outlier detection on toy datasets

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_init_thumb.png)

[GMM Initialization Methods](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_init.html)

GMM Initialization Methods

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_strategies_thumb.png)

[Demonstrating the different strategies of KBinsDiscretizer](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization_strategies.html)

Demonstrating the different strategies of KBinsDiscretizer

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_23_0_thumb.png)

[Release Highlights for scikit-learn 0.23](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_23_0.html)

Release Highlights for scikit-learn 0.23

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_1_0_thumb.png)

[Release Highlights for scikit-learn 1.1](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_1_0.html)

Release Highlights for scikit-learn 1.1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linearsvc_support_vectors_thumb.png)

[Plot the support vectors in LinearSVC](https://scikit-learn.org/stable/auto_examples/svm/plot_linearsvc_support_vectors.html)

Plot the support vectors in LinearSVC

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_thumb.png)

[SVM: Maximum margin separating hyperplane](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane.html)

SVM: Maximum margin separating hyperplane

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_unbalanced_thumb.png)

[SVM: Separating hyperplane for unbalanced classes](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)

SVM: Separating hyperplane for unbalanced classes

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_tie_breaking_thumb.png)

[SVM Tie Breaking Example](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_tie_breaking.html)

SVM Tie Breaking Example

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)