[Skip to main content](https://matplotlib.org/stable/gallery/spines/centered_spines_with_arrows.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/spines/centered_spines_with_arrows.html#sphx-glr-download-gallery-spines-centered-spines-with-arrows-py)
 to download the full example code.

Centered spines with arrows[#](https://matplotlib.org/stable/gallery/spines/centered_spines_with_arrows.html#centered-spines-with-arrows "Link to this heading")

=================================================================================================================================================================

This example shows a way to draw a "math textbook" style plot, where the spines ("axes lines") are drawn at `x = 0` and `y = 0`, and have arrows at their ends.

![centered spines with arrows](https://matplotlib.org/stable/_images/sphx_glr_centered_spines_with_arrows_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
\# Move the left and bottom spines to x = 0 and y = 0, respectively.
[ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\["left", "bottom"\]\].set\_position(("data", 0))
\# Hide the top and right spines.
[ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\["top", "right"\]\].set\_visible(False)

\# Draw arrows (as black triangles: ">k"/"^k") at the end of the axes.  In each
\# case, one of the coordinates (0) is a data coordinate (i.e., y = 0 or x = 0,
\# respectively) and the other one (1) is an axes coordinate (i.e., at the very
\# right/top of the axes).  Also, disable clipping (clip\_on=False) as the marker
\# actually spills out of the Axes.
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(1, 0, ">k", transform\=[ax.get\_yaxis\_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_transform.html#matplotlib.axes.Axes.get_yaxis_transform "matplotlib.axes.Axes.get_yaxis_transform")
(), clip\_on\=False)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(0, 1, "^k", transform\=[ax.get\_xaxis\_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_transform.html#matplotlib.axes.Axes.get_xaxis_transform "matplotlib.axes.Axes.get_xaxis_transform")
(), clip\_on\=False)

\# Some sample data.
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-0.5, 1., 100)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: centered_spines_with_arrows.ipynb`](https://matplotlib.org/stable/_downloads/c26e6f3ef388d7cfadf6a4c5570c9d3c/centered_spines_with_arrows.ipynb)

[`Download Python source code: centered_spines_with_arrows.py`](https://matplotlib.org/stable/_downloads/764239b321df1f4dab55a8a16c76daeb/centered_spines_with_arrows.py)

[`Download zipped: centered_spines_with_arrows.zip`](https://matplotlib.org/stable/_downloads/df0bf773aeab6581524ee4f92de0e84f/centered_spines_with_arrows.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)