[Skip to main content](https://matplotlib.org/stable/gallery/statistics/errorbars_and_boxes.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/errorbars_and_boxes.html#sphx-glr-download-gallery-statistics-errorbars-and-boxes-py)
 to download the full example code.

Create boxes from error bars using PatchCollection[#](https://matplotlib.org/stable/gallery/statistics/errorbars_and_boxes.html#create-boxes-from-error-bars-using-patchcollection "Link to this heading")

===========================================================================================================================================================================================================

In this example, we snazz up a pretty standard error bar plot by adding a rectangle patch defined by the limits of the bars in both the x- and y- directions. To do this, we have to write our own custom function called `make_error_boxes`. Close inspection of this function will reveal the preferred pattern in writing functions for matplotlib:

1.  an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
     object is passed directly to the function
    
2.  the function operates on the `Axes` methods directly, not through the `pyplot` interface
    
3.  plotting keyword arguments that could be abbreviated are spelled out for better code readability in the future (for example we use _facecolor_ instead of _fc_)
    
4.  the artists returned by the `Axes` plotting methods are then returned by the function so that, if desired, their styles can be modified later outside of the function (they are not modified in this example).
    

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import [PatchCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
from matplotlib.patches import [Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")

\# Number of data points
[n](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 5

\# Dummy data
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, [n](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 1)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([n](https://docs.python.org/3/library/functions.html#int "builtins.int")
) \* 5.

\# Dummy errors (above and below)
[xerr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(2, [n](https://docs.python.org/3/library/functions.html#int "builtins.int")
) + 0.1
[yerr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(2, [n](https://docs.python.org/3/library/functions.html#int "builtins.int")
) + 0.2

def make\_error\_boxes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, xdata, ydata, xerror, yerror, facecolor\='r',
                     edgecolor\='none', alpha\=0.5):

    \# Loop over data points; create box from errors at each point
    errorboxes \= \[[Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")\
(([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 \- xe\[0\], [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 \- ye\[0\]), xe.sum(), ye.sum())\
                  for [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, xe, ye in zip(xdata, ydata, xerror.T, yerror.T)\]

    \# Create patch collection with specified colour/alpha
    pc \= [PatchCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
(errorboxes, facecolor\=facecolor, alpha\=alpha,
                         edgecolor\=edgecolor)

    \# Add collection to Axes
    [ax.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
(pc)

    \# Plot errorbars
    artists \= [ax.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
(xdata, ydata, [xerr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=xerror, [yerr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=yerror,
                          fmt\='none', ecolor\='k')

    return artists

\# Create figure and Axes
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1)

\# Call function to create error boxes
[\_](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.ErrorbarContainer "matplotlib.container.ErrorbarContainer")
 \= make\_error\_boxes([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [xerr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yerr](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![errorbars and boxes](https://matplotlib.org/stable/_images/sphx_glr_errorbars_and_boxes_001_2_00x.png)

Tags: [plot-type: errorbar](https://matplotlib.org/stable/_tags/plot-type-errorbar.html)
 [component: rectangle](https://matplotlib.org/stable/_tags/component-rectangle.html)
 [component: patchcollection](https://matplotlib.org/stable/_tags/component-patchcollection.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
     / [`matplotlib.pyplot.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
    
*   [`matplotlib.axes.Axes.add_collection`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
    
*   [`matplotlib.collections.PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
    

[`Download Jupyter notebook: errorbars_and_boxes.ipynb`](https://matplotlib.org/stable/_downloads/2e73e580ebd152110e1775281f45c672/errorbars_and_boxes.ipynb)

[`Download Python source code: errorbars_and_boxes.py`](https://matplotlib.org/stable/_downloads/8a1e61de9e8945cfa899d5457afd5838/errorbars_and_boxes.py)

[`Download zipped: errorbars_and_boxes.zip`](https://matplotlib.org/stable/_downloads/dfc7e0260adb3edbdacc545c8ba86701/errorbars_and_boxes.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)