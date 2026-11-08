[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_label_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_label_demo.html#sphx-glr-download-gallery-images-contours-and-fields-contour-label-demo-py)
 to download the full example code.

Contour Label Demo[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_label_demo.html#contour-label-demo "Link to this heading")

==========================================================================================================================================================

Illustrate some of the more advanced things that one can do with contour labels.

See also the [contour demo example](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_demo.html)
.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.ticker as ticker

Define our surface

[delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.025
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-3.0, 3.0, [delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-2.0, 2.0, [delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 \- [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)
[Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 1)\*\*2 \- ([Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 1)\*\*2)
[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= ([Z1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- [Z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* 2

Make contour labels with custom level formatters

\# This custom formatter removes trailing zeros, e.g. "1.0" becomes "1", and
\# then adds a percent sign.
def fmt([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [s](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= f"{[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:.1f}"
    if [s](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.endswith("0"):
        [s](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= f"{[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:.0f}"
    return rf"{[s](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
} \\%" if [plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\["text.usetex"\] else f"{[s](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
} %"

\# Basic contour plot
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[CS](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 \= [ax.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[ax.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html#matplotlib.axes.Axes.clabel "matplotlib.axes.Axes.clabel")
([CS](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
, [CS.levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
\=[fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
, fontsize\=10)

![contour label demo](https://matplotlib.org/stable/_images/sphx_glr_contour_label_demo_001_2_00x.png)

Label contours with arbitrary strings using a dictionary

[fig1](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# Basic contour plot
[CS1](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 \= [ax1.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
 \= {}
[strs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh'\]
for [l](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [s](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([CS1.levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [strs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
\[[l](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
\] \= [s](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")

\# Label every other level using strings
[ax1.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html#matplotlib.axes.Axes.clabel "matplotlib.axes.Axes.clabel")
([CS1](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
, [CS1.levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::2\], [fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
\=[fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
, fontsize\=10)

![contour label demo](https://matplotlib.org/stable/_images/sphx_glr_contour_label_demo_002_2_00x.png)

Use a Formatter

[fig2](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[CS2](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 \= [ax2.contour](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 100\*\*[Z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, locator\=[plt.LogLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
())
[fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
 \= [ticker.LogFormatterMathtext](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
()
[fmt.create\_dummy\_axis](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.TickHelper.create_dummy_axis "matplotlib.ticker.TickHelper.create_dummy_axis")
()
[ax2.clabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html#matplotlib.axes.Axes.clabel "matplotlib.axes.Axes.clabel")
([CS2](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
, [CS2.levels](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
\=[fmt](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("$100^Z$")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![$100^Z$](https://matplotlib.org/stable/_images/sphx_glr_contour_label_demo_003_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
     / [`matplotlib.pyplot.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
    
*   [`matplotlib.axes.Axes.clabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html#matplotlib.axes.Axes.clabel "matplotlib.axes.Axes.clabel")
     / [`matplotlib.pyplot.clabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel "matplotlib.pyplot.clabel")
    
*   [`matplotlib.ticker.LogFormatterMathtext`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
    
*   [`matplotlib.ticker.TickHelper.create_dummy_axis`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.TickHelper.create_dummy_axis "matplotlib.ticker.TickHelper.create_dummy_axis")
    

**Total running time of the script:** (0 minutes 2.061 seconds)

[`Download Jupyter notebook: contour_label_demo.ipynb`](https://matplotlib.org/stable/_downloads/1ef3d8d533bb63a92ffa1e82e39d76c0/contour_label_demo.ipynb)

[`Download Python source code: contour_label_demo.py`](https://matplotlib.org/stable/_downloads/aad94dfade69ead9a77cbfaa5cfddd61/contour_label_demo.py)

[`Download zipped: contour_label_demo.zip`](https://matplotlib.org/stable/_downloads/cb7cd4d2cf80c6170ecf28308b37bc96/contour_label_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)