[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_digits_denoising.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_digits_denoising.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_digits_denoising.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_digits_denoising.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_digits_denoising.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_digits_denoising.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html#sphx-glr-download-auto-examples-applications-plot-digits-denoising-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Image denoising using kernel PCA[#](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html#image-denoising-using-kernel-pca "Link to this heading")

===================================================================================================================================================================================

This example shows how to use [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
 to denoise images. In short, we take advantage of the approximation function learned during `fit` to reconstruct the original image.

We will compare the results with an exact reconstruction using [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
.

We will use USPS digits dataset to reproduce presented in Sect. 4 of [\[1\]](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html#id2)
.

References

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

Copy to clipboard

Load the dataset via OpenML[#](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html#load-the-dataset-via-openml "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The USPS digits datasets is available in OpenML. We use [`fetch_openml`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
 to get this dataset. In addition, we normalize the dataset such that all pixel values are in the range (0, 1).

import numpy as np

from sklearn.datasets import [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.preprocessing import [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")

X, y \= [fetch\_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html#sklearn.datasets.fetch_openml "sklearn.datasets.fetch_openml")
(data\_id\=41082, as\_frame\=False, return\_X\_y\=True)
X \= [MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler "sklearn.preprocessing.MinMaxScaler")
().fit\_transform(X)

Copy to clipboard

The idea will be to learn a PCA basis (with and without a kernel) on noisy images and then use these models to reconstruct and denoise these images.

Thus, we split our dataset into a training and testing set composed of 1,000 samples for the training and 100 samples for testing. These images are noise-free and we will use them to evaluate the efficiency of the denoising approaches. In addition, we create a copy of the original dataset and add a Gaussian noise.

The idea of this application, is to show that we can denoise corrupted images by learning a PCA basis on some uncorrupted images. We will use both a PCA and a kernel-based PCA to solve this problem.

X\_train, X\_test, y\_train, y\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(
    X, y, stratify\=y, random\_state\=0, train\_size\=1\_000, test\_size\=100
)

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
noise \= rng.normal(scale\=0.25, size\=X\_test.shape)
X\_test\_noisy \= X\_test + noise

noise \= rng.normal(scale\=0.25, size\=X\_train.shape)
X\_train\_noisy \= X\_train + noise

Copy to clipboard

In addition, we will create a helper function to qualitatively assess the image reconstruction by plotting the test images.

import matplotlib.pyplot as plt

def plot\_digits(X, title):
    """Small helper function to plot 100 digits."""
    fig, axs \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=10, ncols\=10, figsize\=(8, 8))
    for img, ax in zip(X, axs.ravel()):
        ax.imshow(img.reshape((16, 16)), cmap\="Greys")
        ax.axis("off")
    fig.suptitle(title, fontsize\=24)

Copy to clipboard

In addition, we will use the mean squared error (MSE) to quantitatively assess the image reconstruction.

Let’s first have a look to see the difference between noise-free and noisy images. We will check the test set in this regard.

plot\_digits(X\_test, "Uncorrupted test images")
plot\_digits(
    X\_test\_noisy, f"Noisy test images\\nMSE: {[np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
((X\_test \- X\_test\_noisy) \*\* 2):.2f}"
)

Copy to clipboard

*   ![Uncorrupted test images](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_001.png)
*   ![Noisy test images MSE: 0.06](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_002.png)

Learn the `PCA` basis[#](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html#learn-the-pca-basis "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

We can now learn our PCA basis using both a linear PCA and a kernel PCA that uses a radial basis function (RBF) kernel.

from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
, [KernelPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")

pca \= [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")
(n\_components\=32, random\_state\=42)
kernel\_pca \= [KernelPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")
(
    n\_components\=400,
    kernel\="rbf",
    gamma\=1e-3,
    fit\_inverse\_transform\=True,
    alpha\=5e-3,
    random\_state\=42,
)

pca.fit(X\_train\_noisy)
\_ \= kernel\_pca.fit(X\_train\_noisy)

Copy to clipboard

Reconstruct and denoise test images[#](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html#reconstruct-and-denoise-test-images "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now, we can transform and reconstruct the noisy test set. Since we used less components than the number of original features, we will get an approximation of the original set. Indeed, by dropping the components explaining variance in PCA the least, we hope to remove noise. Similar thinking happens in kernel PCA; however, we expect a better reconstruction because we use a non-linear kernel to learn the PCA basis and a kernel ridge to learn the mapping function.

X\_reconstructed\_kernel\_pca \= kernel\_pca.inverse\_transform(
    kernel\_pca.transform(X\_test\_noisy)
)
X\_reconstructed\_pca \= pca.inverse\_transform(pca.transform(X\_test\_noisy))

Copy to clipboard

plot\_digits(X\_test, "Uncorrupted test images")
plot\_digits(
    X\_reconstructed\_pca,
    f"PCA reconstruction\\nMSE: {[np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
((X\_test \- X\_reconstructed\_pca) \*\* 2):.2f}",
)
plot\_digits(
    X\_reconstructed\_kernel\_pca,
    (
        "Kernel PCA reconstruction\\n"
        f"MSE: {[np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
((X\_test \- X\_reconstructed\_kernel\_pca) \*\* 2):.2f}"
    ),
)

Copy to clipboard

*   ![Uncorrupted test images](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_003.png)
*   ![PCA reconstruction MSE: 0.01](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_004.png)
*   ![Kernel PCA reconstruction MSE: 0.03](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_005.png)

PCA has a lower MSE than kernel PCA. However, the qualitative analysis might not favor PCA instead of kernel PCA. We observe that kernel PCA is able to remove background noise and provide a smoother image.

However, it should be noted that the results of the denoising with kernel PCA will depend of the parameters `n_components`, `gamma`, and `alpha`.

**Total running time of the script:** (0 minutes 5.452 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_digits_denoising.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_digits_denoising.ipynb)

[`Download Jupyter notebook: plot_digits_denoising.ipynb`](https://scikit-learn.org/stable/_downloads/f499e804840a40d11222872e84726eef/plot_digits_denoising.ipynb)

[`Download Python source code: plot_digits_denoising.py`](https://scikit-learn.org/stable/_downloads/32173eb704d697c23dffbbf3fd74942a/plot_digits_denoising.py)

[`Download zipped: plot_digits_denoising.zip`](https://scikit-learn.org/stable/_downloads/76835ae504ba9a29a0e409a26f38aa8d/plot_digits_denoising.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_agglomeration_thumb.png)

[Feature agglomeration](https://scikit-learn.org/stable/auto_examples/cluster/plot_digits_agglomeration.html)

Feature agglomeration

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_pca_thumb.png)

[Kernel PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html)

Kernel PCA

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_classification_thumb.png)

[Recognizing hand-written digits](https://scikit-learn.org/stable/auto_examples/classification/plot_digits_classification.html)

Recognizing hand-written digits

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_dict_face_patches_thumb.png)

[Online learning of a dictionary of parts of faces](https://scikit-learn.org/stable/auto_examples/cluster/plot_dict_face_patches.html)

Online learning of a dictionary of parts of faces

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/32173eb704d697c23dffbbf3fd74942a/plot_digits_denoising.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/f499e804840a40d11222872e84726eef/plot_digits_denoising.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/76835ae504ba9a29a0e409a26f38aa8d/plot_digits_denoising.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_digits_denoising.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_digits_denoising.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)