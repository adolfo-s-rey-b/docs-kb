[Skip to main content](https://matplotlib.org/stable/gallery/axisartist/simple_axisartist1.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axisartist/simple_axisartist1.html#sphx-glr-download-gallery-axisartist-simple-axisartist1-py)
 to download the full example code.

Custom spines with axisartist[#](https://matplotlib.org/stable/gallery/axisartist/simple_axisartist1.html#custom-spines-with-axisartist "Link to this heading")

================================================================================================================================================================

This example showcases the use of [`axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
 to draw spines at custom positions (here, at `y = 0`).

Note, however, that it is simpler to achieve this effect using standard [`Spine`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spine "matplotlib.spines.Spine")
 methods, as demonstrated in [Centered spines with arrows](https://matplotlib.org/stable/gallery/spines/centered_spines_with_arrows.html)
.

![simple axisartist1](https://matplotlib.org/stable/_images/sphx_glr_simple_axisartist1_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from mpl\_toolkits import axisartist

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6, 3), layout\="constrained")
\# To construct Axes of two different classes, we need to use gridspec (or
\# MATLAB-style add\_subplot calls).
[gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 \= [fig.add\_gridspec](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec")
(1, 2)

[ax0](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0, 0\], axes\_class\=[axisartist.Axes](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.Axes")
)
\# Make a new axis along the first (x) axis which passes through y=0.
[ax0.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["y=0"\] \= [ax0.new\_floating\_axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.new_floating_axis "mpl_toolkits.axisartist.Axes.new_floating_axis")
(nth\_coord\=0, value\=0,
                                        axis\_direction\="bottom")
[ax0.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["y=0"\].toggle(all\=True)
[ax0.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["y=0"\].label.set\_text("y = 0")
\# Make other axis invisible.
[ax0.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["bottom", "top", "right"\].set\_visible(False)

\# Alternatively, one can use AxesZero, which automatically sets up two
\# additional axis, named "xzero" (the y=0 axis) and "yzero" (the x=0 axis).
[ax1](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxesZero.html#mpl_toolkits.axisartist.axislines.AxesZero "mpl_toolkits.axisartist.AxesZero")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
([gs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
\[0, 1\], axes\_class\=[axisartist.axislines.AxesZero](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxesZero.html#mpl_toolkits.axisartist.axislines.AxesZero "mpl_toolkits.axisartist.AxesZero")
)
\# "xzero" and "yzero" default to invisible; make xzero axis visible.
[ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["xzero"\].set\_visible(True)
[ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["xzero"\].label.set\_text("Axis Zero")
\# Make other axis invisible.
[ax1.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\["bottom", "top", "right"\].set\_visible(False)

\# Draw some sample data.
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0.01)
[ax0.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: simple_axisartist1.ipynb`](https://matplotlib.org/stable/_downloads/bf155ae1a8c5bbb926d348ab69ba4e6f/simple_axisartist1.ipynb)

[`Download Python source code: simple_axisartist1.py`](https://matplotlib.org/stable/_downloads/172bea947b5b7014a1272376e04e4e51/simple_axisartist1.py)

[`Download zipped: simple_axisartist1.zip`](https://matplotlib.org/stable/_downloads/c1ddd25840151fd9bf4e63a5ae353a59/simple_axisartist1.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)