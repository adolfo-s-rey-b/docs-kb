[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#main-content)

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
    

What's new in Matplotlib 2.1.0 (Oct 7, 2017)[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#what-s-new-in-matplotlib-2-1-0-oct-7-2017 "Link to this heading")

============================================================================================================================================================================================

Documentation[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#documentation "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

The examples have been migrated to use [sphinx gallery](https://sphinx-gallery.readthedocs.io/en/latest/)
. This allows better mixing of prose and code in the examples, provides links to download the examples as both a Python script and a Jupyter notebook, and improves the thumbnail galleries. The examples have been re-organized into [Tutorials](https://matplotlib.org/stable/tutorials/index.html#tutorials)
 and a [Examples](https://matplotlib.org/stable/gallery/index.html#gallery)
.

Many docstrings and examples have been clarified and improved.

New features[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#new-features "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### String categorical values[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#string-categorical-values "Link to this heading")

All plotting functions now support string categorical values as input. For example:

data \= {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
fig, ax \= plt.subplots()
ax.bar(data.keys(), data.values(), color\='lightgray')

([`Source code`](https://matplotlib.org/stable/_downloads/e6381226801c7748dcd64988770f5abd/whats_new_2-1-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/f379da7b574a03964e3ca404527d447c/whats_new_2-1-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/df2620f0dccf927df74a9c923273cd2b/whats_new_2-1-0-1.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-1-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-1-0-1.2x.png)

### Interactive JS widgets for animation[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#interactive-js-widgets-for-animation "Link to this heading")

Jake Vanderplas' JSAnimation package has been merged into Matplotlib. This adds to Matplotlib the [`HTMLWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.HTMLWriter.html#matplotlib.animation.HTMLWriter "matplotlib.animation.HTMLWriter")
 class for generating a JavaScript HTML animation, suitable for the IPython notebook. This can be activated by default by setting the `animation.html` rc parameter to `jshtml`. One can also call the [`to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
 method to manually convert an animation. This can be displayed using IPython's `HTML` display class:

from IPython.display import HTML
HTML(animation.to\_jshtml())

The [`HTMLWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.HTMLWriter.html#matplotlib.animation.HTMLWriter "matplotlib.animation.HTMLWriter")
 class can also be used to generate an HTML file by asking for the `html` writer.

### Enhancements to polar plot[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#enhancements-to-polar-plot "Link to this heading")

The polar axes transforms have been greatly re-factored to allow for more customization of view limits and tick labelling. Additional options for view limits allow for creating an annulus, a sector, or some combination of the two.

The [`set_rorigin()`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rorigin "matplotlib.projections.polar.PolarAxes.set_rorigin")
 method may be used to provide an offset to the minimum plotting radius, producing an annulus.

The [`set_theta_zero_location()`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_theta_zero_location "matplotlib.projections.polar.PolarAxes.set_theta_zero_location")
 method now has an optional `offset` argument. This argument may be used to further specify the zero location based on the given anchor point.

[![../../_images/sphx_glr_polar_scatter_002.png](https://matplotlib.org/stable/_images/sphx_glr_polar_scatter_002.png)](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_scatter.html#scatter-plot-on-polar-axis-with-offset-origin)

Polar Offset Demo[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#id2 "Link to this image")

The [`set_thetamin()`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetamin "matplotlib.projections.polar.PolarAxes.set_thetamin")
 and [`set_thetamax()`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetamax "matplotlib.projections.polar.PolarAxes.set_thetamax")
 methods may be used to limit the range of angles plotted, producing sectors of a circle.

[![../../_images/sphx_glr_polar_scatter_003.png](https://matplotlib.org/stable/_images/sphx_glr_polar_scatter_003.png)](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_scatter.html#scatter-plot-on-polar-axis-confined-to-a-sector)

Polar Sector Demo[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#id3 "Link to this image")

Previous releases allowed plots containing negative radii for which the negative values are simply used as labels, and the real radius is shifted by the configured minimum. This release also allows negative radii to be used for grids and ticks, which were previously silently ignored.

Radial ticks have been modified to be parallel to the circular grid line, and angular ticks have been modified to be parallel to the grid line. It may also be useful to rotate tick _labels_ to match the boundary. Calling `ax.tick_params(rotation='auto')` will enable the new behavior: radial tick labels will be parallel to the circular grid line, and angular tick labels will be perpendicular to the grid line (i.e., parallel to the outer boundary). Additionally, tick labels now obey the padding settings that previously only worked on Cartesian plots. Consequently, the `frac` argument to [`PolarAxes.set_thetagrids`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetagrids "matplotlib.projections.polar.PolarAxes.set_thetagrids")
 is no longer applied. Tick padding can be modified with the `pad` argument to [`Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
 or [`Axis.set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
.

### `Figure` class now has `subplots` method[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#figure-class-now-has-subplots-method "Link to this heading")

The [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 class now has a [`subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 method which behaves the same as [`pyplot.subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 but on an existing figure.

### Metadata savefig keyword argument[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#metadata-savefig-keyword-argument "Link to this heading")

[`savefig()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig")
 now accepts `metadata` as a keyword argument. It can be used to store key/value pairs in the image metadata.

*   'png' with Agg backend
    
*   'pdf' with PDF backend (see [`writeInfoDict()`](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfFile.writeInfoDict "matplotlib.backends.backend_pdf.PdfFile.writeInfoDict")
     for a list of supported keywords)
    
*   'eps' and 'ps' with PS backend (only 'Creator' key is accepted)
    

plt.savefig('test.png', metadata\={'Software': 'My awesome software'})

### Busy Cursor[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#busy-cursor "Link to this heading")

The interactive GUI backends will now change the cursor to busy when Matplotlib is rendering the canvas.

### PolygonSelector[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#polygonselector "Link to this heading")

A [`PolygonSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")
 class has been added to [`matplotlib.widgets`](https://matplotlib.org/stable/api/widgets_api.html#module-matplotlib.widgets "matplotlib.widgets")
. See [Select indices from a collection using polygon selector](https://matplotlib.org/stable/gallery/widgets/polygon_selector_demo.html)
 for details.

### Added [`matplotlib.ticker.PercentFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter "matplotlib.ticker.PercentFormatter")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#added-matplotlib-ticker-percentformatter "Link to this heading")

The new [`PercentFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.PercentFormatter "matplotlib.ticker.PercentFormatter")
 formatter has some nice features like being able to convert from arbitrary data scales to percents, a customizable percent symbol and either automatic or manual control over the decimal points.

### Reproducible PS, PDF and SVG output[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#reproducible-ps-pdf-and-svg-output "Link to this heading")

The `SOURCE_DATE_EPOCH` environment variable can now be used to set the timestamp value in the PS and PDF outputs. See [source date epoch](https://reproducible-builds.org/specs/source-date-epoch/)
.

Alternatively, calling `savefig` with `metadata={'CreationDate': None}` will omit the timestamp altogether for the PDF backend.

The reproducibility of the output from the PS and PDF backends has so far been tested using various plot elements but only default values of options such as `{ps,pdf}.fonttype` that can affect the output at a low level, and not with the mathtext or usetex features. When Matplotlib calls external tools (such as PS distillers or LaTeX) their versions need to be kept constant for reproducibility, and they may add sources of nondeterminism outside the control of Matplotlib.

For SVG output, the `svg.hashsalt` rc parameter has been added in an earlier release. This parameter changes some random identifiers in the SVG file to be deterministic. The downside of this setting is that if more than one file is generated using deterministic identifiers and they end up as parts of one larger document, the identifiers can collide and cause the different parts to affect each other.

These features are now enabled in the tests for the PDF and SVG backends, so most test output files (but not all of them) are now deterministic.

### Orthographic projection for mplot3d[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#orthographic-projection-for-mplot3d "Link to this heading")

[`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
 now accepts `proj_type` keyword argument and has a method [`set_proj_type()`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type "mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type")
. The default option is `'persp'` as before, and supplying `'ortho'` enables orthographic view.

Compare the z-axis which is vertical in orthographic view, but slightly skewed in the perspective view.

import numpy as np
import matplotlib.pyplot as plt
from mpl\_toolkits.mplot3d import Axes3D

fig \= plt.figure(figsize\=(4, 6))
ax1 \= fig.add\_subplot(2, 1, 1, projection\='3d')
ax1.set\_proj\_type('persp')
ax1.set\_title('Perspective (default)')

ax2 \= fig.add\_subplot(2, 1, 2, projection\='3d')
ax2.set\_proj\_type('ortho')
ax2.set\_title('Orthographic')

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/5be51cee3a735553ee1252476116af41/whats_new_2-1-0-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/d476c9d6f2f42ae4159a8e72fe4393d1/whats_new_2-1-0-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/80d21d0724a9ff54f52b47371caedc77/whats_new_2-1-0-2.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-1-0-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-1-0-2.2x.png)

### `voxels` function for mplot3d[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#voxels-function-for-mplot3d "Link to this heading")

[`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
 now has a [`voxels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.voxels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.voxels "mpl_toolkits.mplot3d.axes3d.Axes3D.voxels")
 method, for visualizing boolean 3D data. Uses could include plotting a sparse 3D heat map, or visualizing a volumetric model.

[![../../_images/sphx_glr_voxels_numpy_logo_001.png](https://matplotlib.org/stable/_images/sphx_glr_voxels_numpy_logo_001.png)](https://matplotlib.org/stable/gallery/mplot3d/voxels_numpy_logo.html)

Voxel Demo[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#id4 "Link to this image")

Improvements[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#improvements "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

### CheckButtons widget `get_status` function[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#checkbuttons-widget-get-status-function "Link to this heading")

A [`get_status()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons.get_status "matplotlib.widgets.CheckButtons.get_status")
 method has been added to the [`matplotlib.widgets.CheckButtons`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.CheckButtons.html#matplotlib.widgets.CheckButtons "matplotlib.widgets.CheckButtons")
 class. This `get_status` method allows user to query the status (True/False) of all of the buttons in the `CheckButtons` object.

### Add `fill_bar` argument to `AnchoredSizeBar`[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#add-fill-bar-argument-to-anchoredsizebar "Link to this heading")

The `mpl_toolkits` class [`AnchoredSizeBar`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar")
 now has an additional `fill_bar` argument, which makes the size bar a solid rectangle instead of just drawing the border of the rectangle. The default is `None`, and whether or not the bar will be filled by default depends on the value of `size_vertical`. If `size_vertical` is nonzero, `fill_bar` will be set to `True`. If `size_vertical` is zero then `fill_bar` will be set to `False`. If you wish to override this default behavior, set `fill_bar` to `True` or `False` to unconditionally always or never use a filled patch rectangle for the size bar.

import matplotlib.pyplot as plt
from mpl\_toolkits.axes\_grid1.anchored\_artists import AnchoredSizeBar

fig, ax \= plt.subplots(figsize\=(3, 3))

bar0 \= AnchoredSizeBar(ax.transData, 0.3, 'unfilled', loc\='lower left',
                       frameon\=False, size\_vertical\=0.05, fill\_bar\=False)
ax.add\_artist(bar0)
bar1 \= AnchoredSizeBar(ax.transData, 0.3, 'filled', loc\='lower right',
                       frameon\=False, size\_vertical\=0.05, fill\_bar\=True)
ax.add\_artist(bar1)

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/2924c74ce325f3ebd23a796de78dc25b/whats_new_2-1-0-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/fed653c181899096ff912b697281b5c3/whats_new_2-1-0-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/8f9c1bbad272a3badb8e13856ba6432e/whats_new_2-1-0-3.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-1-0-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-1-0-3.2x.png)

### Annotation can use a default arrow style[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#annotation-can-use-a-default-arrow-style "Link to this heading")

Annotations now use the default arrow style when setting `arrowprops={}`, rather than no arrow (the new behavior actually matches the documentation).

### Barbs and Quiver Support Dates[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#barbs-and-quiver-support-dates "Link to this heading")

When using the [`quiver()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "matplotlib.axes.Axes.quiver")
 and [`barbs()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barbs.html#matplotlib.axes.Axes.barbs "matplotlib.axes.Axes.barbs")
 plotting methods, it is now possible to pass dates, just like for other methods like [`plot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
. This also allows these functions to handle values that need unit-conversion applied.

### Hexbin default line color[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#hexbin-default-line-color "Link to this heading")

The default `linecolor` keyword argument for [`hexbin()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin")
 is now `'face'`, and supplying `'none'` now prevents lines from being drawn around the hexagons.

### Figure.legend() can be called without arguments[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#figure-legend-can-be-called-without-arguments "Link to this heading")

Calling [`Figure.legend()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
 can now be done with no arguments. In this case a legend will be created that contains all the artists on all the axes contained within the figure.

### Multiple legend keys for legend entries[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#multiple-legend-keys-for-legend-entries "Link to this heading")

A legend entry can now contain more than one legend key. The extended [`HandlerTuple`](https://matplotlib.org/stable/api/legend_handler_api.html#matplotlib.legend_handler.HandlerTuple "matplotlib.legend_handler.HandlerTuple")
 class now accepts two parameters: `ndivide` divides the legend area in the specified number of sections; `pad` changes the padding between the legend keys.

[![../../_images/sphx_glr_legend_demo_004.png](https://matplotlib.org/stable/_images/sphx_glr_legend_demo_004.png)](https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html)

Multiple Legend Keys[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#id5 "Link to this image")

### New parameter _clear_ for [`figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#new-parameter-clear-for-figure "Link to this heading")

When the pyplot's function [`figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
 is called with a `num` parameter, a new window is only created if no existing window with the same value exists. A new bool parameter _clear_ was added for explicitly clearing its existing contents. This is particularly useful when utilized in interactive sessions. Since [`subplots()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 also accepts keyword arguments from [`figure()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
, it can also be used there:

import matplotlib.pyplot as plt

fig0 \= plt.figure(num\=1)
fig0.suptitle("A fancy plot")
print("fig0.texts: ", \[t.get\_text() for t in fig0.texts\])

fig1 \= plt.figure(num\=1, clear\=False)  \# do not clear contents of window
fig1.text(0.5, 0.5, "Really fancy!")
print("fig0 is fig1: ",  fig0 is fig1)
print("fig1.texts: ", \[t.get\_text() for t in fig1.texts\])

fig2, ax2 \= plt.subplots(2, 1, num\=1, clear\=True)  \# clear contents
print("fig0 is fig2: ",  fig0 is fig2)
print("fig2.texts: ", \[t.get\_text() for t in fig2.texts\])

\# The output:
\# fig0.texts:  \['A fancy plot'\]
\# fig0 is fig1:  True
\# fig1.texts:  \['A fancy plot', 'Really fancy!'\]
\# fig0 is fig2:  True
\# fig2.texts:  \[\]

### Specify minimum value to format as scalar for `LogFormatterMathtext`[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#specify-minimum-value-to-format-as-scalar-for-logformattermathtext "Link to this heading")

[`LogFormatterMathtext`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.LogFormatterMathtext "matplotlib.ticker.LogFormatterMathtext")
 now includes the option to specify a minimum value exponent to format as a scalar (i.e., 0.001 instead of 10\-3).

### New quiverkey angle keyword argument[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#new-quiverkey-angle-keyword-argument "Link to this heading")

Plotting a [`quiverkey()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiverkey.html#matplotlib.axes.Axes.quiverkey "matplotlib.axes.Axes.quiverkey")
 now admits the `angle` keyword argument, which sets the angle at which to draw the key arrow.

### Colormap reversed method[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#colormap-reversed-method "Link to this heading")

The methods [`matplotlib.colors.LinearSegmentedColormap.reversed()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.reversed "matplotlib.colors.LinearSegmentedColormap.reversed")
 and [`matplotlib.colors.ListedColormap.reversed()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap.reversed "matplotlib.colors.ListedColormap.reversed")
 return a reversed instance of the Colormap. This implements a way for any Colormap to be reversed.

### [`artist.setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.setp.html#matplotlib.artist.setp "matplotlib.artist.setp")
 (and [`pyplot.setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp")
) accept a _file_ argument[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#artist-setp-and-pyplot-setp-accept-a-file-argument "Link to this heading")

The argument is keyword-only. It allows an output file other than [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "(in Python v3.14)")
 to be specified. It works exactly like the _file_ argument to [`print`](https://docs.python.org/3/library/functions.html#print "(in Python v3.14)")
.

### `streamplot` streamline generation more configurable[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#streamplot-streamline-generation-more-configurable "Link to this heading")

The starting point, direction, and length of the stream lines can now be configured. This allows to follow the vector field for a longer time and can enhance the visibility of the flow pattern in some use cases.

### `Axis.set_tick_params` now responds to _rotation_[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#axis-set-tick-params-now-responds-to-rotation "Link to this heading")

Bulk setting of tick label rotation is now possible via [`tick_params()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
 using the _rotation_ keyword.

ax.tick\_params(which\='both', rotation\=90)

### Ticklabels are turned off instead of being invisible[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#ticklabels-are-turned-off-instead-of-being-invisible "Link to this heading")

Internally, the [`Tick`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Tick "matplotlib.axis.Tick")
's `matplotlib.axis.Tick.label1On` attribute is now used to hide tick labels instead of setting the visibility on the tick label objects. This improves overall performance and fixes some issues. As a consequence, in case those labels ought to be shown, [`tick_params()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
 needs to be used, e.g.

ax.tick\_params(labelbottom\=True)

### Shading in 3D bar plots[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#shading-in-3d-bar-plots "Link to this heading")

A new `shade` parameter has been added the 3D [`bar`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar.html#mpl_toolkits.mplot3d.axes3d.Axes3D.bar "mpl_toolkits.mplot3d.axes3d.Axes3D.bar")
 plotting method. The default behavior remains to shade the bars, but now users have the option of setting `shade` to `False`.

import numpy as np
import matplotlib.pyplot as plt
from mpl\_toolkits.mplot3d import Axes3D

x \= np.arange(2)
y \= np.arange(3)
x2d, y2d \= np.meshgrid(x, y)
x, y \= x2d.ravel(), y2d.ravel()
z \= np.zeros\_like(x)
dz \= x + y

fig \= plt.figure(figsize\=(4, 6))
ax1 \= fig.add\_subplot(2, 1, 1, projection\='3d')
ax1.bar3d(x, y, z, 1, 1, dz, shade\=True)
ax1.set\_title('Shading On')

ax2 \= fig.add\_subplot(2, 1, 2, projection\='3d')
ax2.bar3d(x, y, z, 1, 1, dz, shade\=False)
ax2.set\_title('Shading Off')

plt.show()

([`Source code`](https://matplotlib.org/stable/_downloads/d1952d0ef7c73d4032881160057849a3/whats_new_2-1-0-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/1967fad29780ba4118f00fa5cbe2ede8/whats_new_2-1-0-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/72ea0ba8bc9ec1603d3e487bf60abbeb/whats_new_2-1-0-4.png)
)

[![](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-1-0-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_2-1-0-4.2x.png)

### New `which` Parameter for `autofmt_xdate`[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#new-which-parameter-for-autofmt-xdate "Link to this heading")

A `which` parameter now exists for the method [`autofmt_xdate()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.autofmt_xdate.html#matplotlib.figure.Figure.autofmt_xdate "matplotlib.figure.Figure.autofmt_xdate")
. This allows a user to format `major`, `minor` or `both` tick labels selectively. The default behavior will rotate and align the `major` tick labels.

fig.autofmt\_xdate(bottom\=0.2, rotation\=30, ha\='right', which\='minor')

### New Figure Parameter for `subplot2grid`[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#new-figure-parameter-for-subplot2grid "Link to this heading")

A `fig` parameter now exists for the function [`subplot2grid()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid")
. This allows a user to specify the figure where the subplots will be created. If `fig` is `None` (default) then the method will use the current figure retrieved by [`gcf()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gcf.html#matplotlib.pyplot.gcf "matplotlib.pyplot.gcf")
.

subplot2grid(shape, loc, rowspan\=1, colspan\=1, fig\=myfig)

### Interpolation in `fill_betweenx`[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#interpolation-in-fill-betweenx "Link to this heading")

The `interpolate` parameter now exists for the method [`fill_betweenx()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
. This allows a user to interpolate the data and fill the areas in the crossover points, similarly to [`fill_between()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between")
.

### New keyword argument `sep` for EngFormatter[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#new-keyword-argument-sep-for-engformatter "Link to this heading")

A new `sep` keyword argument has been added to [`EngFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.EngFormatter "matplotlib.ticker.EngFormatter")
 and provides a means to define the string that will be used between the value and its unit. The default string is `" "`, which preserves the former behavior. Additionally, the separator is now present between the value and its unit even in the absence of SI prefix. There was formerly a bug that was causing strings like `"3.14V"` to be returned instead of the expected `"3.14 V"` (with the default behavior).

### Extend `MATPLOTLIBRC` behavior[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#extend-matplotlibrc-behavior "Link to this heading")

The environmental variable can now specify the full file path or the path to a directory containing a `matplotlibrc` file.

### `density` kwarg to hist[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#density-kwarg-to-hist "Link to this heading")

The [`hist()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
 method now prefers `density` to `normed` to control if the histogram should be normalized, following a change upstream to NumPy. This will reduce confusion as the behavior has always been that the integral of the histogram is 1 (rather than sum or maximum value).

Internals[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#internals "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

### New TransformedPatchPath caching object[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#new-transformedpatchpath-caching-object "Link to this heading")

A newly added [`TransformedPatchPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPatchPath "matplotlib.transforms.TransformedPatchPath")
 provides a means to transform a [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 into a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 via a [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 while caching the resulting path. If neither the patch nor the transform have changed, a cached copy of the path is returned.

This class differs from the older [`TransformedPath`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedPath "matplotlib.transforms.TransformedPath")
 in that it is able to refresh itself based on the underlying patch while the older class uses an immutable path.

### Abstract base class for movie writers[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#abstract-base-class-for-movie-writers "Link to this heading")

The new [`AbstractMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter "matplotlib.animation.AbstractMovieWriter")
 class defines the API required by a class that is to be used as the `writer` in the [`matplotlib.animation.Animation.save()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")
 method. The existing [`MovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter "matplotlib.animation.MovieWriter")
 class now derives from the new abstract base class.

### Stricter validation of line style rcParams[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#stricter-validation-of-line-style-rcparams "Link to this heading")

The validation of rcParams that are related to line styles (`lines.linestyle`, `boxplot.*.linestyle`, `grid.linestyle` and `contour.negative_linestyle`) now effectively checks that the values are valid line styles. Strings like `'dashed'` or `'--'` are accepted, as well as even-length sequences of on-off ink like `[1, 1.65]`. In this latter case, the offset value is handled internally and should _not_ be provided by the user.

The new validation scheme replaces the former one used for the `contour.negative_linestyle` rcParams, that was limited to `'solid'` and `'dashed'` line styles.

The validation is case-insensitive. The following are now valid:

grid.linestyle             : (1, 3)   \# loosely dotted grid lines
contour.negative\_linestyle : dashdot  \# previously only solid or dashed

### pytest[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#pytest "Link to this heading")

The automated tests have been switched from [nose](https://nose.readthedocs.io/)
 to [pytest](https://pytest.org/)
.

Performance[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#performance "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

### Path simplification updates[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#path-simplification-updates "Link to this heading")

Line simplification controlled by the `path.simplify` and `path.simplify_threshold` parameters has been improved. You should notice better rendering performance when plotting large amounts of data (as long as the above parameters are set accordingly). Only the line segment portion of paths will be simplified -- if you are also drawing markers and experiencing problems with rendering speed, you should consider using the `markevery` option to [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
. See the [Performance](https://matplotlib.org/stable/users/explain/artists/performance.html#performance)
 section in the usage tutorial for more information.

The simplification works by iteratively merging line segments into a single vector until the next line segment's perpendicular distance to the vector (measured in display-coordinate space) is greater than the `path.simplify_threshold` parameter. Thus, higher values of `path.simplify_threshold` result in quicker rendering times. If you are plotting just to explore data and not for publication quality, pixel perfect plots, then a value of `1.0` can be safely used. If you want to make sure your plot reflects your data _exactly_, then you should set `path.simplify` to false and/or `path.simplify_threshold` to `0`. Matplotlib currently defaults to a conservative value of `1/9`, smaller values are unlikely to cause any visible differences in your plots.

### Implement intersects\_bbox in c++[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_2.1.0.html#implement-intersects-bbox-in-c "Link to this heading")

[`intersects_bbox()`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path.intersects_bbox "matplotlib.path.Path.intersects_bbox")
 has been implemented in c++ which improves the performance of automatically placing the legend.

On this page