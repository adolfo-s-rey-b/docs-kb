[Skip to main content](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_on_structured_data.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/gaussian_process/plot_gpr_on_structured_data.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_on_structured_data.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/gaussian_process/plot_gpr_on_structured_data.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/gaussian_process/plot_gpr_on_structured_data.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/gaussian_process/plot_gpr_on_structured_data.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/gaussian_process/plot_gpr_on_structured_data.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/gaussian_process/plot_gpr_on_structured_data.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_on_structured_data.html#sphx-glr-download-auto-examples-gaussian-process-plot-gpr-on-structured-data-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Gaussian processes on discrete data structures[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_on_structured_data.html#gaussian-processes-on-discrete-data-structures "Link to this heading")

=========================================================================================================================================================================================================================

This example illustrates the use of Gaussian processes for regression and classification tasks on data that are not in fixed-length feature vector form. This is achieved through the use of kernel functions that operate directly on discrete structures such as variable-length sequences, trees, and graphs.

Specifically, here the input variables are some gene sequences stored as variable-length strings consisting of letters ‘A’, ‘T’, ‘C’, and ‘G’, while the output variables are floating point numbers and True/False labels in the regression and classification tasks, respectively.

A kernel between the gene sequences is defined using R-convolution [\[1\]](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_on_structured_data.html#id2)
 by integrating a binary letter-wise kernel over all pairs of letters among a pair of strings.

This example will generate three figures.

In the first figure, we visualize the value of the kernel, i.e. the similarity of the sequences, using a colormap. Brighter color here indicates higher similarity.

In the second figure, we show some regression result on a dataset of 6 sequences. Here we use the 1st, 2nd, 4th, and 5th sequences as the training set to make predictions on the 3rd and 6th sequences.

In the third figure, we demonstrate a classification model by training on 6 sequences and make predictions on another 5 sequences. The ground truth here is simply whether there is at least one ‘A’ in the sequence. Here the model makes four correct classifications and fails on one.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

import numpy as np

from sklearn.base import clone
from sklearn.gaussian\_process import [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
, [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
from sklearn.gaussian\_process.kernels import GenericKernelMixin, [Hyperparameter](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter "sklearn.gaussian_process.kernels.Hyperparameter")
, [Kernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Kernel.html#sklearn.gaussian_process.kernels.Kernel "sklearn.gaussian_process.kernels.Kernel")

class SequenceKernel(GenericKernelMixin, [Kernel](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Kernel.html#sklearn.gaussian_process.kernels.Kernel "sklearn.gaussian_process.kernels.Kernel")
):
    """
    A minimal (but valid) convolutional kernel for sequences of variable
    lengths."""

    def \_\_init\_\_(self, baseline\_similarity\=0.5, baseline\_similarity\_bounds\="fixed"):
        self.baseline\_similarity \= baseline\_similarity
        self.baseline\_similarity\_bounds \= baseline\_similarity\_bounds

    @property
    def hyperparameter\_baseline\_similarity(self):
        return [Hyperparameter](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Hyperparameter.html#sklearn.gaussian_process.kernels.Hyperparameter "sklearn.gaussian_process.kernels.Hyperparameter")
(
            "baseline\_similarity", "numeric", self.baseline\_similarity\_bounds
        )

    def \_f(self, s1, s2):
        """
        kernel value between a pair of sequences
        """
        return sum(
            \[1.0 if c1 \== c2 else self.baseline\_similarity for c1 in s1 for c2 in s2\]
        )

    def \_g(self, s1, s2):
        """
        kernel derivative between a pair of sequences
        """
        return sum(\[0.0 if c1 \== c2 else 1.0 for c1 in s1 for c2 in s2\])

    def \_\_call\_\_(self, X, Y\=None, eval\_gradient\=False):
        if Y is None:
            Y \= X

        if eval\_gradient:
            return (
                [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[self.\_f(x, y) for y in Y\] for x in X\]),
                [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[\[self.\_g(x, y)\] for y in Y\] for x in X\]),
            )
        else:
            return [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[self.\_f(x, y) for y in Y\] for x in X\])

    def diag(self, X):
        return [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[self.\_f(x, x) for x in X\])

    def is\_stationary(self):
        return False

    def clone\_with\_theta(self, theta):
        cloned \= clone(self)
        cloned.theta \= theta
        return cloned

Copy to clipboard

Note

Here, we freeze the value of `baseline_similarity` by setting `baseline_similarity_bounds="fixed"` as LBFGS would otherwise fail to optimize the value of this kernel parameter for some unknown reason.

kernel \= SequenceKernel()

Copy to clipboard

Sequence similarity matrix under the kernel[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_on_structured_data.html#sequence-similarity-matrix-under-the-kernel "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\["AGCT", "AGC", "AACT", "TAA", "AAA", "GAACA"\])

K \= kernel(X)
D \= kernel.diag(X)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 5))
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
([np.diag](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
(D\*\*-0.5).dot(K).dot([np.diag](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")
(D\*\*-0.5)))
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(X)), X)
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(X)), X)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Sequence similarity under the kernel")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Sequence similarity under the kernel](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_on_structured_data_001.png)

Regression[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_on_structured_data.html#regression "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\["AGCT", "AGC", "AACT", "TAA", "AAA", "GAACA"\])
Y \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[1.0, 1.0, 2.0, 2.0, 3.0, 3.0\])

training\_idx \= \[0, 1, 3, 4\]
gp \= [GaussianProcessRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
(kernel\=kernel)
gp.fit(X\[training\_idx\], Y\[training\_idx\])

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 5))
[plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(X)), gp.predict(X), color\="b", label\="prediction")
[plt.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
(training\_idx, Y\[training\_idx\], width\=0.2, color\="r", alpha\=1, label\="training")
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(X)), X)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Regression on sequences")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Regression on sequences](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_on_structured_data_002.png)

