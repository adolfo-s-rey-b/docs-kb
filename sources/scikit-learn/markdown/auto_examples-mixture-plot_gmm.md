[Skip to main content](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/mixture/plot_gmm.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/mixture/plot_gmm.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/mixture/plot_gmm.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/mixture/plot_gmm.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/mixture/plot_gmm.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/mixture/plot_gmm.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm.html#sphx-glr-download-auto-examples-mixture-plot-gmm-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Gaussian Mixture Model Ellipsoids[#](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm.html#gaussian-mixture-model-ellipsoids "Link to this heading")

===================================================================================================================================================================

Plot the confidence ellipsoids of a mixture of two Gaussians obtained with Expectation Maximisation (`GaussianMixture` class) and Variational Inference (`BayesianGaussianMixture` class models with a Dirichlet process prior).

Both models have access to five components with which to fit the data. Note that the Expectation Maximisation model will necessarily use all five components while the Variational Inference model will effectively only use as many as are needed for a good fit. Here we can see that the Expectation Maximisation model splits some components arbitrarily, because it is trying to fit too many components, while the Dirichlet Process model adapts it number of state automatically.

This example doesn’t show it, as we’re in a low-dimensional space, but another advantage of the Dirichlet process model is that it can fit full covariance matrices effectively even when there are less examples per cluster than there are dimensions in the data, due to regularization properties of the inference algorithm.

![Gaussian Mixture, Bayesian Gaussian Mixture with a Dirichlet process prior](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_001.png)

/home/circleci/project/sklearn/mixture/\_base.py:293: ConvergenceWarning: Best performing initialization did not converge. Try different init parameters, or increase max\_iter, tol, or check for degenerate data.
  warnings.warn(

Copy to clipboard

  

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import itertools

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg

from sklearn import mixture

color\_iter \= [itertools.cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle "itertools.cycle")
(\["navy", "c", "cornflowerblue", "gold", "darkorange"\])

def plot\_results(X, Y\_, means, covariances, index, title):
    splot \= [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(2, 1, 1 + index)
    for i, (mean, covar, color) in enumerate(zip(means, covariances, color\_iter)):
        v, w \= [linalg.eigh](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eigh.html#scipy.linalg.eigh "scipy.linalg.eigh")
(covar)
        v \= 2.0 \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(2.0) \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(v)
        u \= w\[0\] / [linalg.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.norm.html#scipy.linalg.norm "scipy.linalg.norm")
(w\[0\])
        \# as the DP will not use every component it has access to
        \# unless it needs it, we shouldn't plot the redundant
        \# components.
        if not [np.any](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")
(Y\_ \== i):
            continue
        [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter")
(X\[Y\_ \== i, 0\], X\[Y\_ \== i, 1\], 0.8, color\=color)

        \# Plot an ellipse to show the Gaussian component
        angle \= [np.arctan](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy.arctan "numpy.arctan")
(u\[1\] / u\[0\])
        angle \= 180.0 \* angle / [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
  \# convert to degrees
        ell \= [mpl.patches.Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
(mean, v\[0\], v\[1\], angle\=180.0 + angle, color\=color)
        ell.set\_clip\_box(splot.bbox)
        ell.set\_alpha(0.5)
        splot.add\_artist(ell)

    [plt.xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim")
(\-9.0, 5.0)
    [plt.ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim")
(\-3.0, 6.0)
    [plt.xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
(())
    [plt.yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
(())
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
(title)

\# Number of samples per component
n\_samples \= 500

\# Generate random sample, two components
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)
C \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[0.0, \-0.1\], \[1.7, 0.4\]\])
X \= [np.r\_](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")
\[\
    [np.dot](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")\
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")\
(n\_samples, 2), C),\
    0.7 \* [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")\
(n\_samples, 2) + [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")\
(\[\-6, 3\]),\
\]

\# Fit a Gaussian mixture with EM using five components
gmm \= [mixture.GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture")
(n\_components\=5, covariance\_type\="full").fit(X)
plot\_results(X, gmm.predict(X), gmm.means\_, gmm.covariances\_, 0, "Gaussian Mixture")

\# Fit a Dirichlet process Gaussian mixture using five components
dpgmm \= [mixture.BayesianGaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")
(n\_components\=5, covariance\_type\="full").fit(X)
plot\_results(
    X,
    dpgmm.predict(X),
    dpgmm.means\_,
    dpgmm.covariances\_,
    1,
    "Bayesian Gaussian Mixture with a Dirichlet process prior",
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 0.219 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo22.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/mixture/plot_gmm.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo22.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/mixture/plot_gmm.ipynb)

[`Download Jupyter notebook: plot_gmm.ipynb`](https://scikit-learn.org/stable/_downloads/df17584e78fbab6ddca8edf79def6190/plot_gmm.ipynb)

[`Download Python source code: plot_gmm.py`](https://scikit-learn.org/stable/_downloads/ef0baa719e32d13119d996e7e1f4a7dd/plot_gmm.py)

[`Download zipped: plot_gmm.zip`](https://scikit-learn.org/stable/_downloads/4f4cd09070f9e2e8fba523ca3ba243f1/plot_gmm.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_sin_thumb.png)

[Gaussian Mixture Model Sine Curve](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_sin.html)

Gaussian Mixture Model Sine Curve

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_concentration_prior_thumb.png)

[Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html)

Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_covariances_thumb.png)

[GMM covariances](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_covariances.html)

GMM covariances

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_selection_thumb.png)

[Gaussian Mixture Model Selection](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html)

Gaussian Mixture Model Selection

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/ef0baa719e32d13119d996e7e1f4a7dd/plot_gmm.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/df17584e78fbab6ddca8edf79def6190/plot_gmm.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/4f4cd09070f9e2e8fba523ca3ba243f1/plot_gmm.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo22.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/mixture/plot_gmm.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo22.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/mixture/plot_gmm.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)