[Skip to main content](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/miscellaneous/plot_kernel_approximation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/miscellaneous/plot_kernel_approximation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/miscellaneous/plot_kernel_approximation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/miscellaneous/plot_kernel_approximation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/miscellaneous/plot_kernel_approximation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/miscellaneous/plot_kernel_approximation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html#sphx-glr-download-auto-examples-miscellaneous-plot-kernel-approximation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Explicit feature map approximation for RBF kernels[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html#explicit-feature-map-approximation-for-rbf-kernels "Link to this heading")

============================================================================================================================================================================================================================

An example illustrating the approximation of the feature map of an RBF kernel.

It shows how to use [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
 and [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
 to approximate the feature map of an RBF kernel for classification with an SVM on the digits dataset. Results using a linear SVM in the original space, a linear SVM using the approximate mappings and using a kernelized SVM are compared. Timings and accuracy for varying amounts of Monte Carlo samplings (in the case of [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
, which uses random Fourier features) and different sized subsets of the training set (for [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
) for the approximate mapping are shown.

Please note that the dataset here is not large enough to show the benefits of kernel approximation, as the exact SVM is still reasonably fast.

Sampling more dimensions clearly leads to better classification results, but comes at a greater cost. This means there is a tradeoff between runtime and accuracy, given by the parameter n\_components. Note that solving the Linear SVM and also the approximate kernel SVM could be greatly accelerated by using stochastic gradient descent via [`SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
. This is not easily possible for the case of the kernelized SVM.

Python package and dataset imports, load dataset[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html#python-package-and-dataset-imports-load-dataset "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

\# Standard scientific Python imports
from time import [time](https://docs.python.org/3/library/time.html#time.time "time.time")

import matplotlib.pyplot as plt
import numpy as np

\# Import datasets, classifiers and performance metrics
from sklearn import datasets, pipeline, svm
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
from sklearn.kernel\_approximation import [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
, [RBFSampler](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")

\# The digits dataset
digits \= [datasets.load\_digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits "sklearn.datasets.load_digits")
(n\_class\=9)

Copy to clipboard

Timing and accuracy plots[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html#timing-and-accuracy-plots "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To apply a classifier on this data, we need to flatten the image, to turn the data in a (samples, feature) matrix:

n\_samples \= len(digits.data)
data \= digits.data / 16.0
data \-= data.mean(axis\=0)

\# We learn the digits on the first half of the digits
data\_train, targets\_train \= (data\[: n\_samples // 2\], digits.target\[: n\_samples // 2\])

\# Now predict the value of the digit on the second half:
data\_test, targets\_test \= (data\[n\_samples // 2 :\], digits.target\[n\_samples // 2 :\])
\# data\_test = scaler.transform(data\_test)

\# Create a classifier: a support vector classifier
kernel\_svm \= [svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
(gamma\=0.2)
linear\_svm \= [svm.LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
(random\_state\=42)

\# create pipeline from kernel approximation
\# and linear svm
feature\_map\_fourier \= [RBFSampler](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
(gamma\=0.2, random\_state\=1)
feature\_map\_nystroem \= [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
(gamma\=0.2, random\_state\=1)
fourier\_approx\_svm \= [pipeline.Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("feature\_map", feature\_map\_fourier),\
        ("svm", [svm.LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")\
(random\_state\=42)),\
    \]
)

nystroem\_approx\_svm \= [pipeline.Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline")
(
    \[\
        ("feature\_map", feature\_map\_nystroem),\
        ("svm", [svm.LinearSVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")\
(random\_state\=42)),\
    \]
)

\# fit and predict using linear and kernel svm:

kernel\_svm\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
kernel\_svm.fit(data\_train, targets\_train)
kernel\_svm\_score \= kernel\_svm.score(data\_test, targets\_test)
kernel\_svm\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- kernel\_svm\_time

linear\_svm\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
linear\_svm.fit(data\_train, targets\_train)
linear\_svm\_score \= linear\_svm.score(data\_test, targets\_test)
linear\_svm\_time \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- linear\_svm\_time

sample\_sizes \= 30 \* [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1, 10)
fourier\_scores \= \[\]
nystroem\_scores \= \[\]
fourier\_times \= \[\]
nystroem\_times \= \[\]

for D in sample\_sizes:
    fourier\_approx\_svm.set\_params(feature\_map\_\_n\_components\=D)
    nystroem\_approx\_svm.set\_params(feature\_map\_\_n\_components\=D)
    start \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    nystroem\_approx\_svm.fit(data\_train, targets\_train)
    nystroem\_times.append([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start)

    start \= [time](https://docs.python.org/3/library/time.html#time.time "time.time")
()
    fourier\_approx\_svm.fit(data\_train, targets\_train)
    fourier\_times.append([time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- start)

    fourier\_score \= fourier\_approx\_svm.score(data\_test, targets\_test)
    nystroem\_score \= nystroem\_approx\_svm.score(data\_test, targets\_test)
    nystroem\_scores.append(nystroem\_score)
    fourier\_scores.append(fourier\_score)

\# plot the results:
[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(16, 4))
accuracy \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(121)
\# second y axis for timings
timescale \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(122)

accuracy.plot(sample\_sizes, nystroem\_scores, label\="Nystroem approx. kernel")
timescale.plot(sample\_sizes, nystroem\_times, "--", label\="Nystroem approx. kernel")

accuracy.plot(sample\_sizes, fourier\_scores, label\="Fourier approx. kernel")
timescale.plot(sample\_sizes, fourier\_times, "--", label\="Fourier approx. kernel")

\# horizontal lines for exact rbf and linear kernels:
accuracy.plot(
    \[sample\_sizes\[0\], sample\_sizes\[\-1\]\],
    \[linear\_svm\_score, linear\_svm\_score\],
    label\="linear svm",
)
timescale.plot(
    \[sample\_sizes\[0\], sample\_sizes\[\-1\]\],
    \[linear\_svm\_time, linear\_svm\_time\],
    "--",
    label\="linear svm",
)

accuracy.plot(
    \[sample\_sizes\[0\], sample\_sizes\[\-1\]\],
    \[kernel\_svm\_score, kernel\_svm\_score\],
    label\="rbf svm",
)
timescale.plot(
    \[sample\_sizes\[0\], sample\_sizes\[\-1\]\],
    \[kernel\_svm\_time, kernel\_svm\_time\],
    "--",
    label\="rbf svm",
)

\# vertical line for dataset dimensionality = 64
accuracy.plot(\[64, 64\], \[0.7, 1\], label\="n\_features")

\# legends and labels
accuracy.set\_title("Classification accuracy")
timescale.set\_title("Training times")
accuracy.set\_xlim(sample\_sizes\[0\], sample\_sizes\[\-1\])
accuracy.set\_xticks(())
accuracy.set\_ylim([np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
(fourier\_scores), 1)
timescale.set\_xlabel("Sampling steps = transformed feature dimension")
accuracy.set\_ylabel("Classification accuracy")
timescale.set\_ylabel("Training time in seconds")
accuracy.legend(loc\="best")
timescale.legend(loc\="best")
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![Classification accuracy, Training times](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_approximation_001.png)

Decision Surfaces of RBF Kernel SVM and Linear SVM[#](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_kernel_approximation.html#decision-surfaces-of-rbf-kernel-svm-and-linear-svm "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The second plot visualized the decision surfaces of the RBF kernel SVM and the linear SVM with approximate kernel maps. The plot shows decision surfaces of the classifiers projected onto the first two principal components of the data. This visualization should be taken with a grain of salt since it is just an interesting slice through the decision surface in 64 dimensions. In particular note that a datapoint (represented as a dot) does not necessarily be classified into the region it is lying in, since it will not lie on the plane that the first two principal components span. The usage of [`RBFSampler`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.RBFSampler.html#sklearn.kernel_approximation.RBFSampler "sklearn.kernel_approximation.RBFSampler")
 and [`Nystroem`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem "sklearn.kernel_approximation.Nystroem")
 is described in detail in [Kernel Approximation](https://scikit-learn.org/stable/modules/kernel_approximation.html#kernel-approximation)
.

\# visualize the decision surface, projected down to the first
\# two principal components of the dataset
pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=8, random\_state\=42).fit(data\_train)

X \= pca.transform(data\_train)

\# Generate grid along first two principal components
multiples \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-2, 2, 0.1)
\# steps along first component
first \= multiples\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\] \* pca.components\_\[0, :\]
\# steps along second component
second \= multiples\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\] \* pca.components\_\[1, :\]
\# combine
grid \= first\[[np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
, :, :\] + second\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
, :\]
flat\_grid \= grid.reshape(\-1, data.shape\[1\])

\# title for the plots
titles \= \[\
    "SVC with rbf kernel",\
    "SVC (linear kernel)\\n with Fourier rbf feature map\\nn\_components=100",\
    "SVC (linear kernel)\\n with Nystroem rbf feature map\\nn\_components=100",\
\]

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(18, 7.5))
plt.rcParams.update({"font.size": 14})
\# predict and plot
for i, clf in enumerate((kernel\_svm, nystroem\_approx\_svm, fourier\_approx\_svm)):
    \# Plot the decision boundary. For that, we will assign a color to each
    \# point in the mesh \[x\_min, x\_max\]x\[y\_min, y\_max\].
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 3, i + 1)
    Z \= clf.predict(flat\_grid)

    \# Put the result into a color plot
    Z \= Z.reshape(grid.shape\[:\-1\])
    levels \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(10)
    lv\_eps \= 0.01  \# Adjust a mapping from calculated contour levels to color.
    [plt.contourf](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
(
        multiples,
        multiples,
        Z,
        levels\=levels \- lv\_eps,
        cmap\=plt.cm.tab10,
        vmin\=0,
        vmax\=10,
        alpha\=0.7,
    )
    [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("off")

    \# Plot also the training points
    [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(
        X\[:, 0\],
        X\[:, 1\],
        c\=targets\_train,
        cmap\=plt.cm.tab10,
        edgecolors\=(0, 0, 0),
        vmin\=0,
        vmax\=10,
    )

    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(titles\[i\])
[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![SVC with rbf kernel, SVC (linear kernel)  with Fourier rbf feature map n_components=100, SVC (linear kernel)  with Nystroem rbf feature map n_components=100](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_approximation_002.png)

**Total running time of the script:** (0 minutes 1.690 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_kernel_approximation.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_kernel_approximation.ipynb)

[`Download Jupyter notebook: plot_kernel_approximation.ipynb`](https://scikit-learn.org/stable/_downloads/083d8568c199bebbc1a847fc6c917e9e/plot_kernel_approximation.ipynb)

[`Download Python source code: plot_kernel_approximation.py`](https://scikit-learn.org/stable/_downloads/e1de994d83a2eb57b73b2f69bb7ada4a/plot_kernel_approximation.py)

[`Download zipped: plot_kernel_approximation.zip`](https://scikit-learn.org/stable/_downloads/fc62e5184f789c3ec66281b9f35fe4cd/plot_kernel_approximation.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_iris_svc_thumb.png)

[Plot different SVM classifiers in the iris dataset](https://scikit-learn.org/stable/auto_examples/svm/plot_iris_svc.html)

Plot different SVM classifiers in the iris dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scalable_poly_kernels_thumb.png)

[Scalable learning with polynomial kernel approximation](https://scikit-learn.org/stable/auto_examples/kernel_approximation/plot_scalable_poly_kernels.html)

Scalable learning with polynomial kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_rbf_parameters_thumb.png)

[RBF SVM parameters](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html)

RBF SVM parameters

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_anova_thumb.png)

[SVM-Anova: SVM with univariate feature selection](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_anova.html)

SVM-Anova: SVM with univariate feature selection

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/e1de994d83a2eb57b73b2f69bb7ada4a/plot_kernel_approximation.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/083d8568c199bebbc1a847fc6c917e9e/plot_kernel_approximation.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/fc62e5184f789c3ec66281b9f35fe4cd/plot_kernel_approximation.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo21.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/miscellaneous/plot_kernel_approximation.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo21.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/miscellaneous/plot_kernel_approximation.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)