[Skip to main content](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/multioutput/plot_classifier_chain_yeast.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/multioutput/plot_classifier_chain_yeast.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/multioutput/plot_classifier_chain_yeast.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/multioutput/plot_classifier_chain_yeast.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/multioutput/plot_classifier_chain_yeast.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/multioutput/plot_classifier_chain_yeast.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html#sphx-glr-download-auto-examples-multioutput-plot-classifier-chain-yeast-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Multilabel classification using a classifier chain[#](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html#multilabel-classification-using-a-classifier-chain "Link to this heading")

============================================================================================================================================================================================================================

This example shows how to use [`ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
 to solve a multilabel classification problem.

The most naive strategy to solve such a task is to independently train a binary classifier on each label (i.e. each column of the target variable). At prediction time, the ensemble of binary classifiers is used to assemble multitask prediction.

This strategy does not allow to model relationship between different tasks. The [`ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
 is the meta-estimator (i.e. an estimator taking an inner estimator) that implements a more advanced strategy. The ensemble of binary classifiers are used as a chain where the prediction of a classifier in the chain is used as a feature for training the next classifier on a new label. Therefore, these additional features allow each chain to exploit correlations among labels.

The [Jaccard similarity](https://scikit-learn.org/stable/modules/model_evaluation.html#jaccard-similarity-score)
 score for chain tends to be greater than that of the set independent base models.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Loading a dataset[#](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html#loading-a-dataset "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

For this example, we use the [yeast](https://www.openml.org/d/40597)
 dataset which contains 2,417 datapoints each with 103 features and 14 possible labels. Each data point has at least one label. As a baseline we first train a logistic regression classifier for each of the 14 labels. To evaluate the performance of these classifiers we predict on a held-out test set and calculate the Jaccard similarity for each sample.

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

\# Load a multi-label dataset from https://www.openml.org/d/40597
X, Y \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
("yeast", version\=4, return\_X\_y\=True)
Y \= Y \== "TRUE"
X\_train, X\_test, Y\_train, Y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, Y, test\_size\=0.2, random\_state\=0)

Copy to clipboard

Fit models[#](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html#fit-models "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

We fit [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 wrapped by [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
 and ensemble of multiple [`ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
.

### LogisticRegression wrapped by OneVsRestClassifier[#](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html#logisticregression-wrapped-by-onevsrestclassifier "Link to this heading")

Since by default [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
 can’t handle data with multiple targets, we need to use [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
. After fitting the model we calculate Jaccard similarity.

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.metrics import [jaccard\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")
from sklearn.multiclass import [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")

base\_lr \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
()
ovr \= [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
(base\_lr)
ovr.fit(X\_train, Y\_train)
Y\_pred\_ovr \= ovr.predict(X\_test)
ovr\_jaccard\_score \= [jaccard\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")
(Y\_test, Y\_pred\_ovr, average\="samples")

Copy to clipboard

### Chain of binary classifiers[#](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html#chain-of-binary-classifiers "Link to this heading")

Because the models in each chain are arranged randomly there is significant variation in performance among the chains. Presumably there is an optimal ordering of the classes in a chain that will yield the best performance. However, we do not know that ordering a priori. Instead, we can build a voting ensemble of classifier chains by averaging the binary predictions of the chains and apply a threshold of 0.5. The Jaccard similarity score of the ensemble is greater than that of the independent models and tends to exceed the score of each chain in the ensemble (although this is not guaranteed with randomly ordered chains).

from sklearn.multioutput import [ClassifierChain](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")

chains \= \[[ClassifierChain](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")\
(base\_lr, order\="random", random\_state\=i) for i in range(10)\]
for chain in chains:
    chain.fit(X\_train, Y\_train)

Y\_pred\_chains \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[chain.predict\_proba(X\_test) for chain in chains\])
chain\_jaccard\_scores \= \[\
    [jaccard\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")\
(Y\_test, Y\_pred\_chain \>= 0.5, average\="samples")\
    for Y\_pred\_chain in Y\_pred\_chains\
\]

Y\_pred\_ensemble \= Y\_pred\_chains.mean(axis\=0)
ensemble\_jaccard\_score \= [jaccard\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html#sklearn.metrics.jaccard_score "sklearn.metrics.jaccard_score")
(
    Y\_test, Y\_pred\_ensemble \>= 0.5, average\="samples"
)

Copy to clipboard

Plot results[#](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html#plot-results "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Plot the Jaccard similarity scores for the independent model, each of the chains, and the ensemble (note that the vertical axis on this plot does not begin at 0).

model\_scores \= \[ovr\_jaccard\_score\] + chain\_jaccard\_scores + \[ensemble\_jaccard\_score\]

model\_names \= (
    "Independent",
    "Chain 1",
    "Chain 2",
    "Chain 3",
    "Chain 4",
    "Chain 5",
    "Chain 6",
    "Chain 7",
    "Chain 8",
    "Chain 9",
    "Chain 10",
    "Ensemble",
)

x\_pos \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(model\_names))

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(7, 4))
ax.grid(True)
ax.set\_title("Classifier Chain Ensemble Performance Comparison")
ax.set\_xticks(x\_pos)
ax.set\_xticklabels(model\_names, rotation\="vertical")
ax.set\_ylabel("Jaccard Similarity Score")
ax.set\_ylim(\[min(model\_scores) \* 0.9, max(model\_scores) \* 1.1\])
colors \= \["r"\] + \["b"\] \* len(chain\_jaccard\_scores) + \["g"\]
ax.bar(x\_pos, model\_scores, alpha\=0.5, color\=colors)
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Classifier Chain Ensemble Performance Comparison](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_chain_yeast_001.png)

Results interpretation[#](https://scikit-learn.org/stable/auto_examples/multioutput/plot_classifier_chain_yeast.html#results-interpretation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are three main takeaways from this plot:

*   Independent model wrapped by [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
     performs worse than the ensemble of classifier chains and some of individual chains. This is caused by the fact that the logistic regression doesn’t model relationship between the labels.
    
*   [`ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
     takes advantage of correlation among labels but due to random nature of labels ordering, it could yield worse result than an independent model.
    
*   An ensemble of chains performs better because it not only captures relationship between labels but also does not make strong assumptions about their correct order.
    

**Total running time of the script:** (0 minutes 1.739 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo25.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/multioutput/plot_classifier_chain_yeast.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo25.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/multioutput/plot_classifier_chain_yeast.ipynb)

[`Download Jupyter notebook: plot_classifier_chain_yeast.ipynb`](https://scikit-learn.org/stable/_downloads/05ca8a4e90b4cc2acd69f9e24b4a1f3a/plot_classifier_chain_yeast.ipynb)

[`Download Python source code: plot_classifier_chain_yeast.py`](https://scikit-learn.org/stable/_downloads/c6856243c97f58098e60fb14d2bf3750/plot_classifier_chain_yeast.py)

[`Download zipped: plot_classifier_chain_yeast.zip`](https://scikit-learn.org/stable/_downloads/5034bd1c22037f56c1da2e8d84719607/plot_classifier_chain_yeast.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multiclass_overview_thumb.png)

[Overview of multiclass training meta-estimators](https://scikit-learn.org/stable/auto_examples/multiclass/plot_multiclass_overview.html)

Overview of multiclass training meta-estimators

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_grid_search_stats_thumb.png)

[Statistical comparison of models using grid search](https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_stats.html)

Statistical comparison of models using grid search

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)

[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

Faces recognition example using eigenfaces and kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_feature_transformation_thumb.png)

[Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html)

Feature transformations with ensembles of trees

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/c6856243c97f58098e60fb14d2bf3750/plot_classifier_chain_yeast.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/05ca8a4e90b4cc2acd69f9e24b4a1f3a/plot_classifier_chain_yeast.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/5034bd1c22037f56c1da2e8d84719607/plot_classifier_chain_yeast.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo25.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/multioutput/plot_classifier_chain_yeast.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo25.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/multioutput/plot_classifier_chain_yeast.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)