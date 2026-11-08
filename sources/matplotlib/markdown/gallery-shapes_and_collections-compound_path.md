[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/compound_path.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/compound_path.html#sphx-glr-download-gallery-shapes-and-collections-compound-path-py)
 to download the full example code.

Compound path[#](https://matplotlib.org/stable/gallery/shapes_and_collections/compound_path.html#compound-path "Link to this heading")

=======================================================================================================================================

Make a compound path -- in this case two simple polygons, a rectangle and a triangle. Use `CLOSEPOLY` and `MOVETO` for the different parts of the compound path

import matplotlib.pyplot as plt

from matplotlib.patches import [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
from matplotlib.path import [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

[vertices](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
[codes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]

[codes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[Path.MOVETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
\] + \[[Path.LINETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
\]\*3 + \[[Path.CLOSEPOLY](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
\]
[vertices](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)\]

[codes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 += \[[Path.MOVETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
\] + \[[Path.LINETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
\]\*2 + \[[Path.CLOSEPOLY](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
\]
[vertices](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 += \[(4, 4), (5, 5), (5, 4), (0, 0)\]

[path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
([vertices](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [codes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[pathpatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 \= [PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
([path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, facecolor\='none', edgecolor\='green')

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([pathpatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('A compound path')

[ax.autoscale\_view](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![A compound path](https://matplotlib.org/stable/_images/sphx_glr_compound_path_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.path`](https://matplotlib.org/stable/api/path_api.html#module-matplotlib.path "matplotlib.path")
    
*   [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
    
*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
    
*   [`matplotlib.axes.Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
    
*   [`matplotlib.axes.Axes.autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
    

[`Download Jupyter notebook: compound_path.ipynb`](https://matplotlib.org/stable/_downloads/59028c7eeed49045809591f183876c57/compound_path.ipynb)

[`Download Python source code: compound_path.py`](https://matplotlib.org/stable/_downloads/2093d89024338e445161580da8e68837/compound_path.py)

[`Download zipped: compound_path.zip`](https://matplotlib.org/stable/_downloads/46c88e91656f97ee893dd0249d97eeb5/compound_path.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)