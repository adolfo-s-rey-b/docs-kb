[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#main-content)

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
    

[What's new in Matplotlib 1.4 (Aug 25, 2014)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#what-s-new-in-matplotlib-1-4-aug-25-2014 "Link to this heading")

========================================================================================================================================================================================================================================================================

Thomas A. Caswell served as the release manager for the 1.4 release.

Note

matplotlib 1.4 supports Python 2.6, 2.7, 3.3, and 3.4

[New colormap](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#new-colormap "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In heatmaps, a green-to-red spectrum is often used to indicate intensity of activity, but this can be problematic for the red/green colorblind. A new, colorblind-friendly colormap is now available at `matplotlib.cm.Wistia`. This colormap maintains the red/green symbolism while achieving deuteranopic legibility through brightness variations. See [here](https://github.com/wistia/heatmap-palette)
 for more information.

[The nbagg backend](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#the-nbagg-backend "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Phil Elson added a new backend, named "nbagg", which enables interactive figures in a live IPython notebook session. The backend makes use of the infrastructure developed for the webagg backend, which itself gives standalone server backed interactive figures in the browser, however nbagg does not require a dedicated matplotlib server as all communications are handled through the IPython Comm machinery.

As with other backends nbagg can be enabled inside the IPython notebook with:

import matplotlib
matplotlib.use('nbagg')

Once figures are created and then subsequently shown, they will placed in an interactive widget inside the notebook allowing panning and zooming in the same way as any other matplotlib backend. Because figures require a connection to the IPython notebook server for their interactivity, once the notebook is saved, each figure will be rendered as a static image - thus allowing non-interactive viewing of figures on services such as [nbviewer](https://nbviewer.jupyter.org/)
.

[New plotting features](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#new-plotting-features "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Power-law normalization[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#power-law-normalization "Link to this heading")

Ben Gamari added a power-law normalization method, [`PowerNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.PowerNorm.html#matplotlib.colors.PowerNorm "matplotlib.colors.PowerNorm")
. This class maps a range of values to the interval \[0,1\] with power-law scaling with the exponent provided by the constructor's _gamma_ argument. Power law normalization can be useful for, e.g., emphasizing small populations in a histogram.

### Fully customizable boxplots[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#fully-customizable-boxplots "Link to this heading")

Paul Hobson overhauled the [`boxplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")
 method such that it is now completely customizable in terms of the styles and positions of the individual artists. Under the hood, [`boxplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")
 relies on a new function ([`boxplot_stats()`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats "matplotlib.cbook.boxplot_stats")
), which accepts any data structure currently compatible with [`boxplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")
, and returns a list of dictionaries containing the positions for each element of the boxplots. Then a second method, [`bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
 is called to draw the boxplots based on the stats.

The [`boxplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")
 function can be used as before to generate boxplots from data in one step. But now the user has the flexibility to generate the statistics independently, or to modify the output of [`boxplot_stats()`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.boxplot_stats "matplotlib.cbook.boxplot_stats")
 prior to plotting with [`bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
.

Lastly, each artist (e.g., the box, outliers, cap, notches) can now be toggled on or off and their styles can be passed in through individual kwargs. See the examples: [Artist customization in box plots](https://matplotlib.org/stable/gallery/statistics/boxplot.html)
 and [Separate calculation and plotting of boxplots](https://matplotlib.org/stable/gallery/statistics/bxp.html)

Added a bool kwarg, `manage_xticks`, which if False disables the management of the ticks and limits on the x-axis by [`bxp()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
.

### Support for datetime axes in 2d plots[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#support-for-datetime-axes-in-2d-plots "Link to this heading")

Andrew Dawson added support for datetime axes to [`contour()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour")
, [`contourf()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf")
, [`pcolormesh()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolormesh.html#matplotlib.pyplot.pcolormesh "matplotlib.pyplot.pcolormesh")
 and [`pcolor()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolor.html#matplotlib.pyplot.pcolor "matplotlib.pyplot.pcolor")
.

### Support for additional spectrum types[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#support-for-additional-spectrum-types "Link to this heading")

Todd Jennings added support for new types of frequency spectrum plots: [`magnitude_spectrum()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.magnitude_spectrum.html#matplotlib.pyplot.magnitude_spectrum "matplotlib.pyplot.magnitude_spectrum")
, [`phase_spectrum()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.phase_spectrum.html#matplotlib.pyplot.phase_spectrum "matplotlib.pyplot.phase_spectrum")
, and [`angle_spectrum()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.angle_spectrum.html#matplotlib.pyplot.angle_spectrum "matplotlib.pyplot.angle_spectrum")
, as well as corresponding functions in mlab.

He also added these spectrum types to [`specgram()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.specgram.html#matplotlib.pyplot.specgram "matplotlib.pyplot.specgram")
, as well as adding support for linear scaling there (in addition to the existing dB scaling). Support for additional spectrum types was also added to [`specgram()`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.specgram "matplotlib.mlab.specgram")
.

He also increased the performance for all of these functions and plot types.

### Support for detrending and windowing 2D arrays in mlab[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#support-for-detrending-and-windowing-2d-arrays-in-mlab "Link to this heading")

Todd Jennings added support for 2D arrays in the [`detrend_mean()`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_mean "matplotlib.mlab.detrend_mean")
, [`detrend_none()`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_none "matplotlib.mlab.detrend_none")
, and [`detrend()`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend "matplotlib.mlab.detrend")
, as well as adding `matplotlib.mlab.apply_window` which support windowing 2D arrays.

### Support for strides in mlab[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#support-for-strides-in-mlab "Link to this heading")

Todd Jennings added some functions to mlab to make it easier to use NumPy strides to create memory-efficient 2D arrays. This includes `matplotlib.mlab.stride_repeat`, which repeats an array to create a 2D array, and `matplotlib.mlab.stride_windows`, which uses a moving window to create a 2D array from a 1D array.

### Formatter for new-style formatting strings[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#formatter-for-new-style-formatting-strings "Link to this heading")

Added [`StrMethodFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.StrMethodFormatter "matplotlib.ticker.StrMethodFormatter")
 which does the same job as [`FormatStrFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "matplotlib.ticker.FormatStrFormatter")
, but accepts new-style formatting strings instead of printf-style formatting strings

### Consistent grid sizes in streamplots[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#consistent-grid-sizes-in-streamplots "Link to this heading")

[`streamplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.streamplot.html#matplotlib.pyplot.streamplot "matplotlib.pyplot.streamplot")
 uses a base grid size of 30x30 for both `density=1` and `density=(1, 1)`. Previously a grid size of 30x30 was used for `density=1`, but a grid size of 25x25 was used for `density=(1, 1)`.

### Get a list of all tick labels (major and minor)[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#get-a-list-of-all-tick-labels-major-and-minor "Link to this heading")

Added the kwarg 'which' to [`Axes.get_xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels")
, [`Axes.get_yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticklabels.html#matplotlib.axes.Axes.get_yticklabels "matplotlib.axes.Axes.get_yticklabels")
 and [`Axis.get_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklabels.html#matplotlib.axis.Axis.get_ticklabels "matplotlib.axis.Axis.get_ticklabels")
. 'which' can be 'major', 'minor', or 'both' select which ticks to return, like [`set_ticks_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_ticks_position.html#matplotlib.axis.XAxis.set_ticks_position "matplotlib.axis.XAxis.set_ticks_position")
. If 'which' is [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 then the old behaviour (controlled by the bool _minor_).

### Separate horizontal/vertical axes padding support in ImageGrid[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#separate-horizontal-vertical-axes-padding-support-in-imagegrid "Link to this heading")

The kwarg 'axes\_pad' to [`mpl_toolkits.axes_grid1.axes_grid.ImageGrid`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_grid.ImageGrid.html#mpl_toolkits.axes_grid1.axes_grid.ImageGrid "mpl_toolkits.axes_grid1.axes_grid.ImageGrid")
 can now be a tuple if separate horizontal/vertical padding is needed. This is supposed to be very helpful when you have a labelled legend next to every subplot and you need to make some space for legend's labels.

### Support for skewed transformations[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#support-for-skewed-transformations "Link to this heading")

The [`Affine2D`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 gained additional methods [`skew`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.skew "matplotlib.transforms.Affine2D.skew")
 and [`skew_deg`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D.skew_deg "matplotlib.transforms.Affine2D.skew_deg")
 to create skewed transformations. Additionally, matplotlib internals were cleaned up to support using such transforms in [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. This transform is important for some plot types, specifically the Skew-T used in meteorology.

[![../../_images/sphx_glr_skewt_001.png](https://matplotlib.org/stable/_images/sphx_glr_skewt_001.png)](https://matplotlib.org/stable/gallery/specialty_plots/skewt.html)

### Support for specifying properties of wedge and text in pie charts.[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#support-for-specifying-properties-of-wedge-and-text-in-pie-charts "Link to this heading")

Added the kwargs 'wedgeprops' and 'textprops' to [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
 to accept properties for wedge and text objects in a pie. For example, one can specify wedgeprops = {'linewidth':3} to specify the width of the borders of the wedges in the pie. For more properties that the user can specify, look at the docs for the wedge and text objects.

### Fixed the direction of errorbar upper/lower limits[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#fixed-the-direction-of-errorbar-upper-lower-limits "Link to this heading")

Larry Bradley fixed the [`errorbar()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
 method such that the upper and lower limits (_lolims_, _uplims_, _xlolims_, _xuplims_) now point in the correct direction.

### More consistent add-object API for Axes[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#more-consistent-add-object-api-for-axes "Link to this heading")

Added the Axes method [`add_image`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_image.html#matplotlib.axes.Axes.add_image "matplotlib.axes.Axes.add_image")
 to put image handling on a par with artists, collections, containers, lines, patches, and tables.

### Violin Plots[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#violin-plots "Link to this heading")

Per Parker, Gregory Kelsie, Adam Ortiz, Kevin Chan, Geoffrey Lee, Deokjae Donald Seo, and Taesu Terry Lim added a basic implementation for violin plots. Violin plots can be used to represent the distribution of sample data. They are similar to box plots, but use a kernel density estimation function to present a smooth approximation of the data sample used. The added features are:

[`violin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violin.html#matplotlib.axes.Axes.violin "matplotlib.axes.Axes.violin")
 - Renders a violin plot from a collection of statistics. [`violin_stats()`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.violin_stats "matplotlib.cbook.violin_stats")
 - Produces a collection of statistics suitable for rendering a violin plot. [`violinplot()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html#matplotlib.pyplot.violinplot "matplotlib.pyplot.violinplot")
 - Creates a violin plot from a set of sample data. This method makes use of [`violin_stats()`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.violin_stats "matplotlib.cbook.violin_stats")
 to process the input data, and [`violin_stats()`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.violin_stats "matplotlib.cbook.violin_stats")
 to do the actual rendering. Users are also free to modify or replace the output of [`violin_stats()`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.violin_stats "matplotlib.cbook.violin_stats")
 in order to customize the violin plots to their liking.

This feature was implemented for a software engineering course at the University of Toronto, Scarborough, run in Winter 2014 by Anya Tafliovich.

### More _markevery_ options to show only a subset of markers[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#more-markevery-options-to-show-only-a-subset-of-markers "Link to this heading")

Rohan Walker extended the _markevery_ property in [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
. You can now specify a subset of markers to show with an int, slice object, numpy fancy indexing, or float. Using a float shows markers at approximately equal display-coordinate-distances along the line.

### Added size related functions to specialized [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
s[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#added-size-related-functions-to-specialized-collections "Link to this heading")

Added the `get_size` and `set_size` functions to control the size of elements of specialized collections ( [`AsteriskPolygonCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.AsteriskPolygonCollection "matplotlib.collections.AsteriskPolygonCollection")
 `matplotlib.collections.BrokenBarHCollection` [`CircleCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.CircleCollection "matplotlib.collections.CircleCollection")
 [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 [`RegularPolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.RegularPolyCollection "matplotlib.collections.RegularPolyCollection")
 [`StarPolygonCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.StarPolygonCollection "matplotlib.collections.StarPolygonCollection")
).

### Fixed the mouse coordinates giving the wrong theta value in Polar graph[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#fixed-the-mouse-coordinates-giving-the-wrong-theta-value-in-polar-graph "Link to this heading")

Added code to [`transform_non_affine`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.InvertedPolarTransform.transform_non_affine "matplotlib.projections.polar.InvertedPolarTransform.transform_non_affine")
 to ensure that the calculated theta value was between the range of 0 and 2 \* pi since the problem was that the value can become negative after applying the direction and rotation to the theta calculation.

### Simple quiver plot for mplot3d toolkit[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#simple-quiver-plot-for-mplot3d-toolkit "Link to this heading")

A team of students in an _Engineering Large Software Systems_ course, taught by Prof. Anya Tafliovich at the University of Toronto, implemented a simple version of a quiver plot in 3D space for the mplot3d toolkit as one of their term project. This feature is documented in [`quiver`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.quiver.html#mpl_toolkits.mplot3d.axes3d.Axes3D.quiver "mpl_toolkits.mplot3d.axes3d.Axes3D.quiver")
. The team members are: Ryan Steve D'Souza, Victor B, xbtsw, Yang Wang, David, Caradec Bisesar and Vlad Vassilovski.

[![../../_images/sphx_glr_quiver3d_001.png](https://matplotlib.org/stable/_images/sphx_glr_quiver3d_001.png)](https://matplotlib.org/stable/gallery/mplot3d/quiver3d.html)

### polar-plot r-tick locations[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#polar-plot-r-tick-locations "Link to this heading")

Added the ability to control the angular position of the r-tick labels on a polar plot via [`set_rlabel_position`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rlabel_position "matplotlib.projections.polar.PolarAxes.set_rlabel_position")
.

[Date handling](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#date-handling "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### n-d array support for date conversion[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#n-d-array-support-for-date-conversion "Link to this heading")

Andrew Dawson added support for n-d array handling to [`matplotlib.dates.num2date()`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.num2date "matplotlib.dates.num2date")
, [`matplotlib.dates.date2num()`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.date2num "matplotlib.dates.date2num")
 and [`matplotlib.dates.datestr2num()`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.datestr2num "matplotlib.dates.datestr2num")
. Support is also added to the unit conversion interfaces [`matplotlib.dates.DateConverter`](https://matplotlib.org/stable/api/dates_api.html#matplotlib.dates.DateConverter "matplotlib.dates.DateConverter")
 and [`matplotlib.units.Registry`](https://matplotlib.org/stable/api/units_api.html#matplotlib.units.Registry "matplotlib.units.Registry")
.

[Configuration (rcParams)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#configuration-rcparams "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### `savefig.transparent` added[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#savefig-transparent-added "Link to this heading")

Controls whether figures are saved with a transparent background by default. Previously [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 always defaulted to a non-transparent background.

### `axes.titleweight`[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#axes-titleweight "Link to this heading")

Added rcParam to control the weight of the title

### `axes.formatter.useoffset` added[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#axes-formatter-useoffset-added "Link to this heading")

Controls the default value of _useOffset_ in [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
. If [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 and the data range is much smaller than the data average, then an offset will be determined such that the tick labels are meaningful. If [`False`](https://docs.python.org/3/library/constants.html#False "(in Python v3.14)")
 then the full number will be formatted in all conditions.

### `nbagg.transparent` added[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#nbagg-transparent-added "Link to this heading")

Controls whether nbagg figures have a transparent background. `nbagg.transparent` is `True` by default.

### XDG compliance[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#xdg-compliance "Link to this heading")

Matplotlib now looks for configuration files (both rcparams and style) in XDG compliant locations.

[`style` package added](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#style-package-added "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can now easily switch between different styles using the new `style` package:

\>>> from matplotlib import style
\>>> style.use('dark\_background')

Subsequent plots will use updated colors, sizes, etc. To list all available styles, use:

\>>> print style.available

You can add your own custom `<style name>.mplstyle` files to `~/.matplotlib/stylelib` or call `use` with a URL pointing to a file with `matplotlibrc` settings.

_Note that this is an experimental feature_, and the interface may change as users test out this new feature.

[Backends](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#backends "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Qt5 backend[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#qt5-backend "Link to this heading")

Martin Fitzpatrick and Tom Badran implemented a Qt5 backend. The differences in namespace locations between Qt4 and Qt5 was dealt with by shimming Qt4 to look like Qt5, thus the Qt5 implementation is the primary implementation. Backwards compatibility for Qt4 is maintained by wrapping the Qt5 implementation.

The Qt5Agg backend currently does not work with IPython's %matplotlib magic.

The 1.4.0 release has a known bug where the toolbar is broken. This can be fixed by:

cd path/to/installed/matplotlib
wget https://github.com/matplotlib/matplotlib/pull/3322.diff
\# unix2dos 3322.diff (if on windows to fix line endings)
patch \-p2 < 3322.diff

### Qt4 backend[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#qt4-backend "Link to this heading")

Rudolf Höfler changed the appearance of the subplottool. All sliders are vertically arranged now, buttons for tight layout and reset were added. Furthermore, the subplottool is now implemented as a modal dialog. It was previously a QMainWindow, leaving the SPT open if one closed the plot window.

In the figure options dialog one can now choose to (re-)generate a simple automatic legend. Any explicitly set legend entries will be lost, but changes to the curves' label, linestyle, et cetera will now be updated in the legend.

Interactive performance of the Qt4 backend has been dramatically improved under windows.

The mapping of key-signals from Qt to values matplotlib understands was greatly improved (For both Qt4 and Qt5).

### Cairo backends[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#cairo-backends "Link to this heading")

The Cairo backends are now able to use the [cairocffi bindings](https://github.com/SimonSapin/cairocffi)
 which are more actively maintained than the [pycairo bindings](https://www.cairographics.org/pycairo/)
.

### Gtk3Agg backend[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#gtk3agg-backend "Link to this heading")

The Gtk3Agg backend now works on Python 3.x, if the [cairocffi bindings](https://github.com/SimonSapin/cairocffi)
 are installed.

### PDF backend[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#pdf-backend "Link to this heading")

Added context manager for saving to multi-page PDFs.

[Text](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#text "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Text URLs supported by SVG backend[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#text-urls-supported-by-svg-backend "Link to this heading")

The SVG backend will now render [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 objects' url as a link in output SVGs. This allows one to make clickable text in saved figures using the url kwarg of the [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 class.

### Anchored sizebar font[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#anchored-sizebar-font "Link to this heading")

Added the `fontproperties` kwarg to [`AnchoredSizeBar`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar.html#mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar "mpl_toolkits.axes_grid1.anchored_artists.AnchoredSizeBar")
 to control the font properties.

[Sphinx extensions](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#sphinx-extensions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `:context:` directive in the [`plot_directive`](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html#module-matplotlib.sphinxext.plot_directive "matplotlib.sphinxext.plot_directive")
 Sphinx extension can now accept an optional `reset` setting, which will cause the context to be reset. This allows more than one distinct context to be present in documentation. To enable this option, use `:context: reset` instead of `:context:` any time you want to reset the context.

[Legend and PathEffects documentation](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#legend-and-patheffects-documentation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 and [Path effects guide](https://matplotlib.org/stable/users/explain/artists/patheffects_guide.html#patheffects-guide)
 have both been updated to better reflect the full potential of each of these powerful features.

[Widgets](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#widgets "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Span Selector[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#span-selector "Link to this heading")

Added an option `span_stays` to the [`SpanSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector "matplotlib.widgets.SpanSelector")
 which makes the selector rectangle stay on the axes after you release the mouse.

[GAE integration](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_1.4.html#gae-integration "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Matplotlib will now run on google app engine.

On this page