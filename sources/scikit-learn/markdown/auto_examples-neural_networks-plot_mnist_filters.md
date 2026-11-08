[Skip to main content](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neural_networks/plot_mnist_filters.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neural_networks/plot_mnist_filters.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neural_networks/plot_mnist_filters.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neural_networks/plot_mnist_filters.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neural_networks/plot_mnist_filters.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neural_networks/plot_mnist_filters.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html#sphx-glr-download-auto-examples-neural-networks-plot-mnist-filters-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Visualization of MLP weights on MNIST[#](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html#visualization-of-mlp-weights-on-mnist "Link to this heading")

=============================================================================================================================================================================================

Sometimes looking at the learned coefficients of a neural network can provide insight into the learning behavior. For example if weights look unstructured, maybe some were not used at all, or if very large coefficients exist, maybe regularization was too low or the learning rate too high.

This example shows how to plot some of the first layer weights in a MLPClassifier trained on the MNIST dataset.

The input data consists of 28x28 pixel handwritten digits, leading to 784 features in the dataset. Therefore the first layer weight matrix has the shape (784, hidden\_layer\_sizes\[0\]). We can therefore visualize a single column of the weight matrix as a 28x28 pixel image.

To make the example run faster, we use very few hidden units, and train only for a very short time. Training longer would result in weights with a much smoother spatial appearance. The example will throw a warning because it doesn’t converge, in this case this is what we want because of resource usage constraints on our Continuous Integration infrastructure that is used to build this documentation on a regular basis.

![plot mnist filters](https://scikit-learn.org/stable/_images/sphx_glr_plot_mnist_filters_001.png)

Iteration 1, loss = 0.44139186
Iteration 2, loss = 0.19174891
Iteration 3, loss = 0.13983521
Iteration 4, loss = 0.11378556
Iteration 5, loss = 0.09443967
Iteration 6, loss = 0.07846529
Iteration 7, loss = 0.06506307
Iteration 8, loss = 0.05534985
Training set score: 0.986429
Test set score: 0.953061

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import warnings

import matplotlib.pyplot as plt

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
from sklearn.exceptions import [ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.neural\_network import [MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")

\# Load data from https://www.openml.org/d/554
X, y \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
("mnist\_784", version\=1, return\_X\_y\=True, as\_frame\=False)
X \= X / 255.0

\# Split data into train partition and test partition
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, random\_state\=0, test\_size\=0.7)

mlp \= [MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
(
    hidden\_layer\_sizes\=(40,),
    max\_iter\=8,
    alpha\=1e-4,
    solver\="sgd",
    verbose\=10,
    random\_state\=1,
    learning\_rate\_init\=0.2,
)

\# this example won't converge because of resource usage constraints on
\# our Continuous Integration infrastructure, so we catch the warning and
\# ignore it here
with [warnings.catch\_warnings](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings")
():
    [warnings.filterwarnings](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings")
("ignore", category\=[ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
, module\="sklearn")
    mlp.fit(X\_train, y\_train)

print("Training set score: %f" % mlp.score(X\_train, y\_train))
print("Test set score: %f" % mlp.score(X\_test, y\_test))

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(4, 4)
\# use global min / max to ensure all weights are shown on the same scale
vmin, vmax \= mlp.coefs\_\[0\].min(), mlp.coefs\_\[0\].max()
for coef, ax in zip(mlp.coefs\_\[0\].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap\=plt.cm.gray, vmin\=0.5 \* vmin, vmax\=0.5 \* vmax)
    ax.set\_xticks(())
    ax.set\_yticks(())

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 5.513 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo27.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neural_networks/plot_mnist_filters.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo27.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neural_networks/plot_mnist_filters.ipynb)

[`Download Jupyter notebook: plot_mnist_filters.ipynb`](https://scikit-learn.org/stable/_downloads/6522aa1dd16bb328d88cb09cbc08eded/plot_mnist_filters.ipynb)

[`Download Python source code: plot_mnist_filters.py`](https://scikit-learn.org/stable/_downloads/7534058b2748ca58f7594203b7723a0e/plot_mnist_filters.py)

[`Download zipped: plot_mnist_filters.zip`](https://scikit-learn.org/stable/_downloads/4f099a716faccfd3dfbe8161514623b1/plot_mnist_filters.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_training_curves_thumb.png)

[Compare Stochastic learning strategies for MLPClassifier](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html)

Compare Stochastic learning strategies for MLPClassifier

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_mnist_thumb.png)

[MNIST classification using multinomial logistic + L1](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_mnist.html)

MNIST classification using multinomial logistic + L1

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_regression_thumb.png)

[Nearest Neighbors regression](https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html)

Nearest Neighbors regression

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_weighted_samples_thumb.png)

[SVM: Weighted samples](https://scikit-learn.org/stable/auto_examples/svm/plot_weighted_samples.html)

SVM: Weighted samples

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/7534058b2748ca58f7594203b7723a0e/plot_mnist_filters.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/6522aa1dd16bb328d88cb09cbc08eded/plot_mnist_filters.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/4f099a716faccfd3dfbe8161514623b1/plot_mnist_filters.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo27.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neural_networks/plot_mnist_filters.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo27.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neural_networks/plot_mnist_filters.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)