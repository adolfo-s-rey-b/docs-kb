[Skip to main content](https://scikit-learn.org/stable/auto_examples/applications/plot_tomography_l1_reconstruction.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/applications/plot_tomography_l1_reconstruction.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/applications/plot_tomography_l1_reconstruction.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/applications/plot_tomography_l1_reconstruction.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/applications/plot_tomography_l1_reconstruction.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/applications/plot_tomography_l1_reconstruction.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/applications/plot_tomography_l1_reconstruction.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/applications/plot_tomography_l1_reconstruction.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/applications/plot_tomography_l1_reconstruction.html#sphx-glr-download-auto-examples-applications-plot-tomography-l1-reconstruction-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Compressive sensing: tomography reconstruction with L1 prior (Lasso)[#](https://scikit-learn.org/stable/auto_examples/applications/plot_tomography_l1_reconstruction.html#compressive-sensing-tomography-reconstruction-with-l1-prior-lasso "Link to this heading")

====================================================================================================================================================================================================================================================================

This example shows the reconstruction of an image from a set of parallel projections, acquired along different angles. Such a dataset is acquired in **computed tomography** (CT).

Without any prior information on the sample, the number of projections required to reconstruct the image is of the order of the linear size `l` of the image (in pixels). For simplicity we consider here a sparse image, where only pixels on the boundary of objects have a non-zero value. Such data could correspond for example to a cellular material. Note however that most images are sparse in a different basis, such as the Haar wavelets. Only `l/7` projections are acquired, therefore it is necessary to use prior information available on the sample (its sparsity): this is an example of **compressive sensing**.

The tomography projection operation is a linear transformation. In addition to the data-fidelity term corresponding to a linear regression, we penalize the L1 norm of the image to account for its sparsity. The resulting optimization problem is called the [Lasso](https://scikit-learn.org/stable/modules/linear_model.html#lasso)
. We use the class [`Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
, that uses the coordinate descent algorithm. Importantly, this implementation is more computationally efficient on a sparse matrix, than the projection operator used here.

The reconstruction with L1 penalization gives a result with zero error (all pixels are successfully labeled with 0 or 1), even if noise was added to the projections. In comparison, an L2 penalization ([`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
) produces a large number of labeling errors for the pixels. Important artifacts are observed on the reconstructed image, contrary to the L1 penalization. Note in particular the circular artifact separating the pixels in the corners, that have contributed to fewer projections than the central disk.

![original image, L2 penalization, L1 penalization](https://scikit-learn.org/stable/_images/sphx_glr_plot_tomography_l1_reconstruction_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage, sparse

from sklearn.linear\_model import [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
, [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")

def \_weights(x, dx\=1, orig\=0):
    x \= [np.ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")
(x)
    floor\_x \= [np.floor](https://numpy.org/doc/stable/reference/generated/numpy.floor.html#numpy.floor "numpy.floor")
((x \- orig) / dx).astype([np.int64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64 "numpy.int64")
)
    alpha \= (x \- orig \- floor\_x \* dx) / dx
    return [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
((floor\_x, floor\_x + 1)), [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
((1 \- alpha, alpha))

def \_generate\_center\_coordinates(l\_x):
    X, Y \= [np.mgrid](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
\[:l\_x, :l\_x\].astype([np.float64](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
    center \= l\_x / 2.0
    X += 0.5 \- center
    Y += 0.5 \- center
    return X, Y

def build\_projection\_operator(l\_x, n\_dir):
    """Compute the tomography design matrix.

    Parameters
    ----------

    l\_x : int
        linear size of image array

    n\_dir : int
        number of angles at which projections are acquired.

    Returns
    -------
    p : sparse matrix of shape (n\_dir l\_x, l\_x\*\*2)
    """
    X, Y \= \_generate\_center\_coordinates(l\_x)
    angles \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
, n\_dir, endpoint\=False)
    data\_inds, weights, camera\_inds \= \[\], \[\], \[\]
    data\_unravel\_indices \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(l\_x\*\*2)
    data\_unravel\_indices \= [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
((data\_unravel\_indices, data\_unravel\_indices))
    for i, angle in enumerate(angles):
        Xrot \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(angle) \* X \- [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(angle) \* Y
        inds, w \= \_weights(Xrot, dx\=1, orig\=X.min())
        mask \= [np.logical\_and](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html#numpy.logical_and "numpy.logical_and")
(inds \>= 0, inds < l\_x)
        weights += list(w\[mask\])
        camera\_inds += list(inds\[mask\] + i \* l\_x)
        data\_inds += list(data\_unravel\_indices\[mask\])
    camera\_inds \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(camera\_inds, dtype\=[np.int32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
)  \# lasso needs int32 inds
    data\_inds \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(data\_inds, dtype\=[np.int32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int32 "numpy.int32")
)
    proj\_operator \= [sparse.coo\_array](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_array.html#scipy.sparse.coo_array "scipy.sparse.coo_array")
((weights, (camera\_inds, data\_inds)))
    return proj\_operator

def generate\_synthetic\_data():
    """Synthetic binary data"""
    rs \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
    n\_pts \= 36
    x, y \= [np.ogrid](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid")
\[0:l, 0:l\]
    mask\_outer \= (x \- l / 2.0) \*\* 2 + (y \- l / 2.0) \*\* 2 < (l / 2.0) \*\* 2
    mask \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
((l, l))
    points \= l \* rs.rand(2, n\_pts)
    mask\[(points\[0\]).astype(int), (points\[1\]).astype(int)\] \= 1
    mask \= [ndimage.gaussian\_filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html#scipy.ndimage.gaussian_filter "scipy.ndimage.gaussian_filter")
(mask, sigma\=l / n\_pts)
    res \= [np.logical\_and](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html#numpy.logical_and "numpy.logical_and")
(mask \> mask.mean(), mask\_outer)
    return [np.logical\_xor](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#numpy.logical_xor "numpy.logical_xor")
(res, [ndimage.binary\_erosion](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.binary_erosion.html#scipy.ndimage.binary_erosion "scipy.ndimage.binary_erosion")
(res))

\# Generate synthetic images, and projections
l \= 128
proj\_operator \= build\_projection\_operator(l, l // 7)
data \= generate\_synthetic\_data()
proj \= proj\_operator @ data.ravel()\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
proj += 0.15 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(\*proj.shape)

\# Reconstruction with L2 (Ridge) penalization
rgr\_ridge \= [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
(alpha\=0.2)
rgr\_ridge.fit(proj\_operator, proj.ravel())
rec\_l2 \= rgr\_ridge.coef\_.reshape(l, l)

\# Reconstruction with L1 (Lasso) penalization
\# the best value of alpha was determined using cross validation
\# with LassoCV
rgr\_lasso \= [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
(alpha\=0.001)
rgr\_lasso.fit(proj\_operator, proj.ravel())
rec\_l1 \= rgr\_lasso.coef\_.reshape(l, l)

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 3.3))
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(131)
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(data, cmap\=plt.cm.gray, interpolation\="nearest")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("off")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("original image")
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(132)
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(rec\_l2, cmap\=plt.cm.gray, interpolation\="nearest")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("L2 penalization")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("off")
[plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(133)
[plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
(rec\_l1, cmap\=plt.cm.gray, interpolation\="nearest")
[plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("L1 penalization")
[plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("off")

[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(hspace\=0.01, wspace\=0.01, top\=1, bottom\=0, left\=0, right\=1)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.969 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_tomography_l1_reconstruction.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_tomography_l1_reconstruction.ipynb)

[`Download Jupyter notebook: plot_tomography_l1_reconstruction.ipynb`](https://scikit-learn.org/stable/_downloads/3daf4e9ab9d86061e19a11d997a09779/plot_tomography_l1_reconstruction.ipynb)

[`Download Python source code: plot_tomography_l1_reconstruction.py`](https://scikit-learn.org/stable/_downloads/c0cf10731954dbd148230cf322eb6fd7/plot_tomography_l1_reconstruction.py)

[`Download zipped: plot_tomography_l1_reconstruction.zip`](https://scikit-learn.org/stable/_downloads/d15e2c63b604233bb04599c0a1a02c8f/plot_tomography_l1_reconstruction.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_coin_ward_segmentation_thumb.png)

[A demo of structured Ward hierarchical clustering on an image of coins](https://scikit-learn.org/stable/auto_examples/cluster/plot_coin_ward_segmentation.html)

A demo of structured Ward hierarchical clustering on an image of coins

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_segmentation_toy_thumb.png)

[Spectral clustering for image segmentation](https://scikit-learn.org/stable/auto_examples/cluster/plot_segmentation_toy.html)

Spectral clustering for image segmentation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_and_elasticnet_thumb.png)

[L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html)

L1-based models for Sparse Signals

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_lasso_dense_vs_sparse_data_thumb.png)

[Lasso on dense and sparse data](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_dense_vs_sparse_data.html)

Lasso on dense and sparse data

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/c0cf10731954dbd148230cf322eb6fd7/plot_tomography_l1_reconstruction.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/3daf4e9ab9d86061e19a11d997a09779/plot_tomography_l1_reconstruction.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/d15e2c63b604233bb04599c0a1a02c8f/plot_tomography_l1_reconstruction.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/applications/plot_tomography_l1_reconstruction.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/applications/plot_tomography_l1_reconstruction.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)