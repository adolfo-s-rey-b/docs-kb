[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_rbf_parameters.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_rbf_parameters.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_rbf_parameters.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_rbf_parameters.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_rbf_parameters.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_rbf_parameters.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html#sphx-glr-download-auto-examples-svm-plot-rbf-parameters-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

RBF SVM parameters[#](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html#rbf-svm-parameters "Link to this heading")

============================================================================================================================================

This example illustrates the effect of the parameters `gamma` and `C` of the Radial Basis Function (RBF) kernel SVM.

Intuitively, the `gamma` parameter defines how far the influence of a single training example reaches, with low values meaning ‘far’ and high values meaning ‘close’. The `gamma` parameters can be seen as the inverse of the radius of influence of samples selected by the model as support vectors.

The `C` parameter trades off correct classification of training examples against maximization of the decision function’s margin. For larger values of `C`, a smaller margin will be accepted if the decision function is better at classifying all training points correctly. A lower `C` will encourage a larger margin, therefore a simpler decision function, at the cost of training accuracy. In other words `C` behaves as a regularization parameter in the SVM.

The first plot is a visualization of the decision function for a variety of parameter values on a simplified classification problem involving only 2 input features and 2 possible target classes (binary classification). Note that this kind of plot is not possible to do for problems with more features.

The second plot is a heatmap of the classifier’s cross-validation accuracy as a function of `C` and `gamma`. For this example we explore a relatively large grid for illustration purposes. In practice, a logarithmic grid from 10−3 to 103 is usually sufficient. If the best parameters lie on the boundaries of the grid, it can be extended in that direction in a subsequent search.

Note that the heat map plot has a special colorbar with a midpoint value close to the score values of the best performing models so as to make it easy to tell them apart in the blink of an eye.

The behavior of the model is very sensitive to the `gamma` parameter. If `gamma` is too large, the radius of the area of influence of the support vectors only includes the support vector itself and no amount of regularization with `C` will be able to prevent overfitting.

When `gamma` is very small, the model is too constrained and cannot capture the complexity or “shape” of the data. The region of influence of any selected support vector would include the whole training set. The resulting model will behave similarly to a linear model with a set of hyperplanes that separate the centers of high density of any pair of two classes.

For intermediate values, we can see on the second plot that good models can be found on a diagonal of `C` and `gamma`. Smooth models (lower `gamma` values) can be made more complex by increasing the importance of classifying each point correctly (larger `C` values) hence the diagonal of good performing models.

Finally, one can also observe that for some intermediate values of `gamma` we get equally performing models when `C` becomes very large. This suggests that the set of support vectors does not change anymore. The radius of the RBF kernel alone acts as a good structural regularizer. Increasing `C` further doesn’t help, likely because there are no more training points in violation (inside the margin or wrongly classified), or at least no better solution can be found. Scores being equal, it may make sense to use the smaller `C` values, since very high `C` values typically increase fitting time.

On the other hand, lower `C` values generally lead to more support vectors, which may increase prediction time. Therefore, lowering the value of `C` involves a trade-off between fitting time and prediction time.

We should also note that small differences in scores results from the random splits of the cross-validation procedure. Those spurious variations can be smoothed out by increasing the number of CV iterations `n_splits` at the expense of compute time. Increasing the value number of `C_range` and `gamma_range` steps will increase the resolution of the hyper-parameter heat map.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Utility class to move the midpoint of a colormap to be around the values of interest.

import numpy as np
from matplotlib.colors import [Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

class MidpointNormalize([Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
):
    def \_\_init\_\_(self, vmin\=None, vmax\=None, midpoint\=None, clip\=False):
        self.midpoint \= midpoint
        [Normalize](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
.\_\_init\_\_(self, vmin, vmax, clip)

    def \_\_call\_\_(self, value, clip\=None):
        x, y \= \[self.vmin, self.midpoint, self.vmax\], \[0, 0.5, 1\]
        return [np.ma.masked\_array](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.html#numpy.ma.masked_array "numpy.ma.masked_array")
([np.interp](https://numpy.org/doc/stable/reference/generated/numpy.interp.html#numpy.interp "numpy.interp")
(value, x, y))

Copy to clipboard

Load and prepare data set[#](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html#load-and-prepare-data-set "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

dataset for grid search

from sklearn.datasets import [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")

iris \= [load\_iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
()
X \= iris.data
y \= iris.target

Copy to clipboard

Dataset for decision function visualization: we only keep the first two features in X and sub-sample the dataset to keep only 2 classes and make it a binary classification problem.

X\_2d \= X\[:, :2\]
X\_2d \= X\_2d\[y \> 0\]
y\_2d \= y\[y \> 0\]
y\_2d \-= 1

Copy to clipboard

It is usually a good idea to scale the data for SVM training. We are cheating a bit in this example in scaling all of the data, instead of fitting the transformation on the training set and just applying it on the test set.

from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

scaler \= [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")
()
X \= scaler.fit\_transform(X)
X\_2d \= scaler.fit\_transform(X\_2d)

Copy to clipboard

Train classifiers[#](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html#train-classifiers "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

For an initial search, a logarithmic grid with basis 10 is often helpful. Using a basis of 2, a finer tuning can be achieved but at a much higher cost.

from sklearn.model\_selection import [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
, [StratifiedShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
from sklearn.svm import [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")

C\_range \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-2, 10, 13)
gamma\_range \= [np.logspace](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")
(\-9, 3, 13)
param\_grid \= dict(gamma\=gamma\_range, C\=C\_range)
cv \= [StratifiedShuffleSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit")
(n\_splits\=5, test\_size\=0.2, random\_state\=42)
grid \= [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
([SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(), param\_grid\=param\_grid, cv\=cv)
grid.fit(X, y)

print(
    f"The best parameters are {grid.best\_params\_} "
    f"with a score of {grid.best\_score\_:0.2f}"
)

Copy to clipboard

The best parameters are {'C': np.float64(1.0), 'gamma': np.float64(0.1)} with a score of 0.97

Copy to clipboard

Now we need to fit a classifier for all parameters in the 2d version (we use a smaller set of parameters here because it takes a while to train)

C\_2d\_range \= \[0.01, 1, 100\]
gamma\_2d\_range \= \[0.1, 1, 10\]
classifiers \= \[\]
for C in C\_2d\_range:
    for gamma in gamma\_2d\_range:
        clf \= [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(C\=C, gamma\=gamma)
        clf.fit(X\_2d, y\_2d)
        classifiers.append((C, gamma, clf))

Copy to clipboard

Visualization[#](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html#visualization "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

We plot the decision boundaries for different values of gamma and C.

import matplotlib.pyplot as plt

from sklearn.inspection import DecisionBoundaryDisplay

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 6))
for k, (C, gamma, clf) in enumerate(classifiers):
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(len(C\_2d\_range), len(gamma\_2d\_range), k + 1)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(f"gamma={gamma}, C={C}", size\="medium")
    \# visualize decision boundary for these parameters
    [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        clf,
        X\_2d,
        eps\=0.5,
        cmap\="RdBu\_r",
        ax\=[plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
(),
        response\_method\="decision\_function",
        plot\_method\="pcolormesh",
    )
    \# also plot the data
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\_2d\[:, 0\], X\_2d\[:, 1\], c\=y\_2d, cmap\=plt.cm.RdBu\_r, edgecolors\="k")
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())

Copy to clipboard

![gamma=0.1, C=0.01, gamma=1, C=0.01, gamma=10, C=0.01, gamma=0.1, C=1, gamma=1, C=1, gamma=10, C=1, gamma=0.1, C=100, gamma=1, C=100, gamma=10, C=100](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_001.png)

Draw heatmap of the validation accuracy as a function of gamma and C

The score are encoded as colors with the hot colormap which varies from dark red to bright yellow. As the most interesting scores are all located in the 0.92 to 0.97 range we use a custom normalizer to set the mid-point to 0.92 so as to make it easier to visualize the small variations of score values in the interesting range while not brutally collapsing all the low score values to the same color.

scores \= grid.cv\_results\_\["mean\_test\_score"\].reshape(len(C\_range), len(gamma\_range))
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 6))
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(left\=0.2, right\=0.95, bottom\=0.15, top\=0.95)
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(
    scores,
    interpolation\="nearest",
    cmap\=plt.cm.hot,
    norm\=MidpointNormalize(vmin\=0.2, midpoint\=0.92),
)
[plt.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel")
("gamma")
[plt.ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel")
("C")
[plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
()
[plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(gamma\_range)), gamma\_range, rotation\=45)
[plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(len(C\_range)), C\_range)
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Validation accuracy")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Validation accuracy](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_002.png)

**Total running time of the script:** (0 minutes 4.829 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_rbf_parameters.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_rbf_parameters.ipynb)

[`Download Jupyter notebook: plot_rbf_parameters.ipynb`](https://scikit-learn.org/stable/_downloads/d55388904f5399e98ed36e971c4da3cf/plot_rbf_parameters.ipynb)

[`Download Python source code: plot_rbf_parameters.py`](https://scikit-learn.org/stable/_downloads/ea8b449d4699d078ef9cc5cded54cc67/plot_rbf_parameters.py)

[`Download zipped: plot_rbf_parameters.zip`](https://scikit-learn.org/stable/_downloads/44ae219cc6359efae1cf5a6dc3e4b2e8/plot_rbf_parameters.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_thumb.png)

[Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Plot different SVM classifiers in the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_kernels_thumb.png)

[Plot classification boundaries with different SVM Kernels](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html)

Plot classification boundaries with different SVM Kernels

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_custom_kernel_thumb.png)

[SVM with custom kernel](https://scikit-learn.org/stable/auto_examples/svm/plot_custom_kernel.html)

SVM with custom kernel

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_approximation_thumb.png)

[Explicit feature map approximation for RBF kernels](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html)

Explicit feature map approximation for RBF kernels

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/ea8b449d4699d078ef9cc5cded54cc67/plot_rbf_parameters.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/d55388904f5399e98ed36e971c4da3cf/plot_rbf_parameters.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/44ae219cc6359efae1cf5a6dc3e4b2e8/plot_rbf_parameters.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_rbf_parameters.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_rbf_parameters.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)