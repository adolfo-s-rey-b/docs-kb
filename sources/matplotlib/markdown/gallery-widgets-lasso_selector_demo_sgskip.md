[Skip to main content](https://matplotlib.org/stable/gallery/widgets/lasso_selector_demo_sgskip.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/lasso_selector_demo_sgskip.html#sphx-glr-download-gallery-widgets-lasso-selector-demo-sgskip-py)
 to download the full example code.

Lasso Selector[#](https://matplotlib.org/stable/gallery/widgets/lasso_selector_demo_sgskip.html#lasso-selector "Link to this heading")

=======================================================================================================================================

Interactively selecting data points with the lasso tool.

This examples plots a scatter plot. You can then select a few points by drawing a lasso loop around the points on the graph. To draw, just click on the graph, hold, and drag it around the points you need to select.

import numpy as np

from matplotlib.path import [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
from matplotlib.widgets import [LassoSelector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#matplotlib.widgets.LassoSelector "matplotlib.widgets.LassoSelector")

class SelectFromCollection:
    """
    Select indices from a matplotlib collection using \`LassoSelector\`.

    Selected indices are saved in the \`ind\` attribute. This tool fades out the
    points that are not part of the selection (i.e., reduces their alpha
    values). If your collection has alpha < 1, this tool will permanently
    alter the alpha values.

    Note that this tool selects collection objects based on their \*origins\*
    (i.e., \`offsets\`).

    Parameters
    ----------
    ax : \`~matplotlib.axes.Axes\`
        Axes to interact with.
    collection : \`matplotlib.collections.Collection\` subclass
        Collection you want to select from.
    alpha\_other : 0 <= float <= 1
        To highlight a selection, this tool sets all selected points to an
        alpha value of 1 and non-selected points to \*alpha\_other\*.
    """

    def \_\_init\_\_(self, ax, collection, alpha\_other\=0.3):
        self.canvas \= ax.figure.canvas
        self.collection \= collection
        self.alpha\_other \= alpha\_other

        self.xys \= collection.get\_offsets()
        self.Npts \= len(self.xys)

        \# Ensure that we have separate colors for each object
        self.fc \= collection.get\_facecolors()
        if len(self.fc) \== 0:
            raise ValueError('Collection must have a facecolor')
        elif len(self.fc) \== 1:
            self.fc \= [np.tile](https://numpy.org/doc/stable/reference/generated/numpy.tile.html#numpy.tile "numpy.tile")
(self.fc, (self.Npts, 1))

        self.lasso \= [LassoSelector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#matplotlib.widgets.LassoSelector "matplotlib.widgets.LassoSelector")
(ax, onselect\=self.onselect)
        self.ind \= \[\]

    def onselect(self, verts):
        path \= [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
(verts)
        self.ind \= [np.nonzero](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
(path.contains\_points(self.xys))\[0\]
        self.fc\[:, \-1\] \= self.alpha\_other
        self.fc\[self.ind, \-1\] \= 1
        self.collection.set\_facecolors(self.fc)
        self.canvas.draw\_idle()

    def disconnect(self):
        self.lasso.disconnect\_events()
        self.fc\[:, \-1\] \= 1
        self.collection.set\_facecolors(self.fc)
        self.canvas.draw\_idle()

if \_\_name\_\_ \== '\_\_main\_\_':
    import matplotlib.pyplot as plt

    \# Fixing random state for reproducibility
    [np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

    data \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(100, 2)

    subplot\_kw \= dict(xlim\=(0, 1), ylim\=(0, 1), autoscale\_on\=False)
    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\=subplot\_kw)

    pts \= ax.scatter(data\[:, 0\], data\[:, 1\], s\=80)
    selector \= SelectFromCollection(ax, pts)

    def accept(event):
        if event.key \== "enter":
            print("Selected points:")
            print(selector.xys\[selector.ind\])
            selector.disconnect()
            ax.set\_title("")
            fig.canvas.draw()

    fig.canvas.mpl\_connect("key\_press\_event", accept)
    ax.set\_title("Press enter to accept selected points.")

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.LassoSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.LassoSelector.html#matplotlib.widgets.LassoSelector "matplotlib.widgets.LassoSelector")
    
*   [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
    

[`Download Jupyter notebook: lasso_selector_demo_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/9a46d0a6b2f658dce2df81d8684cc977/lasso_selector_demo_sgskip.ipynb)

[`Download Python source code: lasso_selector_demo_sgskip.py`](https://matplotlib.org/stable/_downloads/cff0c57a9f43e62cbd6e2ee706caa49e/lasso_selector_demo_sgskip.py)

[`Download zipped: lasso_selector_demo_sgskip.zip`](https://matplotlib.org/stable/_downloads/d3f2169e8e6811dafe67a9615c95287e/lasso_selector_demo_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)