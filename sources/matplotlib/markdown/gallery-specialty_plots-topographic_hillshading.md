[Skip to main content](https://matplotlib.org/stable/gallery/specialty_plots/topographic_hillshading.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/specialty_plots/topographic_hillshading.html#sphx-glr-download-gallery-specialty-plots-topographic-hillshading-py)
 to download the full example code.

Topographic hillshading[#](https://matplotlib.org/stable/gallery/specialty_plots/topographic_hillshading.html#topographic-hillshading "Link to this heading")

==============================================================================================================================================================

Demonstrates the visual effect of varying blend mode and vertical exaggeration on "hillshaded" plots.

Note that the "overlay" and "soft" blend modes work well for complex surfaces such as this example, while the default "hsv" blend mode works best for smooth surfaces such as many mathematical functions.

In most cases, hillshading is used purely for visual purposes, and _dx_/_dy_ can be safely ignored. In that case, you can tweak _vert\_exag_ (vertical exaggeration) by trial and error to give the desired visual effect. However, this example demonstrates how to use the _dx_ and _dy_ keyword arguments to ensure that the _vert\_exag_ parameter is the true vertical exaggeration.

![0.1, 1, 10](https://matplotlib.org/stable/_images/sphx_glr_topographic_hillshading_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.cbook import [get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
from matplotlib.colors import [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")

[dem](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
 \= [get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('jacksboro\_fault\_dem.npz')
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [dem](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
\['elevation'\]
\# -- Optional dx and dy for accurate vertical exaggeration --------------------
\# If you need topographically accurate vertical exaggeration, or you don't want
\# to guess at what \*vert\_exag\* should be, you'll need to specify the cellsize
\# of the grid (i.e. the \*dx\* and \*dy\* parameters).  Otherwise, any \*vert\_exag\*
\# value you specify will be relative to the grid spacing of your input data
\# (in other words, \*dx\* and \*dy\* default to 1.0, and \*vert\_exag\* is calculated
\# relative to those parameters).  Similarly, \*dx\* and \*dy\* are assumed to be in
\# the same units as your input z-values.  Therefore, we'll need to convert the
\# given dx and dy from decimal degrees to meters.
[dx](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [dem](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
\['dx'\], [dem](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
\['dy'\]
[dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= 111200 \* [dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
[dx](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= 111200 \* [dx](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.radians](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([dem](https://numpy.org/doc/stable/reference/generated/numpy.lib.npyio.NpzFile.html#numpy.lib.npyio.NpzFile "numpy.lib.npyio.NpzFile")
\['ymin'\]))
\# -----------------------------------------------------------------------------

\# Shade from the northwest, with the sun 45 degrees from horizontal
[ls](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
 \= [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
(azdeg\=315, altdeg\=45)
[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["gist\_earth"\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=4, ncols\=3, figsize\=(8, 9))
[plt.setp](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, xticks\=\[\], yticks\=\[\])

\# Vary vertical exaggeration and blend mode and plot all combinations
for [col](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [ve](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in zip([axs.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \[0.1, 1, 10\]):
    \# Show the hillshade intensity image in the first row
    [col](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].imshow([ls.hillshade](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.hillshade "matplotlib.colors.LightSource.hillshade")
([z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, vert\_exag\=[ve](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [dx](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
\=[dx](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
\=[dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
), [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='gray')

    \# Place hillshaded plots with different blend modes in the rest of the rows
    for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [mode](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([col](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1:\], \['hsv', 'overlay', 'soft'\]):
        [rgb](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [ls.shade](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.shade "matplotlib.colors.LightSource.shade")
([z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
, blend\_mode\=[mode](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
                       vert\_exag\=[ve](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [dx](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
\=[dx](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
\=[dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
        [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([rgb](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# Label rows and columns
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ve](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], \[0.1, 1, 10\]):
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f'{[ve](https://docs.python.org/3/library/functions.html#int "builtins.int")
}', size\=18)
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [mode](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\], \['Hillshade', 'hsv', 'overlay', 'soft'\]):
    [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
([mode](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, size\=18)

\# Group labels...
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].annotate('Vertical Exaggeration', (0.5, 1), xytext\=(0, 30),
                   textcoords\='offset points', xycoords\='axes fraction',
                   ha\='center', va\='bottom', size\=20)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2, 0\].annotate('Blend Mode', (0, 0.5), xytext\=(\-30, 0),
                   textcoords\='offset points', xycoords\='axes fraction',
                   ha\='right', va\='center', size\=20, rotation\=90)
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(bottom\=0.05, right\=0.95)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 2.231 seconds)

[`Download Jupyter notebook: topographic_hillshading.ipynb`](https://matplotlib.org/stable/_downloads/b3f732fe7a252b2c533d20606b7a1ceb/topographic_hillshading.ipynb)

[`Download Python source code: topographic_hillshading.py`](https://matplotlib.org/stable/_downloads/5a89f9cc49e663155be9290b4b7f2894/topographic_hillshading.py)

[`Download zipped: topographic_hillshading.zip`](https://matplotlib.org/stable/_downloads/125478f2712c200bf34f81989a060719/topographic_hillshading.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)