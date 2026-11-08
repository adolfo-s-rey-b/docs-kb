[Skip to main content](https://matplotlib.org/stable/gallery/scales/power_norm.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/scales/power_norm.html#sphx-glr-download-gallery-scales-power-norm-py)
 to download the full example code.

Exploring normalizations[#](https://matplotlib.org/stable/gallery/scales/power_norm.html#exploring-normalizations "Link to this heading")

==========================================================================================================================================

Various normalization on a multivariate normal distribution.

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import [multivariate\_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.multivariate_normal.html#numpy.random.multivariate_normal "numpy.random.multivariate_normal")

import matplotlib.colors as mcolors

\# Fixing random state for reproducibility.
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(\[\
    [multivariate\_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.multivariate_normal.html#numpy.random.multivariate_normal "numpy.random.multivariate_normal")\
(\[10, 10\], \[\[3, 2\], \[2, 3\]\], size\=100000),\
    [multivariate\_normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.multivariate_normal.html#numpy.random.multivariate_normal "numpy.random.multivariate_normal")\
(\[30, 20\], \[\[3, 1\], \[1, 3\]\], size\=1000)\
\])

[gammas](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0.8, 0.5, 0.3\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=2)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_title('Linear normalization')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].hist2d([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1\], bins\=100)

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [gamma](https://docs.python.org/3/library/functions.html#float "builtins.float")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
\[1:\], [gammas](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(r'Power law $(\\gamma=%1.1f)$' % [gamma](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
    [ax.hist2d](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\], [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1\], bins\=100, norm\=[mcolors.PowerNorm](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.PowerNorm.html#matplotlib.colors.PowerNorm "matplotlib.colors.PowerNorm")
([gamma](https://docs.python.org/3/library/functions.html#float "builtins.float")
))

[fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Linear normalization, Power law $(\gamma=0.8)$, Power law $(\gamma=0.5)$, Power law $(\gamma=0.3)$](https://matplotlib.org/stable/_images/sphx_glr_power_norm_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.colors`](https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors "matplotlib.colors")
    
*   [`matplotlib.colors.PowerNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.PowerNorm.html#matplotlib.colors.PowerNorm "matplotlib.colors.PowerNorm")
    
*   [`matplotlib.axes.Axes.hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d")
    
*   [`matplotlib.pyplot.hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist2d.html#matplotlib.pyplot.hist2d "matplotlib.pyplot.hist2d")
    

**Total running time of the script:** (0 minutes 1.097 seconds)

[`Download Jupyter notebook: power_norm.ipynb`](https://matplotlib.org/stable/_downloads/d09ee8cd933b613a4fe541229e46b25f/power_norm.ipynb)

[`Download Python source code: power_norm.py`](https://matplotlib.org/stable/_downloads/d375b8b6e7cb5e809d09e75e9ecd9b6c/power_norm.py)

[`Download zipped: power_norm.zip`](https://matplotlib.org/stable/_downloads/0c786667da3b5768fdf19bf051c57c98/power_norm.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)