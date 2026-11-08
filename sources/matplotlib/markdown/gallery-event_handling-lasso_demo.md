[Skip to main content](https://matplotlib.org/stable/gallery/event_handling/lasso_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/event_handling/lasso_demo.html#sphx-glr-download-gallery-event-handling-lasso-demo-py)
 to download the full example code.

Lasso Demo[#](https://matplotlib.org/stable/gallery/event_handling/lasso_demo.html#lasso-demo "Link to this heading")

======================================================================================================================

Use a lasso to select a set of points and get the indices of the selected points. A callback is used to change the color of the selected points.

Note

This example exercises the interactive capabilities of Matplotlib, and this will not appear in the static documentation. Please run this code on your machine to see the interactivity.

You can copy and paste individual parts, or download the entire example using the link at the bottom of the page.

![Lasso points using left mouse button](https://matplotlib.org/stable/_images/sphx_glr_lasso_demo_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import colors as mcolors
from matplotlib import path
from matplotlib.collections import [RegularPolyCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.RegularPolyCollection "matplotlib.collections.RegularPolyCollection")
from matplotlib.widgets import [Lasso](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Lasso.html#matplotlib.widgets.Lasso "matplotlib.widgets.Lasso")

class LassoManager:
    def \_\_init\_\_(self, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, data):
        \# The information of whether a point has been selected or not is stored in the
        \# collection's array (0 = out, 1 = in), which then gets colormapped to blue
        \# (out) and red (in).
        self.collection \= [RegularPolyCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.RegularPolyCollection "matplotlib.collections.RegularPolyCollection")
(
            6, sizes\=(100,), offset\_transform\=[ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
,
            offsets\=data, array\=[np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(len(data)),
            clim\=(0, 1), cmap\=[mcolors.ListedColormap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(\["tab:blue", "tab:red"\]))
        [ax.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
(self.collection)
        canvas \= [ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
        canvas.mpl\_connect('button\_press\_event', self.on\_press)
        canvas.mpl\_connect('button\_release\_event', self.on\_release)

    def callback(self, verts):
        data \= self.collection.get\_offsets()
        self.collection.set\_array([path.Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
(verts).contains\_points(data))
        canvas \= self.collection.figure.canvas
        canvas.draw\_idle()
        del self.lasso

    def on\_press(self, event):
        canvas \= self.collection.figure.canvas
        if event.inaxes is not self.collection.axes or canvas.widgetlock.locked():
            return
        self.lasso \= [Lasso](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.Lasso.html#matplotlib.widgets.Lasso "matplotlib.widgets.Lasso")
(event.inaxes, (event.xdata, event.ydata), self.callback)
        canvas.widgetlock(self.lasso)  \# acquire a lock on the widget drawing

    def on\_release(self, event):
        canvas \= self.collection.figure.canvas
        if hasattr(self, 'lasso') and canvas.widgetlock.isowner(self.lasso):
            canvas.widgetlock.release(self.lasso)

if \_\_name\_\_ \== '\_\_main\_\_':
    [np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
().add\_subplot(
        xlim\=(0, 1), ylim\=(0, 1), title\='Lasso points using left mouse button')
    manager \= LassoManager([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(100, 2))
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: lasso_demo.ipynb`](https://matplotlib.org/stable/_downloads/ab5ee0e7c001671dd4e3ae15dafd6811/lasso_demo.ipynb)

[`Download Python source code: lasso_demo.py`](https://matplotlib.org/stable/_downloads/a6cb4df0e5baf29165f46c7de8319b87/lasso_demo.py)

[`Download zipped: lasso_demo.zip`](https://matplotlib.org/stable/_downloads/f36e6d90a01df609be2e247d99793355/lasso_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)