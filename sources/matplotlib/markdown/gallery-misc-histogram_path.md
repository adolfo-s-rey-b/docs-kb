[Skip to main content](https://matplotlib.org/stable/gallery/misc/histogram_path.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/histogram_path.html#sphx-glr-download-gallery-misc-histogram-path-py)
 to download the full example code.

Building histograms using Rectangles and PolyCollections[#](https://matplotlib.org/stable/gallery/misc/histogram_path.html#building-histograms-using-rectangles-and-polycollections "Link to this heading")

============================================================================================================================================================================================================

Using a path patch to draw rectangles.

The technique of using lots of [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 instances, or the faster method of using [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
, were implemented before we had proper paths with moveto, lineto, closepoly, etc. in Matplotlib. Now that we have them, we can draw collections of regularly shaped objects with homogeneous properties more efficiently with a PathCollection. This example makes a histogram -- it's more work to set up the vertex arrays at the outset, but it should be much faster for large numbers of objects.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.patches as patches
import matplotlib.path as path

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)  \# Fixing random state for reproducibility

\# histogram our data with numpy
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(1000)
[n](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.histogram](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 50)

\# get the corners of the rectangles for the histogram
[left](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:\-1\]
[right](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1:\]
[bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(len([left](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[top](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [n](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

\# we need a (numrects x numsides x 2) numpy array for the path helper
\# function to build a compound path
[XY](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[[left](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [left](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [right](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [right](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\], \[[bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [top](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [top](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\]\]).T

\# get the Path object
[barpath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [path.Path.make\_compound\_path\_from\_polys](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.make_compound_path_from_polys "matplotlib.path.Path.make_compound_path_from_polys")
([XY](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# make a patch out of it, don't add a margin at y=0
[patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 \= [patches.PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
([barpath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
)
[patch.sticky\_edges.y](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.sticky_edges.html#matplotlib.artist.Artist.sticky_edges "matplotlib.artist.Artist.sticky_edges")
\[:\] \= \[0\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)
[ax.autoscale\_view](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![histogram path](https://matplotlib.org/stable/_images/sphx_glr_histogram_path_001_2_00x.png)

Instead of creating a three-dimensional array and using [`make_compound_path_from_polys`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.make_compound_path_from_polys "matplotlib.path.Path.make_compound_path_from_polys")
, we could as well create the compound path directly using vertices and codes as shown below

[nrects](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= len([left](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[nverts](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [nrects](https://docs.python.org/3/library/functions.html#int "builtins.int")
\*(1+3+1)
[verts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(([nverts](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 2))
[codes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
([nverts](https://docs.python.org/3/library/functions.html#int "builtins.int")
, int) \* [path.Path.LINETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
[codes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0::5\] \= [path.Path.MOVETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
[codes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[4::5\] \= [path.Path.CLOSEPOLY](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
[verts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0::5, 0\] \= [left](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[verts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0::5, 1\] \= [bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[verts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1::5, 0\] \= [left](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[verts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1::5, 1\] \= [top](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[verts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2::5, 0\] \= [right](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[verts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2::5, 1\] \= [top](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[verts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3::5, 0\] \= [right](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
[verts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[3::5, 1\] \= [bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[barpath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 \= [path.Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
([verts](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [codes](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# make a patch out of it, don't add a margin at y=0
[patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 \= [patches.PathPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
([barpath](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
)
[patch.sticky\_edges.y](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.sticky_edges.html#matplotlib.artist.Artist.sticky_edges "matplotlib.artist.Artist.sticky_edges")
\[:\] \= \[0\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
)
[ax.autoscale\_view](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![histogram path](https://matplotlib.org/stable/_images/sphx_glr_histogram_path_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.patches`](https://matplotlib.org/stable/api/patches_api.html#module-matplotlib.patches "matplotlib.patches")
    
*   [`matplotlib.patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
    
*   [`matplotlib.path`](https://matplotlib.org/stable/api/path_api.html#module-matplotlib.path "matplotlib.path")
    
*   [`matplotlib.path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
    
*   [`matplotlib.path.Path.make_compound_path_from_polys`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.make_compound_path_from_polys "matplotlib.path.Path.make_compound_path_from_polys")
    
*   [`matplotlib.axes.Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
    
*   [`matplotlib.collections.PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
    

This example shows an alternative to

*   [`matplotlib.collections.PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
    
*   [`matplotlib.axes.Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
    

[`Download Jupyter notebook: histogram_path.ipynb`](https://matplotlib.org/stable/_downloads/c9d554269189834fb802c7bd21077f14/histogram_path.ipynb)

[`Download Python source code: histogram_path.py`](https://matplotlib.org/stable/_downloads/5397c6ff8f61d4375f2fa83fa0eaf135/histogram_path.py)

[`Download zipped: histogram_path.zip`](https://matplotlib.org/stable/_downloads/55bde9fac9c698a957b7c99e50ba11f6/histogram_path.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)