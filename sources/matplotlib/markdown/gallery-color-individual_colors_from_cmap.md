[Skip to main content](https://matplotlib.org/stable/gallery/color/individual_colors_from_cmap.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/color/individual_colors_from_cmap.html#sphx-glr-download-gallery-color-individual-colors-from-cmap-py)
 to download the full example code.

Selecting individual colors from a colormap[#](https://matplotlib.org/stable/gallery/color/individual_colors_from_cmap.html#selecting-individual-colors-from-a-colormap "Link to this heading")

================================================================================================================================================================================================

Sometimes we want to use more colors or a different set of colors than the default color cycle provides. Selecting individual colors from one of the provided colormaps can be a convenient way to do this.

We can retrieve colors from any [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 by calling it with a float or a list of floats in the range \[0, 1\]; e.g. `cmap(0.5)` will give the middle color. See also [`Colormap.__call__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.__call__ "matplotlib.colors.Colormap.__call__")
.

Extracting colors from a continuous colormap[#](https://matplotlib.org/stable/gallery/color/individual_colors_from_cmap.html#extracting-colors-from-a-continuous-colormap "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

[n\_lines](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 21
[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\['plasma'\]

\# Take colors at regular intervals spanning the colormap.
[colors](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, [n\_lines](https://docs.python.org/3/library/functions.html#int "builtins.int")
))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained')

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 in enumerate([colors](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, [i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![individual colors from cmap](https://matplotlib.org/stable/_images/sphx_glr_individual_colors_from_cmap_001_2_00x.png)

Extracting colors from a discrete colormap[#](https://matplotlib.org/stable/gallery/color/individual_colors_from_cmap.html#extracting-colors-from-a-discrete-colormap "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The list of all colors in a [`ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 is available as the `colors` attribute. Note that all the colors from Matplotlib's qualitative color maps are also available as color sequences, so may be accessed more directly from the color sequence registry. See [Named color sequences](https://matplotlib.org/stable/gallery/color/color_sequences.html)
.

[colors](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\['Dark2'\].[colors](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained')

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 in enumerate([colors](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
):
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, [i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], [color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[color](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![individual colors from cmap](https://matplotlib.org/stable/_images/sphx_glr_individual_colors_from_cmap_002_2_00x.png)

See Also[#](https://matplotlib.org/stable/gallery/color/individual_colors_from_cmap.html#see-also "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

For more details about manipulating colormaps, see [Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#colormap-manipulation)
. To change the default color cycle, see [Styling with cycler](https://matplotlib.org/stable/users/explain/artists/color_cycle.html#color-cycle)
.

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
    
*   [`matplotlib.colors.Colormap.resampled`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.resampled "matplotlib.colors.Colormap.resampled")
    

Tags: [styling: colormap](https://matplotlib.org/stable/_tags/styling-colormap.html)
 [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)

**Total running time of the script:** (0 minutes 1.267 seconds)

[`Download Jupyter notebook: individual_colors_from_cmap.ipynb`](https://matplotlib.org/stable/_downloads/0733bde90fc614781827c1492842b18a/individual_colors_from_cmap.ipynb)

[`Download Python source code: individual_colors_from_cmap.py`](https://matplotlib.org/stable/_downloads/b1c9924f6057db5fd639115816c61470/individual_colors_from_cmap.py)

[`Download zipped: individual_colors_from_cmap.zip`](https://matplotlib.org/stable/_downloads/77c01f39ed73cfa255dde57fb373b30e/individual_colors_from_cmap.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page