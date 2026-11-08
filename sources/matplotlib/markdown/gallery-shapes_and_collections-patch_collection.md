[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/patch_collection.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/patch_collection.html#sphx-glr-download-gallery-shapes-and-collections-patch-collection-py)
 to download the full example code.

Circles, Wedges and Polygons[#](https://matplotlib.org/stable/gallery/shapes_and_collections/patch_collection.html#circles-wedges-and-polygons "Link to this heading")

=======================================================================================================================================================================

This example demonstrates how to use [`collections.PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
.

See also [Reference for Matplotlib artists](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html)
, which instead adds each artist separately to its own Axes.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import [PatchCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
from matplotlib.patches import [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
, [Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
, [Wedge](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[resolution](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 50  \# the number of vertices
[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 3
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.1\*[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[patches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
for [x1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [y1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [r](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 in zip([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
 \= [Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
(([x1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [y1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
), [r](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
    [patches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.1\*[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[theta1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 360.0\*[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[theta2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 360.0\*[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
for [x1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [y1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [r](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [t1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [t2](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 in zip([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [radii](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [theta1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [theta2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [wedge](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
 \= [Wedge](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
(([x1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [y1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
), [r](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [t1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [t2](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
    [patches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([wedge](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
)

\# Some limiting conditions on Wedge
[patches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 += \[\
    [Wedge](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")\
((.3, .7), .1, 0, 360),             \# Full circle\
    [Wedge](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")\
((.7, .8), .2, 0, 360, width\=0.05),  \# Full ring\
    [Wedge](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")\
((.8, .3), .2, 0, 45),              \# Full sector\
    [Wedge](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")\
((.8, .3), .2, 45, 90, width\=0.10),  \# Ring sector\
\]

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
):
    [polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
 \= [Polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
([np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 2), closed\=True)
    [patches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([polygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
)

[colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 100 \* [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(len([patches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))
[p](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
 \= [PatchCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
([patches](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, alpha\=0.4)
[p.set\_array](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection.set_array "matplotlib.collections.PatchCollection.set_array")
([colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
([p](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
)
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([p](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![patch collection](https://matplotlib.org/stable/_images/sphx_glr_patch_collection_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.Circle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
    
*   [`matplotlib.patches.Wedge`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
    
*   [`matplotlib.patches.Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon")
    
*   [`matplotlib.collections.PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
    
*   [`matplotlib.collections.Collection.set_array`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_array "matplotlib.collections.Collection.set_array")
    
*   [`matplotlib.axes.Axes.add_collection`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
    
*   [`matplotlib.figure.Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
    

[`Download Jupyter notebook: patch_collection.ipynb`](https://matplotlib.org/stable/_downloads/eecce69251db7f6fa0b2442cad0f9e9f/patch_collection.ipynb)

[`Download Python source code: patch_collection.py`](https://matplotlib.org/stable/_downloads/2f6e22c5f0dbcf5e7b461fcc905783c5/patch_collection.py)

[`Download zipped: patch_collection.zip`](https://matplotlib.org/stable/_downloads/2fb556060f52a38f89a875b19f91b536/patch_collection.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)