[Skip to main content](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/auto_examples/linear_model/plot_polynomial_interpolation.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html)
[1.8.0](https://scikit-learn.org/1.8/auto_examples/linear_model/plot_polynomial_interpolation.html)
[1.7.2](https://scikit-learn.org/1.7/auto_examples/linear_model/plot_polynomial_interpolation.html)
[1.6.1](https://scikit-learn.org/1.6/auto_examples/linear_model/plot_polynomial_interpolation.html)
[1.5.2](https://scikit-learn.org/1.5/auto_examples/linear_model/plot_polynomial_interpolation.html)
[1.4.2](https://scikit-learn.org/1.4/auto_examples/linear_model/plot_polynomial_interpolation.html)

Collapse Sidebar Expand Sidebar

Note

[Go to the end](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html#sphx-glr-download-auto-examples-linear-model-plot-polynomial-interpolation-py)
 to download the full example code or to run this example in your browser via JupyterLite or Binder.

Polynomial and Spline interpolation[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html#polynomial-and-spline-interpolation "Link to this heading")

=================================================================================================================================================================================================

This example demonstrates how to approximate a function with polynomials up to degree `degree` by using ridge regression. We show two different ways given `n_samples` of 1d points `x_i`:

*   [`PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
     generates all monomials up to `degree`. This gives us the so called Vandermonde matrix with `n_samples` rows and `degree + 1` columns:
    
    \[\[1, x\_0, x\_0 \*\* 2, x\_0 \*\* 3, ..., x\_0 \*\* degree\],\
     \[1, x\_1, x\_1 \*\* 2, x\_1 \*\* 3, ..., x\_1 \*\* degree\],\
     ...\]
    
    Copy to clipboard
    
    Intuitively, this matrix can be interpreted as a matrix of pseudo features (the points raised to some power). The matrix is akin to (but different from) the matrix induced by a polynomial kernel.
    
*   [`SplineTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
     generates B-spline basis functions. A basis function of a B-spline is a piece-wise polynomial function of degree `degree` that is non-zero only between `degree+1` consecutive knots. Given `n_knots` number of knots, this results in matrix of `n_samples` rows and `n_knots + degree - 1` columns:
    
    \[\[basis\_1(x\_0), basis\_2(x\_0), ...\],\
     \[basis\_1(x\_1), basis\_2(x\_1), ...\],\
     ...\]
    
    Copy to clipboard
    

This example shows that these two transformers are well suited to model non-linear effects with a linear model, using a pipeline to add non-linear features. Kernel methods extend this idea and can induce very high (even infinite) dimensional feature spaces.

\# Authors: The scikit-learn developers
\# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear\_model import [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
from sklearn.pipeline import [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
, [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")

Copy to clipboard

We start by defining a function that we intend to approximate and prepare plotting it.

def f(x):
    """Function to be approximated by polynomial interpolation."""
    return x \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(x)

\# whole range we want to plot
x\_plot \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 11, 100)

Copy to clipboard

To make it interesting, we only give a small subset of points to train on.

x\_train \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10, 100)
rng \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(0)
x\_train \= [np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html#numpy.sort "numpy.sort")
(rng.choice(x\_train, size\=20, replace\=False))
y\_train \= f(x\_train)

\# create 2D-array versions of these arrays to feed to transformers
X\_train \= x\_train\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]
X\_plot \= x\_plot\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]

Copy to clipboard

Now we are ready to create polynomial features and splines, fit on the training points and show how well they interpolate.

\# plot function
lw \= 2
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.set\_prop\_cycle(
    color\=\["black", "teal", "yellowgreen", "gold", "darkorange", "tomato"\]
)
ax.plot(x\_plot, f(x\_plot), linewidth\=lw, label\="ground truth")

\# plot training points
ax.scatter(x\_train, y\_train, label\="training points")

\# polynomial features
for degree in \[3, 4, 5\]:
    model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
(degree), [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
(alpha\=1e-3))
    model.fit(X\_train, y\_train)
    y\_plot \= model.predict(X\_plot)
    ax.plot(x\_plot, y\_plot, label\=f"degree {degree}")

\# B-spline with 4 + 3 - 1 = 6 basis functions
model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
([SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
(n\_knots\=4, degree\=3), [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
(alpha\=1e-3))
model.fit(X\_train, y\_train)

y\_plot \= model.predict(X\_plot)
ax.plot(x\_plot, y\_plot, label\="B-spline")
ax.legend(loc\="lower center")
ax.set\_ylim(\-20, 10)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot polynomial interpolation](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_001.png)

This shows nicely that higher degree polynomials can fit the data better. But at the same time, too high powers can show unwanted oscillatory behaviour and are particularly dangerous for extrapolation beyond the range of fitted data. This is an advantage of B-splines. They usually fit the data as well as polynomials and show very nice and smooth behaviour. They have also good options to control the extrapolation, which defaults to continue with a constant. Note that most often, you would rather increase the number of knots but keep `degree=3`.

In order to give more insights into the generated feature bases, we plot all columns of both transformers separately.

fig, axes \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(16, 5))
pft \= [PolynomialFeatures](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures")
(degree\=3).fit(X\_train)
axes\[0\].plot(x\_plot, pft.transform(X\_plot))
axes\[0\].legend(axes\[0\].lines, \[f"degree {n}" for n in range(4)\])
axes\[0\].set\_title("PolynomialFeatures")

splt \= [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
(n\_knots\=4, degree\=3).fit(X\_train)
axes\[1\].plot(x\_plot, splt.transform(X\_plot))
axes\[1\].legend(axes\[1\].lines, \[f"spline {n}" for n in range(6)\])
axes\[1\].set\_title("SplineTransformer")

\# plot knots of spline
knots \= splt.bsplines\_\[0\].t
axes\[1\].vlines(knots\[3:\-3\], ymin\=0, ymax\=0.8, linestyles\="dashed")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![PolynomialFeatures, SplineTransformer](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_002.png)

In the left plot, we recognize the lines corresponding to simple monomials from `x**0` to `x**3`. In the right figure, we see the six B-spline basis functions of `degree=3` and also the four knot positions that were chosen during `fit`. Note that there are `degree` number of additional knots each to the left and to the right of the fitted interval. These are there for technical reasons, so we refrain from showing them. Every basis function has local support and is continued as a constant beyond the fitted range. This extrapolating behaviour could be changed by the argument `extrapolation`.

Periodic Splines[#](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html#periodic-splines "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

In the previous example we saw the limitations of polynomials and splines for extrapolation beyond the range of the training observations. In some settings, e.g. with seasonal effects, we expect a periodic continuation of the underlying signal. Such effects can be modelled using periodic splines, which have equal function value and equal derivatives at the first and last knot. In the following case we show how periodic splines provide a better fit both within and outside of the range of training data given the additional information of periodicity. The splines period is the distance between the first and last knot, which we specify manually.

Periodic splines can also be useful for naturally periodic features (such as day of the year), as the smoothness at the boundary knots prevents a jump in the transformed values (e.g. from Dec 31st to Jan 1st). For such naturally periodic features or more generally features where the period is known, it is advised to explicitly pass this information to the `SplineTransformer` by setting the knots manually.

def g(x):
    """Function to be approximated by periodic spline interpolation."""
    return [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(x) \- 0.7 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(x \* 3)

y\_train \= g(x\_train)

\# Extend the test data into the future:
x\_plot\_ext \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-1, 21, 200)
X\_plot\_ext \= x\_plot\_ext\[:, [np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
\]

lw \= 2
fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
ax.set\_prop\_cycle(color\=\["black", "tomato", "teal"\])
ax.plot(x\_plot\_ext, g(x\_plot\_ext), linewidth\=lw, label\="ground truth")
ax.scatter(x\_train, y\_train, label\="training points")

for transformer, label in \[\
    ([SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")\
(degree\=3, n\_knots\=10), "spline"),\
    (\
        [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")\
(\
            degree\=3,\
            knots\=[np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")\
(0, 2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")\
, 10)\[:, None\],\
            extrapolation\="periodic",\
        ),\
        "periodic spline",\
    ),\
\]:
    model \= [make\_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
(transformer, [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
(alpha\=1e-3))
    model.fit(X\_train, y\_train)
    y\_plot\_ext \= model.predict(X\_plot\_ext)
    ax.plot(x\_plot\_ext, y\_plot\_ext, label\=label)

ax.legend()
fig.show()

Copy to clipboard

![plot polynomial interpolation](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_003.png)

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
knots \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2 \* [np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
, 4)
splt \= [SplineTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.SplineTransformer.html#sklearn.preprocessing.SplineTransformer "sklearn.preprocessing.SplineTransformer")
(knots\=knots\[:, None\], degree\=3, extrapolation\="periodic").fit(
    X\_train
)
ax.plot(x\_plot\_ext, splt.transform(X\_plot\_ext))
ax.legend(ax.lines, \[f"spline {n}" for n in range(3)\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Copy to clipboard

![plot polynomial interpolation](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_004.png)

**Total running time of the script:** (0 minutes 0.445 seconds)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_polynomial_interpolation.ipynb)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_polynomial_interpolation.ipynb)

[`Download Jupyter notebook: plot_polynomial_interpolation.ipynb`](https://scikit-learn.org/stable/_downloads/97af0ebf12a51edb939605ce096cae13/plot_polynomial_interpolation.ipynb)

[`Download Python source code: plot_polynomial_interpolation.py`](https://scikit-learn.org/stable/_downloads/421ef4f01c94bb40ae3ecc3a1dd0c886/plot_polynomial_interpolation.py)

[`Download zipped: plot_polynomial_interpolation.zip`](https://scikit-learn.org/stable/_downloads/e75dc2347a2a807d30226ce1a4a562ae/plot_polynomial_interpolation.zip)

Related examples

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_ard_thumb.png)

[Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html)

Comparing Linear Bayesian Regressors

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_voting_decision_regions_thumb.png)

[Visualizing the probabilistic predictions of a VotingClassifier](https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html)

Visualizing the probabilistic predictions of a VotingClassifier

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_cyclical_feature_engineering_thumb.png)

[Time-related feature engineering](https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html)

Time-related feature engineering

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_underfitting_overfitting_thumb.png)

[Underfitting vs. Overfitting](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html)

Underfitting vs. Overfitting

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page

[Download source code](https://scikit-learn.org/stable/_downloads/421ef4f01c94bb40ae3ecc3a1dd0c886/plot_polynomial_interpolation.py)

[Download Jupyter notebook](https://scikit-learn.org/stable/_downloads/97af0ebf12a51edb939605ce096cae13/plot_polynomial_interpolation.ipynb)

[Download zipped](https://scikit-learn.org/stable/_downloads/e75dc2347a2a807d30226ce1a4a562ae/plot_polynomial_interpolation.zip)

[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo19.svg)](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/linear_model/plot_polynomial_interpolation.ipynb)

[![Launch binder](https://scikit-learn.org/stable/_images/binder_badge_logo19.svg)](https://mybinder.org/v2/gh/scikit-learn/scikit-learn/1.9.X?urlpath=lab/tree/notebooks/auto_examples/linear_model/plot_polynomial_interpolation.ipynb)

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)