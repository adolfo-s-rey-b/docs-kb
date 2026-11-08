[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_logistic_multinomial.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_logistic_multinomial.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_logistic_multinomial.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_logistic_multinomial.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_logistic_multinomial.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_logistic_multinomial.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html#sphx-glr-download-auto-examples-linear-model-plot-logistic-multinomial-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html#decision-boundaries-of-multinomial-and-one-vs-rest-logistic-regression "Link to this heading")

===================================================================================================================================================================================================================================================================

This example compares decision boundaries of multinomial and one-vs-rest logistic regression on a 2D dataset with three classes.

We make a comparison of the decision boundaries of both methods that is equivalent to call the method `predict`. In addition, we plot the hyperplanes that correspond to the line when the probability estimate for a class is of 0.5.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Dataset Generation[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html#dataset-generation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

We generate a synthetic dataset using the [`make_blobs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
 function. The dataset consists of 1,000 samples from three different classes, centered around \[-5, 0\], \[0, 1.5\], and \[5, -1\]. After generation, we apply a linear transformation to introduce some correlation between the features to make the problem more challenging. This results in a 2D dataset with three overlapping classes, suitable for demonstrating the differences between multinomial and one-vs-rest logistic regression.

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")

cmap \= "coolwarm"

centers \= \[\[\-5, 0\], \[0, 1.5\], \[5, \-1\]\]
X, y \= [make\_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs "sklearn.datasets.make_blobs")
(n\_samples\=1\_000, centers\=centers, random\_state\=40)
transformation \= \[\[0.4, 0.2\], \[\-0.4, 1.2\]\]
X \= [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(X, transformation)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 4))

scatter \= ax.scatter(X\[:, 0\], X\[:, 1\], c\=y, cmap\=cmap, edgecolor\="black")
ax.set(title\="Synthetic Dataset", xlabel\="Feature 1", ylabel\="Feature 2")
\_ \= ax.legend(\*scatter.legend\_elements(), title\="Classes")

Copy to clipboard

![Synthetic Dataset](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_multinomial_001.png)

Classifier Training[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html#classifier-training "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

We train two different logistic regression classifiers: multinomial and one-vs-rest. The multinomial classifier handles all classes simultaneously, while the one-vs-rest approach trains a binary classifier for each class against all others.

from sklearn.linear\_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.multiclass import [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")

logistic\_regression\_multinomial \= [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
().fit(X, y)
logistic\_regression\_ovr \= [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
([LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
()).fit(X, y)

accuracy\_multinomial \= logistic\_regression\_multinomial.score(X, y)
accuracy\_ovr \= logistic\_regression\_ovr.score(X, y)

Copy to clipboard

Decision Boundaries Visualization[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html#decision-boundaries-visualization "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s visualize the decision boundaries of both models that is provided by the method `predict` of the classifiers.

from sklearn.inspection import DecisionBoundaryDisplay

fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(12, 5), sharex\=True, sharey\=True)

for model, title, ax in \[\
    (\
        logistic\_regression\_multinomial,\
        f"Multinomial Logistic Regression\\n(Accuracy: {accuracy\_multinomial:.3f})",\
        ax1,\
    ),\
    (\
        logistic\_regression\_ovr,\
        f"One-vs-Rest Logistic Regression\\n(Accuracy: {accuracy\_ovr:.3f})",\
        ax2,\
    ),\
\]:
    [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        model,
        X,
        ax\=ax,
        response\_method\="predict",
        alpha\=0.8,
        multiclass\_colors\=cmap,
    )
    scatter \= ax.scatter(X\[:, 0\], X\[:, 1\], c\=y, cmap\=cmap, edgecolor\="k")
    legend \= ax.legend(\*scatter.legend\_elements(), title\="Classes")
    ax.add\_artist(legend)
    ax.set\_title(title)

Copy to clipboard

![Multinomial Logistic Regression (Accuracy: 0.995), One-vs-Rest Logistic Regression (Accuracy: 0.976)](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_multinomial_002.png)

We see that the decision boundaries are different. This difference stems from their approaches:

*   Multinomial logistic regression considers all classes simultaneously during optimization.
    
*   One-vs-rest logistic regression fits each class independently against all others.
    

These distinct strategies can lead to varying decision boundaries, especially in complex multi-class problems.

Hyperplanes Visualization[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html#hyperplanes-visualization "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We also visualize the hyperplanes that correspond to the line when the probability estimate for a class is 0.5.

def plot\_hyperplanes(classifier, X, ax, colors):
    xmin, xmax \= X\[:, 0\].min(), X\[:, 0\].max()
    ymin, ymax \= X\[:, 1\].min(), X\[:, 1\].max()
    ax.set(xlim\=(xmin, xmax), ylim\=(ymin, ymax))

    if isinstance(classifier, [OneVsRestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
):
        coef \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[est.coef\_ for est in classifier.estimators\_\])
        intercept \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[est.intercept\_ for est in classifier.estimators\_\])
    else:
        coef \= classifier.coef\_
        intercept \= classifier.intercept\_

    for i, color in zip(range(coef.shape\[0\]), colors):
        w \= coef\[i\]
        a \= \-w\[0\] / w\[1\]
        xx \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(xmin, xmax)
        yy \= a \* xx \- (intercept\[i\]) / w\[1\]
        ax.plot(xx, yy, "--", color\=color, linewidth\=4, label\=f"Class {i}")

    return ax.get\_legend\_handles\_labels()

Copy to clipboard

fig, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(12, 5), sharex\=True, sharey\=True)

for model, title, ax in \[\
    (\
        logistic\_regression\_multinomial,\
        "Multinomial Logistic Regression Hyperplanes",\
        ax1,\
    ),\
    (logistic\_regression\_ovr, "One-vs-Rest Logistic Regression Hyperplanes", ax2),\
\]:
    hyperplane\_handles, hyperplane\_labels \= plot\_hyperplanes(
        model, X, ax, colors\=\["blue", "dimgray", "red"\]
    )
    scatter \= ax.scatter(X\[:, 0\], X\[:, 1\], c\=y, cmap\=cmap, edgecolor\="k")
    scatter\_handles, scatter\_labels \= scatter.legend\_elements()

    all\_handles \= hyperplane\_handles + scatter\_handles
    all\_labels \= hyperplane\_labels + scatter\_labels

    ax.legend(all\_handles, all\_labels, title\="Classes")
    ax.set\_title(title)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Multinomial Logistic Regression Hyperplanes, One-vs-Rest Logistic Regression Hyperplanes](https://scikit-learn.org/stable/_images/sphx_glr_plot_logistic_multinomial_003.png)

While the hyperplanes for classes 0 and 2 are quite similar between the two methods, we observe that the hyperplane for class 1 is notably different. This difference stems from the fundamental approaches of one-vs-rest and multinomial logistic regression:

For one-vs-rest logistic regression:

*   Each hyperplane is determined independently by considering one class against all others.
    
*   For class 1, the hyperplane represents the decision boundary that best separates class 1 from the combined classes 0 and 2.
    
*   This binary approach can lead to simpler decision boundaries but may not capture complex relationships between all classes simultaneously.
    
*   There is no possible interpretation of the conditional class probabilities.
    

For multinomial logistic regression:

*   All hyperplanes are determined simultaneously, considering the relationships between all classes at once.
    
*   The loss minimized by the model is a proper scoring rule, which means that the model is optimized to estimate the conditional class probabilities that are, therefore, meaningful.
    
*   Each hyperplane represents the decision boundary where the probability of one class becomes higher than the others, based on the overall probability distribution.
    
*   This approach can capture more nuanced relationships between classes, potentially leading to more accurate classification in multi-class problems.
    

The difference in hyperplanes, especially for class 1, highlights how these methods can produce different decision boundaries despite similar overall accuracy.

In practice, using multinomial logistic regression is recommended since it minimizes a well-formulated loss function, leading to better-calibrated class probabilities and thus more interpretable results. When it comes to decision boundaries, one should formulate a utility function to transform the class probabilities into a meaningful quantity for the problem at hand. One-vs-rest allows for different decision boundaries but does not allow for fine-grained control over the trade-off between the classes as a utility function would.

**Total running time of the script:** (0 minutes 0.600 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_logistic_multinomial.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_logistic_multinomial.ipynb)

[`Download Jupyter notebook: plot_logistic_multinomial.ipynb`](https://scikit-learn.org/stable/_downloads/4c1663175b07cf9608b07331aa180eb7/plot_logistic_multinomial.ipynb)

[`Download Python source code: plot_logistic_multinomial.py`](https://scikit-learn.org/stable/_downloads/85c522d0f7149f3e8274112a6d62256f/plot_logistic_multinomial.py)

[`Download zipped: plot_logistic_multinomial.zip`](https://scikit-learn.org/stable/_downloads/200e4f5a26d62475b041ec6d03eca0a6/plot_logistic_multinomial.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_20newsgroups_thumb.png)

[Multiclass sparse logistic regression on 20newgroups](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)

Multiclass sparse logistic regression on 20newgroups

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classification_probability_thumb.png)

[Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html)

Plot classification probability

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbm_logistic_classification_thumb.png)

[Restricted Boltzmann Machine features for digit classification](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html)

Restricted Boltzmann Machine features for digit classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_iris_thumb.png)

[Plot multi-class SGD on the iris dataset](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html)

Plot multi-class SGD on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/85c522d0f7149f3e8274112a6d62256f/plot_logistic_multinomial.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/4c1663175b07cf9608b07331aa180eb7/plot_logistic_multinomial.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/200e4f5a26d62475b041ec6d03eca0a6/plot_logistic_multinomial.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_logistic_multinomial.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_logistic_multinomial.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)