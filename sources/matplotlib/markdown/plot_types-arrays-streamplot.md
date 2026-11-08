[Skip to main content](https://matplotlib.org/stable/plot_types/arrays/streamplot.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/plot_types/arrays/streamplot.html#sphx-glr-download-plot-types-arrays-streamplot-py)
 to download the full example code.

streamplot(X, Y, U, V)[#](https://matplotlib.org/stable/plot_types/arrays/streamplot.html#streamplot-x-y-u-v "Link to this heading")

=====================================================================================================================================

Draw streamlines of a vector flow.

See [`streamplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html#matplotlib.axes.Axes.streamplot "matplotlib.axes.Axes.streamplot")
.

![streamplot](https://matplotlib.org/stable/_images/sphx_glr_streamplot_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('\_mpl-gallery-nogrid')

\# make a stream function:
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3, 3, 256), [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-3, 3, 256))
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= (1 \- [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/2 + [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*5 + [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*3) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 \- [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)
\# make U and V out of the streamfunction:
[V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.diff](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "numpy.diff")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1:, :\], axis\=1)
[U](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \-[np.diff](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "numpy.diff")
([Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1:\], axis\=0)

\# plot:
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.streamplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html#matplotlib.axes.Axes.streamplot "matplotlib.axes.Axes.streamplot")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1:, 1:\], [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1:, 1:\], [U](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [V](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: streamplot.ipynb`](https://matplotlib.org/stable/_downloads/d5495da7bfff8a67e9727dec9dd93ded/streamplot.ipynb)

[`Download Python source code: streamplot.py`](https://matplotlib.org/stable/_downloads/a00878546a57593e801c23b20668d112/streamplot.py)

[`Download zipped: streamplot.zip`](https://matplotlib.org/stable/_downloads/35ebfac96679a1b3a26c0d0d2645d776/streamplot.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)