[Skip to main content](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/svm/plot_svm_kernels.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/svm/plot_svm_kernels.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/svm/plot_svm_kernels.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/svm/plot_svm_kernels.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/svm/plot_svm_kernels.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/svm/plot_svm_kernels.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#sphx-glr-download-auto-examples-svm-plot-svm-kernels-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Plot classification boundaries with different SVM Kernels[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#plot-classification-boundaries-with-different-svm-kernels "Link to this heading")

=======================================================================================================================================================================================================================

This example shows how different kernels in a [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 (Support Vector Classifier) influence the classification boundaries in a binary, two-dimensional classification problem.

SVCs aim to find a hyperplane that effectively separates the classes in their training data by maximizing the margin between the outermost data points of each class. This is achieved by finding the best weight vector w that defines the decision boundary hyperplane and minimizes the sum of hinge losses for misclassified samples, as measured by the [`hinge_loss`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.hinge_loss.html#sklearn.metrics.hinge_loss "sklearn.metrics.hinge_loss")
 function. By default, regularization is applied with the parameter `C=1`, which allows for a certain degree of misclassification tolerance.

If the data is not linearly separable in the original feature space, a non-linear kernel parameter can be set. Depending on the kernel, the process involves adding new features or transforming existing features to enrich and potentially add meaning to the data. When a kernel other than `"linear"` is set, the SVC applies the [kernel trick](https://en.wikipedia.org/wiki/Kernel_method#Mathematics:_the_kernel_trick)
, which computes the similarity between pairs of data points using the kernel function without explicitly transforming the entire dataset. The kernel trick surpasses the otherwise necessary matrix transformation of the whole dataset by only considering the relations between all pairs of data points. The kernel function maps two vectors (each pair of observations) to their similarity using their dot product.

The hyperplane can then be calculated using the kernel function as if the dataset were represented in a higher-dimensional space. Using a kernel function instead of an explicit matrix transformation improves performance, as the kernel function has a time complexity of O(n2), whereas matrix transformation scales according to the specific transformation being applied.

In this example, we compare the most common kernel types of Support Vector Machines: the linear kernel (`"linear"`), the polynomial kernel (`"poly"`), the radial basis function kernel (`"rbf"`) and the sigmoid kernel (`"sigmoid"`).

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Creating a dataset[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#creating-a-dataset "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

We create a two-dimensional classification dataset with 16 samples and two classes. We plot the samples with the colors matching their respective targets.

import matplotlib.pyplot as plt
import numpy as np

X \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
    \[\
        \[0.4, \-0.7\],\
        \[\-1.5, \-1.0\],\
        \[\-1.4, \-0.9\],\
        \[\-1.3, \-1.2\],\
        \[\-1.1, \-0.2\],\
        \[\-1.2, \-0.4\],\
        \[\-0.5, 1.2\],\
        \[\-1.5, 2.1\],\
        \[1.0, 1.0\],\
        \[1.3, 0.8\],\
        \[1.2, 0.5\],\
        \[0.2, \-2.0\],\
        \[0.5, \-2.4\],\
        \[0.2, \-2.3\],\
        \[0.0, \-2.7\],\
        \[1.3, 2.1\],\
    \]
)

y \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1\])

\# Plotting settings
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(4, 3))
x\_min, x\_max, y\_min, y\_max \= \-3, 3, \-3, 3
ax.set(xlim\=(x\_min, x\_max), ylim\=(y\_min, y\_max))

\# Plot samples by color and add legend
scatter \= ax.scatter(X\[:, 0\], X\[:, 1\], s\=150, c\=y, label\=y, edgecolors\="k")
ax.legend(\*scatter.legend\_elements(), loc\="upper right", title\="Classes")
ax.set\_title("Samples in two-dimensional feature space")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Samples in two-dimensional feature space](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_kernels_001.png)

We can see that the samples are not clearly separable by a straight line.

