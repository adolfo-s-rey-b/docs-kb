[Skip to main content](https://scikit-learn.org/stable/auto_examples/decomposition/plot_sparse_coding.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/decomposition/plot_sparse_coding.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/decomposition/plot_sparse_coding.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/decomposition/plot_sparse_coding.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/decomposition/plot_sparse_coding.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/decomposition/plot_sparse_coding.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/decomposition/plot_sparse_coding.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/decomposition/plot_sparse_coding.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/decomposition/plot_sparse_coding.html#sphx-glr-download-auto-examples-decomposition-plot-sparse-coding-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Sparse coding with a precomputed dictionary[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_sparse_coding.html#sparse-coding-with-a-precomputed-dictionary "Link to this heading")

=======================================================================================================================================================================================================

Transform a signal as a sparse combination of Ricker wavelets. This example visually compares different sparse coding methods using the [`SparseCoder`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
 estimator. The Ricker (also known as Mexican hat or the second derivative of a Gaussian) is not a particularly good kernel to represent piecewise constant signals like this one. It can therefore be seen how much adding different widths of atoms matters and it therefore motivates learning the dictionary to best fit your type of signals.

The richer dictionary on the right is not larger in size, heavier subsampling is performed in order to stay on the same order of magnitude.

![Sparse coding against fixed width dictionary, Sparse coding against multiple widths dictionary](https://scikit-learn.org/stable/_images/sphx_glr_plot_sparse_coding_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.decomposition import [SparseCoder](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")

def ricker\_function(resolution, center, width):
    """Discrete sub-sampled Ricker (Mexican hat) wavelet"""
    x \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, resolution \- 1, resolution)
    x \= (
        (2 / ([np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(3 \* width) \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
\*\*0.25))
        \* (1 \- (x \- center) \*\* 2 / width\*\*2)
        \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "numpy.exp")
(\-((x \- center) \*\* 2) / (2 \* width\*\*2))
    )
    return x

def ricker\_matrix(width, resolution, n\_components):
    """Dictionary of Ricker (Mexican hat) wavelets"""
    centers \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, resolution \- 1, n\_components)
    D \= [np.empty](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")
((n\_components, resolution))
    for i, center in enumerate(centers):
        D\[i\] \= ricker\_function(resolution, center, width)
    D /= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
([np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(D\*\*2, axis\=1))\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
    return D

resolution \= 1024
subsampling \= 3  \# subsampling factor
width \= 100
n\_components \= resolution // subsampling

\# Compute a wavelet dictionary
D\_fixed \= ricker\_matrix(width\=width, resolution\=resolution, n\_components\=n\_components)
D\_multi \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[\
    tuple(\
        ricker\_matrix(width\=w, resolution\=resolution, n\_components\=n\_components // 5)\
        for w in (10, 50, 100, 500, 1000)\
    )\
\]

\# Generate a signal
y \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, resolution \- 1, resolution)
first\_quarter \= y < resolution / 4
y\[first\_quarter\] \= 3.0
y\[[np.logical\_not](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html#numpy.logical_not "numpy.logical_not")\
(first\_quarter)\] \= \-1.0

\# List the different sparse coding methods in the following format:
\# (title, transform\_algorithm, transform\_alpha,
\#  transform\_n\_nozero\_coefs, color)
estimators \= \[\
    ("OMP", "omp", None, 15, "navy"),\
    ("Lasso", "lasso\_lars", 2, None, "turquoise"),\
\]
lw \= 2

[plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(13, 6))
for subplot, (D, title) in enumerate(
    zip((D\_fixed, D\_multi), ("fixed width", "multiple widths"))
):
    [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(1, 2, subplot + 1)
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
("Sparse coding against %s dictionary" % title)
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(y, lw\=lw, linestyle\="--", label\="Original signal")
    \# Do a wavelet approximation
    for title, algo, alpha, n\_nonzero, color in estimators:
        coder \= [SparseCoder](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
(
            dictionary\=D,
            transform\_n\_nonzero\_coefs\=n\_nonzero,
            transform\_alpha\=alpha,
            transform\_algorithm\=algo,
        )
        x \= coder.transform(y.reshape(1, \-1))
        density \= len([np.flatnonzero](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero")
(x))
        x \= [np.ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")
([np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(x, D))
        squared\_error \= [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
((y \- x) \*\* 2)
        [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
            x,
            color\=color,
            lw\=lw,
            label\="%s: %s nonzero coefs,\\n%.2f error" % (title, density, squared\_error),
        )

    \# Soft thresholding debiasing
    coder \= [SparseCoder](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparseCoder.html#sklearn.decomposition.SparseCoder "sklearn.decomposition.SparseCoder")
(
        dictionary\=D, transform\_algorithm\="threshold", transform\_alpha\=20
    )
    x \= coder.transform(y.reshape(1, \-1))
    \_, idx \= (x != 0).nonzero()
    x\[0, idx\], \_, \_, \_ \= [np.linalg.lstsq](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")
(D\[idx, :\].T, y, rcond\=None)
    x \= [np.ravel](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")
([np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
(x, D))
    squared\_error \= [np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
((y \- x) \*\* 2)
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(
        x,
        color\="darkorange",
        lw\=lw,
        label\="Thresholding w/ debiasing:\\n%d nonzero coefs, %.2f error"
        % (len(idx), squared\_error),
    )
    [plt.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis")
("tight")
    [plt.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
(shadow\=False, loc\="best")
[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(0.04, 0.07, 0.97, 0.90, 0.09, 0.2)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.286 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_sparse_coding.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_sparse_coding.ipynb)

[`Download Jupyter notebook: plot_sparse_coding.ipynb`](https://scikit-learn.org/stable/_downloads/c763870a5d2681d445fc65fcf63bba31/plot_sparse_coding.ipynb)

[`Download Python source code: plot_sparse_coding.py`](https://scikit-learn.org/stable/_downloads/2a14e362a70d246e83fa6a89ca069cee/plot_sparse_coding.py)

[`Download zipped: plot_sparse_coding.zip`](https://scikit-learn.org/stable/_downloads/1548afe7d3147cdbff3b5cba88ffc124/plot_sparse_coding.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_omp_thumb.png)

[Orthogonal Matching Pursuit](https://scikit-learn.org/stable/auto_examples/linear_model/plot_omp.html)

Orthogonal Matching Pursuit

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_faces_decomposition_thumb.png)

[Faces dataset decompositions](https://scikit-learn.org/stable/auto_examples/decomposition/plot_faces_decomposition.html)

Faces dataset decompositions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_sgd_loss_functions_thumb.png)

[SGD: convex loss functions](https://scikit-learn.org/stable/auto_examples/linear_model/plot_sgd_loss_functions.html)

SGD: convex loss functions

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_image_denoising_thumb.png)

[Image denoising using dictionary learning](https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html)

Image denoising using dictionary learning

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/2a14e362a70d246e83fa6a89ca069cee/plot_sparse_coding.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/c763870a5d2681d445fc65fcf63bba31/plot_sparse_coding.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/1548afe7d3147cdbff3b5cba88ffc124/plot_sparse_coding.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo10.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_sparse_coding.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo10.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/decomposition/plot_sparse_coding.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)