[Skip to main content](https://scikit-learn.org/stable/modules/unsupervised_reduction.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/unsupervised_reduction.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/unsupervised_reduction.html)
[1.8.0](https://scikit-learn.org/1.8/modules/unsupervised_reduction.html)
[1.7.2](https://scikit-learn.org/1.7/modules/unsupervised_reduction.html)
[1.6.1](https://scikit-learn.org/1.6/modules/unsupervised_reduction.html)
[1.5.2](https://scikit-learn.org/1.5/modules/unsupervised_reduction.html)
[1.4.2](https://scikit-learn.org/1.4/modules/unsupervised_reduction.html)

Collapse Sidebar Expand Sidebar

8.5. Unsupervised dimensionality reduction[#](https://scikit-learn.org/stable/modules/unsupervised_reduction.html#unsupervised-dimensionality-reduction "Link to this heading")

================================================================================================================================================================================

If your number of features is high, it may be useful to reduce it with an unsupervised step prior to supervised steps. Many of the [Unsupervised learning](https://scikit-learn.org/stable/unsupervised_learning.html#unsupervised-learning)
 methods implement a `transform` method that can be used to reduce the dimensionality. Below we discuss two specific examples of this pattern that are heavily used.

8.5.1. PCA: principal component analysis[#](https://scikit-learn.org/stable/modules/unsupervised_reduction.html#pca-principal-component-analysis "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 looks for a combination of features that capture well the variance of the original features. See [Decomposing signals in components (matrix factorization problems)](https://scikit-learn.org/stable/modules/decomposition.html#decompositions)
.

Examples

*   [Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html#sphx-glr-auto-examples-applications-plot-face-recognition-py)
    

8.5.2. Random projections[#](https://scikit-learn.org/stable/modules/unsupervised_reduction.html#random-projections "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

The module: [`random_projection`](https://scikit-learn.org/stable/api/sklearn.random_projection.html#module-sklearn.random_projection "sklearn.random_projection")
 provides several tools for data reduction by random projections. See the relevant section of the documentation: [Random Projection](https://scikit-learn.org/stable/modules/random_projection.html#random-projection)
.

Examples

*   [The Johnson-Lindenstrauss bound for embedding with random projections](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html#sphx-glr-auto-examples-miscellaneous-plot-johnson-lindenstrauss-bound-py)
    

8.5.3. Feature agglomeration[#](https://scikit-learn.org/stable/modules/unsupervised_reduction.html#feature-agglomeration "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

[`cluster.FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration "sklearn.cluster.FeatureAgglomeration")
 applies [Hierarchical clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)
 to group together features that behave similarly.

Examples

*   [Feature agglomeration vs. univariate selection](https://scikit-learn.org/stable/auto_examples/cluster/plot_feature_agglomeration_vs_univariate_selection.html#sphx-glr-auto-examples-cluster-plot-feature-agglomeration-vs-univariate-selection-py)
    
*   [Feature agglomeration](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html#sphx-glr-auto-examples-cluster-plot-digits-agglomeration-py)
    

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)