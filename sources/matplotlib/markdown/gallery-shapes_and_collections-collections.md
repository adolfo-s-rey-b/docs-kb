[Skip to main content](https://matplotlib.org/stable/gallery/shapes_and_collections/collections.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/shapes_and_collections/collections.html#sphx-glr-download-gallery-shapes-and-collections-collections-py)
 to download the full example code.

Line, Poly and RegularPoly Collection[#](https://matplotlib.org/stable/gallery/shapes_and_collections/collections.html#line-poly-and-regularpoly-collection "Link to this heading")

====================================================================================================================================================================================

For the first two subplots, we will use spirals. Their size will be set in plot units, not data units. Their positions will be set in data units by using the _offsets_ and _offset\_transform_ keyword arguments of the [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 and [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
.

The third subplot will make regular polygons, with the same type of scaling and positioning as in the first two.

The last subplot illustrates the use of `offsets=(xo, yo)`, that is, a single tuple instead of a list of tuples, to generate successively offset curves, with the offset given in data units. This behavior is available only for the LineCollection.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import collections, transforms

[nverts](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 50
[npts](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100

\# Make some spirals
[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([nverts](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [nverts](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[spiral](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[[xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\])

\# Fixing random state for reproducibility
[rs](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
 \= [np.random.RandomState](https://numpy.org/doc/stable/reference/random/legacy.html#numpy.random.RandomState "numpy.random.RandomState")
(19680801)

\# Make some offsets
[xyo](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [rs.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.randn.html#numpy.random.RandomState.randn "numpy.random.RandomState.randn")
([npts](https://docs.python.org/3/library/functions.html#int "builtins.int")
, 2)

\# Make a list of colors from the default color cycle.
[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['axes.prop\_cycle'\].by\_key()\['color'\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, (([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
), ([ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax4](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
)) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2)
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(top\=0.92, left\=0.07, right\=0.97,
                    hspace\=0.3, wspace\=0.3)

[col](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 \= [collections.LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
(
    \[[spiral](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\], offsets\=[xyo](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, offset\_transform\=[ax1.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
, color\=[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
\# transform the line segments such that their size is given in points
[trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 \= [fig.dpi\_scale\_trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 + [transforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale(1.0/72.0)
[col.set\_transform](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection.set_transform "matplotlib.collections.LineCollection.set_transform")
([trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
)  \# the points to pixels transform
[ax1.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
([col](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('LineCollection using offsets')

\# The same data as above, but fill the curves.
[col](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 \= [collections.PolyCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
(
    \[[spiral](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\], offsets\=[xyo](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, offset\_transform\=[ax2.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
, color\=[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 \= [transforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale([fig.dpi](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.dpi.html#matplotlib.figure.Figure.dpi "matplotlib.figure.Figure.dpi")
/72.0)
[col.set\_transform](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection.set_transform "matplotlib.collections.LineCollection.set_transform")
([trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
)  \# the points to pixels transform
[ax2.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
([col](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('PolyCollection using offsets')

\# 7-sided regular polygons
[col](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 \= [collections.RegularPolyCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.RegularPolyCollection "matplotlib.collections.RegularPolyCollection")
(
    7, sizes\=[np.abs](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* 10.0, offsets\=[xyo](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, offset\_transform\=[ax3.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
,
    color\=[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 \= [transforms.Affine2D](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
().scale([fig.dpi](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.dpi.html#matplotlib.figure.Figure.dpi "matplotlib.figure.Figure.dpi")
 / 72.0)
[col.set\_transform](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection.set_transform "matplotlib.collections.LineCollection.set_transform")
([trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
)  \# the points to pixels transform
[ax3.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
([col](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
)
[ax3.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('RegularPolyCollection using offsets')

\# Simulate a series of ocean current profiles, successively
\# offset by 0.1 m/s so that they form what is sometimes called
\# a "waterfall" plot or a "stagger" plot.
[nverts](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 60
[ncurves](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 20
[offs](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (0.1, 0.0)

[yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [nverts](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[ym](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
([yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= (0.2 + ([ym](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \- [yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) / [ym](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
) \*\* 2 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 0.4) \* 0.5
[segs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range([ncurves](https://docs.python.org/3/library/functions.html#int "builtins.int")
):
    [xxx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 0.02\*[rs.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.randn.html#numpy.random.RandomState.randn "numpy.random.RandomState.randn")
([nverts](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [curve](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.column\_stack](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")
(\[[xxx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 \* 100\])
    [segs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([curve](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[col](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 \= [collections.LineCollection](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
([segs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, offsets\=[offs](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, color\=[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax4.add\_collection](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
([col](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
)
[ax4.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Successive data offsets')
[ax4.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Zonal velocity component (m/s)')
[ax4.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Depth (m)')
[ax4.invert\_yaxis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html#matplotlib.axes.Axes.invert_yaxis "matplotlib.axes.Axes.invert_yaxis")
()  \# so that depth increases downward

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![LineCollection using offsets, PolyCollection using offsets, RegularPolyCollection using offsets, Successive data offsets](https://matplotlib.org/stable/_images/sphx_glr_collections_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
    
*   [`matplotlib.collections`](https://matplotlib.org/stable/api/collections_api.html#module-matplotlib.collections "matplotlib.collections")
    
*   [`matplotlib.collections.LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
    
*   [`matplotlib.collections.RegularPolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.RegularPolyCollection "matplotlib.collections.RegularPolyCollection")
    
*   [`matplotlib.axes.Axes.add_collection`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
    
*   [`matplotlib.transforms.Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
    
*   [`matplotlib.transforms.Affine2D.scale`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.scale "matplotlib.transforms.Affine2D.scale")
    

**Total running time of the script:** (0 minutes 1.100 seconds)

[`Download Jupyter notebook: collections.ipynb`](https://matplotlib.org/stable/_downloads/c1fdd4c65339ba1e6d8e9045b456eb06/collections.ipynb)

[`Download Python source code: collections.py`](https://matplotlib.org/stable/_downloads/630514b3cff2ab2df9eb51e7c5cea20b/collections.py)

[`Download zipped: collections.zip`](https://matplotlib.org/stable/_downloads/9b645918e832c122bc6d2d8e54c63695/collections.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)