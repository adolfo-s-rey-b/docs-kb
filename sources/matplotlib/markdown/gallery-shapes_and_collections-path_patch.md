[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/path_patch.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/path_patch.html#sphx-glr-download-gallery-shapes-and-collections-path-patch-py)
 to download the full example code.

PathPatch object[#](https://matplotlib.org/stable/gallery/shapes_and_collections/path_patch.html#pathpatch-object "Link to this heading")

==========================================================================================================================================

This example shows how to create [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 and [`PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 objects through Matplotlib's API.

import matplotlib.pyplot as plt

import matplotlib.patches as mpatches
import matplotlib.path as mpath

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [mpath.Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
[path\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    ([Path.MOVETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (1.58, \-2.57)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (0.35, \-1.1)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (\-1.75, 2.0)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (0.375, 2.0)),\
    ([Path.LINETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (0.85, 1.15)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (2.2, 3.2)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (3, 0.05)),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (2.0, \-0.5)),\
    ([Path.CLOSEPOLY](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, (1.58, \-2.57)),\
    \]
[codes](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [verts](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= zip(\*[path\_data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [mpath.Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
([verts](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [codes](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
[patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 \= [mpatches.PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
([path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
, facecolor\='r', alpha\=0.5)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)

\# plot control points and connecting lines
[x](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [y](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= zip(\*[path.vertices](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.vertices "matplotlib.path.Path.vertices")
)
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [y](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, 'go-')

[ax.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
()
[ax.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
('equal')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![path patch](https://matplotlib.org/stable/_images/sphx_glr_path_patch_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.path`](https://matplotlib.org/stable/api/path_api.html#module-matplotlib.path "matplotlib.path")
    
*   [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
    
*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
    
*   [`matplotlib.axes.Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
    

[`Download Jupyter notebook: path_patch.ipynb`](https://matplotlib.org/stable/_downloads/2a1546a6e0f3ce3734cafdfa34700ca3/path_patch.ipynb)

[`Download Python source code: path_patch.py`](https://matplotlib.org/stable/_downloads/4a648ef9456f696258a19b26debbbdcc/path_patch.py)

[`Download zipped: path_patch.zip`](https://matplotlib.org/stable/_downloads/38b21672c33f5987e1dc3a1c7175031d/path_patch.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)