Training SVC model and plotting decision boundaries[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#training-svc-model-and-plotting-decision-boundaries "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We define a function that fits a [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 classifier, allowing the `kernel` parameter as an input, and then plots the decision boundaries learned by the model using [`DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
.

Notice that for the sake of simplicity, the `C` parameter is set to its default value (`C=1`) in this example and the `gamma` parameter is set to `gamma=2` across all kernels, although it is automatically ignored for the linear kernel. In a real classification task, where performance matters, parameter tuning (by using [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 for instance) is highly recommended to capture different structures within the data.

Setting `response_method="predict"` in [`DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay")
 colors the areas based on their predicted class. Using `response_method="decision_function"` allows us to also plot the decision boundary and the margins to both sides of it. Finally the support vectors used during training (which always lay on the margins) are identified by means of the `support_vectors_` attribute of the trained SVCs, and plotted as well.

from sklearn import svm
from sklearn.inspection import DecisionBoundaryDisplay

def plot\_training\_data\_with\_decision\_boundary(
    kernel, ax\=None, long\_title\=True, support\_vectors\=True
):
    \# Train the SVC
    clf \= [svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(kernel\=kernel, gamma\=2).fit(X, y)

    \# Settings for plotting
    if ax is None:
        \_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(4, 3))
    x\_min, x\_max, y\_min, y\_max \= \-3, 3, \-3, 3
    ax.set(xlim\=(x\_min, x\_max), ylim\=(y\_min, y\_max))

    \# Plot decision boundary and margins
    common\_params \= {"estimator": clf, "X": X, "ax": ax}
    [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        \*\*common\_params,
        response\_method\="predict",
        plot\_method\="pcolormesh",
        alpha\=0.3,
    )
    [DecisionBoundaryDisplay.from\_estimator](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay.from_estimator "sklearn.inspection.DecisionBoundaryDisplay.from_estimator")
(
        \*\*common\_params,
        response\_method\="decision\_function",
        plot\_method\="contour",
        levels\=\[\-1, 0, 1\],
        colors\=\["k", "k", "k"\],
        linestyles\=\["--", "-", "--"\],
    )

    if support\_vectors:
        \# Plot bigger circles around samples that serve as support vectors
        ax.scatter(
            clf.support\_vectors\_\[:, 0\],
            clf.support\_vectors\_\[:, 1\],
            s\=150,
            facecolors\="none",
            edgecolors\="k",
        )

    \# Plot samples by color and add legend
    ax.scatter(X\[:, 0\], X\[:, 1\], c\=y, s\=30, edgecolors\="k")
    ax.legend(\*scatter.legend\_elements(), loc\="upper right", title\="Classes")
    if long\_title:
        ax.set\_title(f" Decision boundaries of {kernel} kernel in SVC")
    else:
        ax.set\_title(kernel)

    if ax is None:
        [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

### Linear kernel[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#linear-kernel "Link to this heading")

Linear kernel is the dot product of the input samples:

K(x1,x2)\=x1⊤x2

It is then applied to any combination of two data points (samples) in the dataset. The dot product of the two points determines the [`cosine_similarity`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html#sklearn.metrics.pairwise.cosine_similarity "sklearn.metrics.pairwise.cosine_similarity")
 between both points. The higher the value, the more similar the points are.

plot\_training\_data\_with\_decision\_boundary("linear")

Copy to clipboard

![Decision boundaries of linear kernel in SVC](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_kernels_002.png)

Training a [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 on a linear kernel results in an untransformed feature space, where the hyperplane and the margins are straight lines. Due to the lack of expressivity of the linear kernel, the trained classes do not perfectly capture the training data.

### Polynomial kernel[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#polynomial-kernel "Link to this heading")

The polynomial kernel changes the notion of similarity. The kernel function is defined as:

K(x1,x2)\=(γ⋅ x1⊤x2+r)d

where d is the degree (`degree`) of the polynomial, γ (`gamma`) controls the influence of each individual training sample on the decision boundary and r is the bias term (`coef0`) that shifts the data up or down. Here, we use the default value for the degree of the polynomial in the kernel function (`degree=3`). When `coef0=0` (the default), the data is only transformed, but no additional dimension is added. Using a polynomial kernel is equivalent to creating [`PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
 and then fitting a [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 with a linear kernel on the transformed data, although this alternative approach would be computationally expensive for most datasets.

plot\_training\_data\_with\_decision\_boundary("poly")

Copy to clipboard

![Decision boundaries of poly kernel in SVC](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_kernels_003.png)

The polynomial kernel with `gamma=2` adapts well to the training data, causing the margins on both sides of the hyperplane to bend accordingly.

### RBF kernel[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#rbf-kernel "Link to this heading")

The radial basis function (RBF) kernel, also known as the Gaussian kernel, is the default kernel for Support Vector Machines in scikit-learn. It measures similarity between two data points in infinite dimensions and then approaches classification by majority vote. The kernel function is defined as:

K(x1,x2)\=exp⁡(−γ⋅‖x1−x2‖2)

where γ (`gamma`) controls the influence of each individual training sample on the decision boundary.

The larger the euclidean distance between two points ‖x1−x2‖2 the closer the kernel function is to zero. This means that two points far away are more likely to be dissimilar.

plot\_training\_data\_with\_decision\_boundary("rbf")

Copy to clipboard

![Decision boundaries of rbf kernel in SVC](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_kernels_004.png)

In the plot we can see how the decision boundaries tend to contract around data points that are close to each other.

### Sigmoid kernel[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#sigmoid-kernel "Link to this heading")

The sigmoid kernel function is defined as:

K(x1,x2)\=tanh⁡(γ⋅x1⊤x2+r)

where the kernel coefficient γ (`gamma`) controls the influence of each individual training sample on the decision boundary and r is the bias term (`coef0`) that shifts the data up or down.

In the sigmoid kernel, the similarity between two data points is computed using the hyperbolic tangent function (tanh). The kernel function scales and possibly shifts the dot product of the two points (x1 and x2).

plot\_training\_data\_with\_decision\_boundary("sigmoid")

Copy to clipboard

![Decision boundaries of sigmoid kernel in SVC](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_kernels_005.png)

We can see that the decision boundaries obtained with the sigmoid kernel appear curved and irregular. The decision boundary tries to separate the classes by fitting a sigmoid-shaped curve, resulting in a complex boundary that may not generalize well to unseen data. From this example it becomes obvious, that the sigmoid kernel has very specific use cases, when dealing with data that exhibits a sigmoidal shape. In this example, careful fine tuning might find more generalizable decision boundaries. Because of its specificity, the sigmoid kernel is less commonly used in practice compared to other kernels.

Conclusion[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#conclusion "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

In this example, we have visualized the decision boundaries trained with the provided dataset. The plots serve as an intuitive demonstration of how different kernels utilize the training data to determine the classification boundaries.

The hyperplanes and margins, although computed indirectly, can be imagined as planes in the transformed feature space. However, in the plots, they are represented relative to the original feature space, resulting in curved decision boundaries for the polynomial, RBF, and sigmoid kernels.

Please note that the plots do not evaluate the individual kernel’s accuracy or quality. They are intended to provide a visual understanding of how the different kernels use the training data.

For a comprehensive evaluation, fine-tuning of [`SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
 parameters using techniques such as [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")
 is recommended to capture the underlying structures within the data.

XOR dataset[#](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_kernels.html#xor-dataset "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

A classical example of a dataset which is not linearly separable is the XOR pattern. HEre we demonstrate how different kernels work on such a dataset.

xx, yy \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3, 3, 500), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3, 3, 500))
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
X \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(300, 2)
y \= [np.logical\_xor](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#numpy.logical_xor "numpy.logical_xor")
(X\[:, 0\] \> 0, X\[:, 1\] \> 0)

\_, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, figsize\=(8, 8))
args \= dict(long\_title\=False, support\_vectors\=False)
plot\_training\_data\_with\_decision\_boundary("linear", ax\[0, 0\], \*\*args)
plot\_training\_data\_with\_decision\_boundary("poly", ax\[0, 1\], \*\*args)
plot\_training\_data\_with\_decision\_boundary("rbf", ax\[1, 0\], \*\*args)
plot\_training\_data\_with\_decision\_boundary("sigmoid", ax\[1, 1\], \*\*args)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![linear, poly, rbf, sigmoid](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_kernels_006.png)

As you can see from the plots above, only the `rbf` kernel can find a reasonable decision boundary for the above dataset.

**Total running time of the script:** (0 minutes 1.486 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_kernels.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_kernels.ipynb)

[`Download Jupyter notebook: plot_svm_kernels.ipynb`](https://scikit-learn.org/stable/_downloads/264f6891fa2130246a013d5f089e7b2e/plot_svm_kernels.ipynb)

[`Download Python source code: plot_svm_kernels.py`](https://scikit-learn.org/stable/_downloads/8975399471ae75debd0b26fbe3013719/plot_svm_kernels.py)

[`Download zipped: plot_svm_kernels.zip`](https://scikit-learn.org/stable/_downloads/d58abbe7bc4eabf74b338ceadfa1c679/plot_svm_kernels.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_thumb.png)

[RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

RBF SVM parameters

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_thumb.png)

[Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Plot different SVM classifiers in the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_margin_thumb.png)

[SVM Margins Example](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_margin.html)

SVM Margins Example

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_separating_hyperplane_unbalanced_thumb.png)

[SVM: Separating hyperplane for unbalanced classes](https://scikit-learn.org/stable/auto_examples/svm/plot_separating_hyperplane_unbalanced.html)

SVM: Separating hyperplane for unbalanced classes

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/8975399471ae75debd0b26fbe3013719/plot_svm_kernels.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/264f6891fa2130246a013d5f089e7b2e/plot_svm_kernels.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/d58abbe7bc4eabf74b338ceadfa1c679/plot_svm_kernels.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo31.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/svm/plot_svm_kernels.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo31.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/svm/plot_svm_kernels.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)