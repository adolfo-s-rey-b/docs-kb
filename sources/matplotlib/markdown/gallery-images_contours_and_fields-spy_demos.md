[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/spy_demos.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/spy_demos.html#sphx-glr-download-gallery-images-contours-and-fields-spy-demos-py)
 to download the full example code.

Spy Demos[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/spy_demos.html#spy-demos "Link to this heading")

===============================================================================================================================

Plot the sparsity pattern of arrays.

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2)
[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\]
[ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\]
[ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\]
[ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\]

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(20, 20)
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[5, :\] \= 0.
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 12\] \= 0.

[ax1.spy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spy.html#matplotlib.axes.Axes.spy "matplotlib.axes.Axes.spy")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, markersize\=5)
[ax2.spy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spy.html#matplotlib.axes.Axes.spy "matplotlib.axes.Axes.spy")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, precision\=0.1, markersize\=5)

[ax3.spy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spy.html#matplotlib.axes.Axes.spy "matplotlib.axes.Axes.spy")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax4.spy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spy.html#matplotlib.axes.Axes.spy "matplotlib.axes.Axes.spy")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, precision\=0.1)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![spy demos](https://matplotlib.org/stable/_images/sphx_glr_spy_demos_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.spy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spy.html#matplotlib.axes.Axes.spy "matplotlib.axes.Axes.spy")
     / [`matplotlib.pyplot.spy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.spy.html#matplotlib.pyplot.spy "matplotlib.pyplot.spy")
    

[`Download Jupyter notebook: spy_demos.ipynb`](https://matplotlib.org/stable/_downloads/a652071adf79bbd1de5a86eb1e3be78c/spy_demos.ipynb)

[`Download Python source code: spy_demos.py`](https://matplotlib.org/stable/_downloads/4fe4be973e85752a53c9544548ec4f8b/spy_demos.py)

[`Download zipped: spy_demos.zip`](https://matplotlib.org/stable/_downloads/158a640c997679687d07ee542e255065/spy_demos.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)