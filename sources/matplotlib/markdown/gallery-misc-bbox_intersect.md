[Skip to main content](https://matplotlib.org/stable/gallery/misc/bbox_intersect.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/bbox_intersect.html#sphx-glr-download-gallery-misc-bbox-intersect-py)
 to download the full example code.

Identify whether artists intersect[#](https://matplotlib.org/stable/gallery/misc/bbox_intersect.html#sphx-glr-gallery-misc-bbox-intersect-py "Link to this heading")

=====================================================================================================================================================================

The lines intersecting the rectangle are colored in red, while the others are left as blue lines. This example showcases the [`intersects_bbox`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.intersects_bbox "matplotlib.path.Path.intersects_bbox")
 function.

![bbox intersect](https://matplotlib.org/stable/_images/sphx_glr_bbox_intersect_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.path import [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
from matplotlib.transforms import Bbox

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[left](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [bottom](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [width](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [height](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= (\-1, \-1, 2, 2)
[rect](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 \= [plt.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
(([left](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [bottom](https://docs.python.org/3/library/functions.html#int "builtins.int")
), [width](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [height](https://docs.python.org/3/library/functions.html#int "builtins.int")
,
                     facecolor\="black", alpha\=0.1)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([rect](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
)

[bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 \= [Bbox.from\_bounds](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.from_bounds "matplotlib.transforms.Bbox.from_bounds")
([left](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [bottom](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [width](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [height](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(12):
    [vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
((2, 2)) \- 0.5) \* 6.0
    [path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
([vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    if [path.intersects\_bbox](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.intersects_bbox "matplotlib.path.Path.intersects_bbox")
([bbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
):
        [color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'r'
    else:
        [color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'b'
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\], [vertices](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1\], [color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: bbox_intersect.ipynb`](https://matplotlib.org/stable/_downloads/ada9c35d50f9be5cfba081119adb6b54/bbox_intersect.ipynb)

[`Download Python source code: bbox_intersect.py`](https://matplotlib.org/stable/_downloads/832476b1f1a894c408ecb93acb7b935c/bbox_intersect.py)

[`Download zipped: bbox_intersect.zip`](https://matplotlib.org/stable/_downloads/39402f8a75c50067ea01a9779e486427/bbox_intersect.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)