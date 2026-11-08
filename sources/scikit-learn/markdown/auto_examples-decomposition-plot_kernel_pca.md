[Skip to main content](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/decomposition/plot_kernel_pca.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/decomposition/plot_kernel_pca.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/decomposition/plot_kernel_pca.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/decomposition/plot_kernel_pca.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/decomposition/plot_kernel_pca.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/decomposition/plot_kernel_pca.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html#sphx-glr-download-auto-examples-decomposition-plot-kernel-pca-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Kernel PCA[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html#kernel-pca "Link to this heading")

==================================================================================================================================

This example shows the difference between the Principal Components Analysis ([`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
) and its kernelized version ([`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
).

On the one hand, we show that [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
 is able to find a projection of the data which linearly separates them while it is not the case with [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
.

Finally, we show that inverting this projection is an approximation with [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
, while it is exact with [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Projecting data: `PCA` vs. `KernelPCA`[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html#projecting-data-pca-vs-kernelpca "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this section, we show the advantages of using a kernel when projecting data using a Principal Component Analysis (PCA). We create a dataset made of two nested circles.

from sklearn.datasets import [make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y \= [make\_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
(n\_samples\=1\_000, factor\=0.3, noise\=0.05, random\_state\=0)
X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, y, stratify\=y, random\_state\=0)

Copy to clipboard

Let’s have a quick first look at the generated dataset.

import matplotlib.pyplot as plt

\_, (train\_ax, test\_ax) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, sharex\=True, sharey\=True, figsize\=(8, 4))

train\_ax.scatter(X\_train\[:, 0\], X\_train\[:, 1\], c\=y\_train)
train\_ax.set\_ylabel("Feature #1")
train\_ax.set\_xlabel("Feature #0")
train\_ax.set\_title("Training data")

test\_ax.scatter(X\_test\[:, 0\], X\_test\[:, 1\], c\=y\_test)
test\_ax.set\_xlabel("Feature #0")
\_ \= test\_ax.set\_title("Testing data")

Copy to clipboard

![Training data, Testing data](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_pca_001.png)

The samples from each class cannot be linearly separated: there is no straight line that can split the samples of the inner set from the outer set.

Now, we will use PCA with and without a kernel to see what is the effect of using such a kernel. The kernel used here is a radial basis function (RBF) kernel.

from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, [KernelPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")

pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=2)
kernel\_pca \= [KernelPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
(
    n\_components\=None, kernel\="rbf", gamma\=10, fit\_inverse\_transform\=True, alpha\=0.1
)

X\_test\_pca \= pca.fit(X\_train).transform(X\_test)
X\_test\_kernel\_pca \= kernel\_pca.fit(X\_train).transform(X\_test)

Copy to clipboard

fig, (orig\_data\_ax, pca\_proj\_ax, kernel\_pca\_proj\_ax) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    ncols\=3, figsize\=(14, 4)
)

orig\_data\_ax.scatter(X\_test\[:, 0\], X\_test\[:, 1\], c\=y\_test)
orig\_data\_ax.set\_ylabel("Feature #1")
orig\_data\_ax.set\_xlabel("Feature #0")
orig\_data\_ax.set\_title("Testing data")

pca\_proj\_ax.scatter(X\_test\_pca\[:, 0\], X\_test\_pca\[:, 1\], c\=y\_test)
pca\_proj\_ax.set\_ylabel("Principal component #1")
pca\_proj\_ax.set\_xlabel("Principal component #0")
pca\_proj\_ax.set\_title("Projection of testing data\\n using PCA")

kernel\_pca\_proj\_ax.scatter(X\_test\_kernel\_pca\[:, 0\], X\_test\_kernel\_pca\[:, 1\], c\=y\_test)
kernel\_pca\_proj\_ax.set\_ylabel("Principal component #1")
kernel\_pca\_proj\_ax.set\_xlabel("Principal component #0")
\_ \= kernel\_pca\_proj\_ax.set\_title("Projection of testing data\\n using KernelPCA")

Copy to clipboard

![Testing data, Projection of testing data  using PCA, Projection of testing data  using KernelPCA](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_pca_002.png)

We recall that PCA transforms the data linearly. Intuitively, it means that the coordinate system will be centered, rescaled on each component with respected to its variance and finally be rotated. The obtained data from this transformation is isotropic and can now be projected on its _principal components_.

Thus, looking at the projection made using PCA (i.e. the middle figure), we see that there is no change regarding the scaling; indeed the data being two concentric circles centered in zero, the original data is already isotropic. However, we can see that the data have been rotated. As a conclusion, we see that such a projection would not help if define a linear classifier to distinguish samples from both classes.

Using a kernel allows to make a non-linear projection. Here, by using an RBF kernel, we expect that the projection will unfold the dataset while keeping approximately preserving the relative distances of pairs of data points that are close to one another in the original space.

We observe such behaviour in the figure on the right: the samples of a given class are closer to each other than the samples from the opposite class, untangling both sample sets. Now, we can use a linear classifier to separate the samples from the two classes.

Projecting into the original feature space[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html#projecting-into-the-original-feature-space "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

One particularity to have in mind when using [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
 is related to the reconstruction (i.e. the back projection in the original feature space). With [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, the reconstruction will be exact if `n_components` is the same than the number of original features. This is the case in this example.

We can investigate if we get the original dataset when back projecting with [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
.

X\_reconstructed\_pca \= pca.inverse\_transform(pca.transform(X\_test))
X\_reconstructed\_kernel\_pca \= kernel\_pca.inverse\_transform(kernel\_pca.transform(X\_test))

Copy to clipboard

fig, (orig\_data\_ax, pca\_back\_proj\_ax, kernel\_pca\_back\_proj\_ax) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(
    ncols\=3, sharex\=True, sharey\=True, figsize\=(13, 4)
)

orig\_data\_ax.scatter(X\_test\[:, 0\], X\_test\[:, 1\], c\=y\_test)
orig\_data\_ax.set\_ylabel("Feature #1")
orig\_data\_ax.set\_xlabel("Feature #0")
orig\_data\_ax.set\_title("Original test data")

pca\_back\_proj\_ax.scatter(X\_reconstructed\_pca\[:, 0\], X\_reconstructed\_pca\[:, 1\], c\=y\_test)
pca\_back\_proj\_ax.set\_xlabel("Feature #0")
pca\_back\_proj\_ax.set\_title("Reconstruction via PCA")

kernel\_pca\_back\_proj\_ax.scatter(
    X\_reconstructed\_kernel\_pca\[:, 0\], X\_reconstructed\_kernel\_pca\[:, 1\], c\=y\_test
)
kernel\_pca\_back\_proj\_ax.set\_xlabel("Feature #0")
\_ \= kernel\_pca\_back\_proj\_ax.set\_title("Reconstruction via KernelPCA")

Copy to clipboard

![Original test data, Reconstruction via PCA, Reconstruction via KernelPCA](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_pca_003.png)

While we see a perfect reconstruction with [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
 we observe a different result for [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
.

Indeed, [`inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA.inverse_transform "sklearn.decomposition.KernelPCA.inverse_transform")
 cannot rely on an analytical back-projection and thus an exact reconstruction. Instead, a [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
 is internally trained to learn a mapping from the kernalized PCA basis to the original feature space. This method therefore comes with an approximation introducing small differences when back projecting in the original feature space.

To improve the reconstruction using [`inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA.inverse_transform "sklearn.decomposition.KernelPCA.inverse_transform")
, one can tune `alpha` in [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
, the regularization term which controls the reliance on the training data during the training of the mapping.

**Total running time of the script:** (0 minutes 0.551 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_kernel_pca.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_kernel_pca.ipynb)

[`Download Jupyter notebook: plot_kernel_pca.ipynb`](https://scikit-learn.org/stable/_downloads/c0a901203201090b01ac6d929a31ce08/plot_kernel_pca.ipynb)

[`Download Python source code: plot_kernel_pca.py`](https://scikit-learn.org/stable/_downloads/023324c27491610e7c0ccff87c59abf9/plot_kernel_pca.py)

[`Download zipped: plot_kernel_pca.zip`](https://scikit-learn.org/stable/_downloads/cc6cb3aee22cfec68cced9928e78b9af/plot_kernel_pca.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_thumb.png)

[Image denoising using kernel PCA](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html)

Image denoising using kernel PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)

[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)

Importance of Feature Scaling

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)

[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)

Principal Component Analysis (PCA) on Iris Dataset

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_thumb.png)

[Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)

Incremental PCA

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/023324c27491610e7c0ccff87c59abf9/plot_kernel_pca.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c0a901203201090b01ac6d929a31ce08/plot_kernel_pca.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/cc6cb3aee22cfec68cced9928e78b9af/plot_kernel_pca.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_kernel_pca.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_kernel_pca.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)