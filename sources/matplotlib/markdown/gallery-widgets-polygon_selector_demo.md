[Skip to main content](https://matplotlib.org/stable/gallery/widgets/polygon_selector_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/widgets/polygon_selector_demo.html#sphx-glr-download-gallery-widgets-polygon-selector-demo-py)
 to download the full example code.

Select indices from a collection using polygon selector[#](https://matplotlib.org/stable/gallery/widgets/polygon_selector_demo.html#select-indices-from-a-collection-using-polygon-selector "Link to this heading")

====================================================================================================================================================================================================================

Shows how one can select indices of a polygon interactively.

import numpy as np

from matplotlib.path import [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
from matplotlib.widgets import [PolygonSelector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")

class SelectFromCollection:
    """
    Select indices from a matplotlib collection using \`PolygonSelector\`.

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

    def \_\_init\_\_(self, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, collection, alpha\_other\=0.3):
        self.canvas \= [ax.figure.canvas](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure")
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

        self.poly \= [PolygonSelector](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, self.onselect, draw\_bounding\_box\=True)
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
        self.poly.disconnect\_events()
        self.fc\[:, \-1\] \= 1
        self.collection.set\_facecolors(self.fc)
        self.canvas.draw\_idle()

if \_\_name\_\_ \== '\_\_main\_\_':
    import matplotlib.pyplot as plt

    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
    [grid\_size](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 5
    [grid\_x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.tile](https://numpy.org/doc/stable/reference/generated/numpy.tile.html#numpy.tile "numpy.tile")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([grid\_size](https://docs.python.org/3/library/functions.html#int "builtins.int")
), [grid\_size](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [grid\_y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.repeat](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([grid\_size](https://docs.python.org/3/library/functions.html#int "builtins.int")
), [grid\_size](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [pts](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 \= [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([grid\_x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [grid\_y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

    selector \= SelectFromCollection([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [pts](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
)

    print("Select points in the figure by enclosing them within a polygon.")
    print("Press the 'esc' key to start a new polygon.")
    print("Try holding the 'shift' key to move all of the vertices.")
    print("Try holding the 'ctrl' key to move a single vertex.")

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

    selector.disconnect()

    \# After figure is closed print the coordinates of the selected points
    print('\\nSelected points:')
    print([selector.xys](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
\[[selector.ind](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\])

![polygon selector demo](https://matplotlib.org/stable/_images/sphx_glr_polygon_selector_demo_001_2_00x.png)

Select points in the figure by enclosing them within a polygon.
Press the 'esc' key to start a new polygon.
Try holding the 'shift' key to move all of the vertices.
Try holding the 'ctrl' key to move a single vertex.

Selected points:
\[\]

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.widgets.PolygonSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")
    
*   [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
    

[`Download Jupyter notebook: polygon_selector_demo.ipynb`](https://matplotlib.org/stable/_downloads/222a2781dd2ff81219e63a88162c5b95/polygon_selector_demo.ipynb)

[`Download Python source code: polygon_selector_demo.py`](https://matplotlib.org/stable/_downloads/e01448737f71ce88ac3f2177a351c1de/polygon_selector_demo.py)

[`Download zipped: polygon_selector_demo.zip`](https://matplotlib.org/stable/_downloads/06b5c5a0b86cd39d561c43c10a75ea81/polygon_selector_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)