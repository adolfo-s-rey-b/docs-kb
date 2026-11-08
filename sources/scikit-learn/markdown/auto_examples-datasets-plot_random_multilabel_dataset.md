[Skip to main content](https://scikit-learn.org/stable/auto_examples/datasets/plot_random_multilabel_dataset.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/datasets/plot_random_multilabel_dataset.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/datasets/plot_random_multilabel_dataset.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/datasets/plot_random_multilabel_dataset.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/datasets/plot_random_multilabel_dataset.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/datasets/plot_random_multilabel_dataset.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/datasets/plot_random_multilabel_dataset.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/datasets/plot_random_multilabel_dataset.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/datasets/plot_random_multilabel_dataset.html#sphx-glr-download-auto-examples-datasets-plot-random-multilabel-dataset-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plot randomly generated multilabel dataset[#](https://scikit-learn.org/stable/auto_examples/datasets/plot_random_multilabel_dataset.html#plot-randomly-generated-multilabel-dataset "Link to this heading")

============================================================================================================================================================================================================

This illustrates the [`make_multilabel_classification`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")
 dataset generator. Each sample consists of counts of two features (up to 50 in total), which are differently distributed in each of two classes.

Points are labeled as follows, where Y means the class is present:

| 1   | 2   | 3   | Color |
| --- | --- | --- | --- |
| Y   | N   | N   | Red |
| N   | Y   | N   | Blue |
| N   | N   | Y   | Yellow |
| Y   | Y   | N   | Purple |
| Y   | N   | Y   | Orange |
| Y   | Y   | N   | Green |
| Y   | Y   | Y   | Brown |

A star marks the expected sample for each class; its size reflects the probability of selecting that class label.

The left and right examples highlight the `n_labels` parameter: more of the samples in the right plot have 2 or 3 labels.

Note that this two-dimensional example is very degenerate: generally the number of features would be much greater than the “document length”, while here we have much larger documents than vocabulary. Similarly, with `n_classes > n_features`, it is much less likely that a feature distinguishes a particular class.

![n_labels=1, length=50, n_labels=3, length=50](https://scikit-learn.org/stable/_images/sphx_glr_plot_random_multilabel_dataset_001.png)

The data was generated from (random\_state=431):
Class   P(C)    P(w0|C) P(w1|C)
red     0.39    0.96    0.04
blue    0.20    0.17    0.83
yellow  0.41    0.71    0.29

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import make\_multilabel\_classification as [make\_ml\_clf](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")

COLORS \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
    \[\
        "!",\
        "#FF3333",  \# red\
        "#0198E1",  \# blue\
        "#BF5FFF",  \# purple\
        "#FCD116",  \# yellow\
        "#FF7216",  \# orange\
        "#4DBD33",  \# green\
        "#87421F",  \# brown\
    \]
)

\# Use same random seed for multiple calls to make\_multilabel\_classification to
\# ensure same distributions
RANDOM\_SEED \= [np.random.randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")
(2\*\*10)

def plot\_2d(ax, n\_labels\=1, n\_classes\=3, length\=50):
    X, Y, p\_c, p\_w\_c \= [make\_ml\_clf](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_multilabel_classification.html#sklearn.datasets.make_multilabel_classification "sklearn.datasets.make_multilabel_classification")
(
        n\_samples\=150,
        n\_features\=2,
        n\_classes\=n\_classes,
        n\_labels\=n\_labels,
        length\=length,
        allow\_unlabeled\=False,
        return\_distributions\=True,
        random\_state\=RANDOM\_SEED,
    )

    ax.scatter(
        X\[:, 0\], X\[:, 1\], color\=COLORS.take((Y \* \[1, 2, 4\]).sum(axis\=1)), marker\="."
    )
    ax.scatter(
        p\_w\_c\[0\] \* length,
        p\_w\_c\[1\] \* length,
        marker\="\*",
        linewidth\=0.5,
        edgecolor\="black",
        s\=20 + 1500 \* p\_c\*\*2,
        color\=COLORS.take(\[1, 2, 4\]),
    )
    ax.set\_xlabel("Feature 0 count")
    return p\_c, p\_w\_c

\_, (ax1, ax2) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, sharex\="row", sharey\="row", figsize\=(8, 4))
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(bottom\=0.15)

p\_c, p\_w\_c \= plot\_2d(ax1, n\_labels\=1)
ax1.set\_title("n\_labels=1, length=50")
ax1.set\_ylabel("Feature 1 count")

plot\_2d(ax2, n\_labels\=3)
ax2.set\_title("n\_labels=3, length=50")
ax2.set\_xlim(left\=0, auto\=True)
ax2.set\_ylim(bottom\=0, auto\=True)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

print("The data was generated from (random\_state=%d):" % RANDOM\_SEED)
print("Class", "P(C)", "P(w0|C)", "P(w1|C)", sep\="\\t")
for k, p, p\_w in zip(\["red", "blue", "yellow"\], p\_c, p\_w\_c.T):
    print("%s\\t%0.2f\\t%0.2f\\t%0.2f" % (k, p, p\_w\[0\], p\_w\[1\]))

Copy to clipboard

**Total running time of the script:** (0 minutes 0.118 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo9.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/datasets/plot_random_multilabel_dataset.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo9.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/datasets/plot_random_multilabel_dataset.ipynb)

[`Download Jupyter notebook: plot_random_multilabel_dataset.ipynb`](https://scikit-learn.org/stable/_downloads/a8ae7970b854e7e2bea48bb7688bd7b6/plot_random_multilabel_dataset.ipynb)

[`Download Python source code: plot_random_multilabel_dataset.py`](https://scikit-learn.org/stable/_downloads/59fa6c0bdd3e601dd83ea28de5feeffd/plot_random_multilabel_dataset.py)

[`Download zipped: plot_random_multilabel_dataset.zip`](https://scikit-learn.org/stable/_downloads/791b155aa29ed0f81163191b9eb8abb8/plot_random_multilabel_dataset.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_multilabel_thumb.png)

[Multilabel classification](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multilabel.html)

Multilabel classification

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_discretization_thumb.png)

[Using KBinsDiscretizer to discretize continuous features](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_discretization.html)

Using KBinsDiscretizer to discretize continuous features

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_self_training_varying_threshold_thumb.png)

[Effect of varying threshold for self-training](https://scikit-learn.org/stable/auto_examples/semi_supervised/plot_self_training_varying_threshold.html)

Effect of varying threshold for self-training

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_concentration_prior_thumb.png)

[Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html)

Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/59fa6c0bdd3e601dd83ea28de5feeffd/plot_random_multilabel_dataset.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/a8ae7970b854e7e2bea48bb7688bd7b6/plot_random_multilabel_dataset.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/791b155aa29ed0f81163191b9eb8abb8/plot_random_multilabel_dataset.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo9.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/datasets/plot_random_multilabel_dataset.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo9.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/datasets/plot_random_multilabel_dataset.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)