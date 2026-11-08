[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#main-content)

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
    

[What's new in Matplotlib 1.5 (Oct 29, 2015)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#what-s-new-in-matplotlib-1-5-oct-29-2015 "Link to this heading")

========================================================================================================================================================================================================================================================================

Note

matplotlib 1.5 supports Python 2.7, 3.4, and 3.5

[Interactive OO usage](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#interactive-oo-usage "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s now keep track of if their internal state has been changed but not reflected in the display ('stale') by a call to `draw`. It is thus possible to pragmatically determine if a given [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 needs to be re-drawn in an interactive session.

To facilitate interactive usage a `draw_all` method has been added to `pyplot` which will redraw all of the figures which are 'stale'.

To make this convenient for interactive use matplotlib now registers a function either with IPython's 'post\_execute' event or with the displayhook in the standard python REPL to automatically call `plt.draw_all` just before control is returned to the REPL. This ensures that the draw command is deferred and only called once.

The upshot of this is that for interactive backends (including `%matplotlib notebook`) in interactive mode (with `plt.ion()`)

import matplotlib.pyplot as plt
fig, ax \= plt.subplots()
ln, \= ax.plot(\[0, 1, 4, 9, 16\])
plt.show()
ln.set\_color('g')

will automatically update the plot to be green. Any subsequent modifications to the `Artist` objects will do likewise.

This is the first step of a larger consolidation and simplification of the pyplot internals.

[Working with labeled data like pandas DataFrames](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#working-with-labeled-data-like-pandas-dataframes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Plot methods which take arrays as inputs can now also work with labeled data and unpack such data.

This means that the following two examples produce the same plot:

Example

df \= pandas.DataFrame({"var1":\[1,2,3,4,5,6\], "var2":\[1,2,3,4,5,6\]})
plt.plot(df\["var1"\], df\["var2"\])

Example

plt.plot("var1", "var2", data\=df)

This works for most plotting methods, which expect arrays/sequences as inputs. `data` can be anything which supports `__getitem__` (`dict`, `pandas.DataFrame`, `h5py`, ...) to access `array` like values with string keys.

In addition to this, some other changes were made, which makes working with labeled data (ex `pandas.Series`) easier:

*   For plotting methods with `label` keyword argument, one of the data inputs is designated as the label source. If the user does not supply a `label` that value object will be introspected for a label, currently by looking for a `name` attribute. If the value object does not have a `name` attribute but was specified by as a key into the `data` kwarg, then the key is used. In the above examples, this results in an implicit `label="var2"` for both cases.
    
*   `plot()` now uses the index of a `Series` instead of `np.arange(len(y))`, if no `x` argument is supplied.
    

[Added `axes.prop_cycle` key to rcParams](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#added-axes-prop-cycle-key-to-rcparams "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is a more generic form of the now-deprecated `axes.color_cycle` param. Now, we can cycle more than just colors, but also linestyles, hatches, and just about any other artist property. Cycler notation is used for defining property cycles. Adding cyclers together will be like you are [`zip`](https://docs.python.org/3/library/functions.html#zip "(in Python v3.14)")
\-ing together two or more property cycles together:

axes.prop\_cycle: cycler('color', 'rgb') + cycler('lw', \[1, 2, 3\])

You can even multiply cyclers, which is like using [`itertools.product`](https://docs.python.org/3/library/itertools.html#itertools.product "(in Python v3.14)")
 on two or more property cycles.

[![../../_images/sphx_glr_color_cycle_001.png](https://matplotlib.org/stable/_images/sphx_glr_color_cycle_001.png)](https://matplotlib.org/users/explain/artists/color_cycle.html)

[New Colormaps](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#new-colormaps "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All four of the colormaps proposed as the new default are available as `'viridis'` (the new default in 2.0), `'magma'`, `'plasma'`, and `'inferno'`

([`Source code`](https://matplotlib.org/stable/_downloads/24d1216c8d4e0066bfd36b37f38f434c/whats_new_1-5-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/1bda18c01104f0bbfc0e172245db8958/whats_new_1-5-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/9c3c96aff2212aca017453fb98ae5fde/whats_new_1-5-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-1.2x.png)

[Styles](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#styles "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Several new styles have been added, including many styles from the Seaborn project. Additionally, in order to prep for the upcoming 2.0 style-change release, a 'classic' and 'default' style has been added. For this release, the 'default' and 'classic' styles are identical. By using them now in your scripts, you can help ensure a smooth transition during future upgrades of matplotlib, so that you can upgrade to the snazzy new defaults when you are ready!

import matplotlib.style
matplotlib.style.use('classic')

The 'default' style will give you matplotlib's latest plotting styles:

matplotlib.style.use('default')

[Backends](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#backends "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### New backend selection[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#new-backend-selection "Link to this heading")

The environment variable [`MPLBACKEND`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLBACKEND)
 can now be used to set the matplotlib backend.

### wx backend has been updated[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#wx-backend-has-been-updated "Link to this heading")

The wx backend can now be used with both wxPython classic and [Phoenix](https://wxpython.org/Phoenix/docs/html/main.html)
.

wxPython classic has to be at least version 2.8.12 and works on Python 2.x. As of May 2015 no official release of wxPython Phoenix is available but a current snapshot will work on Python 2.7+ and 3.4+.

If you have multiple versions of wxPython installed, then the user code is responsible setting the wxPython version. How to do this is explained in the comment at the beginning of the example [Embed in wx #2](https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_wx2_sgskip.html)
.

[Configuration (rcParams)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#configuration-rcparams "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Some parameters have been added, others have been improved.

| Parameter | Description |
| --- | --- |
| `xaxis.labelpad`, `yaxis.labelpad` | mplot3d now respects these attributes, which default to `[rcParams["axes.labelpad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.labelpad#rcparam-axes-labelpad) ` (default: `4.0`) |
| `[rcParams["axes.labelpad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.labelpad#rcparam-axes-labelpad) ` (default: `4.0`) | Default space between the axis and the label |
| `[rcParams["errorbar.capsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=errorbar.capsize#rcparam-errorbar-capsize) ` (default: `0.0`) | Default length of end caps on error bars |
| `[rcParams["xtick.minor.visible"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.minor.visible#rcparam-xtick-minor-visible) ` (default: `False`), `[rcParams["ytick.minor.visible"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.minor.visible#rcparam-ytick-minor-visible) ` (default: `False`) | Default visibility of minor x/y ticks |
| `[rcParams["legend.framealpha"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.framealpha#rcparam-legend-framealpha) ` (default: `0.8`) | Default transparency of the legend frame box |
| `[rcParams["legend.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.facecolor#rcparam-legend-facecolor) ` (default: `'inherit'`) | Default facecolor of legend frame box (or `'inherit'` from `[rcParams["axes.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.facecolor#rcparam-axes-facecolor) ` (default: `'white'`)) |
| `[rcParams["legend.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.edgecolor#rcparam-legend-edgecolor) ` (default: `'0.8'`) | Default edgecolor of legend frame box (or `'inherit'` from `[rcParams["axes.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.edgecolor#rcparam-axes-edgecolor) ` (default: `'black'`)) |
| `[rcParams["figure.titlesize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titlesize#rcparam-figure-titlesize) ` (default: `'large'`) | Default font size for figure suptitles |
| `[rcParams["figure.titleweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titleweight#rcparam-figure-titleweight) ` (default: `'normal'`) | Default font weight for figure suptitles |
| `[rcParams["image.composite_image"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.composite_image#rcparam-image-composite-image) ` (default: `True`) | Whether a vector graphics backend should composite several images into a single image or not when saving. Useful when needing to edit the files further in Inkscape or other programs. |
| `[rcParams["markers.fillstyle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=markers.fillstyle#rcparam-markers-fillstyle) ` (default: `'full'`) | Default fillstyle of markers. Possible values are `'full'` (the default), `'left'`, `'right'`, `'bottom'`, `'top'` and `'none'` |
| `[rcParams["toolbar"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=toolbar#rcparam-toolbar) ` (default: `'toolbar2'`) | Added `'toolmanager'` as a valid value, enabling the experimental `ToolManager` feature. |

[Widgets](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#widgets "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Active state of Selectors[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#active-state-of-selectors "Link to this heading")

All selectors now implement `set_active` and `get_active` methods (also called when accessing the `active` property) to properly update and query whether they are active.

### Moved `ignore`, `set_active`, and `get_active` methods to base class `Widget`[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#moved-ignore-set-active-and-get-active-methods-to-base-class-widget "Link to this heading")

Pushes up duplicate methods in child class to parent class to avoid duplication of code.

### Adds enable/disable feature to MultiCursor[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#adds-enable-disable-feature-to-multicursor "Link to this heading")

A MultiCursor object can be disabled (and enabled) after it has been created without destroying the object. Example:

multi\_cursor.active \= False

### Improved RectangleSelector and new EllipseSelector Widget[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#improved-rectangleselector-and-new-ellipseselector-widget "Link to this heading")

Adds an _interactive_ keyword which enables visible handles for manipulating the shape after it has been drawn.

Adds keyboard modifiers for:

*   Moving the existing shape (default key = 'space')
    
*   Making the shape square (default 'shift')
    
*   Make the initial point the center of the shape (default 'control')
    
*   Square and center can be combined
    

### Allow Artists to Display Pixel Data in Cursor[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#allow-artists-to-display-pixel-data-in-cursor "Link to this heading")

Adds [`get_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_cursor_data.html#matplotlib.artist.Artist.get_cursor_data "matplotlib.artist.Artist.get_cursor_data")
 and [`format_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.format_cursor_data.html#matplotlib.artist.Artist.format_cursor_data "matplotlib.artist.Artist.format_cursor_data")
 methods to artists which can be used to add zdata to the cursor display in the status bar. Also adds an implementation for Images.

[New plotting features](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#new-plotting-features "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Auto-wrapping Text[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#auto-wrapping-text "Link to this heading")

Added the keyword argument "wrap" to Text, which automatically breaks long lines of text when being drawn. Works for any rotated text, different modes of alignment, and for text that are either labels or titles. This breaks at the `Figure`, not `Axes` edge.

([`Source code`](https://matplotlib.org/stable/_downloads/6dcabfecfa7b61bf634018bae523edb5/whats_new_1-5-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/be3b64321459ebb37570c214d47fd539/whats_new_1-5-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/d3877c1333bf10a8671cfe0d0fae6b03/whats_new_1-5-2.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-2.2x.png)

### Contour plot corner masking[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#contour-plot-corner-masking "Link to this heading")

Ian Thomas rewrote the C++ code that calculates contours to add support for corner masking. This is controlled by a new keyword argument `corner_mask` in the functions [`contour()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
 and [`contourf()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
. The previous behaviour, which is now obtained using `corner_mask=False`, was for a single masked point to completely mask out all four quads touching that point. The new behaviour, obtained using `corner_mask=True`, only masks the corners of those quads touching the point; any triangular corners comprising three unmasked points are contoured as usual. If the `corner_mask` keyword argument is not specified, the default value is taken from rcParams.

[![../../_images/sphx_glr_contour_corner_mask_001.png](https://matplotlib.org/stable/_images/sphx_glr_contour_corner_mask_001.png)](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_corner_mask.html)

### Mostly unified linestyles for [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 and [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#mostly-unified-linestyles-for-line2d-patch-and-collection "Link to this heading")

The handling of linestyles for Lines, Patches and Collections has been unified. Now they all support defining linestyles with short symbols, like "--", as well as with full names, like "dashed". Also the definition using a dash pattern (`(0., [3., 3.])`) is supported for all methods using [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 or [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
.

### Legend marker order[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#legend-marker-order "Link to this heading")

Added ability to place the label before the marker in a legend box with `markerfirst` keyword

### Support for legend for PolyCollection and stackplot[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#support-for-legend-for-polycollection-and-stackplot "Link to this heading")

Added a [`legend_handler`](https://matplotlib.org/stable/api/legend_handler_api.html#module-matplotlib.legend_handler "matplotlib.legend_handler")
 for [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 as well as a _labels_ argument to [`stackplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stackplot.html#matplotlib.axes.Axes.stackplot "matplotlib.axes.Axes.stackplot")
.

### Support for alternate pivots in mplot3d quiver plot[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#support-for-alternate-pivots-in-mplot3d-quiver-plot "Link to this heading")

Added a `pivot` kwarg to [`quiver`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.quiver.html#mpl_toolkits.mplot3d.axes3d.Axes3D.quiver "mpl_toolkits.mplot3d.axes3d.Axes3D.quiver")
 that controls the pivot point around which the quiver line rotates. This also determines the placement of the arrow head along the quiver line.

### Logit Scale[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#logit-scale "Link to this heading")

Added support for the 'logit' axis scale, a nonlinear transformation

\\\[x -> \\log10(x / (1-x))\\\]

for data between 0 and 1 excluded.

### Add step kwargs to fill\_between[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#add-step-kwargs-to-fill-between "Link to this heading")

Added `step` kwarg to [`Axes.fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
 to allow to fill between lines drawn using the 'step' draw style. The values of `step` match those of the `where` kwarg of [`Axes.step`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.step.html#matplotlib.axes.Axes.step "matplotlib.axes.Axes.step")
. The asymmetry of the kwargs names is not ideal, but [`Axes.fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
 already has a `where` kwarg.

This is particularly useful for plotting pre-binned histograms.

### Square Plot[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#square-plot "Link to this heading")

Implemented square plots feature as a new parameter in the axis function. When argument 'square' is specified, equal scaling is set, and the limits are set such that `xmax-xmin == ymax-ymin`.

([`Source code`](https://matplotlib.org/stable/_downloads/da734fd400276502ba62e19c0ef7a94e/whats_new_1-5-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/1bf8e839eba110fd983b34c68f75394d/whats_new_1-5-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/bba5ee4b4c1695a35ae8d57aa4d8812d/whats_new_1-5-3.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-3.2x.png)

### Updated figimage to take optional resize parameter[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#updated-figimage-to-take-optional-resize-parameter "Link to this heading")

Added the ability to plot simple 2D-Array using `plt.figimage(X, resize=True)`. This is useful for plotting simple 2D-Array without the Axes or whitespacing around the image.

([`Source code`](https://matplotlib.org/stable/_downloads/4d226a03c7a32e853b5be89cbf6ec7fc/whats_new_1-5-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/e1de8d5c2c27bd6474414ddbb9b0a887/whats_new_1-5-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/b87e916130300394c6ddcf0be5f87190/whats_new_1-5-4.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-4.2x.png)

### Updated Figure.savefig() can now use figure's dpi[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#updated-figure-savefig-can-now-use-figure-s-dpi "Link to this heading")

Added support to save the figure with the same dpi as the figure on the screen using `dpi='figure'`:.

Example:

f \= plt.figure(dpi\=25)  \# dpi set to 25
S \= plt.scatter(\[1,2,3\],\[4,5,6\])
f.savefig('output.png', dpi\='figure')  \# output savefig dpi set to 25 (same as figure)

### Updated Table to control edge visibility[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#updated-table-to-control-edge-visibility "Link to this heading")

Added the ability to toggle the visibility of lines in Tables. Functionality added to the [`pyplot.table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.table.html#matplotlib.pyplot.table "matplotlib.pyplot.table")
 factory function under the keyword argument "edges". Values can be the strings "open", "closed", "horizontal", "vertical" or combinations of the letters "L", "R", "T", "B" which represent left, right, top, and bottom respectively.

Example:

table(..., edges\="open")  \# No line visible
table(..., edges\="closed")  \# All lines visible
table(..., edges\="horizontal")  \# Only top and bottom lines visible
table(..., edges\="LT")  \# Only left and top lines visible.

### Zero r/cstride support in plot\_wireframe[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#zero-r-cstride-support-in-plot-wireframe "Link to this heading")

Adam Hughes added support to mplot3d's plot\_wireframe to draw only row or column line plots.

([`Source code`](https://matplotlib.org/stable/_downloads/9561da76967947caf203032f9fc2bd0d/whats_new_1-5-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/42e5a806754b5f4edd586daeccd0717a/whats_new_1-5-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/eefcc446ed4eff2d90bde7669f37b910/whats_new_1-5-5.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-5.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-5.2x.png)

### Plot bar and barh with labels[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#plot-bar-and-barh-with-labels "Link to this heading")

Added kwarg _tick\_label_ to [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 and [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
 to support plotting bar graphs with a text label for each bar.

([`Source code`](https://matplotlib.org/stable/_downloads/5532ea7d2c6ddcb8ab257b3301d20e47/whats_new_1-5-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/445669bfabe1f8e5dedb52025384dfc5/whats_new_1-5-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/78b826c3054ed469c5a0f3ce09a6da6f/whats_new_1-5-6.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-6.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_1-5-6.2x.png)

### Added center and frame kwargs to pie[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#added-center-and-frame-kwargs-to-pie "Link to this heading")

These control where the center of the pie graph are and if the Axes frame is shown.

### Fixed 3D filled contour plot polygon rendering[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#fixed-3d-filled-contour-plot-polygon-rendering "Link to this heading")

Certain cases of 3D filled contour plots that produce polygons with multiple holes produced improper rendering due to a loss of path information between [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 and [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
. A function [`set_verts_and_codes()`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection.set_verts_and_codes "matplotlib.collections.PolyCollection.set_verts_and_codes")
 was added to allow path information to be retained for proper rendering.

### Dense colorbars are rasterized[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#dense-colorbars-are-rasterized "Link to this heading")

Vector file formats (pdf, ps, svg) are efficient for many types of plot element, but for some they can yield excessive file size and even rendering artifacts, depending on the renderer used for screen display. This is a problem for colorbars that show a large number of shades, as is most commonly the case. Now, if a colorbar is showing 50 or more colors, it will be rasterized in vector backends.

### DateFormatter strftime[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#dateformatter-strftime "Link to this heading")

[`DateFormatter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateFormatter "matplotlib.dates.DateFormatter")
's `__call__` method will format a [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)")
 object with the format string passed to the formatter's constructor. This method accepts datetimes with years before 1900, unlike [`datetime.datetime.strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "(in Python v3.14)")
.

### Artist-level {get,set}\_usetex for text[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#artist-level-get-set-usetex-for-text "Link to this heading")

Add `{get,set}_usetex` methods to [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 objects which allow artist-level control of LaTeX rendering vs. the internal mathtex rendering.

### `Axes.remove()` works as expected[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#axes-remove-works-as-expected "Link to this heading")

As with artists added to an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 objects can be removed from their figure via [`remove()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.remove.html#matplotlib.artist.Artist.remove "matplotlib.artist.Artist.remove")
.

### API Consistency fix within Locators set\_params() function[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#api-consistency-fix-within-locators-set-params-function "Link to this heading")

[`set_params()`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.set_params "matplotlib.ticker.Locator.set_params")
 function, which sets parameters within a [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 type instance, is now available to all [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 types. The implementation also prevents unsafe usage by strictly defining the parameters that a user can set.

To use, call `set_params()` on a [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
 instance with desired arguments:

loc \= matplotlib.ticker.LogLocator()
\# Set given attributes for loc.
loc.set\_params(numticks\=8, numdecs\=8, subs\=\[2.0\], base\=8)
\# The below will error, as there is no such parameter for LogLocator
\# named foo
\# loc.set\_params(foo='bar')

### Date Locators[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#date-locators "Link to this heading")

Date Locators (derived from [`DateLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateLocator "matplotlib.dates.DateLocator")
) now implement the [`tick_values`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator.tick_values "matplotlib.ticker.Locator.tick_values")
 method. This is expected of all Locators derived from [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
.

The Date Locators can now be used easily without creating axes

from datetime import datetime
from matplotlib.dates import YearLocator
t0 \= datetime(2002, 10, 9, 12, 10)
tf \= datetime(2005, 10, 9, 12, 15)
loc \= YearLocator()
values \= loc.tick\_values(t0, tf)

### OffsetBoxes now support clipping[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#offsetboxes-now-support-clipping "Link to this heading")

[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s draw onto objects of type [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
 through [`DrawingArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")
 and [`TextArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")
. The [`TextArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.TextArea "matplotlib.offsetbox.TextArea")
 calculates the required space for the text and so the text is always within the bounds, for this nothing has changed.

However, [`DrawingArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")
 acts as a parent for zero or more [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s that draw on it and may do so beyond the bounds. Now child [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s can be clipped to the bounds of the [`DrawingArea`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DrawingArea "matplotlib.offsetbox.DrawingArea")
.

### OffsetBoxes now considered by tight\_layout[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#offsetboxes-now-considered-by-tight-layout "Link to this heading")

When [`tight_layout()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
 or [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
 or [`GridSpec.tight_layout()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec.tight_layout "matplotlib.gridspec.GridSpec.tight_layout")
 is called, [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
es that are anchored outside the axes will not get chopped out. The [`OffsetBox`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.OffsetBox "matplotlib.offsetbox.OffsetBox")
es will also not get overlapped by other axes in case of multiple subplots.

### Per-page pdf notes in multi-page pdfs (PdfPages)[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#per-page-pdf-notes-in-multi-page-pdfs-pdfpages "Link to this heading")

Add a new method [`attach_note()`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.attach_note "matplotlib.backends.backend_pdf.PdfPages.attach_note")
 to the PdfPages class, allowing the attachment of simple text notes to pages in a multi-page pdf of figures. The new note is visible in the list of pdf annotations in a viewer that has this facility (Adobe Reader, OSX Preview, Skim, etc.). Per default the note itself is kept off-page to prevent it to appear in print-outs.

[`PdfPages.attach_note`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.attach_note "matplotlib.backends.backend_pdf.PdfPages.attach_note")
 needs to be called before [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 in order to be added to the correct figure.

### Updated fignum\_exists to take figure name[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#updated-fignum-exists-to-take-figure-name "Link to this heading")

Added the ability to check the existence of a figure using its name instead of just the figure number. Example:

figure('figure')
fignum\_exists('figure') #true

[ToolManager](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#toolmanager "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Federico Ariza wrote the new [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
 that comes as replacement for [`NavigationToolbar2`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2 "matplotlib.backend_bases.NavigationToolbar2")

[`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
 offers a new way of looking at the user interactions with the figures. Before we had the [`NavigationToolbar2`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2 "matplotlib.backend_bases.NavigationToolbar2")
 with its own tools like `zoom/pan/home/save/...` and also we had the shortcuts like `yscale/grid/quit/....`. [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
 relocate all those actions as Tools (located in [`backend_tools`](https://matplotlib.org/stable/api/backend_tools_api.html#module-matplotlib.backend_tools "matplotlib.backend_tools")
), and defines a way to access/trigger/reconfigure them.

The Toolbars are replaced by [`ToolContainerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase "matplotlib.backend_bases.ToolContainerBase")
s that are just GUI interfaces to trigger the tools. But don't worry the default backends include a [`ToolContainerBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.ToolContainerBase "matplotlib.backend_bases.ToolContainerBase")
 called `toolbar`

Note

At the moment, we release this primarily for feedback purposes and should be treated as experimental until further notice as API changes will occur. For the moment the [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
 works only with the GTK3 and Tk backends. Make sure you use one of those. Port for the rest of the backends is coming soon.

To activate the [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")
 include the following at the top of your file

\>>> matplotlib.rcParams\['toolbar'\] \= 'toolmanager'

### Interact with the ToolContainer[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#interact-with-the-toolcontainer "Link to this heading")

The most important feature is the ability to easily reconfigure the ToolContainer (aka toolbar). For example, if we want to remove the "forward" button we would just do.

\>>> fig.canvas.manager.toolmanager.remove\_tool('forward')

Now if you want to programmatically trigger the "home" button

\>>> fig.canvas.manager.toolmanager.trigger\_tool('home')

### New Tools for ToolManager[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#new-tools-for-toolmanager "Link to this heading")

It is possible to add new tools to the ToolManager

A very simple tool that prints "You're awesome" would be:

from matplotlib.backend\_tools import ToolBase
class AwesomeTool(ToolBase):
    def trigger(self, \*args, \*\*kwargs):
        print("You're awesome")

To add this tool to [`ToolManager`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager "matplotlib.backend_managers.ToolManager")

\>>> fig.canvas.manager.toolmanager.add\_tool('Awesome', AwesomeTool)

If we want to add a shortcut ("d") for the tool

\>>> fig.canvas.manager.toolmanager.update\_keymap('Awesome', 'd')

To add it to the toolbar inside the group 'foo'

\>>> fig.canvas.manager.toolbar.add\_tool('Awesome', 'foo')

There is a second class of tools, "Toggleable Tools", this are almost the same as our basic tools, just that belong to a group, and are mutually exclusive inside that group. For tools derived from [`ToolToggleBase`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase "matplotlib.backend_tools.ToolToggleBase")
 there are two basic methods [`enable`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.enable "matplotlib.backend_tools.ToolToggleBase.enable")
 and [`disable`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolToggleBase.disable "matplotlib.backend_tools.ToolToggleBase.disable")
 that are called automatically whenever it is toggled.

A full example is located in [Tool Manager](https://matplotlib.org/stable/gallery/user_interfaces/toolmanager_sgskip.html)

[cbook.is\_sequence\_of\_strings recognizes string objects](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#cbook-is-sequence-of-strings-recognizes-string-objects "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is primarily how pandas stores a sequence of strings

import pandas as pd
import matplotlib.cbook as cbook

a \= np.array(\['a', 'b', 'c'\])
print(cbook.is\_sequence\_of\_strings(a))  \# True

a \= np.array(\['a', 'b', 'c'\], dtype\=object)
print(cbook.is\_sequence\_of\_strings(a))  \# True

s \= pd.Series(\['a', 'b', 'c'\])
print(cbook.is\_sequence\_of\_strings(s))  \# True

Previously, the last two prints returned false.

[New `close-figs` argument for plot directive](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#new-close-figs-argument-for-plot-directive "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Matplotlib has a sphinx extension `plot_directive` that creates plots for inclusion in sphinx documents. Matplotlib 1.5 adds a new option to the plot directive - `close-figs` - that closes any previous figure windows before creating the plots. This can help avoid some surprising duplicates of plots when using `plot_directive`.

[Support for URL string arguments to `imread`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#support-for-url-string-arguments-to-imread "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`imread()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html#matplotlib.pyplot.imread "matplotlib.pyplot.imread")
 function now accepts URL strings that point to remote PNG files. This circumvents the generation of a HTTPResponse object directly.

[Display hook for animations in the IPython notebook](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#display-hook-for-animations-in-the-ipython-notebook "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`Animation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation "matplotlib.animation.Animation")
 instances gained a `_repr_html_` method to support inline display of animations in the notebook. The method used to display is controlled by the `animation.html` rc parameter, which currently supports values of `none` and `html5`. `none` is the default, performing no display. `html5` converts the animation to an h264 encoded video, which is embedded directly in the notebook.

Users not wishing to use the `_repr_html_` display hook can also manually call the [`to_html5_video`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_html5_video "matplotlib.animation.Animation.to_html5_video")
 method to get the HTML and display using IPython's `HTML` display class:

from IPython.display import HTML
HTML(anim.to\_html5\_video())

[Prefixed pkg-config for building](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#id16)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.5.html#prefixed-pkg-config-for-building "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Handling of pkg-config has been fixed in so far as it is now possible to set it using the environment variable `PKG_CONFIG`. This is important if your toolchain is prefixed. This is done in a simpilar way as setting `CC` or `CXX` before building. An example follows:

export PKG\_CONFIG\=x86\_64\-pc\-linux\-gnu\-pkg\-config

On this page