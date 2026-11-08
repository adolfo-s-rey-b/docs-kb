[Skip to main content](https://matplotlib.org/stable/gallery/misc/contour_manual.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/contour_manual.html#sphx-glr-download-gallery-misc-contour-manual-py)
 to download the full example code.

Manual Contour[#](https://matplotlib.org/stable/gallery/misc/contour_manual.html#manual-contour "Link to this heading")

========================================================================================================================

Example of displaying your own contour lines and polygons using ContourSet.

import matplotlib.pyplot as plt

from matplotlib.contour import [ContourSet](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
from matplotlib.path import Path

Contour lines for each level are a list/tuple of polygons.

[lines0](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[\[0, 0\], \[0, 4\]\]\]
[lines1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[\[2, 0\], \[1, 2\], \[1, 3\]\]\]
[lines2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[\[3, 0\], \[3, 2\]\], \[\[3, 3\], \[3, 4\]\]\]  \# Note two lines.

Filled contours between two levels are also a list/tuple of polygons. Points can be ordered clockwise or anticlockwise.

[filled01](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[\[0, 0\], \[0, 4\], \[1, 3\], \[1, 2\], \[2, 0\]\]\]
[filled12](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[\[2, 0\], \[3, 0\], \[3, 2\], \[1, 3\], \[1, 2\]\],   \# Note two polygons.\
            \[\[1, 4\], \[3, 4\], \[3, 3\]\]\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# Filled contours using filled=True.
[cs](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 \= [ContourSet](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, \[0, 1, 2\], \[[filled01](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
, [filled12](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\], filled\=True, cmap\="bone")
[cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([cs](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
)

\# Contour lines (non-filled).
[lines](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 \= [ContourSet](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
(
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, \[0, 1, 2\], \[[lines0](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
, [lines1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
, [lines2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\], cmap\="cool", linewidths\=3)
[cbar.add\_lines](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar.add_lines "matplotlib.colorbar.Colorbar.add_lines")
([lines](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
)

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-0.5, 3.5), ylim\=(\-0.5, 4.5),
       title\='User-specified contours')

![User-specified contours](https://matplotlib.org/stable/_images/sphx_glr_contour_manual_001_2_00x.png)

Multiple filled contour lines can be specified in a single list of polygon vertices along with a list of vertex kinds (code types) as described in the Path class. This is particularly useful for polygons with holes.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[filled01](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[\[0, 0\], \[3, 0\], \[3, 3\], \[0, 3\], \[1, 1\], \[1, 2\], \[2, 2\], \[2, 1\]\]\]
[M](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
 \= [Path.MOVETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
[L](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
 \= [Path.LINETO](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
[kinds01](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\[[M](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, [L](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, [L](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, [L](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, [M](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, [L](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, [L](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
, [L](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")\
\]\]
[cs](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 \= [ContourSet](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, \[0, 1\], \[[filled01](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\], \[[kinds01](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\], filled\=True)
[cbar](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 \= [fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([cs](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
)

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(\-0.5, 3.5), ylim\=(\-0.5, 3.5),
       title\='User specified filled contours with holes')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![User specified filled contours with holes](https://matplotlib.org/stable/_images/sphx_glr_contour_manual_002_2_00x.png)

[`Download Jupyter notebook: contour_manual.ipynb`](https://matplotlib.org/stable/_downloads/4928d08e05b81a18d1af837559d85b47/contour_manual.ipynb)

[`Download Python source code: contour_manual.py`](https://matplotlib.org/stable/_downloads/6f6ddec07749bdbe4eea6b25d5dc81a6/contour_manual.py)

[`Download zipped: contour_manual.zip`](https://matplotlib.org/stable/_downloads/614a78b64adba9806fa0ef11224eb413/contour_manual.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)