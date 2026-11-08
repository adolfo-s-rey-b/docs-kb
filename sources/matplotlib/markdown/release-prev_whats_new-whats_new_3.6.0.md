[Skip to main content](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#main-content)

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
    

[What's new in Matplotlib 3.6.0 (Sep 15, 2022)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id1)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#what-s-new-in-matplotlib-3-6-0-sep-15-2022 "Link to this heading")

================================================================================================================================================================================================================================================================================

For a list of all of the issues and pull requests since the last revision, see the [GitHub statistics for 3.11.2 (Sep 10, 2026)](https://matplotlib.org/stable/release/github_stats.html#github-stats)
.

[Figure and Axes creation / management](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id2)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#figure-and-axes-creation-management "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`subplots`, `subplot_mosaic` accept _height\_ratios_ and _width\_ratios_ arguments](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id3)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#subplots-subplot-mosaic-accept-height-ratios-and-width-ratios-arguments "Link to this heading")

The relative width and height of columns and rows in [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 and [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
 can be controlled by passing _height\_ratios_ and _width\_ratios_ keyword arguments to the methods:

fig \= plt.figure()
axs \= fig.subplots(3, 1, sharex\=True, height\_ratios\=\[3, 1, 1\])

([`Source code`](https://matplotlib.org/stable/_downloads/7cd2b6da99331fb721667b0061c9507f/whats_new_3-6-0-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/c3619df72a4d2845775de993fff1fc1b/whats_new_3-6-0-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/c06f00bca53a982be5fc90788309169c/whats_new_3-6-0-1.png)
)

[![A figure with three subplots in three rows and one column. The height of the subplot in the first row is three times than the subplots in the 2nd and 3rd row.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-1.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-1.2x.png)

Previously, this required passing the ratios in _gridspec\_kw_ arguments:

fig \= plt.figure()
axs \= fig.subplots(3, 1, sharex\=True,
                   gridspec\_kw\=dict(height\_ratios\=\[3, 1, 1\]))

### [Constrained layout is no longer considered experimental](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id4)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#constrained-layout-is-no-longer-considered-experimental "Link to this heading")

The constrained layout engine and API is no longer considered experimental. Arbitrary changes to behaviour and API are no longer permitted without a deprecation period.

### [New `layout_engine` module](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id5)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#new-layout-engine-module "Link to this heading")

Matplotlib ships with `tight_layout` and `constrained_layout` layout engines. A new [`layout_engine`](https://matplotlib.org/stable/api/layout_engine_api.html#module-matplotlib.layout_engine "matplotlib.layout_engine")
 module is provided to allow downstream libraries to write their own layout engines and [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 objects can now take a [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
 subclass as an argument to the _layout_ parameter.

### [Compressed layout for fixed-aspect ratio Axes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id6)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#compressed-layout-for-fixed-aspect-ratio-axes "Link to this heading")

Simple arrangements of Axes with fixed aspect ratios can now be packed together with `fig, axs = plt.subplots(2, 3, layout='compressed')`.

With `layout='tight'` or `'constrained'`, Axes with a fixed aspect ratio can leave large gaps between each other:

([`Source code`](https://matplotlib.org/stable/_downloads/aa71eb40de94eda8dda77cd6f0f83859/whats_new_3-6-0-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/ecee5c182d8a9f9e1e3db7f65d547b51/whats_new_3-6-0-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/f607fc3d020e330032a1602f347d5244/whats_new_3-6-0-2.png)
)

[![A figure labelled "fixed-aspect plots, layout=constrained". Figure has subplots displayed in 2 rows and 2 columns; Subplots have large gaps between each other.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-2.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-2.2x.png)

Using the `layout='compressed'` layout reduces the space between the Axes, and adds the extra space to the outer margins:

([`Source code`](https://matplotlib.org/stable/_downloads/e601d85fb810271305e651a4ee43f996/whats_new_3-6-0-3.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/f689827510166547239b86978a2122ad/whats_new_3-6-0-3.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/cf5c9dce99a30ec8a671629954f86f71/whats_new_3-6-0-3.png)
)

[![Four identical two by two heatmaps, each cell a different color: purple, blue, yellow, green going clockwise from upper left corner. The four heatmaps are laid out in a two by two grid with minimum white space between the heatmaps.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-3.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-3.2x.png)

See [Grids of fixed aspect-ratio Axes: "compressed" layout](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#compressed-layout)
 for further details.

### [Layout engines may now be removed](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id7)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#layout-engines-may-now-be-removed "Link to this heading")

The layout engine on a Figure may now be removed by calling [`Figure.set_layout_engine`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html#matplotlib.figure.Figure.set_layout_engine "matplotlib.figure.Figure.set_layout_engine")
 with `'none'`. This may be useful after computing layout in order to reduce computations, e.g., for subsequent animation loops.

A different layout engine may be set afterwards, so long as it is compatible with the previous layout engine.

### [`Axes.inset_axes` flexibility](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id8)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#axes-inset-axes-flexibility "Link to this heading")

[`matplotlib.axes.Axes.inset_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes")
 now accepts the _projection_, _polar_ and _axes\_class_ keyword arguments, so that subclasses of [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 may be returned.

fig, ax \= plt.subplots()

ax.plot(\[0, 2\], \[1, 2\])

polar\_ax \= ax.inset\_axes(\[0.75, 0.25, 0.2, 0.2\], projection\='polar')
polar\_ax.plot(\[0, 2\], \[1, 2\])

([`Source code`](https://matplotlib.org/stable/_downloads/10dd6cb2ca6bb3701da453452b8d0dcb/whats_new_3-6-0-4.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/04b9472891d123497a4bc38ea978bff3/whats_new_3-6-0-4.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/fc3fa506cec4e3e0c8149395a8583f37/whats_new_3-6-0-4.png)
)

[![Plot of a straight line y=x, with a small inset axes in the lower right corner that shows a circle with radial grid lines and a line plotted in polar coordinates.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-4.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-4.2x.png)

### [WebP is now a supported output format](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id9)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#webp-is-now-a-supported-output-format "Link to this heading")

Figures may now be saved in WebP format by using the `.webp` file extension, or passing `format='webp'` to [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
. This relies on [Pillow](https://pillow.readthedocs.io/en/latest/)
 support for WebP.

### [Garbage collection is no longer run on figure close](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id10)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#garbage-collection-is-no-longer-run-on-figure-close "Link to this heading")

Matplotlib has a large number of circular references (between Figure and Manager, between Axes and Figure, Axes and Artist, Figure and Canvas, etc.) so when the user drops their last reference to a Figure (and clears it from pyplot's state), the objects will not immediately be deleted.

To account for this we have long (since before 2004) had a [`gc.collect`](https://docs.python.org/3/library/gc.html#gc.collect "(in Python v3.14)")
 (of the lowest two generations only) in the closing code in order to promptly clean up after ourselves. However this is both not doing what we want (as most of our objects will actually survive) and due to clearing out the first generation opened us up to having unbounded memory usage.

In cases with a very tight loop between creating the figure and destroying it (e.g. `plt.figure(); plt.close()`) the first generation will never grow large enough for Python to consider running the collection on the higher generations. This will lead to unbounded memory usage as the long-lived objects are never re-considered to look for reference cycles and hence are never deleted.

We now no longer do any garbage collection when a figure is closed, and rely on Python automatically deciding to run garbage collection periodically. If you have strict memory requirements, you can call [`gc.collect`](https://docs.python.org/3/library/gc.html#gc.collect "(in Python v3.14)")
 yourself but this may have performance impacts in a tight computation loop.

[Plotting methods](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id11)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#plotting-methods "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Striped lines (experimental)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id12)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#striped-lines-experimental "Link to this heading")

The new _gapcolor_ parameter to [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 enables the creation of striped lines.

x \= np.linspace(1., 3., 10)
y \= x\*\*3

fig, ax \= plt.subplots()
ax.plot(x, y, linestyle\='--', color\='orange', gapcolor\='blue',
        linewidth\=3, label\='a striped line')
ax.legend()

([`Source code`](https://matplotlib.org/stable/_downloads/ef24883a4238c3b3a786c5294e66cf92/whats_new_3-6-0-5.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/ca6a80c6cbb06cac0b6eea5b69e935f6/whats_new_3-6-0-5.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/e3177f07ee946902a82dadd7edc838c5/whats_new_3-6-0-5.png)
)

[![Plot of x**3 where the line is an orange-blue striped line, achieved using the keywords linestyle='--', color='orange', gapcolor='blue'](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-5.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-5.2x.png)

### [Custom cap widths in box and whisker plots in `bxp` and `boxplot`](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id13)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#custom-cap-widths-in-box-and-whisker-plots-in-bxp-and-boxplot "Link to this heading")

The new _capwidths_ parameter to [`bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp")
 and [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
 allows controlling the widths of the caps in box and whisker plots.

x \= np.linspace(\-7, 7, 140)
x \= np.hstack(\[\-25, x, 25\])
capwidths \= \[0.01, 0.2\]

fig, ax \= plt.subplots()
ax.boxplot(\[x, x\], notch\=True, capwidths\=capwidths)
ax.set\_title(f'{capwidths\=}')

([`Source code`](https://matplotlib.org/stable/_downloads/0936e35c7fe8b3d40b59c60685bca821/whats_new_3-6-0-6.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/c71ee47b756f36a4b80a282cd9e3562f/whats_new_3-6-0-6.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/fed270c3d3c2744af3c28fb9a98bae16/whats_new_3-6-0-6.png)
)

[![A box plot with capwidths 0.01 and 0.2](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-6.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-6.2x.png)

### [Easier labelling of bars in bar plot](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id14)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#easier-labelling-of-bars-in-bar-plot "Link to this heading")

The _label_ argument of [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
 and [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
 can now be passed a list of labels for the bars. The list must be the same length as _x_ and labels the individual bars. Repeated labels are not de-duplicated and will cause repeated label entries, so this is best used when bars also differ in style (e.g., by passing a list to _color_, as below.)

x \= \["a", "b", "c"\]
y \= \[10, 20, 15\]
color \= \['C0', 'C1', 'C2'\]

fig, ax \= plt.subplots()
ax.bar(x, y, color\=color, label\=x)
ax.legend()

([`Source code`](https://matplotlib.org/stable/_downloads/f019e012f664ac9d23c52d3d468495b9/whats_new_3-6-0-7.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/ae9fabdf9d0c4beb0daf7868af6f16c1/whats_new_3-6-0-7.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/5a90e942a3e612246400119738b8ab2e/whats_new_3-6-0-7.png)
)

[![Bar chart: blue bar height 10, orange bar height 20, green bar height 15 legend with blue box labeled a, orange box labeled b, and green box labeled c](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-7.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-7.2x.png)

### [New style format string for colorbar ticks](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id15)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#new-style-format-string-for-colorbar-ticks "Link to this heading")

The _format_ argument of [`colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 (and other colorbar methods) now accepts `{}`\-style format strings.

fig, ax \= plt.subplots()
im \= ax.imshow(z)
fig.colorbar(im, format\='{x:.2e}')  \# Instead of '%.2e'

### [Linestyles for negative contours may be set individually](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id16)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#linestyles-for-negative-contours-may-be-set-individually "Link to this heading")

The line style of negative contours may be set by passing the _negative\_linestyles_ argument to [`Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
. Previously, this style could only be set globally via `[rcParams["contour.negative_linestyle"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=contour.negative_linestyle#rcparam-contour-negative-linestyle) ` (default: `'dashed'`).

delta \= 0.025
x \= np.arange(\-3.0, 3.0, delta)
y \= np.arange(\-2.0, 2.0, delta)
X, Y \= np.meshgrid(x, y)
Z1 \= np.exp(\-X\*\*2 \- Y\*\*2)
Z2 \= np.exp(\-(X \- 1)\*\*2 \- (Y \- 1)\*\*2)
Z \= (Z1 \- Z2) \* 2

fig, axs \= plt.subplots(1, 2)

CS \= axs\[0\].contour(X, Y, Z, 6, colors\='k')
axs\[0\].clabel(CS, fontsize\=9, inline\=True)
axs\[0\].set\_title('Default negative contours')

CS \= axs\[1\].contour(X, Y, Z, 6, colors\='k', negative\_linestyles\='dotted')
axs\[1\].clabel(CS, fontsize\=9, inline\=True)
axs\[1\].set\_title('Dotted negative contours')

([`Source code`](https://matplotlib.org/stable/_downloads/4064e2d59e4f6fc99d4dec99976e3eac/whats_new_3-6-0-8.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/2a5129b8714ea7e1416ae11bf3865d65/whats_new_3-6-0-8.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/c06a485797eb8ec3f46cea06ef576365/whats_new_3-6-0-8.png)
)

[![Two contour plots, each showing two positive and two negative contours. The positive contours are shown in solid black lines in both plots. In one plot the negative contours are shown in dashed lines, which is the current styling. In the other plot they're shown in dotted lines, which is one of the new options.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-8.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-8.2x.png)

### [Improved quad contour calculations via ContourPy](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id17)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#improved-quad-contour-calculations-via-contourpy "Link to this heading")

The contouring functions [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour")
 and [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
 have a new keyword argument _algorithm_ to control which algorithm is used to calculate the contours. There is a choice of four algorithms to use, and the default is to use `algorithm='mpl2014'` which is the same algorithm that Matplotlib has been using since 2014.

Previously Matplotlib shipped its own C++ code for calculating the contours of quad grids. Now the external library [ContourPy](https://github.com/contourpy/contourpy)
 is used instead.

Other possible values of the _algorithm_ keyword argument at this time are `'mpl2005'`, `'serial'` and `'threaded'`; see the [ContourPy documentation](https://contourpy.readthedocs.io/)
 for further details.

Note

Contour lines and polygons produced by `algorithm='mpl2014'` will be the same as those produced before this change to within floating-point tolerance. The exception is for duplicate points, i.e. contours containing adjacent (x, y) points that are identical; previously the duplicate points were removed, now they are kept. Contours affected by this will produce the same visual output, but there will be a greater number of points in the contours.

The locations of contour labels obtained by using [`clabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html#matplotlib.axes.Axes.clabel "matplotlib.axes.Axes.clabel")
 may also be different.

### [`errorbar` supports _markerfacecoloralt_](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id18)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#errorbar-supports-markerfacecoloralt "Link to this heading")

The _markerfacecoloralt_ parameter is now passed to the line plotter from [`Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
. The documentation now accurately lists which properties are passed to [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, rather than claiming that all keyword arguments are passed on.

x \= np.arange(0.1, 4, 0.5)
y \= np.exp(\-x)

fig, ax \= plt.subplots()
ax.errorbar(x, y, xerr\=0.2, yerr\=0.4,
            linestyle\=':', color\='darkgrey',
            marker\='o', markersize\=20, fillstyle\='left',
            markerfacecolor\='tab:blue', markerfacecoloralt\='tab:orange',
            markeredgecolor\='tab:brown', markeredgewidth\=2)

([`Source code`](https://matplotlib.org/stable/_downloads/847f312b8a9693b78021225644e337e1/whats_new_3-6-0-9.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/78628157290bd6c4c720c98c32af0846/whats_new_3-6-0-9.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/3c92153f023ef2b5eaec1758191bc9c5/whats_new_3-6-0-9.png)
)

[![Graph with error bar showing ±0.2 error on the x-axis, and ±0.4 error on the y-axis. Error bar marker is a circle radius 20. Error bar face color is blue.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-9.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-9.2x.png)

### [`streamplot` can disable streamline breaks](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id19)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#streamplot-can-disable-streamline-breaks "Link to this heading")

It is now possible to specify that streamplots have continuous, unbroken streamlines. Previously streamlines would end to limit the number of lines within a single grid cell. See the difference between the plots below:

([`Source code`](https://matplotlib.org/stable/_downloads/2e718a72cd05b533f170921a539bec0d/whats_new_3-6-0-10.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/520122d7af3ad5557759531981faf819/whats_new_3-6-0-10.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/57fbc23709b5fca188ecba8a391543aa/whats_new_3-6-0-10.png)
)

[![A figure with two streamplots. First streamplot has broken streamlines. Second streamplot has continuous streamlines.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-10.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-10.2x.png)

### [New axis scale `asinh` (experimental)](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id20)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#new-axis-scale-asinh-experimental "Link to this heading")

The new `asinh` axis scale offers an alternative to `symlog` that smoothly transitions between the quasi-linear and asymptotically logarithmic regions of the scale. This is based on an arcsinh transformation that allows plotting both positive and negative values that span many orders of magnitude.

([`Source code`](https://matplotlib.org/stable/_downloads/598949647b3fdb5b7d603141259b293f/whats_new_3-6-0-11.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/584932b99087c1d6fac948ccedf1ec86/whats_new_3-6-0-11.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/45cc69ddb2ea529a1f0ff93fd9e5489c/whats_new_3-6-0-11.png)
)

[![Figure with 2 subplots. Subplot on the left uses symlog scale on the y axis. The transition at -2 is not smooth. Subplot on the right use asinh scale. The transition at -2 is smooth.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-11.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-11.2x.png)

### [`stairs(..., fill=True)` hides patch edge by setting linewidth](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id21)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#stairs-fill-true-hides-patch-edge-by-setting-linewidth "Link to this heading")

`stairs(..., fill=True)` would previously hide Patch edges by setting `edgecolor="none"`. Consequently, calling `set_color()` on the Patch later would make the Patch appear larger.

Now, by using `linewidth=0`, this apparent size change is prevented. Likewise calling `stairs(..., fill=True, linewidth=3)` will behave more transparently.

### [Fix the dash offset of the Patch class](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id22)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#fix-the-dash-offset-of-the-patch-class "Link to this heading")

Formerly, when setting the line style on a [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 object using a dash tuple, the offset was ignored. Now the offset is applied to the Patch as expected and it can be used as it is used with [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 objects.

### [Rectangle patch rotation point](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id23)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#rectangle-patch-rotation-point "Link to this heading")

The rotation point of the [`Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 can now be set to 'xy', 'center' or a 2-tuple of numbers using the _rotation\_point_ argument.

([`Source code`](https://matplotlib.org/stable/_downloads/66ff405070d277643342980a4bc510e8/whats_new_3-6-0-12.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/806cd76732e21345c25660240c9fb61b/whats_new_3-6-0-12.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/ce4dd0d205912d8c94c9f867f46a7dca/whats_new_3-6-0-12.png)
)

[![Blue square that isn't rotated. Green square rotated 45 degrees relative to center. Orange square rotated 45 degrees relative to lower right corner. Red square rotated 45 degrees relative to point in upper right quadrant.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-12.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-12.2x.png)

[Colors and colormaps](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id24)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#colors-and-colormaps "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Color sequence registry](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id25)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#color-sequence-registry "Link to this heading")

The color sequence registry, [`ColorSequenceRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry "matplotlib.colors.ColorSequenceRegistry")
, contains sequences (i.e., simple lists) of colors that are known to Matplotlib by name. This will not normally be used directly, but through the universal instance at [`matplotlib.color_sequences`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.color_sequences "matplotlib.color_sequences")
.

### [Colormap method for creating a different lookup table size](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id26)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#colormap-method-for-creating-a-different-lookup-table-size "Link to this heading")

The new method [`Colormap.resampled`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.resampled "matplotlib.colors.Colormap.resampled")
 creates a new [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 instance with the specified lookup table size. This is a replacement for manipulating the lookup table size via `get_cmap`.

Use:

get\_cmap(name).resampled(N)

instead of:

get\_cmap(name, lut\=N)

### [Setting norms with strings](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id27)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#setting-norms-with-strings "Link to this heading")

Norms can now be set (e.g. on images) using the string name of the corresponding scale, e.g. `imshow(array, norm="log")`. Note that in that case, it is permissible to also pass _vmin_ and _vmax_, as a new Norm instance will be created under the hood.

[Titles, ticks, and labels](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id28)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#titles-ticks-and-labels "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`plt.xticks` and `plt.yticks` support _minor_ keyword argument](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id29)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#plt-xticks-and-plt-yticks-support-minor-keyword-argument "Link to this heading")

It is now possible to set or get minor ticks using [`pyplot.xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks")
 and [`pyplot.yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks")
 by setting `minor=True`.

plt.figure()
plt.plot(\[1, 2, 3, 3.5\], \[2, 1, 0, \-0.5\])
plt.xticks(\[1, 2, 3\], \["One", "Zwei", "Trois"\])
plt.xticks(\[np.sqrt(2), 2.5, np.pi\],
           \[r"$\\sqrt{2}$", r"$\\frac{5}{2}$", r"$\\pi$"\], minor\=True)

([`Source code`](https://matplotlib.org/stable/_downloads/ead90d519e2789eb5c06fa95cfb906c6/whats_new_3-6-0-13.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/734615da13704cb7a53503cccc53f1e1/whats_new_3-6-0-13.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/5c971c242dcea85b3c74b1da381716eb/whats_new_3-6-0-13.png)
)

[![Plot showing a line from 1,2 to 3.5,-0.5. X axis showing the 1, 2 and 3 minor ticks on the x axis as One, Zwei, Trois.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-13.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-13.2x.png)

[Legends](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id30)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#legends "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Legend can control alignment of title and handles](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id31)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#legend-can-control-alignment-of-title-and-handles "Link to this heading")

[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")
 now supports controlling the alignment of the title and handles via the keyword argument _alignment_. You can also use [`Legend.set_alignment`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.set_alignment "matplotlib.legend.Legend.set_alignment")
 to control the alignment on existing Legends.

fig, axs \= plt.subplots(3, 1)
for i, alignment in enumerate(\['left', 'center', 'right'\]):
    axs\[i\].plot(range(10), label\='test')
    axs\[i\].legend(title\=f'{alignment\=}', alignment\=alignment)

([`Source code`](https://matplotlib.org/stable/_downloads/b49d9f07c6ef1411d0e66cb7ff2540c4/whats_new_3-6-0-14.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/e53f7606375e52a0918055f6c6cfb1a8/whats_new_3-6-0-14.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/430b24a89b7c0e8559a741ac4efb659e/whats_new_3-6-0-14.png)
)

[![Figure with 3 subplots. All the subplots are titled test. The three subplots have legends titled alignment='left', alignment='center', alignment='right'. The legend texts are respectively aligned left, center and right.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-14.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-14.2x.png)

### [_ncol_ keyword argument to `legend` renamed to _ncols_](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id32)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#ncol-keyword-argument-to-legend-renamed-to-ncols "Link to this heading")

The _ncol_ keyword argument to [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
 for controlling the number of columns is renamed to _ncols_ for consistency with the _ncols_ and _nrows_ keywords of [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 and [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
. _ncol_ remains supported for backwards compatibility, but is discouraged.

[Markers](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id33)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#markers "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`marker` can now be set to the string "none"](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id34)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#marker-can-now-be-set-to-the-string-none "Link to this heading")

The string "none" means _no-marker_, consistent with other APIs which support the lowercase version. Using "none" is recommended over using "None", to avoid confusion with the None object.

### [Customization of `MarkerStyle` join and cap style](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id35)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#customization-of-markerstyle-join-and-cap-style "Link to this heading")

New [`MarkerStyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.markers.MarkerStyle.html#matplotlib.markers.MarkerStyle "matplotlib.markers.MarkerStyle")
 parameters allow control of join style and cap style, and for the user to supply a transformation to be applied to the marker (e.g. a rotation).

from matplotlib.markers import CapStyle, JoinStyle, MarkerStyle
from matplotlib.transforms import Affine2D

fig, axs \= plt.subplots(3, 1, layout\='constrained')
for ax in axs:
    ax.axis('off')
    ax.set\_xlim(\-0.5, 2.5)

axs\[0\].set\_title('Cap styles', fontsize\=14)
for col, cap in enumerate(CapStyle):
    axs\[0\].plot(col, 0, markersize\=32, markeredgewidth\=8,
                marker\=MarkerStyle('1', capstyle\=cap))
    \# Show the marker edge for comparison with the cap.
    axs\[0\].plot(col, 0, markersize\=32, markeredgewidth\=1,
                markerfacecolor\='none', markeredgecolor\='lightgrey',
                marker\=MarkerStyle('1'))
    axs\[0\].annotate(cap.name, (col, 0),
                    xytext\=(20, \-5), textcoords\='offset points')

axs\[1\].set\_title('Join styles', fontsize\=14)
for col, join in enumerate(JoinStyle):
    axs\[1\].plot(col, 0, markersize\=32, markeredgewidth\=8,
                marker\=MarkerStyle('\*', joinstyle\=join))
    \# Show the marker edge for comparison with the join.
    axs\[1\].plot(col, 0, markersize\=32, markeredgewidth\=1,
                markerfacecolor\='none', markeredgecolor\='lightgrey',
                marker\=MarkerStyle('\*'))
    axs\[1\].annotate(join.name, (col, 0),
                    xytext\=(20, \-5), textcoords\='offset points')

axs\[2\].set\_title('Arbitrary transforms', fontsize\=14)
for col, (size, rot) in enumerate(zip(\[2, 5, 7\], \[0, 45, 90\])):
    t \= Affine2D().rotate\_deg(rot).scale(size)
    axs\[2\].plot(col, 0, marker\=MarkerStyle('\*', transform\=t))

([`Source code`](https://matplotlib.org/stable/_downloads/891a8e5b575ffd83b1f4360636b9b214/whats_new_3-6-0-15.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/7eb5382a8a46eddd032b7e12c561ed43/whats_new_3-6-0-15.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/a4c398e524d0e5d74fa89d95309a4293/whats_new_3-6-0-15.png)
)

[![Three rows of markers, columns are blue, green, and purple. First row is y-shaped markers with different capstyles: butt, end is squared off at endpoint; projecting, end is squared off at short distance from endpoint; round, end is rounded. Second row is star-shaped markers with different join styles: miter, star points are sharp triangles; round, star points are rounded; bevel, star points are beveled. Last row shows stars rotated at different angles: small star rotated 0 degrees - top point vertical; medium star rotated 45 degrees - top point tilted right; large star rotated 90 degrees - top point tilted left.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-15.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-15.2x.png)

[Fonts and Text](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id36)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#fonts-and-text "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Font fallback](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id37)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#font-fallback "Link to this heading")

It is now possible to specify a list of fonts families and Matplotlib will try them in order to locate a required glyph.

plt.rcParams\["font.size"\] \= 20
fig \= plt.figure(figsize\=(4.75, 1.85))

text \= "There are 几个汉字 in between!"
fig.text(0.05, 0.65, text, family\=\["Noto Sans CJK JP", "Noto Sans TC"\])
fig.text(0.05, 0.45, text, family\=\["DejaVu Sans", "Noto Sans CJK JP", "Noto Sans TC"\])

([`Source code`](https://matplotlib.org/stable/_downloads/7146582925f78826041ecdfb89b4576b/whats_new_3-6-0-16.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/aae7a61a12a2fec87beb915aeb6b97db/whats_new_3-6-0-16.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/a7f7d0f752c5d61be8a247cba9a97e4f/whats_new_3-6-0-16.png)
)

[![The phrase "There are 几个汉字 in between!" rendered in various fonts.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-16.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-16.2x.png)

Demonstration of mixed English and Chinese text with font fallback.

This currently works with the Agg (and all of the GUI embeddings), svg, pdf, ps, and inline backends.

### [List of available font names](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id38)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#list-of-available-font-names "Link to this heading")

The list of available fonts are now easily accessible. To get a list of the available font names in Matplotlib use:

from matplotlib import font\_manager
font\_manager.get\_font\_names()

### [`math_to_image` now has a _color_ keyword argument](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id39)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#math-to-image-now-has-a-color-keyword-argument "Link to this heading")

To easily support external libraries that rely on the MathText rendering of Matplotlib to generate equation images, a _color_ keyword argument was added to [`math_to_image`](https://matplotlib.org/stable/api/mathtext_api.html#matplotlib.mathtext.math_to_image "matplotlib.mathtext.math_to_image")
.

from matplotlib import mathtext
mathtext.math\_to\_image('$x^2$', 'filename.png', color\='Maroon')

### [Active URL area rotates with link text](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id40)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#active-url-area-rotates-with-link-text "Link to this heading")

When link text is rotated in a figure, the active URL area will now include the rotated link area. Previously, the active area remained in the original, non-rotated, position.

[rcParams improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id41)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#rcparams-improvements "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Allow setting figure label size and weight globally and separately from title](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id42)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#allow-setting-figure-label-size-and-weight-globally-and-separately-from-title "Link to this heading")

For figure labels, `Figure.supxlabel` and `Figure.supylabel`, the size and weight can be set separately from the figure title using `[rcParams["figure.labelsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.labelsize#rcparam-figure-labelsize) ` (default: `'large'`) and `[rcParams["figure.labelweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.labelweight#rcparam-figure-labelweight) ` (default: `'normal'`).

\# Original (previously combined with below) rcParams:
plt.rcParams\['figure.titlesize'\] \= 64
plt.rcParams\['figure.titleweight'\] \= 'bold'

\# New rcParams:
plt.rcParams\['figure.labelsize'\] \= 32
plt.rcParams\['figure.labelweight'\] \= 'bold'

fig, axs \= plt.subplots(2, 2, layout\='constrained')
for ax in axs.flat:
    ax.set(xlabel\='xlabel', ylabel\='ylabel')

fig.suptitle('suptitle')
fig.supxlabel('supxlabel')
fig.supylabel('supylabel')

([`Source code`](https://matplotlib.org/stable/_downloads/19f2fa0796f5616688c56760af7bf090/whats_new_3-6-0-17.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/37b1cb1845401de745fdbcc20bc3c73d/whats_new_3-6-0-17.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/a7bd3c9df9a9ab2b8058a24b83c7dc0c/whats_new_3-6-0-17.png)
)

[![A figure with 4 plots organised in 2 rows and 2 columns. The title of the figure is suptitle in bold and 64 points. The x axis is labelled supxlabel, and y axis is labelled subylabel. Both labels are 32 points and bold.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-17.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-17.2x.png)

Note that if you have changed `[rcParams["figure.titlesize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titlesize#rcparam-figure-titlesize) ` (default: `'large'`) or `[rcParams["figure.titleweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titleweight#rcparam-figure-titleweight) ` (default: `'normal'`), you must now also change the introduced parameters for a result consistent with past behaviour.

### [Mathtext parsing can be disabled globally](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id43)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#mathtext-parsing-can-be-disabled-globally "Link to this heading")

The `[rcParams["text.parse_math"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.parse_math#rcparam-text-parse-math) ` (default: `True`) setting may be used to disable parsing of mathtext in all [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 objects (most notably from the [`Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
 method).

### [Double-quoted strings in matplotlibrc](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id44)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#double-quoted-strings-in-matplotlibrc "Link to this heading")

You can now use double-quotes around strings. This allows using the '#' character in strings. Without quotes, '#' is interpreted as start of a comment. In particular, you can now define hex-colors:

grid.color: "#b0b0b0"

[3D Axes improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id45)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#d-axes-improvements "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Standardized views for primary plane viewing angles](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id46)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#standardized-views-for-primary-plane-viewing-angles "Link to this heading")

When viewing a 3D plot in one of the primary view planes (i.e., perpendicular to the XY, XZ, or YZ planes), the Axis will be displayed in a standard location. For further information on 3D views, see [mplot3d View Angles](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#toolkit-mplot3d-view-angles)
 and [Primary 3D view planes](https://matplotlib.org/stable/gallery/mplot3d/view_planes_3d.html)
.

### [Custom focal length for 3D camera](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id47)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#custom-focal-length-for-3d-camera "Link to this heading")

The 3D Axes can now better mimic real-world cameras by specifying the focal length of the virtual camera. The default focal length of 1 corresponds to a Field of View (FOV) of 90°, and is backwards-compatible with existing 3D plots. An increased focal length between 1 and infinity "flattens" the image, while a decreased focal length between 1 and 0 exaggerates the perspective and gives the image more apparent depth.

The focal length can be calculated from a desired FOV via the equation:

![](https://matplotlib.org/stable/_images/mathmpl/math-54442dfe2e-2x.png)

from mpl\_toolkits.mplot3d import axes3d

X, Y, Z \= axes3d.get\_test\_data(0.05)

fig, axs \= plt.subplots(1, 3, figsize\=(7, 4),
                        subplot\_kw\={'projection': '3d'})

for ax, focal\_length in zip(axs, \[0.2, 1, np.inf\]):
    ax.plot\_wireframe(X, Y, Z, rstride\=10, cstride\=10)
    ax.set\_proj\_type('persp', focal\_length\=focal\_length)
    ax.set\_title(f"{focal\_length\=}")

([`Source code`](https://matplotlib.org/stable/_downloads/1a23bf8e3a025ffe996bfbc0c862f885/whats_new_3-6-0-18.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/9f17a1d3c0ff45afea0e6f107fa57fdd/whats_new_3-6-0-18.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/c6cb2eab476f9795dd23a82528172d0b/whats_new_3-6-0-18.png)
)

[![A figure showing 3 basic 3D Wireframe plots. From left to right, the plots use focal length of 0.2, 1 and infinity. Focal length between 0.2 and 1 produce plot with depth while focal length between 1 and infinity show relatively flattened image.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-18.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-18.2x.png)

### [3D plots gained a 3rd "roll" viewing angle](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id48)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#d-plots-gained-a-3rd-roll-viewing-angle "Link to this heading")

3D plots can now be viewed from any orientation with the addition of a 3rd roll angle, which rotates the plot about the viewing axis. Interactive rotation using the mouse still only controls elevation and azimuth, meaning that this feature is relevant to users who create more complex camera angles programmatically. The default roll angle of 0 is backwards-compatible with existing 3D plots.

from mpl\_toolkits.mplot3d import axes3d

X, Y, Z \= axes3d.get\_test\_data(0.05)

fig, ax \= plt.subplots(subplot\_kw\={'projection': '3d'})

ax.plot\_wireframe(X, Y, Z, rstride\=10, cstride\=10)
ax.view\_init(elev\=0, azim\=0, roll\=30)
ax.set\_title('elev=0, azim=0, roll=30')

([`Source code`](https://matplotlib.org/stable/_downloads/6f41f095a18b4d2d021b3c723c0bf62e/whats_new_3-6-0-19.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/9b50bddd24b18f8c76b10e65e98a235a/whats_new_3-6-0-19.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/794f32143a39354ca9be0ac537b3b2f4/whats_new_3-6-0-19.png)
)

[![View of a wireframe of a 3D contour that is somewhat a thickened s shape. Elevation and azimuth are 0 degrees so the shape is viewed straight on, but tilted because the roll is 30 degrees.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-19.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-19.2x.png)

### [Equal aspect ratio for 3D plots](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id49)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#equal-aspect-ratio-for-3d-plots "Link to this heading")

Users can set the aspect ratio for the X, Y, Z axes of a 3D plot to be 'equal', 'equalxy', 'equalxz', or 'equalyz' rather than the default of 'auto'.

from itertools import combinations, product

aspects \= \[\
    \['auto', 'equal', '.'\],\
    \['equalxy', 'equalyz', 'equalxz'\],\
\]
fig, axs \= plt.subplot\_mosaic(aspects, figsize\=(7, 6),
                              subplot\_kw\={'projection': '3d'})

\# Draw rectangular cuboid with side lengths \[1, 1, 5\]
r \= \[0, 1\]
scale \= np.array(\[1, 1, 5\])
pts \= combinations(np.array(list(product(r, r, r))), 2)
for start, end in pts:
    if np.sum(np.abs(start \- end)) \== r\[1\] \- r\[0\]:
        for ax in axs.values():
            ax.plot3D(\*zip(start\*scale, end\*scale), color\='C0')

\# Set the aspect ratios
for aspect, ax in axs.items():
    ax.set\_box\_aspect((3, 4, 5))
    ax.set\_aspect(aspect)
    ax.set\_title(f'set\_aspect({aspect!r})')

([`Source code`](https://matplotlib.org/stable/_downloads/c43b213b2222d60dd0e7b72cba857617/whats_new_3-6-0-20.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/0211e3a853237992e3aa4ac63431d1e7/whats_new_3-6-0-20.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/5947b27bd271ba296bf61fac19e006f5/whats_new_3-6-0-20.png)
)

[![Five plots, each showing a different aspect option for a rectangle that has height 4, depth 1, and width 1. auto: none of the dimensions have equal aspect, depth and width form a rectangular and height appears shrunken in proportion. equal: all the dimensions have equal aspect. equalxy: width and depth equal, height not so looks shrunken in proportion. equalyz: depth and height equal, width not so elongated. equalxz: width and height equal, depth not so elongated.](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-20.2x.png)](https://matplotlib.org/stable/_images/release-prev_whats_new-whats_new_3-6-0-20.2x.png)

[Interactive tool improvements](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id50)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#interactive-tool-improvements "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Rotation, aspect ratio correction and add/remove state](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id51)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#rotation-aspect-ratio-correction-and-add-remove-state "Link to this heading")

The [`RectangleSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.RectangleSelector.html#matplotlib.widgets.RectangleSelector "matplotlib.widgets.RectangleSelector")
 and [`EllipseSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.EllipseSelector.html#matplotlib.widgets.EllipseSelector "matplotlib.widgets.EllipseSelector")
 can now be rotated interactively between -45° and 45°. The range limits are currently dictated by the implementation. The rotation is enabled or disabled by striking the _r_ key ('r' is the default key mapped to 'rotate' in _state\_modifier\_keys_) or by calling `selector.add_state('rotate')`.

The aspect ratio of the axes can now be taken into account when using the "square" state. This is enabled by specifying `use_data_coordinates='True'` when the selector is initialized.

In addition to changing selector state interactively using the modifier keys defined in _state\_modifier\_keys_, the selector state can now be changed programmatically using the _add\_state_ and _remove\_state_ methods.

from matplotlib.widgets import RectangleSelector

values \= np.arange(0, 100)

fig \= plt.figure()
ax \= fig.add\_subplot()
ax.plot(values, values)

selector \= RectangleSelector(ax, print, interactive\=True,
                             drag\_from\_anywhere\=True,
                             use\_data\_coordinates\=True)
selector.add\_state('rotate')  \# alternatively press 'r' key
\# rotate the selector interactively

selector.remove\_state('rotate')  \# alternatively press 'r' key

selector.add\_state('square')

### [`MultiCursor` now supports Axes split over multiple figures](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id52)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#multicursor-now-supports-axes-split-over-multiple-figures "Link to this heading")

Previously, [`MultiCursor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib.widgets.MultiCursor "matplotlib.widgets.MultiCursor")
 only worked if all target Axes belonged to the same figure.

As a consequence of this change, the first argument to the [`MultiCursor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.MultiCursor.html#matplotlib.widgets.MultiCursor "matplotlib.widgets.MultiCursor")
 constructor has become unused (it was previously the joint canvas of all Axes, but the canvases are now directly inferred from the list of Axes).

### [`PolygonSelector` bounding boxes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id53)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#polygonselector-bounding-boxes "Link to this heading")

[`PolygonSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")
 now has a _draw\_bounding\_box_ argument, which when set to [`True`](https://docs.python.org/3/library/constants.html#True "(in Python v3.14)")
 will draw a bounding box around the polygon once it is complete. The bounding box can be resized and moved, allowing the points of the polygon to be easily resized.

### [Setting `PolygonSelector` vertices](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id54)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#setting-polygonselector-vertices "Link to this heading")

The vertices of [`PolygonSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector "matplotlib.widgets.PolygonSelector")
 can now be set programmatically by using the [`PolygonSelector.verts`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.PolygonSelector.html#matplotlib.widgets.PolygonSelector.verts "matplotlib.widgets.PolygonSelector.verts")
 property. Setting the vertices this way will reset the selector, and create a new complete selector with the supplied vertices.

### [`SpanSelector` widget can now be snapped to specified values](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id55)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#spanselector-widget-can-now-be-snapped-to-specified-values "Link to this heading")

The [`SpanSelector`](https://matplotlib.org/stable/api/_as_gen/matplotlib.widgets.SpanSelector.html#matplotlib.widgets.SpanSelector "matplotlib.widgets.SpanSelector")
 widget can now be snapped to values specified by the _snap\_values_ argument.

### [More toolbar icons are styled for dark themes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id56)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#more-toolbar-icons-are-styled-for-dark-themes "Link to this heading")

On the macOS and Tk backends, toolbar icons will now be inverted when using a dark theme.

[Platform-specific changes](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id57)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#platform-specific-changes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Wx backend uses standard toolbar](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id58)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#wx-backend-uses-standard-toolbar "Link to this heading")

Instead of a custom sizer, the toolbar is set on Wx windows as a standard toolbar.

### [Improvements to macosx backend](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id59)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#improvements-to-macosx-backend "Link to this heading")

#### [Modifier keys handled more consistently](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id60)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#modifier-keys-handled-more-consistently "Link to this heading")

The macosx backend now handles modifier keys in a manner more consistent with other backends. See the table in [Event connections](https://matplotlib.org/stable/users/explain/figure/event_handling.html#event-connections)
 for further information.

#### [`savefig.directory` rcParam support](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id61)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#savefig-directory-rcparam-support "Link to this heading")

The macosx backend will now obey the `[rcParams["savefig.directory"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.directory#rcparam-savefig-directory) ` (default: `'~'`) setting. If set to a non-empty string, then the save dialog will default to this directory, and preserve subsequent save directories as they are changed.

#### [`figure.raise_window` rcParam support](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id62)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#figure-raise-window-rcparam-support "Link to this heading")

The macosx backend will now obey the `[rcParams["figure.raise_window"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.raise_window#rcparam-figure-raise-window) ` (default: `True`) setting. If set to False, figure windows will not be raised to the top on update.

#### [Full-screen toggle support](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id63)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#full-screen-toggle-support "Link to this heading")

As supported on other backends, the macosx backend now supports toggling fullscreen view. By default, this view can be toggled by pressing the f key.

#### [Improved animation and blitting support](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id64)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#improved-animation-and-blitting-support "Link to this heading")

The macosx backend has been improved to fix blitting, animation frames with new artists, and to reduce unnecessary draw calls.

### [macOS application icon applied on Qt backend](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id65)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#macos-application-icon-applied-on-qt-backend "Link to this heading")

When using the Qt-based backends on macOS, the application icon will now be set, as is done on other backends/platforms.

### [New minimum macOS version](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id66)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#new-minimum-macos-version "Link to this heading")

The macosx backend now requires macOS >= 10.12.

### [Windows on ARM support](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#id67)
[#](https://matplotlib.org/stable/release/prev_whats_new/whats_new_3.6.0.html#windows-on-arm-support "Link to this heading")

Preliminary support for Windows on arm64 target has been added. This support requires FreeType 2.11 or above.

No binary wheels are available yet but it may be built from source.

On this page