[Skip to main content](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html#sphx-glr-download-gallery-statistics-confidence-ellipse-py)
 to download the full example code.

Plot a confidence ellipse of a two-dimensional dataset[#](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html#plot-a-confidence-ellipse-of-a-two-dimensional-dataset "Link to this heading")

==================================================================================================================================================================================================================

This example shows how to plot a confidence ellipse of a two-dimensional dataset, using its pearson correlation coefficient.

The approach that is used to obtain the correct geometry is explained and proved here:

[https://carstenschelp.github.io/2018/09/14/Plot\_Confidence\_Ellipse\_001.html](https://carstenschelp.github.io/2018/09/14/Plot_Confidence_Ellipse_001.html)

The method avoids the use of an iterative eigen decomposition algorithm and makes use of the fact that a normalized covariance matrix (composed of pearson correlation coefficients and ones) is particularly easy to handle.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
import matplotlib.transforms as transforms

The plotting function itself[#](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html#the-plotting-function-itself "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

This function plots the confidence ellipse of the covariance of the given array-like variables x and y. The ellipse is plotted into the given Axes object _ax_.

The radiuses of the ellipse can be controlled by n\_std which is the number of standard deviations. The default value is 3 which makes the ellipse enclose 98.9% of the points if the data is normally distributed like in these examples (3 standard deviations in 1-D contain 99.7% of the data, which is 98.9% of the data in 2-D).

def confidence\_ellipse([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, n\_std\=3.0, facecolor\='none', \*\*kwargs):
    """
    Create a plot of the covariance confidence ellipse of \*x\* and \*y\*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The Axes object to draw the ellipse into.

    n\_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    \*\*kwargs
        Forwarded to \`~matplotlib.patches.Ellipse\`

    Returns
    -------
    matplotlib.patches.Ellipse
    """
    if [x.size](https://docs.python.org/3/library/functions.html#int "builtins.int")
 != [y.size](https://docs.python.org/3/library/functions.html#int "builtins.int")
:
        raise ValueError("x and y must be the same size")

    cov \= [np.cov](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov "numpy.cov")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    pearson \= cov\[0, 1\]/[np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(cov\[0, 0\] \* cov\[1, 1\])
    \# Using a special case to obtain the eigenvalues of this
    \# two-dimensional dataset.
    ell\_radius\_x \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(1 + pearson)
    ell\_radius\_y \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(1 \- pearson)
    ellipse \= [Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
((0, 0), width\=ell\_radius\_x \* 2, height\=ell\_radius\_y \* 2,
                      facecolor\=facecolor, \*\*kwargs)

    \# Calculating the standard deviation of x from
    \# the squareroot of the variance and multiplying
    \# with the given number of standard deviations.
    scale\_x \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(cov\[0, 0\]) \* n\_std
    mean\_x \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

    \# calculating the standard deviation of y ...
    scale\_y \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(cov\[1, 1\]) \* n\_std
    mean\_y \= [np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

    transf \= [transforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
() \\
        .rotate\_deg(45) \\
        .[scale](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
(scale\_x, scale\_y) \\
        .translate(mean\_x, mean\_y)

    ellipse.set\_transform(transf + [ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
)
    return [ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
(ellipse)

A helper function to create a correlated dataset[#](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html#a-helper-function-to-create-a-correlated-dataset "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Creates a random two-dimensional dataset with the specified two-dimensional mean (mu) and dimensions (scale). The correlation can be controlled by the param 'dependency', a 2x2 matrix.

def get\_correlated\_dataset(n, [dependency](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [scale](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
):
    latent \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(n, 2)
    dependent \= latent.dot([dependency](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
    scaled \= dependent \* [scale](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
    scaled\_with\_offset \= scaled + [mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
    \# return x and y of the new, correlated dataset
    return scaled\_with\_offset\[:, 0\], scaled\_with\_offset\[:, 1\]

Positive, negative and weak correlation[#](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html#positive-negative-and-weak-correlation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note that the shape for the weak correlation (right) is an ellipse, not a circle because x and y are differently scaled. However, the fact that x and y are uncorrelated is shown by the axes of the ellipse being aligned with the x- and y-axis of the coordinate system.

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

[PARAMETERS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'Positive correlation': \[\[0.85, 0.35\],\
                             \[0.15, \-0.65\]\],
    'Negative correlation': \[\[0.9, \-0.4\],\
                             \[0.1, \-0.6\]\],
    'Weak correlation': \[\[1, 0\],\
                         \[0, 1\]\],
}

[mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= 2, 4
[scale](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= 3, 5

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 3, figsize\=(9, 3))
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, ([title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [dependency](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
) in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [PARAMETERS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items()):
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= get\_correlated\_dataset(800, [dependency](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [scale](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
    [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, s\=0.5)

    [ax.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
(c\='grey', lw\=1)
    [ax.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
(c\='grey', lw\=1)

    confidence\_ellipse([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, edgecolor\='red')

    [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\], [mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\], c\='red', s\=3)
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
([title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Positive correlation, Negative correlation, Weak correlation](https://matplotlib.org/stable/_images/sphx_glr_confidence_ellipse_001_2_00x.png)

Different number of standard deviations[#](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html#different-number-of-standard-deviations "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A plot with n\_std = 3 (blue), 2 (purple) and 1 (red)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax\_nstd](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 6))

[dependency\_nstd](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[0.8, 0.75\],\
                   \[\-0.2, 0.35\]\]
[mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= 0, 0
[scale](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= 8, 5

[ax\_nstd.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
(c\='grey', lw\=1)
[ax\_nstd.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
(c\='grey', lw\=1)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= get\_correlated\_dataset(500, [dependency\_nstd](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [scale](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
[ax\_nstd.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, s\=0.5)

confidence\_ellipse([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ax\_nstd](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, n\_std\=1,
                   label\=r'$1\\sigma$', edgecolor\='firebrick')
confidence\_ellipse([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ax\_nstd](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, n\_std\=2,
                   label\=r'$2\\sigma$', edgecolor\='fuchsia', linestyle\='--')
confidence\_ellipse([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ax\_nstd](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, n\_std\=3,
                   label\=r'$3\\sigma$', edgecolor\='blue', linestyle\=':')

[ax\_nstd.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\], [mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\], c\='red', s\=3)
[ax\_nstd.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Different standard deviations')
[ax\_nstd.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Different standard deviations](https://matplotlib.org/stable/_images/sphx_glr_confidence_ellipse_002_2_00x.png)

Using the keyword arguments[#](https://matplotlib.org/stable/gallery/statistics/confidence_ellipse.html#using-the-keyword-arguments "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the keyword arguments specified for [`matplotlib.patches.Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 in order to have the ellipse rendered in different ways.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax\_kwargs](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 6))
[dependency\_kwargs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[\-0.8, 0.5\],\
                     \[\-0.2, 0.5\]\]
[mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= 2, \-3
[scale](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= 6, 5

[ax\_kwargs.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
(c\='grey', lw\=1)
[ax\_kwargs.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
(c\='grey', lw\=1)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= get\_correlated\_dataset(500, [dependency\_kwargs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [scale](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
\# Plot the ellipse with zorder=0 in order to demonstrate
\# its transparency (caused by the use of alpha).
confidence\_ellipse([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ax\_kwargs](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
,
                   alpha\=0.5, facecolor\='pink', edgecolor\='purple', zorder\=0)

[ax\_kwargs.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, s\=0.5)
[ax\_kwargs.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\], [mu](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\], c\='red', s\=3)
[ax\_kwargs.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Using keyword arguments')

[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(hspace\=0.25)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Using keyword arguments](https://matplotlib.org/stable/_images/sphx_glr_confidence_ellipse_003_2_00x.png)

Tags: [plot-type: specialty](https://matplotlib.org/stable/_tags/plot-type-specialty.html)
 [plot-type: scatter](https://matplotlib.org/stable/_tags/plot-type-scatter.html)
 [component: ellipse](https://matplotlib.org/stable/_tags/component-ellipse.html)
 [component: patch](https://matplotlib.org/stable/_tags/component-patch.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.transforms.Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
    
*   [`matplotlib.patches.Ellipse`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
    

**Total running time of the script:** (0 minutes 1.829 seconds)

[`Download Jupyter notebook: confidence_ellipse.ipynb`](https://matplotlib.org/stable/_downloads/3cce71e0693a21efebb16112b9101a2b/confidence_ellipse.ipynb)

[`Download Python source code: confidence_ellipse.py`](https://matplotlib.org/stable/_downloads/331a8f0ed4f8c08eecd40b9703eb70a5/confidence_ellipse.py)

[`Download zipped: confidence_ellipse.zip`](https://matplotlib.org/stable/_downloads/3c8344511495058237bf1858829ee31b/confidence_ellipse.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page