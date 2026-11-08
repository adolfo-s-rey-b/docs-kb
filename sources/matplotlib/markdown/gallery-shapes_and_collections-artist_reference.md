[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html#sphx-glr-download-gallery-shapes-and-collections-artist-reference-py)
 to download the full example code.

Reference for Matplotlib artists[#](https://matplotlib.org/stable/gallery/shapes_and_collections/artist_reference.html#reference-for-matplotlib-artists "Link to this heading")

================================================================================================================================================================================

This example displays several of Matplotlib's graphics primitives (artists). A full list of artists is documented at [the artist API](https://matplotlib.org/stable/api/artist_api.html#artist-api)
.

See also [Circles, Wedges and Polygons](https://matplotlib.org/stable/gallery/shapes_and_collections/patch_collection.html)
, which groups all artists into a single [`PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
 instead.

Copyright (c) 2010, Bartosz Telenczuk BSD License

import matplotlib.pyplot as plt

import matplotlib as mpl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import matplotlib.path as mpath

\# Prepare the data for the PathPatch below.
[Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [mpath.Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
[codes](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [verts](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= zip(\*\[\
    ([Path.MOVETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, \[0.018, \-0.11\]),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, \[\-0.031, \-0.051\]),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, \[\-0.115, 0.073\]),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, \[\-0.03, 0.073\]),\
    ([Path.LINETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, \[\-0.011, 0.039\]),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, \[0.043, 0.121\]),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, \[0.075, \-0.005\]),\
    ([Path.CURVE4](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, \[0.035, \-0.027\]),\
    ([Path.CLOSEPOLY](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, \[0.018, \-0.11\])\])

[artists](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    [mpatches.Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")\
((0, 0), 0.1, ec\="none"),\
    [mpatches.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")\
((\-0.025, \-0.05), 0.05, 0.1, ec\="none"),\
    [mpatches.Wedge](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")\
((0, 0), 0.1, 30, 270, ec\="none"),\
    [mpatches.RegularPolygon](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.RegularPolygon.html#matplotlib.patches.RegularPolygon "matplotlib.patches.RegularPolygon")\
((0, 0), 5, radius\=0.1),\
    [mpatches.Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")\
((0, 0), 0.2, 0.1),\
    [mpatches.Arrow](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arrow.html#matplotlib.patches.Arrow "matplotlib.patches.Arrow")\
(\-0.05, \-0.05, 0.1, 0.1, width\=0.1),\
    [mpatches.PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")\
([mpath.Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")\
([verts](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
, [codes](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")\
), ec\="none"),\
    [mpatches.FancyBboxPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")\
((\-0.025, \-0.05), 0.05, 0.1, ec\="none",\
                            boxstyle\=[mpatches.BoxStyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.BoxStyle.html#matplotlib.patches.BoxStyle "matplotlib.patches.BoxStyle")\
("Round", pad\=0.02)),\
    [mlines.Line2D](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")\
(\[\-0.06, 0.0, 0.1\], \[0.05, \-0.05, 0.05\], lw\=5),\
\]

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(6, 6), layout\="constrained").subplots(3, 3)
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, ([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
) in enumerate(zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [artists](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)):
    [artist.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set "matplotlib.lines.Line2D.set")
(color\=[mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["hsv"\]([i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 / len([artists](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)))
    [ax.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
)
    [ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(title\=type([artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
).\_\_name\_\_,
           aspect\=1, xlim\=(\-.2, .2), ylim\=(\-.2, .2))
    [ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Circle, Rectangle, Wedge, RegularPolygon, Ellipse, Arrow, PathPatch, FancyBboxPatch, Line2D](https://matplotlib.org/stable/_images/sphx_glr_artist_reference_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.path`](https://matplotlib.org/stable/api/path_api.html#module-matplotlib.path "matplotlib.path")
    
*   [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
    
*   [`matplotlib.lines`](https://matplotlib.org/stable/api/lines_api.html#module-matplotlib.lines "matplotlib.lines")
    
*   [`matplotlib.lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
    
*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.Circle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
    
*   [`matplotlib.patches.Ellipse`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
    
*   [`matplotlib.patches.Wedge`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
    
*   [`matplotlib.patches.Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
    
*   [`matplotlib.patches.Arrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arrow.html#matplotlib.patches.Arrow "matplotlib.patches.Arrow")
    
*   [`matplotlib.patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
    
*   [`matplotlib.patches.FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
    
*   [`matplotlib.patches.RegularPolygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.RegularPolygon.html#matplotlib.patches.RegularPolygon "matplotlib.patches.RegularPolygon")
    
*   [`matplotlib.axes.Axes.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
    

**Total running time of the script:** (0 minutes 1.017 seconds)

[`Download Jupyter notebook: artist_reference.ipynb`](https://matplotlib.org/stable/_downloads/8ecdfd594df7e4d6632cf5ae2d9a5764/artist_reference.ipynb)

[`Download Python source code: artist_reference.py`](https://matplotlib.org/stable/_downloads/57b7f4e80c39d1b607caeb4ddb875a88/artist_reference.py)

[`Download zipped: artist_reference.zip`](https://matplotlib.org/stable/_downloads/59674c06193260f18e0a5a2f13138206/artist_reference.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)