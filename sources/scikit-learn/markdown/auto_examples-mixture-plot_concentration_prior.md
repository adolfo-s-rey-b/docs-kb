[Skip to main content](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/mixture/plot_concentration_prior.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/mixture/plot_concentration_prior.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/mixture/plot_concentration_prior.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/mixture/plot_concentration_prior.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/mixture/plot_concentration_prior.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/mixture/plot_concentration_prior.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html#sphx-glr-download-auto-examples-mixture-plot-concentration-prior-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Concentration Prior Type Analysis of Variation Bayesian Gaussian Mixture[#](https://scikit-learn.org/stable/auto_examples/mixture/plot_concentration_prior.html#concentration-prior-type-analysis-of-variation-bayesian-gaussian-mixture "Link to this heading")

=================================================================================================================================================================================================================================================================

This example plots the ellipsoids obtained from a toy dataset (mixture of three Gaussians) fitted by the `BayesianGaussianMixture` class models with a Dirichlet distribution prior (`weight_concentration_prior_type='dirichlet_distribution'`) and a Dirichlet process prior (`weight_concentration_prior_type='dirichlet_process'`). On each figure, we plot the results for three different values of the weight concentration prior.

The `BayesianGaussianMixture` class can adapt its number of mixture components automatically. The parameter `weight_concentration_prior` has a direct link with the resulting number of components with non-zero weights. Specifying a low value for the concentration prior will make the model put most of the weight on few components set the remaining components weights very close to zero. High values of the concentration prior will allow a larger number of components to be active in the mixture.

The Dirichlet process prior allows to define an infinite number of components and automatically selects the correct number of components: it activates a component only if it is necessary.

On the contrary the classical finite mixture model with a Dirichlet distribution prior will favor more uniformly weighted components and therefore tends to divide natural clusters into unnecessary sub-components.

*   ![Finite mixture with a Dirichlet distribution prior and $\gamma_0=$$1.0e-03$, Finite mixture with a Dirichlet distribution prior and $\gamma_0=$$1.0e+00$, Finite mixture with a Dirichlet distribution prior and $\gamma_0=$$1.0e+03$](https://scikit-learn.org/stable/_images/sphx_glr_plot_concentration_prior_001.png)
*   ![Infinite mixture with a Dirichlet process prior and $\gamma_0=$$1.0e+00$, Infinite mixture with a Dirichlet process prior and $\gamma_0=$$1.0e+03$, Infinite mixture with a Dirichlet process prior and $\gamma_0=$$1.0e+05$](https://scikit-learn.org/stable/_images/sphx_glr_plot_concentration_prior_002.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib as mpl
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

from sklearn.mixture import [BayesianGaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")

def plot\_ellipses(ax, weights, means, covars):
    for n in range(means.shape\[0\]):
        eig\_vals, eig\_vecs \= [np.linalg.eigh](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html#numpy.linalg.eigh "numpy.linalg.eigh")
(covars\[n\])
        unit\_eig\_vec \= eig\_vecs\[0\] / [np.linalg.norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm "numpy.linalg.norm")
(eig\_vecs\[0\])
        angle \= [np.arctan2](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2 "numpy.arctan2")
(unit\_eig\_vec\[1\], unit\_eig\_vec\[0\])
        \# Ellipse needs degrees
        angle \= 180 \* angle / [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
        \# eigenvector normalization
        eig\_vals \= 2 \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(2) \* [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "numpy.sqrt")
(eig\_vals)
        ell \= [mpl.patches.Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
(
            means\[n\], eig\_vals\[0\], eig\_vals\[1\], angle\=180 + angle, edgecolor\="black"
        )
        ell.set\_clip\_box(ax.bbox)
        ell.set\_alpha(weights\[n\])
        ell.set\_facecolor("#56B4E9")
        ax.add\_artist(ell)

def plot\_results(ax1, ax2, estimator, X, y, title, plot\_title\=False):
    ax1.set\_title(title)
    ax1.scatter(X\[:, 0\], X\[:, 1\], s\=5, marker\="o", color\=colors\[y\], alpha\=0.8)
    ax1.set\_xlim(\-2.0, 2.0)
    ax1.set\_ylim(\-3.0, 3.0)
    ax1.set\_xticks(())
    ax1.set\_yticks(())
    plot\_ellipses(ax1, estimator.weights\_, estimator.means\_, estimator.covariances\_)

    ax2.get\_xaxis().set\_tick\_params(direction\="out")
    ax2.yaxis.grid(True, alpha\=0.7)
    for k, w in enumerate(estimator.weights\_):
        ax2.bar(
            k,
            w,
            width\=0.9,
            color\="#56B4E9",
            zorder\=3,
            align\="center",
            edgecolor\="black",
        )
        ax2.text(k, w + 0.007, "%.1f%%" % (w \* 100.0), horizontalalignment\="center")
    ax2.set\_xlim(\-0.6, 2 \* n\_components \- 0.4)
    ax2.set\_ylim(0.0, 1.1)
    ax2.tick\_params(axis\="y", which\="both", left\=False, right\=False, labelleft\=False)
    ax2.tick\_params(axis\="x", which\="both", top\=False)

    if plot\_title:
        ax1.set\_ylabel("Estimated Mixtures")
        ax2.set\_ylabel("Weight of each component")

\# Parameters of the dataset
random\_state, n\_components, n\_features \= 2, 3, 2
colors \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\["#0072B2", "#F0E442", "#D55E00"\])

covars \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(
    \[\[\[0.7, 0.0\], \[0.0, 0.1\]\], \[\[0.5, 0.0\], \[0.0, 0.1\]\], \[\[0.5, 0.0\], \[0.0, 0.1\]\]\]
)
samples \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[200, 500, 200\])
means \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[0.0, \-0.70\], \[0.0, 0.0\], \[0.0, 0.70\]\])

\# mean\_precision\_prior= 0.8 to minimize the influence of the prior
estimators \= \[\
    (\
        "Finite mixture with a Dirichlet distribution\\n" r"prior and $\\gamma\_0=$",\
        [BayesianGaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")\
(\
            weight\_concentration\_prior\_type\="dirichlet\_distribution",\
            n\_components\=2 \* n\_components,\
            reg\_covar\=0,\
            init\_params\="random",\
            max\_iter\=1500,\
            mean\_precision\_prior\=0.8,\
            random\_state\=random\_state,\
        ),\
        \[0.001, 1, 1000\],\
    ),\
    (\
        "Infinite mixture with a Dirichlet process\\n" r"prior and $\\gamma\_0=$",\
        [BayesianGaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture "sklearn.mixture.BayesianGaussianMixture")\
(\
            weight\_concentration\_prior\_type\="dirichlet\_process",\
            n\_components\=2 \* n\_components,\
            reg\_covar\=0,\
            init\_params\="random",\
            max\_iter\=1500,\
            mean\_precision\_prior\=0.8,\
            random\_state\=random\_state,\
        ),\
        \[1, 1000, 100000\],\
    ),\
\]

\# Generate data
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(random\_state)
X \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(
    \[\
        rng.multivariate\_normal(means\[j\], covars\[j\], samples\[j\])\
        for j in range(n\_components)\
    \]
)
y \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[[np.full](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")\
(samples\[j\], j, dtype\=int) for j in range(n\_components)\])

\# Plot results in two different figures
for title, estimator, concentrations\_prior in estimators:
    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(4.7 \* 3, 8))
    [plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(
        bottom\=0.04, top\=0.90, hspace\=0.05, wspace\=0.05, left\=0.03, right\=0.99
    )

    gs \= [gridspec.GridSpec](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
(3, len(concentrations\_prior))
    for k, concentration in enumerate(concentrations\_prior):
        estimator.weight\_concentration\_prior \= concentration
        estimator.fit(X)
        plot\_results(
            [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(gs\[0:2, k\]),
            [plt.subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")
(gs\[2, k\]),
            estimator,
            X,
            y,
            r"%s$%.1e$" % (title, concentration),
            plot\_title\=k \== 0,
        )

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 7.155 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo22.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/mixture/plot_concentration_prior.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo22.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/mixture/plot_concentration_prior.ipynb)

[`Download Jupyter notebook: plot_concentration_prior.ipynb`](https://scikit-learn.org/stable/_downloads/28df2114703b91f224d70205e9b75a7d/plot_concentration_prior.ipynb)

[`Download Python source code: plot_concentration_prior.py`](https://scikit-learn.org/stable/_downloads/ac9ba06dbb8ef65d14cff69663ec06f2/plot_concentration_prior.py)

[`Download zipped: plot_concentration_prior.zip`](https://scikit-learn.org/stable/_downloads/7c67ecf521b229ecc7e544b6321fb996/plot_concentration_prior.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_sin_thumb.png)

[Gaussian Mixture Model Sine Curve](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_sin.html)

Gaussian Mixture Model Sine Curve

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_thumb.png)

[Gaussian Mixture Model Ellipsoids](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm.html)

Gaussian Mixture Model Ellipsoids

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_pdf_thumb.png)

[Density Estimation for a Gaussian mixture](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_pdf.html)

Density Estimation for a Gaussian mixture

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gmm_selection_thumb.png)

[Gaussian Mixture Model Selection](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html)

Gaussian Mixture Model Selection

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/ac9ba06dbb8ef65d14cff69663ec06f2/plot_concentration_prior.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/28df2114703b91f224d70205e9b75a7d/plot_concentration_prior.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/7c67ecf521b229ecc7e544b6321fb996/plot_concentration_prior.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo22.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/mixture/plot_concentration_prior.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo22.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/mixture/plot_concentration_prior.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)