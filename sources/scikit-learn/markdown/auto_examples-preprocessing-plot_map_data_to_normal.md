[Skip to main content](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/preprocessing/plot_map_data_to_normal.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/preprocessing/plot_map_data_to_normal.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/preprocessing/plot_map_data_to_normal.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/preprocessing/plot_map_data_to_normal.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/preprocessing/plot_map_data_to_normal.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/preprocessing/plot_map_data_to_normal.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html#sphx-glr-download-auto-examples-preprocessing-plot-map-data-to-normal-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Map data to a normal distribution[#](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_map_data_to_normal.html#map-data-to-a-normal-distribution "Link to this heading")

========================================================================================================================================================================================

This example demonstrates the use of the Box-Cox and Yeo-Johnson transforms through [`PowerTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
 to map data from various distributions to a normal distribution.

The power transform is useful as a transformation in modeling problems where homoscedasticity and normality are desired. Below are examples of Box-Cox and Yeo-Johnwon applied to six different probability distributions: Lognormal, Chi-squared, Weibull, Gaussian, Uniform, and Bimodal.

Note that the transformations successfully map the data to a normal distribution when applied to certain datasets, but are ineffective with others. This highlights the importance of visualizing the data before and after transformation.

Also note that even though Box-Cox seems to perform better than Yeo-Johnson for lognormal and chi-squared distributions, keep in mind that Box-Cox does not support inputs with negative values.

For comparison, we also add the output from [`QuantileTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
. It can force any arbitrary distribution into a gaussian, provided that there are enough training samples (thousands). Because it is a non-parametric method, it is harder to interpret than the parametric ones (Box-Cox and Yeo-Johnson).

On “small” datasets (less than a few hundred points), the quantile transformer is prone to overfitting. The use of the power transform is then recommended.

![Lognormal, Chi-squared, Weibull, After Box-Cox $\lambda$ = -0.0, After Box-Cox $\lambda$ = 0.27, After Box-Cox $\lambda$ = 12.59, After Yeo-Johnson $\lambda$ = -0.83, After Yeo-Johnson $\lambda$ = -0.12, After Yeo-Johnson $\lambda$ = 24.53, After Quantile transform, After Quantile transform, After Quantile transform, Gaussian, Uniform, Bimodal, After Box-Cox $\lambda$ = 0.54, After Box-Cox $\lambda$ = 0.63, After Box-Cox $\lambda$ = 1.69, After Yeo-Johnson $\lambda$ = 0.54, After Yeo-Johnson $\lambda$ = 0.42, After Yeo-Johnson $\lambda$ = 1.7, After Quantile transform, After Quantile transform, After Quantile transform](https://scikit-learn.org/stable/_images/sphx_glr_plot_map_data_to_normal_001.png)

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.model\_selection import [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
from sklearn.preprocessing import [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
, [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")

N\_SAMPLES \= 1000
FONT\_SIZE \= 6
BINS \= 30

rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(304)
bc \= [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
(method\="box-cox")
yj \= [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer "sklearn.preprocessing.PowerTransformer")
(method\="yeo-johnson")
\# n\_quantiles is set to the training set size rather than the default value
\# to avoid a warning being raised by this example
qt \= [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer "sklearn.preprocessing.QuantileTransformer")
(
    n\_quantiles\=500, output\_distribution\="normal", random\_state\=rng
)
size \= (N\_SAMPLES, 1)

\# lognormal distribution
X\_lognormal \= rng.lognormal(size\=size)

\# chi-squared distribution
df \= 3
X\_chisq \= rng.chisquare(df\=df, size\=size)

\# weibull distribution
a \= 50
X\_weibull \= rng.weibull(a\=a, size\=size)

\# gaussian distribution
loc \= 100
X\_gaussian \= rng.normal(loc\=loc, size\=size)

\# uniform distribution
X\_uniform \= rng.uniform(low\=0, high\=1, size\=size)

\# bimodal distribution
loc\_a, loc\_b \= 100, 105
X\_a, X\_b \= rng.normal(loc\=loc\_a, size\=size), rng.normal(loc\=loc\_b, size\=size)
X\_bimodal \= [np.concatenate](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
(\[X\_a, X\_b\], axis\=0)

\# create plots
distributions \= \[\
    ("Lognormal", X\_lognormal),\
    ("Chi-squared", X\_chisq),\
    ("Weibull", X\_weibull),\
    ("Gaussian", X\_gaussian),\
    ("Uniform", X\_uniform),\
    ("Bimodal", X\_bimodal),\
\]

colors \= \["#D81B60", "#0188FF", "#FFC107", "#B7A2FF", "#000000", "#2EC5AC"\]

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=8, ncols\=3, figsize\=plt.figaspect(2))
axes \= axes.flatten()
axes\_idxs \= \[\
    (0, 3, 6, 9),\
    (1, 4, 7, 10),\
    (2, 5, 8, 11),\
    (12, 15, 18, 21),\
    (13, 16, 19, 22),\
    (14, 17, 20, 23),\
\]
axes\_list \= \[(axes\[i\], axes\[j\], axes\[k\], axes\[l\]) for (i, j, k, l) in axes\_idxs\]

for distribution, color, axes in zip(distributions, colors, axes\_list):
    name, X \= distribution
    X\_train, X\_test \= [train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")
(X, test\_size\=0.5)

    \# perform power transforms and quantile transform
    X\_trans\_bc \= bc.fit(X\_train).transform(X\_test)
    lmbda\_bc \= round(bc.lambdas\_\[0\], 2)
    X\_trans\_yj \= yj.fit(X\_train).transform(X\_test)
    lmbda\_yj \= round(yj.lambdas\_\[0\], 2)
    X\_trans\_qt \= qt.fit(X\_train).transform(X\_test)

    ax\_original, ax\_bc, ax\_yj, ax\_qt \= axes

    ax\_original.hist(X\_train, color\=color, bins\=BINS)
    ax\_original.set\_title(name, fontsize\=FONT\_SIZE)
    ax\_original.tick\_params(axis\="both", which\="major", labelsize\=FONT\_SIZE)

    for ax, X\_trans, meth\_name, lmbda in zip(
        (ax\_bc, ax\_yj, ax\_qt),
        (X\_trans\_bc, X\_trans\_yj, X\_trans\_qt),
        ("Box-Cox", "Yeo-Johnson", "Quantile transform"),
        (lmbda\_bc, lmbda\_yj, None),
    ):
        ax.hist(X\_trans, color\=color, bins\=BINS)
        title \= "After {}".format(meth\_name)
        if lmbda is not None:
            title += "\\n$\\\\lambda$ = {}".format(lmbda)
        ax.set\_title(title, fontsize\=FONT\_SIZE)
        ax.tick\_params(axis\="both", which\="major", labelsize\=FONT\_SIZE)
        ax.set\_xlim(\[\-3.5, 3.5\])

[plt.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

**Total running time of the script:** (0 minutes 1.788 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_map_data_to_normal.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_map_data_to_normal.ipynb)

[`Download Jupyter notebook: plot_map_data_to_normal.ipynb`](https://scikit-learn.org/stable/_downloads/fc26dc0b9d906466315a49a860435409/plot_map_data_to_normal.ipynb)

[`Download Python source code: plot_map_data_to_normal.py`](https://scikit-learn.org/stable/_downloads/4a586e9878904f51e624d94c03b3beff/plot_map_data_to_normal.py)

[`Download zipped: plot_map_data_to_normal.zip`](https://scikit-learn.org/stable/_downloads/98db344b333b9fbda7598300288d1b1e/plot_map_data_to_normal.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_all_scaling_thumb.png)

[Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html)

Compare the effect of different scalers on data with outliers

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_early_stopping_thumb.png)

[Early stopping in Gradient Boosting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html)

Early stopping in Gradient Boosting

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_johnson_lindenstrauss_bound_thumb.png)

[The Johnson-Lindenstrauss bound for embedding with random projections](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_johnson_lindenstrauss_bound.html)

The Johnson-Lindenstrauss bound for embedding with random projections

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_svm_scale_c_thumb.png)

[Scaling the regularization parameter for SVCs](https://scikit-learn.org/stable/auto_examples/svm/plot_svm_scale_c.html)

Scaling the regularization parameter for SVCs

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

[Download source code](https://scikit-learn.org/stable/_downloads/4a586e9878904f51e624d94c03b3beff/plot_map_data_to_normal.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/fc26dc0b9d906466315a49a860435409/plot_map_data_to_normal.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/98db344b333b9fbda7598300288d1b1e/plot_map_data_to_normal.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/preprocessing/plot_map_data_to_normal.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo28.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/preprocessing/plot_map_data_to_normal.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)