Classification[#](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_on_structured_data.html#classification "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

X\_train \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\["AGCT", "CGA", "TAAC", "TCG", "CTTT", "TGCT"\])
\# whether there are 'A's in the sequence
Y\_train \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[True, True, True, False, False, False\])

gp \= [GaussianProcessClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
(kernel)
gp.fit(X\_train, Y\_train)

X\_test \= \["AAA", "ATAG", "CTC", "CT", "C"\]
Y\_test \= \[True, True, False, False, False\]

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 5))
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(X\_train)),
    \[1.0 if c else \-1.0 for c in Y\_train\],
    s\=100,
    marker\="o",
    edgecolor\="none",
    facecolor\=(1, 0.75, 0),
    label\="training",
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    len(X\_train) + [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(X\_test)),
    \[1.0 if c else \-1.0 for c in Y\_test\],
    s\=100,
    marker\="o",
    edgecolor\="none",
    facecolor\="r",
    label\="truth",
)
[plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
    len(X\_train) + [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(X\_test)),
    \[1.0 if c else \-1.0 for c in gp.predict(X\_test)\],
    s\=100,
    marker\="x",
    facecolor\="b",
    linewidth\=2,
    label\="prediction",
)
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(X\_train) + len(X\_test)), [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
((X\_train, X\_test)))
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(\[\-1, 1\], \[False, True\])
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Classification on sequences")
[plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Classification on sequences](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_on_structured_data_003.png)

**Total running time of the script:** (0 minutes 0.215 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpr_on_structured_data.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpr_on_structured_data.ipynb)

[`Download Jupyter notebook: plot_gpr_on_structured_data.ipynb`](https://scikit-learn.org/stable/_downloads/46c19b52b5a5ab5796725eb7e0688309/plot_gpr_on_structured_data.ipynb)

[`Download Python source code: plot_gpr_on_structured_data.py`](https://scikit-learn.org/stable/_downloads/348dd747b709a747e14c8bcdddf0a9b6/plot_gpr_on_structured_data.py)

[`Download zipped: plot_gpr_on_structured_data.zip`](https://scikit-learn.org/stable/_downloads/419245a165589a136566a555741c80e8/plot_gpr_on_structured_data.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpc_iris_thumb.png)

[Gaussian process classification (GPC) on iris dataset](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpc_iris.html)

Gaussian process classification (GPC) on iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gpr_noisy_targets_thumb.png)

[Gaussian Processes regression: basic introductory example](https://scikit-learn.org/stable/auto_examples/gaussian_process/plot_gpr_noisy_targets.html)

Gaussian Processes regression: basic introductory example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_thumb.png)

[RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

RBF SVM parameters

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_iris_thumb.png)

[Plot the decision surfaces of ensembles of trees on the iris dataset](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html)

Plot the decision surfaces of ensembles of trees on the iris dataset

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/348dd747b709a747e14c8bcdddf0a9b6/plot_gpr_on_structured_data.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/46c19b52b5a5ab5796725eb7e0688309/plot_gpr_on_structured_data.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/419245a165589a136566a555741c80e8/plot_gpr_on_structured_data.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo15.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/gaussian_process/plot_gpr_on_structured_data.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo15.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/gaussian_process/plot_gpr_on_structured_data.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)