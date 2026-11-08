[Skip to main content](https://scikit-learn.org/stable/auto_examples/cluster/plot_inductive_clustering.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/cluster/plot_inductive_clustering.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/cluster/plot_inductive_clustering.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/cluster/plot_inductive_clustering.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/cluster/plot_inductive_clustering.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/cluster/plot_inductive_clustering.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/cluster/plot_inductive_clustering.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/cluster/plot_inductive_clustering.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/cluster/plot_inductive_clustering.html#sphx-glr-download-auto-examples-cluster-plot-inductive-clustering-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Inductive Clustering[#](https://scikit-learn.org/stable/auto_examples/cluster/plot_inductive_clustering.html#inductive-clustering "Link to this heading")

==========================================================================================================================================================

Clustering can be expensive, especially when our dataset contains millions of datapoints. Many clustering algorithms are not [inductive](https://scikit-learn.org/stable/glossary.html#term-inductive)
 and so cannot be directly applied to new data samples without recomputing the clustering, which may be intractable. Instead, we can use clustering to then learn an inductive model with a classifier, which has several benefits:

*   it allows the clusters to scale and apply to new data
    
*   unlike re-fitting the clusters to new samples, it makes sure the labelling procedure is consistent over time
    
*   it allows us to use the inferential capabilities of the classifier to describe or explain the clusters
    

This example illustrates a generic implementation of a meta-estimator which extends clustering by inducing a classifier from the cluster labels.

![Ward Linkage, Unknown instances, Classify unknown instances](https://scikit-learn.org/stable/_images/sphx_glr_plot_inductive_clustering_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt

from sklearn.base import [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
, [ClusterMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClusterMixin.html#sklearn.base.ClusterMixin "sklearn.base.ClusterMixin")
, clone
from sklearn.cluster import [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.utils.metaestimators import [available\_if](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#sklearn.utils.metaestimators.available_if "sklearn.utils.metaestimators.available_if")
from sklearn.utils.validation import [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")

N\_SAMPLES \= 5000
RANDOM\_STATE \= 42

def \_classifier\_has(attr):
    """Check if we can delegate a method to the underlying classifier.

    First, we check the first fitted classifier if available, otherwise we
    check the unfitted classifier.
    """
    return lambda estimator: (
        hasattr(estimator.classifier\_, attr)
        if hasattr(estimator, "classifier\_")
        else hasattr(estimator.classifier, attr)
    )

class InductiveClusterer([ClusterMixin](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClusterMixin.html#sklearn.base.ClusterMixin "sklearn.base.ClusterMixin")
, [BaseEstimator](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator")
):
    def \_\_init\_\_(self, clusterer, classifier):
        self.clusterer \= clusterer
        self.classifier \= classifier

    def fit(self, X, y\=None):
        self.clusterer\_ \= clone(self.clusterer)
        self.classifier\_ \= clone(self.classifier)
        y \= self.clusterer\_.fit\_predict(X)
        self.classifier\_.fit(X, y)
        self.labels\_ \= y
        return self

    @available\_if(\_classifier\_has("predict"))
    def predict(self, X):
        [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
(self)
        return self.classifier\_.predict(X)

    @available\_if(\_classifier\_has("decision\_function"))
    def decision\_function(self, X):
        [check\_is\_fitted](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted")
(self)
        return self.classifier\_.decision\_function(X)

def plot\_scatter(X, color, alpha\=0.5):
    return [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[:, 0\], X\[:, 1\], c\=color, alpha\=alpha, edgecolor\="k")

\# Generate some training data from clustering
X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=N\_SAMPLES,
    cluster\_std\=\[1.0, 1.0, 0.5\],
    centers\=\[(\-5, \-5), (0, 0), (5, 5)\],
    random\_state\=RANDOM\_STATE,
)

\# Train a clustering algorithm on the training data and get the cluster labels
clusterer \= [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering")
(n\_clusters\=3)
cluster\_labels \= clusterer.fit\_predict(X)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(12, 4))

[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(131)
plot\_scatter(X, cluster\_labels)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Ward Linkage")

\# Generate new samples and plot them along with the original dataset
X\_new, y\_new \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(
    n\_samples\=10, centers\=\[(\-7, \-1), (\-2, 4), (3, 6)\], random\_state\=RANDOM\_STATE
)

[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(132)
plot\_scatter(X, cluster\_labels)
plot\_scatter(X\_new, "black", 1)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Unknown instances")

\# Declare the inductive learning model that it will be used to
\# predict cluster membership for unknown instances
classifier \= [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
(random\_state\=RANDOM\_STATE)
inductive\_learner \= InductiveClusterer(clusterer, classifier).fit(X)

probable\_clusters \= inductive\_learner.predict(X\_new)

ax \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(133)
plot\_scatter(X, cluster\_labels)
plot\_scatter(X\_new, probable\_clusters)

\# Plotting decision regions
[DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
    inductive\_learner,
    X,
    response\_method\="predict",
    multiclass\_colors\="viridis",
    alpha\=0.4,
    ax\=ax,
)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Classify unknown instances")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 2.324 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_inductive_clustering.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_inductive_clustering.ipynb)

[`Download Jupyter notebook: plot_inductive_clustering.ipynb`](https://scikit-learn.org/stable/_downloads/768c66e612686c51be7a0d956e60a0a8/plot_inductive_clustering.ipynb)

[`Download Python source code: plot_inductive_clustering.py`](https://scikit-learn.org/stable/_downloads/c4355efac5fa3ae540eec1deb5c097b8/plot_inductive_clustering.py)

[`Download zipped: plot_inductive_clustering.zip`](https://scikit-learn.org/stable/_downloads/a687ddc099cdaf81b25dcd61b9cb7672/plot_inductive_clustering.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_sklearn_is_fitted_thumb.png)

[\_\_sklearn\_is\_fitted\_\_ as Developer API](https://scikit-learn.org/stable/auto_examples/developing_estimators/sklearn_is_fitted.html)

\_\_sklearn\_is\_fitted\_\_ as Developer API

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_linkage_thumb.png)

[Various Agglomerative Clustering on a 2D embedding of digits](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_linkage.html)

Various Agglomerative Clustering on a 2D embedding of digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_linkage_comparison_thumb.png)

[Comparing different hierarchical linkage methods on toy datasets](https://scikit-learn.org/stable/auto_examples/cluster/plot_linkage_comparison.html)

Comparing different hierarchical linkage methods on toy datasets

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/c4355efac5fa3ae540eec1deb5c097b8/plot_inductive_clustering.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/768c66e612686c51be7a0d956e60a0a8/plot_inductive_clustering.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/a687ddc099cdaf81b25dcd61b9cb7672/plot_inductive_clustering.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo5.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/cluster/plot_inductive_clustering.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo5.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/cluster/plot_inductive_clustering.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)