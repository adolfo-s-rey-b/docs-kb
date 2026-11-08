[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#main-content)

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
    

Changes to the default style[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#changes-to-the-default-style "Link to this heading")

==================================================================================================================================================================

The most important changes in matplotlib 2.0 are the changes to the default style.

While it is impossible to select the best default for all cases, these are designed to work well in the most common cases.

A 'classic' style sheet is provided so reverting to the 1.x default values is a single line of python

import matplotlib.style
import matplotlib as mpl
mpl.style.use('classic')

See [The matplotlibrc file](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files)
 for details about how to persistently and selectively revert many of these changes.

[Colors, color cycles, and colormaps](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#colors-color-cycles-and-colormaps "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Colors in default property cycle](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#colors-in-default-property-cycle "Link to this heading")

The colors in the default property cycle have been changed from `['b', 'g', 'r', 'c', 'm', 'y', 'k']` to the category10 color palette used by [Vega](https://github.com/vega/vega/wiki/Scales#scale-range-literals)
 and [d3](https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md#category10)
 originally developed at Tableau.

([`Source code`](https://matplotlib.org/stable/_downloads/0ecb18ff813a1eba755e04286c055f86/dflt_style_changes-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/98a45b36f4fce10e6dffc99ae7e91e58/dflt_style_changes-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/6f419b9f07260086d9bd437456c575ed/dflt_style_changes-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-1.2x.png)

In addition to changing the colors, an additional method to specify colors was added. Previously, the default colors were the single character short-hand notations for red, green, blue, cyan, magenta, yellow, and black. This made them easy to type and usable in the abbreviated style string in `plot`, however the new default colors are only specified via hex values. To access these colors outside of the property cycling the notation for colors `'CN'`, where `N` takes values 0-9, was added to denote the first 10 colors in `[rcParams["axes.prop_cycle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.prop_cycle#rcparam-axes-prop-cycle) ` (default: `cycler('color', [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), (1.0, 0.4980392156862745, 0.054901960784313725), (0.17254901960784313, 0.6274509803921569, 0.17254901960784313), (0.8392156862745098, 0.15294117647058825, 0.1568627450980392), (0.5803921568627451, 0.403921568627451, 0.7411764705882353), (0.5490196078431373, 0.33725490196078434, 0.29411764705882354), (0.8901960784313725, 0.4666666666666667, 0.7607843137254902), (0.4980392156862745, 0.4980392156862745, 0.4980392156862745), (0.7372549019607844, 0.7411764705882353, 0.13333333333333333), (0.09019607843137255, 0.7450980392156863, 0.8117647058823529)])`). See [Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 for more details.

To restore the old color cycle use

from cycler import cycler
mpl.rcParams\['axes.prop\_cycle'\] \= cycler(color\='bgrcmyk')

or set

axes.prop\_cycle    : cycler('color', 'bgrcmyk')

in your `matplotlibrc` file.

### [Colormap](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#colormap "Link to this heading")

The new default colormap used by [`matplotlib.cm.ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 instances is 'viridis' (aka [option D](https://bids.github.io/colormap/)
).

([`Source code`](https://matplotlib.org/stable/_downloads/beac74687f5bc32a51d7292939f062e4/dflt_style_changes-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/4b1e7f6bddb741490bb451e4f7790375/dflt_style_changes-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/3c8dc484e12865138542e76c621bc53f/dflt_style_changes-2.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-2.2x.png)

For an introduction to color theory and how 'viridis' was generated watch Nathaniel Smith and Stéfan van der Walt's talk from SciPy2015. See [here for many more details](https://bids.github.io/colormap/)
 about the other alternatives and the tools used to create the color map. For details on all of the colormaps available in matplotlib see [Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html#colormaps)
.

The previous default can be restored using

mpl.rcParams\['image.cmap'\] \= 'jet'

or setting

image.cmap    : 'jet'

in your `matplotlibrc` file; however this is strongly discouraged.

### [Interactive figures](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#interactive-figures "Link to this heading")

The default interactive figure background color has changed from grey to white, which matches the default background color used when saving.

The previous defaults can be restored by

mpl.rcParams\['figure.facecolor'\] \= '0.75'

or by setting

figure.facecolor : '0.75'

in your `matplotlibrc` file.

### [Grid lines](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#grid-lines "Link to this heading")

The default style of grid lines was changed from black dashed lines to thicker solid light grey lines.

([`Source code`](https://matplotlib.org/stable/_downloads/8a7897d38d9becada8bd5cc93bece409/dflt_style_changes-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/9932c129f1a85da99d31212cc5a5fe53/dflt_style_changes-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/87178d3bcd1b00900e5f330c9fecbe42/dflt_style_changes-3.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-3.2x.png)

The previous default can be restored by using:

mpl.rcParams\['grid.color'\] \= 'k'
mpl.rcParams\['grid.linestyle'\] \= ':'
mpl.rcParams\['grid.linewidth'\] \= 0.5

or by setting:

grid.color       :   k       \# grid color
grid.linestyle   :   :       \# dotted
grid.linewidth   :   0.5     \# in points

in your `matplotlibrc` file.

[Figure size, font size, and screen dpi](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#figure-size-font-size-and-screen-dpi "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The default dpi used for on-screen display was changed from 80 dpi to 100 dpi, the same as the default dpi for saving files. Due to this change, the on-screen display is now more what-you-see-is-what-you-get for saved files. To keep the figure the same size in terms of pixels, in order to maintain approximately the same size on the screen, the default figure size was reduced from 8x6 inches to 6.4x4.8 inches. As a consequence of this the default font sizes used for the title, tick labels, and axes labels were reduced to maintain their size relative to the overall size of the figure. By default the dpi of the saved image is now the dpi of the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 instance being saved.

This will have consequences if you are trying to match text in a figure directly with external text.

The previous defaults can be restored by

mpl.rcParams\['figure.figsize'\] \= \[8.0, 6.0\]
mpl.rcParams\['figure.dpi'\] \= 80
mpl.rcParams\['savefig.dpi'\] \= 100

mpl.rcParams\['font.size'\] \= 12
mpl.rcParams\['legend.fontsize'\] \= 'large'
mpl.rcParams\['figure.titlesize'\] \= 'medium'

or by setting:

figure.figsize   : \[8.0, 6.0\]
figure.dpi       : 80
savefig.dpi      : 100

font.size        : 12.0
legend.fontsize  : 'large'
figure.titlesize : 'medium'

In your `matplotlibrc` file.

In addition, the `forward` kwarg to [`set_size_inches`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_size_inches.html#matplotlib.figure.Figure.set_size_inches "matplotlib.figure.Figure.set_size_inches")
 now defaults to [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 to improve the interactive experience. Backend canvases that adjust the size of their bound [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 must pass `forward=False` to avoid circular behavior. This default is not configurable.

[Plotting functions](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#plotting-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`scatter`](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#scatter "Link to this heading")

The following changes were made to the default behavior of [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")

*   The default size of the elements in a scatter plot is now based on `[rcParams["lines.markersize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.markersize#rcparam-lines-markersize) ` (default: `6.0`) so it is consistent with `plot(X, Y, 'o')`. The old value was 20, and the new value is 36 (6^2).
    
*   Scatter markers no longer have a black edge.
    
*   If the color of the markers is not specified it will follow the property cycle, pulling from the 'patches' cycle on the `Axes`.
    

([`Source code`](https://matplotlib.org/stable/_downloads/154e9bc75ed8ecfb294287ea5f0a1951/dflt_style_changes-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/fbc3e00db1aeb74cfb7412ae76ab50df/dflt_style_changes-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/47e90e0e48648754899faafa86a4de35/dflt_style_changes-4.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-4.2x.png)

The classic default behavior of [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
 can only be recovered through `mpl.style.use('classic')`. The marker size can be recovered via

mpl.rcParam\['lines.markersize'\] \= np.sqrt(20)

however, this will also affect the default marker size of [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
. To recover the classic behavior on a per-call basis pass the following kwargs:

classic\_kwargs \= {'s': 20, 'edgecolors': 'k', 'c': 'b'}

### [`plot`](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#plot "Link to this heading")

The following changes were made to the default behavior of [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")

*   the default linewidth increased from 1 to 1.5
    
*   the dash patterns associated with `'--'`, `':'`, and `'-.'` have changed
    
*   the dash patterns now scale with line width
    

([`Source code`](https://matplotlib.org/stable/_downloads/bee3b2f55fc965363e31f2517d937a72/dflt_style_changes-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/8b5a5cf6b45b864de23b2aa85cb7c7f7/dflt_style_changes-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/a4f0e5a54fe19d079553c3e23f8f917c/dflt_style_changes-5.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-5.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-5.2x.png)

The previous defaults can be restored by setting:

mpl.rcParams\['lines.linewidth'\] \= 1.0
mpl.rcParams\['lines.dashed\_pattern'\] \= \[6, 6\]
mpl.rcParams\['lines.dashdot\_pattern'\] \= \[3, 5, 1, 5\]
mpl.rcParams\['lines.dotted\_pattern'\] \= \[1, 3\]
mpl.rcParams\['lines.scale\_dashes'\] \= False

or by setting:

lines.linewidth   : 1.0
lines.dashed\_pattern : 6, 6
lines.dashdot\_pattern : 3, 5, 1, 5
lines.dotted\_pattern : 1, 3
lines.scale\_dashes: False

in your `matplotlibrc` file.

### [`errorbar`](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#errorbar "Link to this heading")

By default, caps on the ends of errorbars are not present.

([`Source code`](https://matplotlib.org/stable/_downloads/07b3d68c9aba9f3abe0b8b1478bfbd36/dflt_style_changes-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/defd4bf4c667d93a90203794a5ef5a21/dflt_style_changes-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/8310b6f6221ca5518033e1f8a2764250/dflt_style_changes-6.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-6.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-6.2x.png)

This also changes the return value of [`errorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
 as the list of 'caplines' will be empty by default.

The previous defaults can be restored by setting:

mpl.rcParams\['errorbar.capsize'\] \= 3

or by setting

errorbar.capsize : 3

in your `matplotlibrc` file.

### [`boxplot`](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#boxplot "Link to this heading")

Previously, boxplots were composed of a mish-mash of styles that were, for better for worse, inherited from Matlab. Most of the elements were blue, but the medians were red. The fliers (outliers) were black plus-symbols ('+') and the whiskers were dashed lines, which created ambiguity if the (solid and black) caps were not drawn.

For the new defaults, everything is black except for the median and mean lines (if drawn), which are set to the first two elements of the current color cycle. Also, the default flier markers are now hollow circles, which maintain the ability of the plus-symbols to overlap without obscuring data too much.

([`Source code`](https://matplotlib.org/stable/_downloads/e5ab1e8bc13389820a5b6d980acf5908/dflt_style_changes-7.py)
)

The previous defaults can be restored by setting:

mpl.rcParams\['boxplot.flierprops.color'\] \= 'k'
mpl.rcParams\['boxplot.flierprops.marker'\] \= '+'
mpl.rcParams\['boxplot.flierprops.markerfacecolor'\] \= 'none'
mpl.rcParams\['boxplot.flierprops.markeredgecolor'\] \= 'k'
mpl.rcParams\['boxplot.boxprops.color'\] \= 'b'
mpl.rcParams\['boxplot.whiskerprops.color'\] \= 'b'
mpl.rcParams\['boxplot.whiskerprops.linestyle'\] \= '--'
mpl.rcParams\['boxplot.medianprops.color'\] \= 'r'
mpl.rcParams\['boxplot.meanprops.color'\] \= 'r'
mpl.rcParams\['boxplot.meanprops.marker'\] \= '^'
mpl.rcParams\['boxplot.meanprops.markerfacecolor'\] \= 'r'
mpl.rcParams\['boxplot.meanprops.markeredgecolor'\] \= 'k'
mpl.rcParams\['boxplot.meanprops.markersize'\] \= 6
mpl.rcParams\['boxplot.meanprops.linestyle'\] \= '--'
mpl.rcParams\['boxplot.meanprops.linewidth'\] \= 1.0

or by setting:

boxplot.flierprops.color:           'k'
boxplot.flierprops.marker:          '+'
boxplot.flierprops.markerfacecolor: 'none'
boxplot.flierprops.markeredgecolor: 'k'
boxplot.boxprops.color:             'b'
boxplot.whiskerprops.color:         'b'
boxplot.whiskerprops.linestyle:     '--'
boxplot.medianprops.color:          'r'
boxplot.meanprops.color:            'r'
boxplot.meanprops.marker:           '^'
boxplot.meanprops.markerfacecolor:  'r'
boxplot.meanprops.markeredgecolor:  'k'
boxplot.meanprops.markersize:        6
boxplot.meanprops.linestyle:         '--'
boxplot.meanprops.linewidth:         1.0

in your `matplotlibrc` file.

### [`fill_between` and `fill_betweenx`](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#fill-between-and-fill-betweenx "Link to this heading")

[`fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
 and [`fill_betweenx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
 both follow the patch color cycle.

([`Source code`](https://matplotlib.org/stable/_downloads/c0562bb2361c224cd64565bac1f14bbf/dflt_style_changes-8.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/c401ca59ae3ecf2800f20b56fc803a7b/dflt_style_changes-8.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/4abf606cc6163fc3744f8df1068df338/dflt_style_changes-8.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-8.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-8.2x.png)

If the facecolor is set via the `facecolors` or `color` keyword argument, then the color is not cycled.

To restore the previous behavior, explicitly pass the keyword argument `facecolors='C0'` to the method call.

### [Patch edges and color](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#patch-edges-and-color "Link to this heading")

Most artists drawn with a patch (`~matplotlib.axes.Axes.bar`, `~matplotlib.axes.Axes.pie`, etc) no longer have a black edge by default. The default face color is now `'C0'` instead of `'b'`.

([`Source code`](https://matplotlib.org/stable/_downloads/89f9f997b5b286b9a7e5a78a1cf44d5d/dflt_style_changes-9.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/9e09443bf8c1794dae5c8ff5bc2cf041/dflt_style_changes-9.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/6acade146fc3f03882dd4b417262d336/dflt_style_changes-9.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-9.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-9.2x.png)

The previous defaults can be restored by setting:

mpl.rcParams\['patch.force\_edgecolor'\] \= True
mpl.rcParams\['patch.facecolor'\] \= 'b'

or by setting:

patch.facecolor        : b
patch.force\_edgecolor  : True

in your `matplotlibrc` file.

### [`hexbin`](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#hexbin "Link to this heading")

The default value of the _linecolor_ keyword argument for [`hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")
 has changed from `'none'` to `'face'`. If 'none' is now supplied, no line edges are drawn around the hexagons.

### [`bar` and `barh`](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#bar-and-barh "Link to this heading")

The default value of the `align` kwarg for both [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 and [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
 is changed from `'edge'` to `'center'`.

([`Source code`](https://matplotlib.org/stable/_downloads/f981d3c652a3ea3114652e1f8a520a5b/dflt_style_changes-10.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/da1c2a71757532c67f99f5f31e792943/dflt_style_changes-10.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/3d8b9dd513a29bc577e66c2c2827ad32/dflt_style_changes-10.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-10.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-10.2x.png)

To restore the previous behavior explicitly pass the keyword argument `align='edge'` to the method call.

[Hatching](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id16)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#hatching "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The color of the lines in the hatch is now determined by

*   If an edge color is explicitly set, use that for the hatch color
    
*   If the edge color is not explicitly set, use `[rcParams["hatch.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=hatch.color#rcparam-hatch-color) ` (default: `'edge'`) which is looked up at artist creation time.
    

The width of the lines in a hatch pattern is now configurable by the rcParams `[rcParams["hatch.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=hatch.linewidth#rcparam-hatch-linewidth) ` (default: `1.0`), which defaults to 1 point. The old behavior for the line width was different depending on backend:

*   PDF: 0.1 pt
    
*   SVG: 1.0 pt
    
*   PS: 1 px
    
*   Agg: 1 px
    

The old line width behavior cannot be restored across all backends simultaneously, but can be restored for a single backend by setting:

mpl.rcParams\['hatch.linewidth'\] \= 0.1  \# previous pdf hatch linewidth
mpl.rcParams\['hatch.linewidth'\] \= 1.0  \# previous svg hatch linewidth

The behavior of the PS and Agg backends was DPI dependent, thus:

mpl.rcParams\['figure.dpi'\] \= dpi
mpl.rcParams\['savefig.dpi'\] \= dpi  \# or leave as default 'figure'
mpl.rcParams\['hatch.linewidth'\] \= 1.0 / dpi  \# previous ps and Agg hatch linewidth

There is no direct API level control of the hatch color or linewidth.

Hatching patterns are now rendered at a consistent density, regardless of DPI. Formerly, high DPI figures would be more dense than the default, and low DPI figures would be less dense. This old behavior cannot be directly restored, but the density may be increased by repeating the hatch specifier.

[Fonts](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id17)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#fonts "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Normal text](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id18)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#normal-text "Link to this heading")

The default font has changed from "Bitstream Vera Sans" to "DejaVu Sans". DejaVu Sans has additional international and math characters, but otherwise has the same appearance as Bitstream Vera Sans. Latin, Greek, Cyrillic, Armenian, Georgian, Hebrew, and Arabic are [all supported](https://dejavu-fonts.github.io/)
 (but right-to-left rendering is still not handled by matplotlib). In addition, DejaVu contains a sub-set of emoji symbols.

([`Source code`](https://matplotlib.org/stable/_downloads/74fb5f7eb61966e449acce522a5cfeb4/dflt_style_changes-11.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/6154e435b1e2c493b572e1c8aacd8ba3/dflt_style_changes-11.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/563eed8f79156be1655f945068029e3b/dflt_style_changes-11.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-11.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-11.2x.png)

See the [DejaVu Sans PDF sample for full coverage](http://dejavu.sourceforge.net/samples/DejaVuSans.pdf)
.

### [Math text](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id19)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#math-text "Link to this heading")

The default math font when using the built-in math rendering engine (mathtext) has changed from "Computer Modern" (i.e. LaTeX-like) to "DejaVu Sans". This change has no effect if the TeX backend is used (i.e. `text.usetex` is `True`).

([`Source code`](https://matplotlib.org/stable/_downloads/c800604a28501b7fb472433e3561fd3f/dflt_style_changes-12.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/48258c0aea288cc33fb2918321ce3635/dflt_style_changes-12.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/86e2bd20911cf25bcd712aacb76e6fa4/dflt_style_changes-12.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-12.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-12.2x.png)

([`Source code`](https://matplotlib.org/stable/_downloads/ba3bb2a386534aee8b596c377e5403ae/dflt_style_changes-13.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/9b29ce24c2ca68878f120bc36bfc9318/dflt_style_changes-13.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/af0bc1bce751ec3386906c1403509a39/dflt_style_changes-13.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-13.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-13.2x.png)

To revert to the old behavior set the:

mpl.rcParams\['mathtext.fontset'\] \= 'cm'
mpl.rcParams\['mathtext.rm'\] \= 'serif'

or set:

mathtext.fontset: cm
mathtext.rm : serif

in your `matplotlibrc` file.

This `rcParam` is consulted when the text is drawn, not when the artist is created. Thus all mathtext on a given `canvas` will use the same fontset.

[Legends](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id20)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#legends "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   By default, the number of points displayed in a legend is now 1.
    
*   The default legend location is `'best'`, so the legend will be automatically placed in a location to minimize overlap with data.
    
*   The legend defaults now include rounded corners, a lighter boundary, and partially transparent boundary and background.
    

([`Source code`](https://matplotlib.org/stable/_downloads/9d328825d69429a35575d407e464082f/dflt_style_changes-14.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/b30d23124d053a01e802e570452c99f9/dflt_style_changes-14.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/c7deb2b40f51f6016c63f06371ace2d3/dflt_style_changes-14.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-14.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-14.2x.png)

The previous defaults can be restored by setting:

mpl.rcParams\['legend.fancybox'\] \= False
mpl.rcParams\['legend.loc'\] \= 'upper right'
mpl.rcParams\['legend.numpoints'\] \= 2
mpl.rcParams\['legend.fontsize'\] \= 'large'
mpl.rcParams\['legend.framealpha'\] \= None
mpl.rcParams\['legend.scatterpoints'\] \= 3
mpl.rcParams\['legend.edgecolor'\] \= 'inherit'

or by setting:

legend.fancybox      : False
legend.loc           : upper right
legend.numpoints     : 2      \# the number of points in the legend line
legend.fontsize      : large
legend.framealpha    : None    \# opacity of legend frame
legend.scatterpoints : 3 \# number of scatter points
legend.edgecolor     : inherit   \# legend edge color ('inherit'
                                 \# means it uses axes.edgecolor)

in your `matplotlibrc` file.

[Image](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id21)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#image "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Interpolation](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id22)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#interpolation "Link to this heading")

The default interpolation method for [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 is now `'nearest'` and by default it resamples the data (both up and down sampling) before colormapping.

([`Source code`](https://matplotlib.org/stable/_downloads/36917702aabb48473a2bd48e71eac5c0/dflt_style_changes-15.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/223b95466277d485cd76aaba3619115f/dflt_style_changes-15.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/d5f467ed0bbe85163e545694796372ea/dflt_style_changes-15.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-15.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-15.2x.png)

To restore the previous behavior set:

mpl.rcParams\['image.interpolation'\] \= 'bilinear'
mpl.rcParams\['image.resample'\] \= False

or set:

image.interpolation  : bilinear  \# see help(imshow) for options
image.resample  : False

in your `matplotlibrc` file.

### [Colormapping pipeline](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id23)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#colormapping-pipeline "Link to this heading")

Previously, the input data was normalized, then colormapped, and then resampled to the resolution required for the screen. This meant that the final resampling was being done in color space. Because the color maps are not generally linear in RGB space, colors not in the colormap may appear in the final image. This bug was addressed by an almost complete overhaul of the image handling code.

The input data is now normalized, then resampled to the correct resolution (in normalized dataspace), and then colormapped to RGB space. This ensures that only colors from the colormap appear in the final image. (If your viewer subsequently resamples the image, the artifact may reappear.)

The previous behavior cannot be restored.

### [Shading](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id24)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#shading "Link to this heading")

*   The default shading mode for light source shading, in `matplotlib.colors.LightSource.shade`, is now `overlay`. Formerly, it was `hsv`.
    

[Plot layout](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id25)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#plot-layout "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Auto limits](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id26)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#auto-limits "Link to this heading")

The previous auto-scaling behavior was to find 'nice' round numbers as view limits that enclosed the data limits, but this could produce bad plots if the data happened to fall on a vertical or horizontal line near the chosen 'round number' limit. The new default sets the view limits to 5% wider than the data range.

([`Source code`](https://matplotlib.org/stable/_downloads/8a264c8209cc2c499842fa66ad20d8bd/dflt_style_changes-16.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/8063fab0c007e34f5a57693672f104ee/dflt_style_changes-16.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/8854f6884c589608fe57d397e91ffd3c/dflt_style_changes-16.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-16.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-16.2x.png)

The size of the padding in the x and y directions is controlled by the `'axes.xmargin'` and `'axes.ymargin'` rcParams respectively. Whether the view limits should be 'round numbers' is controlled by `[rcParams["axes.autolimit_mode"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.autolimit_mode#rcparam-axes-autolimit-mode) ` (default: `'data'`). In the original `'round_number'` mode, the view limits coincide with ticks.

The previous default can be restored by using:

mpl.rcParams\['axes.autolimit\_mode'\] \= 'round\_numbers'
mpl.rcParams\['axes.xmargin'\] \= 0
mpl.rcParams\['axes.ymargin'\] \= 0

or setting:

axes.autolimit\_mode: round\_numbers
axes.xmargin: 0
axes.ymargin: 0

in your `matplotlibrc` file.

### [Z-order](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id27)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#z-order "Link to this heading")

*   Ticks and grids are now plotted above solid elements such as filled contours, but below lines. To return to the previous behavior of plotting ticks and grids above lines, set `rcParams['axes.axisbelow'] = False`.
    

### [Ticks](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id28)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#ticks "Link to this heading")

#### Direction[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#direction "Link to this heading")

To reduce the collision of tick marks with data, the default ticks now point outward by default. In addition, ticks are now drawn only on the bottom and left spines to prevent a porcupine appearance, and for a cleaner separation between subplots.

([`Source code`](https://matplotlib.org/stable/_downloads/b41c9da17fdca623ddf6eb70ec5f2947/dflt_style_changes-17.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/10ab7af656b11131b6641f6f484ddd99/dflt_style_changes-17.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/576de7f862d47cdeaec373e2b7f3d909/dflt_style_changes-17.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-17.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-17.2x.png)

To restore the previous behavior set:

mpl.rcParams\['xtick.direction'\] \= 'in'
mpl.rcParams\['ytick.direction'\] \= 'in'
mpl.rcParams\['xtick.top'\] \= True
mpl.rcParams\['ytick.right'\] \= True

or set:

xtick.top: True
xtick.direction: in

ytick.right: True
ytick.direction: in

in your `matplotlibrc` file.

#### Number of ticks[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#number-of-ticks "Link to this heading")

The default [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 used for the x and y axis is [`AutoLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoLocator "matplotlib.ticker.AutoLocator")
 which tries to find, up to some maximum number, 'nicely' spaced ticks. The locator now includes an algorithm to estimate the maximum number of ticks that will leave room for the tick labels. By default it also ensures that there are at least two ticks visible.

([`Source code`](https://matplotlib.org/stable/_downloads/e74637571f84dc7b13f9977b3ba0eb27/dflt_style_changes-18.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/8d432521928dba2ee5e536b6b60504bd/dflt_style_changes-18.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/0eb03e38be890c80ee5a2bd11a47d781/dflt_style_changes-18.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-18.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-18.2x.png)

There is no way, other than using `mpl.style.use('classic')`, to restore the previous behavior as the default. On an axis-by-axis basis you may either control the existing locator via:

ax.xaxis.get\_major\_locator().set\_params(nbins\=9, steps\=\[1, 2, 5, 10\])

or create a new [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
:

import matplotlib.ticker as mticker
ax.set\_major\_locator(mticker.MaxNLocator(nbins\=9, steps\=\[1, 2, 5, 10\])

The algorithm used by [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
 has been improved, and this may change the choice of tick locations in some cases. This also affects [`AutoLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.AutoLocator "matplotlib.ticker.AutoLocator")
, which uses `MaxNLocator` internally.

For a log-scaled axis the default locator is the [`LogLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogLocator "matplotlib.ticker.LogLocator")
. Previously the maximum number of ticks was set to 15, and could not be changed. Now there is a _numticks_ kwarg for setting the maximum to any integer value, to the string 'auto', or to its default value of None which is equivalent to 'auto'. With the 'auto' setting the maximum number will be no larger than 9, and will be reduced depending on the length of the axis in units of the tick font size. As in the case of the AutoLocator, the heuristic algorithm reduces the incidence of overlapping tick labels but does not prevent it.

### [Tick label formatting](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id29)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#tick-label-formatting "Link to this heading")

#### `LogFormatter` labeling of minor ticks[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#logformatter-labeling-of-minor-ticks "Link to this heading")

Minor ticks on a log axis are now labeled when the axis view limits span a range less than or equal to the interval between two major ticks. See [`LogFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatter "matplotlib.ticker.LogFormatter")
 for details. The minor tick labeling is turned off when using `mpl.style.use('classic')`, but cannot be controlled independently via [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
.

([`Source code`](https://matplotlib.org/stable/_downloads/03bbcc624aeab2045fd565cc5cfd4f1c/dflt_style_changes-19.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/519f2c09ad569a669ed341466b4fe757/dflt_style_changes-19.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/df6be65ed2a233bd18ff293a565aab76/dflt_style_changes-19.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-19.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-19.2x.png)

#### `ScalarFormatter` tick label formatting with offsets[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#scalarformatter-tick-label-formatting-with-offsets "Link to this heading")

With the default `[rcParams["axes.formatter.useoffset"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.useoffset#rcparam-axes-formatter-useoffset) ` (default: `True`), an offset will be used when it will save 4 or more digits. This can be controlled with the new `[rcParams["axes.formatter.offset_threshold"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.formatter.offset_threshold#rcparam-axes-formatter-offset-threshold) ` (default: `4`). To restore the previous behavior of using an offset to save 2 or more digits, use `rcParams['axes.formatter.offset_threshold'] = 2`.

([`Source code`](https://matplotlib.org/stable/_downloads/b5edc23ca916b7502d5316c36093a6a5/dflt_style_changes-20.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/732158d958be119e04d37b32ac86f94a/dflt_style_changes-20.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/79e5cca1225ac62fc21f0b7d7e3a7003/dflt_style_changes-20.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-20.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-dflt_style_changes-20.2x.png)

#### `AutoDateFormatter` format strings[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#autodateformatter-format-strings "Link to this heading")

The default date formats are now all based on ISO format, i.e., with the slowest-moving value first. The date formatters are configurable through the `date.autoformatter.*` rcParams.

| Threshold (tick interval >= than) | rcParam | classic | v2.0 |
| --- | --- | --- | --- |
| 365 days | `'date.autoformatter.year'` | `'%Y'` | `'%Y'` |
| 30 days | `'date.autoformatter.month'` | `'%b %Y'` | `'%Y-%m'` |
| 1 day | `'date.autoformatter.day'` | `'%b %d %Y'` | `'%Y-%m-%d'` |
| 1 hour | `'date.autoformatter.hour'` | `'%H:%M:%S'` | `'%H:%M'` |
| 1 minute | `'date.autoformatter.minute'` | `'%H:%M:%S.%f'` | `'%H:%M:%S'` |
| 1 second | `'date.autoformatter.second'` | `'%H:%M:%S.%f'` | `'%H:%M:%S'` |
| 1 microsecond | `'date.autoformatter.microsecond'` | `'%H:%M:%S.%f'` | `'%H:%M:%S.%f'` |

Python's `%x` and `%X` date formats may be of particular interest to format dates based on the current locale.

The previous default can be restored by:

mpl.rcParams\['date.autoformatter.year'\] \= '%Y'
mpl.rcParams\['date.autoformatter.month'\] \= '%b %Y'
mpl.rcParams\['date.autoformatter.day'\] \= '%b %d %Y'
mpl.rcParams\['date.autoformatter.hour'\] \= '%H:%M:%S'
mpl.rcParams\['date.autoformatter.minute'\] \= '%H:%M:%S.%f'
mpl.rcParams\['date.autoformatter.second'\] \= '%H:%M:%S.%f'
mpl.rcParams\['date.autoformatter.microsecond'\] \= '%H:%M:%S.%f'

or setting

date.autoformatter.year   : %Y
date.autoformatter.month  : %b %Y
date.autoformatter.day    : %b %d %Y
date.autoformatter.hour   : %H:%M:%S
date.autoformatter.minute : %H:%M:%S.%f
date.autoformatter.second : %H:%M:%S.%f
date.autoformatter.microsecond : %H:%M:%S.%f

in your `matplotlibrc` file.

[mplot3d](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#id30)
[#](https://matplotlib.org/stable/release/prev_whats_new/dflt_style_changes.html#mplot3d "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   mplot3d now obeys some style-related rcParams, rather than using hard-coded defaults. These include:
    
    *   xtick.major.width
        
    *   ytick.major.width
        
    *   xtick.color
        
    *   ytick.color
        
    *   axes.linewidth
        
    *   axes.edgecolor
        
    *   grid.color
        
    *   grid.linewidth
        
    *   grid.linestyle
        

On this page