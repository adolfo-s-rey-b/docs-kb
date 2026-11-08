[Skip to main content](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/neural_networks/plot_mlp_training_curves.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/neural_networks/plot_mlp_training_curves.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/neural_networks/plot_mlp_training_curves.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/neural_networks/plot_mlp_training_curves.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/neural_networks/plot_mlp_training_curves.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/neural_networks/plot_mlp_training_curves.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html#sphx-glr-download-auto-examples-neural-networks-plot-mlp-training-curves-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Compare Stochastic learning strategies for MLPClassifier[#](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mlp_training_curves.html#compare-stochastic-learning-strategies-for-mlpclassifier "Link to this heading")

=========================================================================================================================================================================================================================================

This example visualizes some training loss curves for different stochastic learning strategies, including SGD and Adam. Because of time-constraints, we use several small datasets, for which L-BFGS might be more suitable. The general trend shown in these examples seems to carry over to larger datasets, however.

Note that those results can be highly dependent on the value of `learning_rate_init`.

![iris, digits, circles, moons](https://scikit-learn.org/stable/_images/sphx_glr_plot_mlp_training_curves_001.png)

learning on dataset iris
training: constant learning-rate
Training set score: 0.980000
Training set loss: 0.096950
training: constant with momentum
Training set score: 0.980000
Training set loss: 0.049530
training: constant with Nesterov's momentum
Training set score: 0.980000
Training set loss: 0.049540
training: inv-scaling learning-rate
Training set score: 0.360000
Training set loss: 0.978444
training: inv-scaling with momentum
Training set score: 0.860000
Training set loss: 0.504185
training: inv-scaling with Nesterov's momentum
Training set score: 0.860000
Training set loss: 0.503452
training: adam
Training set score: 0.980000
Training set loss: 0.045311

learning on dataset digits
training: constant learning-rate
Training set score: 0.956038
Training set loss: 0.243802
training: constant with momentum
Training set score: 0.992766
Training set loss: 0.041297
training: constant with Nesterov's momentum
Training set score: 0.993879
Training set loss: 0.042898
training: inv-scaling learning-rate
Training set score: 0.638843
Training set loss: 1.855465
training: inv-scaling with momentum
Training set score: 0.909293
Training set loss: 0.318387
training: inv-scaling with Nesterov's momentum
Training set score: 0.912632
Training set loss: 0.290584
training: adam
Training set score: 0.991653
Training set loss: 0.045934

learning on dataset circles
training: constant learning-rate
Training set score: 0.840000
Training set loss: 0.601052
training: constant with momentum
Training set score: 0.940000
Training set loss: 0.157334
training: constant with Nesterov's momentum
Training set score: 0.940000
Training set loss: 0.154453
training: inv-scaling learning-rate
Training set score: 0.500000
Training set loss: 0.692470
training: inv-scaling with momentum
Training set score: 0.500000
Training set loss: 0.689751
training: inv-scaling with Nesterov's momentum
Training set score: 0.500000
Training set loss: 0.689143
training: adam
Training set score: 0.940000
Training set loss: 0.150527

learning on dataset moons
training: constant learning-rate
Training set score: 0.850000
Training set loss: 0.341523
training: constant with momentum
Training set score: 0.850000
Training set loss: 0.336188
training: constant with Nesterov's momentum
Training set score: 0.850000
Training set loss: 0.335919
training: inv-scaling learning-rate
Training set score: 0.500000
Training set loss: 0.689015
training: inv-scaling with momentum
Training set score: 0.830000
Training set loss: 0.513034
training: inv-scaling with Nesterov's momentum
Training set score: 0.830000
Training set loss: 0.512595
training: adam
Training set score: 0.930000
Training set loss: 0.170087

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import warnings

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.exceptions import [ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
from sklearn.neural\_network import [MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
from sklearn.preprocessing import [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")

\# different learning rate schedules and momentum parameters
params \= \[\
    {\
        "solver": "sgd",\
        "learning\_rate": "constant",\
        "momentum": 0,\
        "learning\_rate\_init": 0.2,\
    },\
    {\
        "solver": "sgd",\
        "learning\_rate": "constant",\
        "momentum": 0.9,\
        "nesterovs\_momentum": False,\
        "learning\_rate\_init": 0.2,\
    },\
    {\
        "solver": "sgd",\
        "learning\_rate": "constant",\
        "momentum": 0.9,\
        "nesterovs\_momentum": True,\
        "learning\_rate\_init": 0.2,\
    },\
    {\
        "solver": "sgd",\
        "learning\_rate": "invscaling",\
        "momentum": 0,\
        "learning\_rate\_init": 0.2,\
    },\
    {\
        "solver": "sgd",\
        "learning\_rate": "invscaling",\
        "momentum": 0.9,\
        "nesterovs\_momentum": False,\
        "learning\_rate\_init": 0.2,\
    },\
    {\
        "solver": "sgd",\
        "learning\_rate": "invscaling",\
        "momentum": 0.9,\
        "nesterovs\_momentum": True,\
        "learning\_rate\_init": 0.2,\
    },\
    {"solver": "adam", "learning\_rate\_init": 0.01},\
\]

labels \= \[\
    "constant learning-rate",\
    "constant with momentum",\
    "constant with Nesterov's momentum",\
    "inv-scaling learning-rate",\
    "inv-scaling with momentum",\
    "inv-scaling with Nesterov's momentum",\
    "adam",\
\]

plot\_args \= \[\
    {"c": "red", "linestyle": "-"},\
    {"c": "green", "linestyle": "-"},\
    {"c": "blue", "linestyle": "-"},\
    {"c": "red", "linestyle": "--"},\
    {"c": "green", "linestyle": "--"},\
    {"c": "blue", "linestyle": "--"},\
    {"c": "black", "linestyle": "-"},\
\]

def plot\_on\_dataset(X, y, ax, name):
    \# for each dataset, plot learning for each learning strategy
    print("\\nlearning on dataset %s" % name)
    ax.set\_title(name)

    X \= [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
().fit\_transform(X)
    mlps \= \[\]
    if name \== "digits":
        \# digits is larger but converges fairly quickly
        max\_iter \= 15
    else:
        max\_iter \= 400

    for label, param in zip(labels, params):
        print("training: %s" % label)
        mlp \= [MLPClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
(random\_state\=0, max\_iter\=max\_iter, \*\*param)

        \# some parameter combinations will not converge as can be seen on the
        \# plots so they are ignored here
        with [warnings.catch\_warnings](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings")
():
            [warnings.filterwarnings](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings")
(
                "ignore", category\=[ConvergenceWarning](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning")
, module\="sklearn"
            )
            mlp.fit(X, y)

        mlps.append(mlp)
        print("Training set score: %f" % mlp.score(X, y))
        print("Training set loss: %f" % mlp.loss\_)
    for mlp, label, args in zip(mlps, labels, plot\_args):
        ax.plot(mlp.loss\_curve\_, label\=label, \*\*args)

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(15, 10))
\# load / generate some toy datasets
iris \= [datasets.load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X\_digits, y\_digits \= [datasets.load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(return\_X\_y\=True)
data\_sets \= \[\
    (iris.data, iris.target),\
    (X\_digits, y\_digits),\
    [datasets.make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")\
(noise\=0.2, factor\=0.5, random\_state\=1),\
    [datasets.make\_moons](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html#sklearn.datasets.make_moons "sklearn.datasets.make_moons")\
(noise\=0.3, random\_state\=0),\
\]

for ax, data, name in zip(
    axes.ravel(), data\_sets, \["iris", "digits", "circles", "moons"\]
):
    plot\_on\_dataset(\*data, ax\=ax, name\=name)

fig.legend(ax.get\_lines(), labels, ncol\=3, loc\="upper center")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 3.207 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo27.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neural_networks/plot_mlp_training_curves.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo27.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neural_networks/plot_mlp_training_curves.ipynb)

[`Download Jupyter notebook: plot_mlp_training_curves.ipynb`](https://scikit-learn.org/stable/_downloads/646b2c083be2d0f557b369a51cec966d/plot_mlp_training_curves.ipynb)

[`Download Python source code: plot_mlp_training_curves.py`](https://scikit-learn.org/stable/_downloads/1a0eed524b181183d59e57a5a9df565b/plot_mlp_training_curves.py)

[`Download zipped: plot_mlp_training_curves.zip`](https://scikit-learn.org/stable/_downloads/4cfbe7582ae87a68ed98582a86d0bb9c/plot_mlp_training_curves.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_mnist_filters_thumb.png)

[Visualization of MLP weights on MNIST](https://scikit-learn.org/stable/auto_examples/neural_networks/plot_mnist_filters.html)

Visualization of MLP weights on MNIST

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regularization_thumb.png)

[Gradient Boosting regularization](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regularization.html)

Gradient Boosting regularization

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_iris_thumb.png)

[Plot multi-class SGD on the iris dataset](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_iris.html)

Plot multi-class SGD on the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_logistic_regression_20newsgroups_thumb.png)

[Multiclass sparse logistic regression on 20newgroups](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sparse_logistic_regression_20newsgroups.html)

Multiclass sparse logistic regression on 20newgroups

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/1a0eed524b181183d59e57a5a9df565b/plot_mlp_training_curves.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/646b2c083be2d0f557b369a51cec966d/plot_mlp_training_curves.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/4cfbe7582ae87a68ed98582a86d0bb9c/plot_mlp_training_curves.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo27.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/neural_networks/plot_mlp_training_curves.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo27.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/neural_networks/plot_mlp_training_curves.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)