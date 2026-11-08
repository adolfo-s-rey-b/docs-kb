[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_collection.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_collection.html#sphx-glr-download-gallery-shapes-and-collections-ellipse-collection-py)
 to download the full example code.

Ellipse Collection[#](https://matplotlib.org/stable/gallery/shapes_and_collections/ellipse_collection.html#ellipse-collection "Link to this heading")

======================================================================================================================================================

Drawing a collection of ellipses. While this would equally be possible using a [`EllipseCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection "matplotlib.collections.EllipseCollection")
 or [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
, the use of an [`EllipseCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection "matplotlib.collections.EllipseCollection")
 allows for much shorter code.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import [EllipseCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection "matplotlib.collections.EllipseCollection")

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(10)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(15)
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[XY](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.ravel(), [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.ravel()))

[ww](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / 10.0
[hh](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / 15.0
[aa](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 9

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ec](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection "matplotlib.collections.EllipseCollection")
 \= [EllipseCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection "matplotlib.collections.EllipseCollection")
([ww](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [hh](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [aa](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, units\='x', offsets\=[XY](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
                       offset\_transform\=[ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
)
[ec.set\_array](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection.set_array "matplotlib.collections.EllipseCollection.set_array")
(([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
).ravel())
[ax.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
([ec](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection "matplotlib.collections.EllipseCollection")
)
[ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('X')
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('y')
[cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [plt.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
([ec](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection "matplotlib.collections.EllipseCollection")
)
[cbar.set\_label](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.set_label "matplotlib.colorbar.Colorbar.set_label")
('X+Y')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![ellipse collection](https://matplotlib.org/stable/_images/sphx_glr_ellipse_collection_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.collections`](https://matplotlib.org/stable/api/collections_api.html#module-matplotlib.collections "matplotlib.collections")
    
*   [`matplotlib.collections.EllipseCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EllipseCollection "matplotlib.collections.EllipseCollection")
    
*   [`matplotlib.axes.Axes.add_collection`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
    
*   [`matplotlib.cm.ScalarMappable.set_array`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable.set_array "matplotlib.cm.ScalarMappable.set_array")
    

[`Download Jupyter notebook: ellipse_collection.ipynb`](https://matplotlib.org/stable/_downloads/7b0f509c752f8ccc41afab443f524854/ellipse_collection.ipynb)

[`Download Python source code: ellipse_collection.py`](https://matplotlib.org/stable/_downloads/bceb4b9f5e5ac5d82ae5766799c93e0e/ellipse_collection.py)

[`Download zipped: ellipse_collection.zip`](https://matplotlib.org/stable/_downloads/e8cf2f5973f6ecffa51835f1ff9028f8/ellipse_collection.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)