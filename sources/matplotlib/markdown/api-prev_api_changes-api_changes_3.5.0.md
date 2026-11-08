[Skip to main content](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#main-content)

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
    

API Changes for 3.5.0[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#api-changes-for-3-5-0 "Link to this heading")

=================================================================================================================================================

[Behaviour changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#id1)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#behaviour-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### First argument to `subplot_mosaic` renamed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#first-argument-to-subplot-mosaic-renamed "Link to this heading")

Both [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
, and [`pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 have had the first positional argument renamed from _layout_ to _mosaic_. As we have consolidated the _constrained\_layout_ and _tight\_layout_ keyword arguments in the Figure creation functions of [`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 into a single _layout_ keyword argument, the original `subplot_mosaic` argument name would collide.

As this API is provisional, we are changing this argument name with no deprecation period.

### `Axes` children are no longer separated by type[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#axes-children-are-no-longer-separated-by-type "Link to this heading")

Formerly, [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 children were separated by [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 type, into sublists such as `Axes.lines`. For methods that produced multiple elements (such as [`Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
), though individual parts would have similar _zorder_, this separation might cause them to be drawn at different times, causing inconsistent results when overlapping other Artists.

Now, the children are no longer separated by type, and the sublist properties are generated dynamically when accessed. Consequently, Artists will now always appear in the correct sublist; e.g., if [`axes.Axes.add_line`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_line.html#matplotlib.axes.Axes.add_line "matplotlib.axes.Axes.add_line")
 is called on a [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
, it will appear in the `Axes.patches` sublist, _not_ `Axes.lines`. The `Axes.add_*` methods will now warn if passed an unexpected type.

Modification of the following sublists is still accepted, but deprecated:

*   `Axes.artists`
    
*   `Axes.collections`
    
*   `Axes.images`
    
*   `Axes.lines`
    
*   `Axes.patches`
    
*   `Axes.tables`
    
*   `Axes.texts`
    

To remove an Artist, use its [`Artist.remove`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.remove.html#matplotlib.artist.Artist.remove "matplotlib.artist.Artist.remove")
 method. To add an Artist, use the corresponding `Axes.add_*` method.

### `MatplotlibDeprecationWarning` now subclasses `DeprecationWarning`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#matplotlibdeprecationwarning-now-subclasses-deprecationwarning "Link to this heading")

Historically, it has not been possible to filter [`MatplotlibDeprecationWarning`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.MatplotlibDeprecationWarning "matplotlib.MatplotlibDeprecationWarning")
s by checking for [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "(in Python v3.14)")
, since we subclass [`UserWarning`](https://docs.python.org/3/library/exceptions.html#UserWarning "(in Python v3.14)")
 directly.

The decision to not subclass [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "(in Python v3.14)")
 has to do with a decision from core Python in the 2.x days to not show [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "(in Python v3.14)")
s to users. However, there is now a more sophisticated filter in place (see [https://www.python.org/dev/peps/pep-0565/](https://www.python.org/dev/peps/pep-0565/)
).

Users will now see [`MatplotlibDeprecationWarning`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.MatplotlibDeprecationWarning "matplotlib.MatplotlibDeprecationWarning")
 only during interactive sessions, and these can be silenced by the standard mechanism:

warnings.filterwarnings("ignore", category\=DeprecationWarning)

Library authors must now enable [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "(in Python v3.14)")
s explicitly in order for (non-interactive) CI/CD pipelines to report back these warnings, as is standard for the rest of the Python ecosystem:

warnings.filterwarnings("always", DeprecationWarning)

### `Artist.set` applies artist properties in the order in which they are given[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#artist-set-applies-artist-properties-in-the-order-in-which-they-are-given "Link to this heading")

The change only affects the interaction between the _color_, _edgecolor_, _facecolor_, and (for [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
s) _alpha_ properties: the _color_ property now needs to be passed first in order not to override the other properties. This is consistent with e.g. [`Artist.update`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#matplotlib.artist.Artist.update "matplotlib.artist.Artist.update")
, which did not reorder the properties passed to it.

### `pcolor(mesh)` shading defaults to auto[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#pcolor-mesh-shading-defaults-to-auto "Link to this heading")

The _shading_ keyword argument for [`Axes.pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 and [`Axes.pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 default has been changed to 'auto'.

Passing `Z(M, N)`, `x(N)`, `y(M)` to `pcolormesh` with `shading='flat'` will now raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
. Use `shading='auto'` or `shading='nearest'` for `x` and `y` to be treated as cell centers, or drop the last column and row of `Z` to get the old behaviour with `shading='flat'`.

### Colorbars now have pan and zoom functionality[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#colorbars-now-have-pan-and-zoom-functionality "Link to this heading")

Interactive plots with colorbars can now be zoomed and panned on the colorbar axis. This adjusts the _vmin_ and _vmax_ of the [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 associated with the colorbar. This is currently only enabled for continuous norms. Norms used with `contourf` and categoricals, such as [`BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 and [`NoNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.NoNorm.html#matplotlib.colors.NoNorm "matplotlib.colors.NoNorm")
, have the interactive capability disabled by default. [`cb.ax.set_navigate()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate")
 can be used to set whether a colorbar axes is interactive or not.

### Colorbar lines no longer clipped[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#colorbar-lines-no-longer-clipped "Link to this heading")

If a colorbar has lines added to it (e.g. for contour lines), these will no longer be clipped. This is an improvement for lines on the edge of the colorbar, but could lead to lines off the colorbar if the limits of the colorbar are changed.

### `Figure.suppressComposite` now also controls compositing of Axes images[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#figure-suppresscomposite-now-also-controls-compositing-of-axes-images "Link to this heading")

### The output of `NonUniformImage` and `PcolorImage` has changed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#the-output-of-nonuniformimage-and-pcolorimage-has-changed "Link to this heading")

Pixel-level differences may be observed in images generated using [`NonUniformImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
 or [`PcolorImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.PcolorImage "matplotlib.image.PcolorImage")
, typically for pixels exactly at the boundary between two data cells (no user-facing axes method currently generates [`NonUniformImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "matplotlib.image.NonUniformImage")
s, and only [`pcolorfast`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html#matplotlib.axes.Axes.pcolorfast "matplotlib.axes.Axes.pcolorfast")
 can generate [`PcolorImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.PcolorImage "matplotlib.image.PcolorImage")
s). These artists are also now slower, normally by ~1.5x but sometimes more (in particular for `NonUniformImage(interpolation="bilinear")`. This slowdown arises from fixing occasional floating point inaccuracies.

### Change of the (default) legend handler for `Line2D` instances[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#change-of-the-default-legend-handler-for-line2d-instances "Link to this heading")

The default legend handler for Line2D instances ([`HandlerLine2D`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2D "matplotlib.legend_handler.HandlerLine2D")
) now consistently exposes all the attributes and methods related to the line marker ([#11358](https://github.com/matplotlib/matplotlib/issues/11358/)
). This makes it easy to change the marker features after instantiating a legend.

import matplotlib.pyplot as plt

fig, ax \= plt.subplots()

ax.plot(\[1, 3, 2\], marker\="s", label\="Line", color\="pink", mec\="red", ms\=8)
leg \= ax.legend()

leg.legendHandles\[0\].set\_color("lightgray")
leg.legendHandles\[0\].set\_mec("black")  \# marker edge color

The former legend handler for Line2D objects has been renamed [`HandlerLine2DCompound`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerLine2DCompound "matplotlib.legend_handler.HandlerLine2DCompound")
. To revert to the previous behaviour, one can use

import matplotlib.legend as mlegend
from matplotlib.legend\_handler import HandlerLine2DCompound
from matplotlib.lines import Line2D

mlegend.Legend.update\_default\_handler\_map({Line2D: HandlerLine2DCompound()})

### Setting `Line2D` marker edge/face color to _None_ use rcParams[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#setting-line2d-marker-edge-face-color-to-none-use-rcparams "Link to this heading")

`Line2D.set_markeredgecolor(None)` and `Line2D.set_markerfacecolor(None)` now set the line property using the corresponding rcParam (`[rcParams["lines.markeredgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.markeredgecolor#rcparam-lines-markeredgecolor) ` (default: `'auto'`) and `[rcParams["lines.markerfacecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=lines.markerfacecolor#rcparam-lines-markerfacecolor) ` (default: `'auto'`)). This is consistent with other [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 property setters.

### Default theta tick locations for wedge polar plots have changed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#default-theta-tick-locations-for-wedge-polar-plots-have-changed "Link to this heading")

For polar plots that don't cover a full circle, the default theta tick locations are now at multiples of 10°, 15°, 30°, 45°, 90°, rather than using values that mostly make sense for linear plots (20°, 25°, etc.).

### `axvspan` now plots full wedges in polar plots[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#axvspan-now-plots-full-wedges-in-polar-plots "Link to this heading")

... rather than triangles.

### Convenience converter from `Scale` to `Normalize` now public[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#convenience-converter-from-scale-to-normalize-now-public "Link to this heading")

Downstream libraries can take advantage of [`colors.make_norm_from_scale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.make_norm_from_scale.html#matplotlib.colors.make_norm_from_scale "matplotlib.colors.make_norm_from_scale")
 to create a [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 subclass directly from an existing scale. Usually norms have a scale, and the advantage of having a [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")
 attached to a norm is to provide a scale, and associated tick locators and formatters, for the colorbar.

### `ContourSet` always use `PathCollection`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#contourset-always-use-pathcollection "Link to this heading")

In order to correct rendering issues with closed loops, the [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 now creates a [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 instead of a [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 for line contours. This type matches the artist used for filled contours.

This affects [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
 itself and its subclasses, [`QuadContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.QuadContourSet "matplotlib.contour.QuadContourSet")
 (returned by [`Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
), and [`TriContourSet`](https://matplotlib.org/stable/api/tri_api.html#matplotlib.tri.TriContourSet "matplotlib.tri.TriContourSet")
 (returned by [`Axes.tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour")
).

### `hatch.SmallFilledCircles` inherits from `hatch.Circles`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#hatch-smallfilledcircles-inherits-from-hatch-circles "Link to this heading")

The [`hatch.SmallFilledCircles`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.SmallFilledCircles "matplotlib.hatch.SmallFilledCircles")
 class now inherits from [`hatch.Circles`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.Circles "matplotlib.hatch.Circles")
 rather than from [`hatch.SmallCircles`](https://matplotlib.org/stable/api/hatch_api.html#matplotlib.hatch.SmallCircles "matplotlib.hatch.SmallCircles")
.

### hexbin with a log norm[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#hexbin-with-a-log-norm "Link to this heading")

[`hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")
 no longer (incorrectly) adds 1 to every bin value if a log norm is being used.

### Setting invalid `rcParams["date.converter"]` now raises ValueError[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#setting-invalid-rcparams-date-converter-now-raises-valueerror "Link to this heading")

Previously, invalid values passed to `[rcParams["date.converter"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=date.converter#rcparam-date-converter) ` (default: `'auto'`) would be ignored with a [`UserWarning`](https://docs.python.org/3/library/exceptions.html#UserWarning "(in Python v3.14)")
, but now raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)")
.

### `Text` and `TextBox` added _parse\_math_ option[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#text-and-textbox-added-parse-math-option "Link to this heading")

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 and [`TextBox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox "matplotlib.widgets.TextBox")
 objects now allow a _parse\_math_ keyword-only argument which controls whether math should be parsed from the displayed string. If _True_, the string will be parsed as a math text object. If _False_, the string will be considered a literal and no parsing will occur.

For [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
, this argument defaults to _True_. For [`TextBox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.TextBox.html#matplotlib.widgets.TextBox "matplotlib.widgets.TextBox")
 this argument defaults to _False_.

### `Type1Font` objects now decrypt the encrypted part[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#type1font-objects-now-decrypt-the-encrypted-part "Link to this heading")

Type 1 fonts have a large part of their code encrypted as an obsolete copy-protection measure. This part is now available decrypted as the `decrypted` attribute of `matplotlib.type1font.Type1Font`. This decrypted data is not yet parsed, but this is a prerequisite for implementing subsetting.

### 3D contourf polygons placed between levels[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#d-contourf-polygons-placed-between-levels "Link to this heading")

The polygons used in a 3D [`contourf`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.contourf.html#mpl_toolkits.mplot3d.axes3d.Axes3D.contourf "mpl_toolkits.mplot3d.axes3d.Axes3D.contourf")
 plot are now placed halfway between the contour levels, as each polygon represents the location of values that lie between two levels.

### `AxesDivider` now defaults to rcParams-specified pads[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#axesdivider-now-defaults-to-rcparams-specified-pads "Link to this heading")

[`AxesDivider.append_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes "mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes")
, `AxesDivider.new_horizontal`, and `AxesDivider.new_vertical` now default to paddings specified by `[rcParams["figure.subplot.wspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.wspace#rcparam-figure-subplot-wspace) ` (default: `0.2`) and `[rcParams["figure.subplot.hspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.hspace#rcparam-figure-subplot-hspace) ` (default: `0.2`) rather than zero.

[Deprecations](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#id2)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#deprecations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Discouraged: `Figure` parameters _tight\_layout_ and _constrained\_layout_[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#discouraged-figure-parameters-tight-layout-and-constrained-layout "Link to this heading")

The `Figure` parameters _tight\_layout_ and _constrained\_layout_ are triggering competing layout mechanisms and thus should not be used together.

To make the API clearer, we've merged them under the new parameter _layout_ with values 'constrained' (equal to `constrained_layout=True`), 'tight' (equal to `tight_layout=True`). If given, _layout_ takes precedence.

The use of _tight\_layout_ and _constrained\_layout_ is discouraged in favor of _layout_. However, these parameters will stay available for backward compatibility.

### Modification of `Axes` children sublists[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#modification-of-axes-children-sublists "Link to this heading")

See [Axes children are no longer separated by type](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#behavioural-api-changes-3-5-axes-children-combined)
 for more information; modification of the following sublists is deprecated:

*   `Axes.artists`
    
*   `Axes.collections`
    
*   `Axes.images`
    
*   `Axes.lines`
    
*   `Axes.patches`
    
*   `Axes.tables`
    
*   `Axes.texts`
    

To remove an Artist, use its [`Artist.remove`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.remove.html#matplotlib.artist.Artist.remove "matplotlib.artist.Artist.remove")
 method. To add an Artist, use the corresponding `Axes.add_*` method.

### Passing incorrect types to `Axes.add_*` methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#passing-incorrect-types-to-axes-add-methods "Link to this heading")

The following `Axes.add_*` methods will now warn if passed an unexpected type. See their documentation for the types they expect.

*   [`Axes.add_collection`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection")
    
*   [`Axes.add_image`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_image.html#matplotlib.axes.Axes.add_image "matplotlib.axes.Axes.add_image")
    
*   [`Axes.add_line`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_line.html#matplotlib.axes.Axes.add_line "matplotlib.axes.Axes.add_line")
    
*   [`Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
    
*   [`Axes.add_table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_table.html#matplotlib.axes.Axes.add_table "matplotlib.axes.Axes.add_table")
    

### Discouraged: `plot_date`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#discouraged-plot-date "Link to this heading")

The use of `plot_date` is discouraged. This method exists for historic reasons and may be deprecated in the future.

*   `datetime`\-like data should directly be plotted using [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
    .
    
*   If you need to plot plain numeric data as [Matplotlib date format](https://matplotlib.org/stable/api/dates_api.html#date-format)
     or need to set a timezone, call `ax.xaxis.axis_date` / `ax.yaxis.axis_date` before [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
    . See [`Axis.axis_date`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.axis_date.html#matplotlib.axis.Axis.axis_date "matplotlib.axis.Axis.axis_date")
    .
    

### `epoch2num` and `num2epoch` are deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#epoch2num-and-num2epoch-are-deprecated "Link to this heading")

These methods convert from unix timestamps to matplotlib floats, but are not used internally to matplotlib, and should not be needed by end users. To convert a unix timestamp to datetime, simply use [`datetime.datetime.utcfromtimestamp`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp "(in Python v3.14)")
, or to use NumPy [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "(in NumPy v2.5)")
 `dt = np.datetime64(e*1e6, 'us')`.

### Auto-removal of grids by [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 and [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#auto-removal-of-grids-by-pcolor-and-pcolormesh "Link to this heading")

[`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor")
 and [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh")
 currently remove any visible axes major grid. This behavior is deprecated; please explicitly call `ax.grid(False)` to remove the grid.

### The first parameter of `Axes.grid` and `Axis.grid` has been renamed to _visible_[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#the-first-parameter-of-axes-grid-and-axis-grid-has-been-renamed-to-visible "Link to this heading")

The parameter was previously named _b_. This deprecation only matters if that parameter was passed using a keyword argument, e.g. `grid(b=False)`.

### Unification and cleanup of Selector widget API[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#unification-and-cleanup-of-selector-widget-api "Link to this heading")

The API for Selector widgets has been unified to use:

*   _props_ for the properties of the Artist representing the selection.
    
*   _handle\_props_ for the Artists representing handles for modifying the selection.
    
*   _grab\_range_ for the maximal tolerance to grab a handle with the mouse.
    

Additionally, several internal parameters and attribute have been deprecated with the intention of keeping them private.

#### RectangleSelector and EllipseSelector[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#rectangleselector-and-ellipseselector "Link to this heading")

The _drawtype_ keyword argument to [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")
 is deprecated. In the future the only behaviour will be the default behaviour of `drawtype='box'`.

Support for `drawtype=line` will be removed altogether as it is not clear which points are within and outside a selector that is just a line. As a result, the _lineprops_ keyword argument to [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")
 is also deprecated.

To retain the behaviour of `drawtype='none'`, use `rectprops={'visible': False}` to make the drawn [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 invisible.

Cleaned up attributes and arguments are:

*   The `active_handle` attribute has been privatized and deprecated.
    
*   The `drawtype` attribute has been privatized and deprecated.
    
*   The `eventpress` attribute has been privatized and deprecated.
    
*   The `eventrelease` attribute has been privatized and deprecated.
    
*   The `interactive` attribute has been privatized and deprecated.
    
*   The _marker\_props_ argument is deprecated, use _handle\_props_ instead.
    
*   The _maxdist_ argument is deprecated, use _grab\_range_ instead.
    
*   The _rectprops_ argument is deprecated, use _props_ instead.
    
*   The `rectprops` attribute has been privatized and deprecated.
    
*   The `state` attribute has been privatized and deprecated.
    
*   The `to_draw` attribute has been privatized and deprecated.
    

#### PolygonSelector[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#polygonselector "Link to this heading")

*   The _line_ attribute is deprecated. If you want to change the selector artist properties, use the `set_props` or `set_handle_props` methods.
    
*   The _lineprops_ argument is deprecated, use _props_ instead.
    
*   The _markerprops_ argument is deprecated, use _handle\_props_ instead.
    
*   The _maxdist_ argument and attribute is deprecated, use _grab\_range_ instead.
    
*   The _vertex\_select\_radius_ argument and attribute is deprecated, use _grab\_range_ instead.
    

#### SpanSelector[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#spanselector "Link to this heading")

*   The `active_handle` attribute has been privatized and deprecated.
    
*   The `eventpress` attribute has been privatized and deprecated.
    
*   The `eventrelease` attribute has been privatized and deprecated.
    
*   The _maxdist_ argument and attribute is deprecated, use _grab\_range_ instead.
    
*   The `pressv` attribute has been privatized and deprecated.
    
*   The `prev` attribute has been privatized and deprecated.
    
*   The `rect` attribute has been privatized and deprecated.
    
*   The _rectprops_ argument is deprecated, use _props_ instead.
    
*   The `rectprops` attribute has been privatized and deprecated.
    
*   The _span\_stays_ argument is deprecated, use the _interactive_ argument instead.
    
*   The `span_stays` attribute has been privatized and deprecated.
    
*   The `state` attribute has been privatized and deprecated.
    

#### LassoSelector[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#lassoselector "Link to this heading")

*   The _lineprops_ argument is deprecated, use _props_ instead.
    
*   The `onpress` and `onrelease` methods are deprecated. They are straight aliases for `press` and `release`.
    

### `ConversionInterface.convert` no longer needs to accept unitless values[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#conversioninterface-convert-no-longer-needs-to-accept-unitless-values "Link to this heading")

Previously, custom subclasses of [`units.ConversionInterface`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.ConversionInterface "matplotlib.units.ConversionInterface")
 needed to implement a `convert` method that not only accepted instances of the unit, but also unitless values (which are passed through as is). This is no longer the case (`convert` is never called with a unitless value), and such support in [`StrCategoryConverter`](https://matplotlib.org/stable/api/category_api.html#matplotlib.category.StrCategoryConverter "matplotlib.category.StrCategoryConverter")
 is deprecated. Likewise, the `.ConversionInterface.is_numlike` helper is deprecated.

Consider calling [`Axis.convert_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.convert_units.html#matplotlib.axis.Axis.convert_units "matplotlib.axis.Axis.convert_units")
 instead, which still supports unitless values.

### Locator and Formatter wrapper methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#locator-and-formatter-wrapper-methods "Link to this heading")

The `set_view_interval`, `set_data_interval` and `set_bounds` methods of [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
s and [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
s (and their common base class, TickHelper) are deprecated. Directly manipulate the view and data intervals on the underlying axis instead.

### Unused positional parameters to `print_<fmt>` methods[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#unused-positional-parameters-to-print-fmt-methods "Link to this heading")

None of the `print_<fmt>` methods implemented by canvas subclasses used positional arguments other that the first (the output filename or file-like), so these extra parameters are deprecated.

### `QuadMesh` signature[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#quadmesh-signature "Link to this heading")

The [`QuadMesh`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.QuadMesh "matplotlib.collections.QuadMesh")
 signature

def \_\_init\_\_(meshWidth, meshHeight, coordinates,
             antialiased\=True, shading\='flat', \*\*kwargs)

is deprecated and replaced by the new signature

def \_\_init\_\_(coordinates, \*, antialiased\=True, shading\='flat', \*\*kwargs)

In particular:

*   The _coordinates_ argument must now be a (M, N, 2) array-like. Previously, the grid shape was separately specified as (_meshHeight_ + 1, _meshWidth_ + 1) and _coordinates_ could be an array-like of any shape with M \* N \* 2 elements.
    
*   All parameters except _coordinates_ are keyword-only now.
    

### rcParams will no longer cast inputs to str[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#rcparams-will-no-longer-cast-inputs-to-str "Link to this heading")

After a deprecation period, rcParams that expect a (non-pathlike) str will no longer cast non-str inputs using [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
. This will avoid confusing errors in subsequent code if e.g. a list input gets implicitly cast to a str.

### Case-insensitive scales[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#case-insensitive-scales "Link to this heading")

Previously, scales could be set case-insensitively (e.g., `set_xscale("LoG")`). This is deprecated; all builtin scales use lowercase names.

### Interactive cursor details[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#interactive-cursor-details "Link to this heading")

Setting a mouse cursor on a window has been moved from the toolbar to the canvas. Consequently, several implementation details on toolbars and within backends have been deprecated.

#### `NavigationToolbar2.set_cursor` and `backend_tools.SetCursorBase.set_cursor`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#navigationtoolbar2-set-cursor-and-backend-tools-setcursorbase-set-cursor "Link to this heading")

Instead, use the [`FigureCanvasBase.set_cursor`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.set_cursor "matplotlib.backend_bases.FigureCanvasBase.set_cursor")
 method on the canvas (available as the `canvas` attribute on the toolbar or the Figure.)

#### `backend_tools.SetCursorBase` and subclasses[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#backend-tools-setcursorbase-and-subclasses "Link to this heading")

`backend_tools.SetCursorBase` was subclassed to provide backend-specific implementations of `set_cursor`. As that is now deprecated, the subclassing is no longer necessary. Consequently, the following subclasses are also deprecated:

*   `matplotlib.backends.backend_gtk3.SetCursorGTK3`
    
*   `matplotlib.backends.backend_qt5.SetCursorQt`
    
*   `matplotlib.backends._backend_tk.SetCursorTk`
    
*   `matplotlib.backends.backend_wx.SetCursorWx`
    

Instead, use the [`backend_tools.ToolSetCursor`](https://matplotlib.org/stable/api/backend_tools_api.html#matplotlib.backend_tools.ToolSetCursor "matplotlib.backend_tools.ToolSetCursor")
 class.

#### `cursord` in GTK, Qt, and wx backends[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#cursord-in-gtk-qt-and-wx-backends "Link to this heading")

The `backend_gtk3.cursord`, `backend_qt.cursord`, and `backend_wx.cursord` dictionaries are deprecated. This makes the GTK module importable on headless environments.

### Miscellaneous deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#miscellaneous-deprecations "Link to this heading")

*   `is_url` and `URL_REGEX` are deprecated. (They were previously defined in the toplevel [`matplotlib`](https://matplotlib.org/stable/index.html#module-matplotlib "matplotlib")
     module.)
    
*   The `ArrowStyle.beginarrow` and `ArrowStyle.endarrow` attributes are deprecated; use the `arrow` attribute to define the desired heads and tails of the arrow.
    
*   `backend_pgf.LatexManager.str_cache` is deprecated.
    
*   `backends.qt_compat.ETS` and `backends.qt_compat.QT_RC_MAJOR_VERSION` are deprecated, with no replacement.
    
*   The `blocking_input` module has been deprecated. Instead, use `canvas.start_event_loop()` and `canvas.stop_event_loop()` while connecting event callbacks as needed.
    
*   `cbook.report_memory` is deprecated; use `psutil.virtual_memory` instead.
    
*   `cm.LUTSIZE` is deprecated. Use `[rcParams["image.lut"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.lut#rcparam-image-lut) ` (default: `256`) instead. This value only affects colormap quantization levels for default colormaps generated at module import time.
    
*   `Collection.__init__` previously ignored _transOffset_ without _offsets_ also being specified. In the future, _transOffset_ will begin having an effect regardless of _offsets_. In the meantime, if you wish to set _transOffset_, call [`Collection.set_offset_transform`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection.set_offset_transform "matplotlib.collections.Collection.set_offset_transform")
     explicitly.
    
*   `Colorbar.patch` is deprecated; this attribute is not correctly updated anymore.
    
*   `ContourLabeler.get_label_width` is deprecated.
    
*   `dviread.PsfontsMap` now raises LookupError instead of KeyError for missing fonts.
    
*   `Dvi.baseline` is deprecated (with no replacement).
    
*   The _format_ parameter of `dviread.find_tex_file` is deprecated (with no replacement).
    
*   `FancyArrowPatch.get_path_in_displaycoord` and `ConnectionPatch.get_path_in_displaycoord` are deprecated. The path in display coordinates can still be obtained, as for other patches, using `patch.get_transform().transform_path(patch.get_path())`.
    
*   The `font_manager.win32InstalledFonts` and `font_manager.get_fontconfig_fonts` helper functions have been deprecated.
    
*   All parameters of `imshow` starting from _aspect_ will become keyword-only.
    
*   `QuadMesh.convert_mesh_to_paths` and `QuadMesh.convert_mesh_to_triangles` are deprecated. `QuadMesh.get_paths()` can be used as an alternative for the former; there is no replacement for the latter.
    
*   `ScalarMappable.callbacksSM` is deprecated. Use `ScalarMappable.callbacks` instead.
    
*   `streamplot.get_integrator` is deprecated.
    
*   `style.core.STYLE_FILE_PATTERN`, `style.core.load_base_library`, and `style.core.iter_user_libraries` are deprecated.
    
*   `SubplotParams.validate` is deprecated. Use [`SubplotParams.update`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams.update "matplotlib.gridspec.SubplotParams.update")
     to change [`SubplotParams`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams "matplotlib.gridspec.SubplotParams")
     while always keeping it in a valid state.
    
*   The `grey_arrayd`, `font_family`, `font_families`, and `font_info` attributes of [`TexManager`](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager "matplotlib.texmanager.TexManager")
     are deprecated.
    
*   `Text.get_prop_tup` is deprecated with no replacements (because the [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
     class cannot know whether a backend needs to update cache e.g. when the text's color changes).
    
*   `Tick.apply_tickdir` didn't actually update the tick markers on the existing Line2D objects used to draw the ticks and is deprecated; use [`Axis.set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
     instead.
    
*   `tight_layout.auto_adjust_subplotpars` is deprecated.
    
*   The `grid_info` attribute of `axisartist` classes has been deprecated.
    
*   `axisartist.clip_path` is deprecated with no replacement.
    
*   `axes_grid1.axes_grid.CbarAxes` and `axes_grid1.axisartist.CbarAxes` are deprecated (they are now dynamically generated based on the owning axes class).
    
*   The `axes_grid1.Divider.get_vsize_hsize` and `axes_grid1.Grid.get_vsize_hsize` methods are deprecated. Copy their implementations if needed.
    
*   `AxesDivider.append_axes(..., add_to_figure=False)` is deprecated. Use `ax.remove()` to remove the Axes from the figure if needed.
    
*   `FixedAxisArtistHelper.change_tick_coord` is deprecated with no replacement.
    
*   `floating_axes.GridHelperCurveLinear.get_boundary` is deprecated, with no replacement.
    
*   `ParasiteAxesBase.get_images_artists` has been deprecated.
    
*   The "units finalize" signal (previously emitted by Axis instances) is deprecated. Connect to "units" instead.
    
*   Passing formatting parameters positionally to `stem()` is deprecated
    

### `plot_directive` deprecations[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#plot-directive-deprecations "Link to this heading")

The `:encoding:` option to `.. plot` directive has had no effect since Matplotlib 1.3.1, and is now deprecated.

The following helpers in [`matplotlib.sphinxext.plot_directive`](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#module-matplotlib.sphinxext.plot_directive "matplotlib.sphinxext.plot_directive")
 are deprecated:

*   `unescape_doctest` (use [`doctest.script_from_examples`](https://docs.python.org/3/library/doctest.html#doctest.script_from_examples "(in Python v3.14)")
     instead),
    
*   `split_code_at_show`,
    
*   `run_code`.
    

### Testing support[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#testing-support "Link to this heading")

#### `matplotlib.test()` is deprecated[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#matplotlib-test-is-deprecated "Link to this heading")

Run tests using `pytest` from the commandline instead. The variable `matplotlib.default_test_modules` is only used for `matplotlib.test()` and is thus deprecated as well.

To test an installed copy, be sure to specify both `matplotlib` and `mpl_toolkits` with `--pyargs`:

pytest \--pyargs matplotlib.tests mpl\_toolkits.tests

See [Testing](https://matplotlib.org/stable/devel/testing.html#testing)
 for more details.

#### Unused pytest fixtures and markers[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#unused-pytest-fixtures-and-markers "Link to this heading")

The fixture `matplotlib.testing.conftest.mpl_image_comparison_parameters` is not used internally by Matplotlib. If you use this please copy it into your code base.

The `@pytest.mark.style` marker is deprecated; use `@mpl.style.context`, which has the same effect.

### Support for `nx1 = None` or `ny1 = None` in `AxesLocator` and `Divider.locate`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#support-for-nx1-none-or-ny1-none-in-axeslocator-and-divider-locate "Link to this heading")

In [`axes_grid1.axes_divider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.html#module-mpl_toolkits.axes_grid1.axes_divider "mpl_toolkits.axes_grid1.axes_divider")
, various internal APIs will stop supporting passing `nx1 = None` or `ny1 = None` to mean `nx + 1` or `ny + 1`, in preparation for a possible future API which allows indexing and slicing of dividers (possibly `divider[a:b] == divider.new_locator(a, b)`, but also `divider[a:] == divider.new_locator(a, <end>)`). The user-facing [`Divider.new_locator`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator "mpl_toolkits.axes_grid1.axes_divider.Divider.new_locator")
 API is unaffected -- it correctly normalizes `nx1 = None` and `ny1 = None` as needed.

[Removals](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#id3)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#removals "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following deprecated APIs have been removed:

### Removed behaviour[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#removed-behaviour "Link to this heading")

#### Stricter validation of function parameters[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#stricter-validation-of-function-parameters "Link to this heading")

*   Calling [`Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
     with no arguments will raise an error. Adding a free-floating axes needs a position rectangle. If you want a figure-filling single axes, use [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
     instead.
    
*   [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
     validates its inputs; in particular, for `add_subplot(rows, cols, index)`, all parameters must be integral. Previously strings and floats were accepted and converted to int.
    
*   Passing _None_ as the _which_ argument to `autofmt_xdate` is no longer supported; use its more explicit synonym, `which="major"`, instead.
    
*   Setting the _orientation_ of an `eventplot()` or [`EventCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.EventCollection "matplotlib.collections.EventCollection")
     to "none" or _None_ is no longer supported; set it to "horizontal" instead. Moreover, the two orientations ("horizontal" and "vertical") are now case-sensitive.
    
*   Passing parameters _norm_ and _vmin_/_vmax_ simultaneously to functions using colormapping such as `scatter()` and `imshow()` is no longer supported. Instead of `norm=LogNorm(), vmin=min_val, vmax=max_val` pass `norm=LogNorm(min_val, max_val)`. _vmin_ and _vmax_ should only be used without setting _norm_.
    
*   Passing _None_ as either the _radius_ or _startangle_ arguments of an [`Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
     is no longer accepted; use the explicit defaults of 1 and 0, respectively, instead.
    
*   Passing _None_ as the _normalize_ argument of [`Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
     (the former default) is no longer accepted, and the pie will always be normalized by default. If you wish to plot an incomplete pie, explicitly pass `normalize=False`.
    
*   Support for passing _None_ to `subplot_class_factory` has been removed. Explicitly pass in the base [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
     class instead.
    
*   Passing multiple keys as a single comma-separated string or multiple arguments to [`ToolManager.update_keymap`](https://matplotlib.org/stable/api/backend_managers_api.html#matplotlib.backend_managers.ToolManager.update_keymap "matplotlib.backend_managers.ToolManager.update_keymap")
     is no longer supported; pass keys as a list of strings instead.
    
*   Passing the dash offset as _None_ is no longer accepted, as this was never universally implemented, e.g. for vector output. Set the offset to 0 instead.
    
*   Setting a custom method overriding [`Artist.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.contains.html#matplotlib.artist.Artist.contains "matplotlib.artist.Artist.contains")
     using `Artist.set_contains` has been removed, as has `Artist.get_contains`. There is no replacement, but you may still customize pick events using [`Artist.set_picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker")
    .
    
*   [`semilogx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogx.html#matplotlib.axes.Axes.semilogx "matplotlib.axes.Axes.semilogx")
    , [`semilogy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogy.html#matplotlib.axes.Axes.semilogy "matplotlib.axes.Axes.semilogy")
    , [`loglog`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.loglog.html#matplotlib.axes.Axes.loglog "matplotlib.axes.Axes.loglog")
    , [`LogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale "matplotlib.scale.LogScale")
    , and [`SymmetricalLogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogScale "matplotlib.scale.SymmetricalLogScale")
     used to take keyword arguments that depends on the axis orientation ("basex" vs "basey", "subsx" vs "subsy", "nonposx" vs "nonposy"); these parameter names have been removed in favor of "base", "subs", "nonpositive". This removal also affects e.g. `ax.set_yscale("log", basey=...)` which must now be spelled `ax.set_yscale("log", base=...)`.
    
    The change from "nonpos" to "nonpositive" also affects [`LogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogTransform "matplotlib.scale.LogTransform")
    , [`InvertedLogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.InvertedLogTransform "matplotlib.scale.InvertedLogTransform")
    , [`SymmetricalLogTransform`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.SymmetricalLogTransform "matplotlib.scale.SymmetricalLogTransform")
    , etc.
    
    To use _different_ bases for the x-axis and y-axis of a [`loglog`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.loglog.html#matplotlib.axes.Axes.loglog "matplotlib.axes.Axes.loglog")
     plot, use e.g. `ax.set_xscale("log", base=10); ax.set_yscale("log", base=2)`.
    
*   Passing _None_, or no argument, to `parasite_axes_class_factory`, `parasite_axes_auxtrans_class_factory`, `host_axes_class_factory` is no longer accepted; pass an explicit base class instead.
    

#### Case-sensitivity is now enforced more[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#case-sensitivity-is-now-enforced-more "Link to this heading")

*   Upper or mixed-case property names are no longer normalized to lowercase in [`Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
     and [`Artist.update`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.update.html#matplotlib.artist.Artist.update "matplotlib.artist.Artist.update")
    . This allows one to pass names such as _patchA_ or _UVC_.
    
*   Case-insensitive capstyles and joinstyles are no longer lower-cased; please pass capstyles ("miter", "round", "bevel") and joinstyles ("butt", "round", "projecting") as lowercase.
    
*   Saving metadata in PDF with the PGF backend no longer changes keys to lowercase. Only the canonically cased keys listed in the PDF specification (and the [`PdfPages`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.PdfPages "matplotlib.backends.backend_pgf.PdfPages")
     documentation) are accepted.
    

#### No implicit initialization of `Tick` attributes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#no-implicit-initialization-of-tick-attributes "Link to this heading")

The [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")
 constructor no longer initializes the attributes `tick1line`, `tick2line`, `gridline`, `label1`, and `label2` via `_get_tick1line`, `_get_tick2line`, `_get_gridline`, `_get_text1`, and `_get_text2`. Please directly set the attribute in the subclass' `__init__` instead.

#### `NavigationToolbar2` subclass changes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#navigationtoolbar2-subclass-changes "Link to this heading")

Overriding the `_init_toolbar` method of [`NavigationToolbar2`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2 "matplotlib.backend_bases.NavigationToolbar2")
 to initialize third-party toolbars is no longer supported. Instead, the toolbar should be initialized in the `__init__` method of the subclass (which should call the base-class' `__init__` as appropriate).

The `press` and `release` methods of [`NavigationToolbar2`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.NavigationToolbar2 "matplotlib.backend_bases.NavigationToolbar2")
 were called when pressing or releasing a mouse button, but _only_ when an interactive pan or zoom was occurring (contrary to what the docs stated). They are no longer called; if you write a backend which needs to customize such events, please directly override `press_pan`/`press_zoom`/`release_pan`/`release_zoom` instead.

#### Removal of old file mode flag[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#removal-of-old-file-mode-flag "Link to this heading")

Flags containing "U" passed to [`cbook.to_filehandle`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.to_filehandle "matplotlib.cbook.to_filehandle")
 and [`cbook.open_file_cm`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.open_file_cm "matplotlib.cbook.open_file_cm")
 are no longer accepted. This is consistent with their removal from [`open`](https://docs.python.org/3/library/functions.html#open "(in Python v3.14)")
 in Python 3.9.

#### Keymaps toggling `Axes.get_navigate` have been removed[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#keymaps-toggling-axes-get-navigate-have-been-removed "Link to this heading")

This includes numeric key events and rcParams.

#### The `TTFPATH` and `AFMPATH` environment variables[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#the-ttfpath-and-afmpath-environment-variables "Link to this heading")

Support for the (undocumented) `TTFPATH` and `AFMPATH` environment variables has been removed. Register additional fonts using `matplotlib.font_manager.fontManager.addfont()`.

### Modules[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#modules "Link to this heading")

*   `matplotlib.backends.qt_editor.formsubplottool`; use `matplotlib.backends.backend_qt.SubplotToolQt` instead.
    
*   `matplotlib.compat`
    
*   `matplotlib.ttconv`
    
*   The Qt4-based backends, `qt4agg` and `qt4cairo`, have been removed. Qt4 has reached its end-of-life in 2015 and there are no releases of either PyQt4 or PySide for recent versions of Python. Please use one of the Qt5 or Qt6 backends.
    

### Classes, methods and attributes[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#classes-methods-and-attributes "Link to this heading")

The following module-level classes/variables have been removed:

*   `backend_bases.StatusbarBase` and all its subclasses, and `StatusBarWx`; messages are displayed in the toolbar
    
*   `backend_pgf.GraphicsContextPgf`
    
*   `MODIFIER_KEYS`, `SUPER`, `ALT`, `CTRL`, and `SHIFT` of [`matplotlib.backends.backend_qt5agg`](https://matplotlib.org/stable/api/backend_qt_api.html#module-matplotlib.backends.backend_qt5agg "matplotlib.backends.backend_qt5agg")
     and [`matplotlib.backends.backend_qt5cairo`](https://matplotlib.org/stable/api/backend_qt_api.html#module-matplotlib.backends.backend_qt5cairo "matplotlib.backends.backend_qt5cairo")
    
*   `backend_wx.DEBUG_MSG`
    
*   `dviread.Encoding`
    
*   `Fil`, `Fill`, `Filll`, `NegFil`, `NegFill`, `NegFilll`, and `SsGlue` from [`mathtext`](https://matplotlib.org/stable/api/mathtext_api.html#module-matplotlib.mathtext "matplotlib.mathtext")
    ; directly construct glue instances with `Glue("fil")`, etc.
    
*   `mathtext.GlueSpec`
    
*   `OldScalarFormatter`, `IndexFormatter` and `IndexDateFormatter`; use [`FuncFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FuncFormatter "matplotlib.ticker.FuncFormatter")
     instead
    
*   `OldAutoLocator`
    
*   `AVConvBase`, `AVConvWriter` and `AVConvFileWriter`. Debian 8 (2015, EOL 06/2020) and Ubuntu 14.04 (EOL 04/2019) were the last versions of Debian and Ubuntu to ship avconv. It remains possible to force the use of avconv by using the FFmpeg-based writers with `[rcParams["animation.ffmpeg_path"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.ffmpeg_path#rcparam-animation-ffmpeg-path) ` (default: `'ffmpeg'`) set to "avconv".
    
*   `matplotlib.axes._subplots._subplot_classes`
    
*   `axes_grid1.axes_rgb.RGBAxesBase`; use `RGBAxes` instead
    

The following class attributes have been removed:

*   `backend_pgf.LatexManager.latex_stdin_utf8`
    
*   `backend_pgf.PdfPages.metadata`
    
*   `ContourSet.ax` and `Quiver.ax`; use `ContourSet.axes` or `Quiver.axes` as with other artists
    
*   `DateFormatter.illegal_s`
    
*   `dates.YearLocator.replaced`; [`YearLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.YearLocator "matplotlib.dates.YearLocator")
     is now a subclass of [`RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")
    , and the attribute `YearLocator.replaced` has been removed. For tick locations that required modifying this, a custom rrule and [`RRuleLocator`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.RRuleLocator "matplotlib.dates.RRuleLocator")
     can be used instead.
    
*   `FigureManagerBase.statusbar`; messages are displayed in the toolbar
    
*   `FileMovieWriter.clear_temp`
    
*   `mathtext.Glue.glue_subtype`
    
*   `MovieWriter.args_key`, `MovieWriter.exec_key`, and `HTMLWriter.args_key`
    
*   `NavigationToolbar2QT.basedir`; the base directory to the icons is `os.path.join(mpl.get_data_path(), "images")`
    
*   `NavigationToolbar2QT.ctx`
    
*   `NavigationToolbar2QT.parent`; to access the parent window, use `toolbar.canvas.parent()` or `toolbar.parent()`
    
*   `prevZoomRect`, `retinaFix`, `savedRetinaImage`, `wxoverlay`, `zoomAxes`, `zoomStartX`, and `zoomStartY` attributes of `NavigationToolbar2Wx`
    
*   `NonUniformImage.is_grayscale`, `PcolorImage.is_grayscale`, for consistency with `AxesImage.is_grayscale`. (Note that previously, these attributes were only available _after rendering the image_).
    
*   `RendererCairo.fontweights`, `RendererCairo.fontangles`
    
*   `used_characters` of [`RendererPdf`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf "matplotlib.backends.backend_pdf.RendererPdf")
    , [`PdfFile`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile "matplotlib.backends.backend_pdf.PdfFile")
    , and [`RendererPS`](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS "matplotlib.backends.backend_ps.RendererPS")
    
*   `LogScale.LogTransform`, `LogScale.InvertedLogTransform`, `SymmetricalScale.SymmetricalTransform`, and `SymmetricalScale.InvertedSymmetricalTransform`; directly access the transform classes from [`matplotlib.scale`](https://matplotlib.org/stable/api/scale_api.html#module-matplotlib.scale "matplotlib.scale")
    
*   `cachedir`, `rgba_arrayd`, `serif`, `sans_serif`, `cursive`, and `monospace` attributes of [`TexManager`](https://matplotlib.org/stable/api/texmanager_api.html#matplotlib.texmanager.TexManager "matplotlib.texmanager.TexManager")
    
*   `axleft`, `axright`, `axbottom`, `axtop`, `axwspace`, and `axhspace` attributes of [`widgets.SubplotTool`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SubplotTool.html#matplotlib.widgets.SubplotTool "matplotlib.widgets.SubplotTool")
    ; access the `ax` attribute of the corresponding slider
    
*   `widgets.TextBox.params_to_disable`
    
*   `angle_helper.LocatorBase.den`; it has been renamed to _nbins_
    
*   `axes_grid.CbarAxesBase.cbid` and `axes_grid.CbarAxesBase.locator`; use `mappable.colorbar_cid` or `colorbar.locator` instead
    

The following class methods have been removed:

*   `Axes.update_datalim_bounds`; use `ax.dataLim.set(Bbox.union([ax.dataLim, bounds]))`
    
*   `pan` and `zoom` methods of [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
     and [`Locator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Locator "matplotlib.ticker.Locator")
     have been removed; panning and zooming are now implemented using the `start_pan`, `drag_pan`, and `end_pan` methods of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
    
*   `.BboxBase.inverse_transformed`; call [`BboxBase.transformed`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase.transformed "matplotlib.transforms.BboxBase.transformed")
     on the [`inverted()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.inverted "matplotlib.transforms.Transform.inverted")
     transform
    
*   `Collection.set_offset_position` and `Collection.get_offset_position` have been removed; the `offset_position` of the [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
     class is now "screen"
    
*   `Colorbar.on_mappable_changed` and `Colorbar.update_bruteforce`; use `Colorbar.update_normal()` instead
    
*   `docstring.Substitution.from_params` has been removed; directly assign to `params` of `docstring.Substitution` instead
    
*   `DraggableBase.artist_picker`; set the artist's picker instead
    
*   `DraggableBase.on_motion_blit`; use [`DraggableBase.on_motion`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.DraggableBase.on_motion "matplotlib.offsetbox.DraggableBase.on_motion")
     instead
    
*   `FigureCanvasGTK3._renderer_init`
    
*   `Locator.refresh()` and the associated helper methods `NavigationToolbar2.draw()` and `ToolViewsPositions.refresh_locators()`
    
*   `track_characters` and `merge_used_characters` of [`RendererPdf`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.RendererPdf "matplotlib.backends.backend_pdf.RendererPdf")
    , [`PdfFile`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile "matplotlib.backends.backend_pdf.PdfFile")
    , and [`RendererPS`](https://matplotlib.org/stable/api/backend_ps_api.html#matplotlib.backends.backend_ps.RendererPS "matplotlib.backends.backend_ps.RendererPS")
    
*   `RendererWx.get_gc`
    
*   `SubplotSpec.get_rows_columns`; use the `GridSpec.nrows`, `GridSpec.ncols`, `SubplotSpec.rowspan`, and `SubplotSpec.colspan` properties instead.
    
*   `ScalarMappable.update_dict`, `ScalarMappable.add_checker()`, and `ScalarMappable.check_update()`; register a callback in `ScalarMappable.callbacks` to be notified of updates
    
*   `TexManager.make_tex_preview` and `TexManager.make_dvi_preview`
    
*   `funcleft`, `funcright`, `funcbottom`, `functop`, `funcwspace`, and `funchspace` methods of [`widgets.SubplotTool`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SubplotTool.html#matplotlib.widgets.SubplotTool "matplotlib.widgets.SubplotTool")
    
*   `axes_grid1.axes_rgb.RGBAxes.add_RGB_to_figure`
    
*   `axisartist.axis_artist.AxisArtist.dpi_transform`
    
*   `axisartist.grid_finder.MaxNLocator.set_factor` and `axisartist.grid_finder.FixedLocator.set_factor`; the factor is always 1 now
    

### Functions[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#functions "Link to this heading")

*   `bezier.make_path_regular` has been removed; use `Path.cleaned()` (or `Path.cleaned(curves=True)`, etc.) instead, but note that these methods add a `STOP` code at the end of the path.
    
*   `bezier.concatenate_paths` has been removed; use `Path.make_compound_path()` instead.
    
*   `cbook.local_over_kwdict` has been removed; use [`cbook.normalize_kwargs`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.normalize_kwargs "matplotlib.cbook.normalize_kwargs")
     instead.
    
*   `qt_compat.is_pyqt5` has been removed due to the release of PyQt6. The Qt version can be checked using `QtCore.qVersion()`.
    
*   `testing.compare.make_external_conversion_command` has been removed.
    
*   `axes_grid1.axes_rgb.imshow_rgb` has been removed; use `imshow(np.dstack([r, g, b]))` instead.
    

### Arguments[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#arguments "Link to this heading")

*   The _s_ parameter to [`Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
     and [`pyplot.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")
     is no longer supported; use the new name _text_.
    
*   The _inframe_ parameter to [`matplotlib.axes.Axes.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw.html#matplotlib.axes.Axes.draw "matplotlib.axes.Axes.draw")
     has been removed; use [`Axes.redraw_in_frame`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.redraw_in_frame.html#matplotlib.axes.Axes.redraw_in_frame "matplotlib.axes.Axes.redraw_in_frame")
     instead.
    
*   The _required_, _forbidden_ and _allowed_ parameters of [`cbook.normalize_kwargs`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.normalize_kwargs "matplotlib.cbook.normalize_kwargs")
     have been removed.
    
*   The _ismath_ parameter of the `draw_tex` method of all renderer classes has been removed (as a call to `draw_tex` — not to be confused with `draw_text`! — means that the entire string should be passed to the `usetex` machinery anyways). Likewise, the text machinery will no longer pass the _ismath_ parameter when calling `draw_tex` (this should only matter for backend implementers).
    
*   The _quality_, _optimize_, and _progressive_ parameters of [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
     (which only affected JPEG output) have been removed, as well as from the corresponding `print_jpg` methods. JPEG output options can be set by directly passing the relevant parameters in _pil\_kwargs_.
    
*   The _clear\_temp_ parameter of [`FileMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter "matplotlib.animation.FileMovieWriter")
     has been removed; files placed in a temporary directory (using `frame_prefix=None`, the default) will be cleared; files placed elsewhere will not.
    
*   The _copy_ parameter of `mathtext.Glue` has been removed.
    
*   The _quantize_ parameter of [`Path.cleaned()`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.cleaned "matplotlib.path.Path.cleaned")
     has been removed.
    
*   The _dummy_ parameter of [`RendererPgf`](https://matplotlib.org/stable/api/backend_pgf_api.html#matplotlib.backends.backend_pgf.RendererPgf "matplotlib.backends.backend_pgf.RendererPgf")
     has been removed.
    
*   The _props_ parameter of [`Shadow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
     has been removed; use keyword arguments instead.
    
*   The _recursionlimit_ parameter of `matplotlib.test` has been removed.
    
*   The _label_ parameter of [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")
     has no effect and has been removed.
    
*   [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")
     no longer accepts a positional parameter and the keyword argument _nbins_ simultaneously because they specify the same quantity.
    
*   The _add\_all_ parameter to `axes_grid.Grid`, `axes_grid.ImageGrid`, `axes_rgb.make_rgb_axes`, and `axes_rgb.RGBAxes` have been removed; the APIs always behave as if `add_all=True`.
    
*   The _den_ parameter of `axisartist.angle_helper.LocatorBase` has been removed; use _nbins_ instead.
    
*   The _s_ keyword argument to [`AnnotationBbox.get_fontsize`](https://matplotlib.org/stable/api/offsetbox_api.html#matplotlib.offsetbox.AnnotationBbox.get_fontsize "matplotlib.offsetbox.AnnotationBbox.get_fontsize")
     has no effect and has been removed.
    
*   The _offset\_position_ keyword argument of the [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
     class has been removed; the `offset_position` now "screen".
    
*   Arbitrary keyword arguments to `StreamplotSet` have no effect and have been removed.
    
*   The _fontdict_ and _minor_ parameters of [`Axes.set_xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels")
     / [`Axes.set_yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels")
     are now keyword-only.
    
*   All parameters of [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
     except _nrows_ and _ncols_ are now keyword-only; this avoids typing e.g. `subplots(1, 1, 1)` when meaning `subplot(1, 1, 1)`, but actually getting `subplots(1, 1, sharex=1)`.
    
*   All parameters of [`pyplot.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")
     are now keyword-only, to be consistent with [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
    .
    
*   `ColorbarBase` only takes a single positional argument now, the `Axes` to create it in, with all other options required to be keyword arguments. The warning for keyword arguments that were overridden by the mappable is now removed.
    
*   Omitting the _renderer_ parameter to [`matplotlib.axes.Axes.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw.html#matplotlib.axes.Axes.draw "matplotlib.axes.Axes.draw")
     is no longer supported; use `axes.draw_artist(axes)` instead.
    
*   Passing `ismath="TeX!"` to [`RendererAgg.get_text_width_height_descent`](https://matplotlib.org/stable/api/backend_agg_api.html#matplotlib.backends.backend_agg.RendererAgg.get_text_width_height_descent "matplotlib.backends.backend_agg.RendererAgg.get_text_width_height_descent")
     is no longer supported; pass `ismath="TeX"` instead,
    
*   Changes to the signature of the [`matplotlib.axes.Axes.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw.html#matplotlib.axes.Axes.draw "matplotlib.axes.Axes.draw")
     method make it consistent with all other artists; thus additional parameters to [`Artist.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.draw.html#matplotlib.artist.Artist.draw "matplotlib.artist.Artist.draw")
     have also been removed.
    

### rcParams[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#rcparams "Link to this heading")

*   The `animation.avconv_path` and `animation.avconv_args` rcParams have been removed.
    
*   The `animation.html_args` rcParam has been removed.
    
*   The `keymap.all_axes` rcParam has been removed.
    
*   The `mathtext.fallback_to_cm` rcParam has been removed. Use `[rcParams["mathtext.fallback"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=mathtext.fallback#rcparam-mathtext-fallback) ` (default: `'cm'`) instead.
    
*   The `savefig.jpeg_quality` rcParam has been removed.
    
*   The `text.latex.preview` rcParam has been removed.
    
*   The following deprecated rcParams validators, defined in [`rcsetup`](https://matplotlib.org/stable/api/rcsetup_api.html#module-matplotlib.rcsetup "matplotlib.rcsetup")
    , have been removed:
    
    *   `validate_alignment`
        
    *   `validate_axes_titlelocation`
        
    *   `validate_axis_locator`
        
    *   `validate_bool_maybe_none`
        
    *   `validate_fontset`
        
    *   `validate_grid_axis`
        
    *   `validate_hinting`
        
    *   `validate_legend_loc`
        
    *   `validate_mathtext_default`
        
    *   `validate_movie_frame_fmt`
        
    *   `validate_movie_html_fmt`
        
    *   `validate_movie_writer`
        
    *   `validate_nseq_float`
        
    *   `validate_nseq_int`
        
    *   `validate_orientation`
        
    *   `validate_pgf_texsystem`
        
    *   `validate_ps_papersize`
        
    *   `validate_svg_fonttype`
        
    *   `validate_toolbar`
        
    *   `validate_webagg_address`
        
*   Some rcParam validation has become stricter:
    
    *   `[rcParams["axes.axisbelow"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.axisbelow#rcparam-axes-axisbelow) ` (default: `'line'`) no longer accepts strings starting with "line" (case-insensitive) as "line"; use "line" (case-sensitive) instead.
        
    *   `[rcParams["text.latex.preamble"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.latex.preamble#rcparam-text-latex-preamble) ` (default: `''`) and `pdf.preamble` no longer accept non-string values.
        
    *   All `*.linestyle` rcParams no longer accept `offset = None`; set the offset to 0 instead.
        

[Development changes](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#id4)
[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#development-changes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Increase to minimum supported versions of dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#increase-to-minimum-supported-versions-of-dependencies "Link to this heading")

For Matplotlib 3.5, the [minimum supported versions](https://matplotlib.org/stable/install/dependencies.html#dependencies)
 and some [optional dependencies](https://matplotlib.org/stable/install/dependencies.html#optional-dependencies)
 are being bumped:

| Dependency | min in mpl3.4 | min in mpl3.5 |
| --- | --- | --- |
| NumPy | 1.16 | 1.17 |
| Tk (optional) | 8.3 | 8.4 |

This is consistent with our [Dependency version policy](https://matplotlib.org/stable/devel/min_dep_policy.html#min-deps-policy)
 and [NEP29](https://numpy.org/neps/nep-0029-deprecation_policy.html)

### New wheel architectures[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#new-wheel-architectures "Link to this heading")

Wheels have been added for:

*   Python 3.10
    
*   PyPy 3.7
    
*   macOS on Apple Silicon (both arm64 and universal2)
    

### New build dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#new-build-dependencies "Link to this heading")

Versioning has been switched from bundled versioneer to [setuptools-scm](https://github.com/pypa/setuptools_scm/)
 using the `release-branch-semver` version scheme. The latter is well-maintained, but may require slight modification to packaging scripts.

The [setuptools-scm-git-archive](https://pypi.org/project/setuptools-scm-git-archive/)
 plugin is also used for consistent version export.

### Data directory is no longer optional[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#data-directory-is-no-longer-optional "Link to this heading")

Historically, the `mpl-data` directory has been optional (example files were unnecessary, and fonts could be deleted if a suitable dependency on a system font were provided). Though example files are still optional, they have been substantially pared down, and we now consider the directory to be required.

Specifically, the `matplotlibrc` file found there is used for runtime verifications and must exist. Packagers may still symlink fonts to system versions if needed.

### New runtime dependencies[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#new-runtime-dependencies "Link to this heading")

#### fontTools for type 42 subsetting[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#fonttools-for-type-42-subsetting "Link to this heading")

A new dependency [fontTools](https://fonttools.readthedocs.io/)
 is integrated into Matplotlib 3.5. It is designed to be used with PS/EPS and PDF documents; and handles Type 42 font subsetting.

#### Underscore support in LaTeX[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#underscore-support-in-latex "Link to this heading")

The [underscore](https://ctan.org/pkg/underscore)
 package is now a requirement to improve support for underscores in LaTeX.

This is consistent with our [Dependency version policy](https://matplotlib.org/stable/devel/min_dep_policy.html#min-deps-policy)
.

### Matplotlib-specific build options moved from `setup.cfg` to `mplsetup.cfg`[#](https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.5.0.html#matplotlib-specific-build-options-moved-from-setup-cfg-to-mplsetup-cfg "Link to this heading")

In order to avoid conflicting with the use of `setup.cfg` by `setuptools`, the Matplotlib-specific build options have moved from `setup.cfg` to `mplsetup.cfg`. The `setup.cfg.template` has been correspondingly been renamed to `mplsetup.cfg.template`.

Note that the path to this configuration file can still be set via the `MPLSETUPCFG` environment variable, which allows one to keep using the same file before and after this change.

On this page