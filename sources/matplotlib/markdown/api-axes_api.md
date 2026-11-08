[Skip to main content](https://matplotlib.org/stable/api/axes_api.html#main-content)

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
    

`matplotlib.axes`[#](https://matplotlib.org/stable/api/axes_api.html#matplotlib-axes "Link to this heading")

=============================================================================================================

The [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 class represents one (sub-)plot in a figure. It contains the plotted data, axis ticks, labels, title, legend, etc. Its methods are the main interface for manipulating the plot.

[The Axes class](https://matplotlib.org/stable/api/axes_api.html#id1)
[#](https://matplotlib.org/stable/api/axes_api.html#the-axes-class "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes") | An Axes object encapsulates all the elements of an individual (sub-)plot in a figure. |

### [Attributes](https://matplotlib.org/stable/api/axes_api.html#id2)
[#](https://matplotlib.org/stable/api/axes_api.html#attributes "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.viewLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.viewLim.html#matplotlib.axes.Axes.viewLim "matplotlib.axes.Axes.viewLim") | The view limits as [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")<br> in data coordinates. |
| [`Axes.dataLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.dataLim.html#matplotlib.axes.Axes.dataLim "matplotlib.axes.Axes.dataLim") | The bounding [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")<br> enclosing all data displayed in the Axes. |
| [`Axes.spines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spines.html#matplotlib.axes.Axes.spines "matplotlib.axes.Axes.spines") | The [`Spines`](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")<br> container for the Axes' spines, i.e. the lines denoting the data area boundaries. |
| [`Axes.transAxes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.transAxes.html#matplotlib.axes.Axes.transAxes "matplotlib.axes.Axes.transAxes") | The transformation from axes coordinates to display coordinates. |
| [`Axes.transData`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.transData.html#matplotlib.axes.Axes.transData "matplotlib.axes.Axes.transData") | The transformation from data coordinates to display coordinates. |

[Plotting](https://matplotlib.org/stable/api/axes_api.html#id3)
[#](https://matplotlib.org/stable/api/axes_api.html#plotting "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

### [Basic](https://matplotlib.org/stable/api/axes_api.html#id4)
[#](https://matplotlib.org/stable/api/axes_api.html#basic "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot") | Plot y versus x as lines and/or markers. |
| [`Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar") | Plot y versus x as lines and/or markers with attached errorbars. |
| [`Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter") | A scatter plot of _y_ vs. _x_ with varying marker size and/or color. |
| [`Axes.step`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.step.html#matplotlib.axes.Axes.step "matplotlib.axes.Axes.step") | Make a step plot. |
| [`Axes.loglog`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.loglog.html#matplotlib.axes.Axes.loglog "matplotlib.axes.Axes.loglog") | Make a plot with log scaling on both the x- and y-axis. |
| [`Axes.semilogx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogx.html#matplotlib.axes.Axes.semilogx "matplotlib.axes.Axes.semilogx") | Make a plot with log scaling on the x-axis. |
| [`Axes.semilogy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogy.html#matplotlib.axes.Axes.semilogy "matplotlib.axes.Axes.semilogy") | Make a plot with log scaling on the y-axis. |
| [`Axes.fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_between.html#matplotlib.axes.Axes.fill_between "matplotlib.axes.Axes.fill_between") | Fill the area between two horizontal curves. |
| [`Axes.fill_betweenx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx") | Fill the area between two vertical curves. |
| [`Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar") | Make a bar plot. |
| [`Axes.barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh") | Make a horizontal bar plot. |
| [`Axes.bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "matplotlib.axes.Axes.bar_label") | Label a bar plot. |
| [`Axes.grouped_bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grouped_bar.html#matplotlib.axes.Axes.grouped_bar "matplotlib.axes.Axes.grouped_bar") | Make a grouped bar plot. |
| [`Axes.stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stem.html#matplotlib.axes.Axes.stem "matplotlib.axes.Axes.stem") | Create a stem plot. |
| [`Axes.eventplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.eventplot.html#matplotlib.axes.Axes.eventplot "matplotlib.axes.Axes.eventplot") | Plot identical parallel lines at the given positions. |
| [`Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie") | Plot a pie chart. |
| [`Axes.pie_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label") | Label a pie chart. |
| [`Axes.stackplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stackplot.html#matplotlib.axes.Axes.stackplot "matplotlib.axes.Axes.stackplot") | Draw a stacked area plot or a streamgraph. |
| [`Axes.broken_barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.broken_barh.html#matplotlib.axes.Axes.broken_barh "matplotlib.axes.Axes.broken_barh") | Plot a horizontal sequence of rectangles. |
| [`Axes.vlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib.axes.Axes.vlines "matplotlib.axes.Axes.vlines") | Plot vertical lines at each _x_ from _ymin_ to _ymax_. |
| [`Axes.hlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hlines.html#matplotlib.axes.Axes.hlines "matplotlib.axes.Axes.hlines") | Plot horizontal lines at each _y_ from _xmin_ to _xmax_. |
| [`Axes.fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill") | Plot filled polygons. |

### [Spans](https://matplotlib.org/stable/api/axes_api.html#id5)
[#](https://matplotlib.org/stable/api/axes_api.html#spans "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.axhline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline") | Add a horizontal line spanning the whole or fraction of the Axes. |
| [`Axes.axhspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html#matplotlib.axes.Axes.axhspan "matplotlib.axes.Axes.axhspan") | Add a horizontal span (rectangle) across the Axes. |
| [`Axes.axvline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline") | Add a vertical line spanning the whole or fraction of the Axes. |
| [`Axes.axvspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvspan.html#matplotlib.axes.Axes.axvspan "matplotlib.axes.Axes.axvspan") | Add a vertical span (rectangle) across the Axes. |
| [`Axes.axline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html#matplotlib.axes.Axes.axline "matplotlib.axes.Axes.axline") | Add an infinitely long straight line. |

### [Spectral](https://matplotlib.org/stable/api/axes_api.html#id6)
[#](https://matplotlib.org/stable/api/axes_api.html#spectral "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.acorr`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.acorr.html#matplotlib.axes.Axes.acorr "matplotlib.axes.Axes.acorr") | Plot the autocorrelation of _x_. |
| [`Axes.angle_spectrum`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.angle_spectrum.html#matplotlib.axes.Axes.angle_spectrum "matplotlib.axes.Axes.angle_spectrum") | Plot the angle spectrum. |
| [`Axes.cohere`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.cohere.html#matplotlib.axes.Axes.cohere "matplotlib.axes.Axes.cohere") | Plot the coherence between _x_ and _y_. |
| [`Axes.csd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.csd.html#matplotlib.axes.Axes.csd "matplotlib.axes.Axes.csd") | Plot the cross-spectral density. |
| [`Axes.magnitude_spectrum`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.magnitude_spectrum.html#matplotlib.axes.Axes.magnitude_spectrum "matplotlib.axes.Axes.magnitude_spectrum") | Plot the magnitude spectrum. |
| [`Axes.phase_spectrum`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.phase_spectrum.html#matplotlib.axes.Axes.phase_spectrum "matplotlib.axes.Axes.phase_spectrum") | Plot the phase spectrum. |
| [`Axes.psd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.psd.html#matplotlib.axes.Axes.psd "matplotlib.axes.Axes.psd") | Plot the power spectral density. |
| [`Axes.specgram`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.specgram.html#matplotlib.axes.Axes.specgram "matplotlib.axes.Axes.specgram") | Plot a spectrogram. |
| [`Axes.xcorr`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xcorr.html#matplotlib.axes.Axes.xcorr "matplotlib.axes.Axes.xcorr") | Plot the cross correlation between _x_ and _y_. |

### [Statistics](https://matplotlib.org/stable/api/axes_api.html#id7)
[#](https://matplotlib.org/stable/api/axes_api.html#statistics "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.ecdf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ecdf.html#matplotlib.axes.Axes.ecdf "matplotlib.axes.Axes.ecdf") | Compute and plot the empirical cumulative distribution function of _x_. |
| [`Axes.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot") | Draw a box and whisker plot. |
| [`Axes.violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot") | Make a violin plot. |
| [`Axes.bxp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bxp.html#matplotlib.axes.Axes.bxp "matplotlib.axes.Axes.bxp") | Draw a box and whisker plot from pre-computed statistics. |
| [`Axes.violin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violin.html#matplotlib.axes.Axes.violin "matplotlib.axes.Axes.violin") | Draw a violin plot from pre-computed statistics. |

### [Binned](https://matplotlib.org/stable/api/axes_api.html#id8)
[#](https://matplotlib.org/stable/api/axes_api.html#binned "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hexbin.html#matplotlib.axes.Axes.hexbin "matplotlib.axes.Axes.hexbin") | Make a 2D hexagonal binning plot of points _x_, _y_. |
| [`Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist") | Compute and plot a histogram. |
| [`Axes.hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html#matplotlib.axes.Axes.hist2d "matplotlib.axes.Axes.hist2d") | Make a 2D histogram plot. |
| [`Axes.stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stairs.html#matplotlib.axes.Axes.stairs "matplotlib.axes.Axes.stairs") | Draw a stepwise constant function as a line or a filled plot. |

### [Contours](https://matplotlib.org/stable/api/axes_api.html#id9)
[#](https://matplotlib.org/stable/api/axes_api.html#contours "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.clabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clabel.html#matplotlib.axes.Axes.clabel "matplotlib.axes.Axes.clabel") | Label a contour plot. |
| [`Axes.contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour "matplotlib.axes.Axes.contour") | Plot contour lines. |
| [`Axes.contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf") | Plot filled contours. |

### [2D arrays](https://matplotlib.org/stable/api/axes_api.html#id10)
[#](https://matplotlib.org/stable/api/axes_api.html#d-arrays "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow") | Display data as an image, i.e., on a 2D regular raster. |
| [`Axes.matshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.matshow.html#matplotlib.axes.Axes.matshow "matplotlib.axes.Axes.matshow") | Plot the values of a 2D matrix or array as color-coded image. |
| [`Axes.pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolor.html#matplotlib.axes.Axes.pcolor "matplotlib.axes.Axes.pcolor") | Create a pseudocolor plot with a non-regular rectangular grid. |
| [`Axes.pcolorfast`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolorfast.html#matplotlib.axes.Axes.pcolorfast "matplotlib.axes.Axes.pcolorfast") | Create a pseudocolor plot with a non-regular rectangular grid. |
| [`Axes.pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pcolormesh.html#matplotlib.axes.Axes.pcolormesh "matplotlib.axes.Axes.pcolormesh") | Create a pseudocolor plot with a non-regular rectangular grid. |
| [`Axes.spy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.spy.html#matplotlib.axes.Axes.spy "matplotlib.axes.Axes.spy") | Plot the sparsity pattern of a 2D array. |

### [Unstructured triangles](https://matplotlib.org/stable/api/axes_api.html#id11)
[#](https://matplotlib.org/stable/api/axes_api.html#unstructured-triangles "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.tripcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tripcolor.html#matplotlib.axes.Axes.tripcolor "matplotlib.axes.Axes.tripcolor") | Create a pseudocolor plot of an unstructured triangular grid. |
| [`Axes.triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.triplot.html#matplotlib.axes.Axes.triplot "matplotlib.axes.Axes.triplot") | Draw an unstructured triangular grid as lines and/or markers. |
| [`Axes.tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontour.html#matplotlib.axes.Axes.tricontour "matplotlib.axes.Axes.tricontour") | Draw contour lines on an unstructured triangular grid. |
| [`Axes.tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tricontourf.html#matplotlib.axes.Axes.tricontourf "matplotlib.axes.Axes.tricontourf") | Draw contour regions on an unstructured triangular grid. |

### [Text and annotations](https://matplotlib.org/stable/api/axes_api.html#id12)
[#](https://matplotlib.org/stable/api/axes_api.html#text-and-annotations "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate") | Annotate the point _xy_ with text _text_. |
| [`Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text") | Add text to the Axes. |
| [`Axes.table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.table.html#matplotlib.axes.Axes.table "matplotlib.axes.Axes.table") | Add a table to an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br>. |
| [`Axes.arrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.arrow.html#matplotlib.axes.Axes.arrow "matplotlib.axes.Axes.arrow") | \[_Discouraged_\] Add an arrow to the Axes. |
| [`Axes.inset_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html#matplotlib.axes.Axes.inset_axes "matplotlib.axes.Axes.inset_axes") | Add a child inset Axes to this existing Axes. |
| [`Axes.indicate_inset`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset.html#matplotlib.axes.Axes.indicate_inset "matplotlib.axes.Axes.indicate_inset") | Add an inset indicator to the Axes. |
| [`Axes.indicate_inset_zoom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html#matplotlib.axes.Axes.indicate_inset_zoom "matplotlib.axes.Axes.indicate_inset_zoom") | Add an inset indicator rectangle to the Axes based on the axis limits for an _inset\_ax_ and draw connectors between _inset\_ax_ and the rectangle. |
| [`Axes.secondary_xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_xaxis.html#matplotlib.axes.Axes.secondary_xaxis "matplotlib.axes.Axes.secondary_xaxis") | Add a second x-axis to this [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br>. |
| [`Axes.secondary_yaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.secondary_yaxis.html#matplotlib.axes.Axes.secondary_yaxis "matplotlib.axes.Axes.secondary_yaxis") | Add a second y-axis to this [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br>. |

### [Vector fields](https://matplotlib.org/stable/api/axes_api.html#id13)
[#](https://matplotlib.org/stable/api/axes_api.html#vector-fields "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.barbs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barbs.html#matplotlib.axes.Axes.barbs "matplotlib.axes.Axes.barbs") | Plot a 2D field of wind barbs. |
| [`Axes.quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html#matplotlib.axes.Axes.quiver "matplotlib.axes.Axes.quiver") | Plot a 2D field of arrows. |
| [`Axes.quiverkey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiverkey.html#matplotlib.axes.Axes.quiverkey "matplotlib.axes.Axes.quiverkey") | Add a key to a quiver plot. |
| [`Axes.streamplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.streamplot.html#matplotlib.axes.Axes.streamplot "matplotlib.axes.Axes.streamplot") | Draw streamlines of a vector flow. |

[Clearing](https://matplotlib.org/stable/api/axes_api.html#id14)
[#](https://matplotlib.org/stable/api/axes_api.html#clearing "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.cla`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.cla.html#matplotlib.axes.Axes.cla "matplotlib.axes.Axes.cla") | Clear the Axes. |
| [`Axes.clear`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.clear.html#matplotlib.axes.Axes.clear "matplotlib.axes.Axes.clear") | Clear the Axes. |

[Appearance](https://matplotlib.org/stable/api/axes_api.html#id15)
[#](https://matplotlib.org/stable/api/axes_api.html#appearance "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.axis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis") | Convenience method to get or set some axis properties. |
| [`Axes.set_axis_off`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off") | Hide all visual components of the x- and y-axis. |
| [`Axes.set_axis_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_on.html#matplotlib.axes.Axes.set_axis_on "matplotlib.axes.Axes.set_axis_on") | Do not hide all visual components of the x- and y-axis. |
| [`Axes.set_frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | Set whether the Axes rectangle patch is drawn. |
| [`Axes.get_frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_frame_on.html#matplotlib.axes.Axes.get_frame_on "matplotlib.axes.Axes.get_frame_on") | Get whether the Axes rectangle patch is drawn. |
| [`Axes.set_axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | Set whether axis ticks and gridlines are above or below most artists. |
| [`Axes.get_axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_axisbelow.html#matplotlib.axes.Axes.get_axisbelow "matplotlib.axes.Axes.get_axisbelow") | Get whether axis ticks and gridlines are above or below most artists. |
| [`Axes.grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid") | Configure the grid lines. |
| [`Axes.get_facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_facecolor.html#matplotlib.axes.Axes.get_facecolor "matplotlib.axes.Axes.get_facecolor") | Get the facecolor of the Axes. |
| [`Axes.set_facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | Set the facecolor of the Axes. |

[Property cycle](https://matplotlib.org/stable/api/axes_api.html#id16)
[#](https://matplotlib.org/stable/api/axes_api.html#property-cycle "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.set_prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | Set the property cycle of the Axes. |

[Axis / limits](https://matplotlib.org/stable/api/axes_api.html#id17)
[#](https://matplotlib.org/stable/api/axes_api.html#axis-limits "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Axis access](https://matplotlib.org/stable/api/axes_api.html#id18)
[#](https://matplotlib.org/stable/api/axes_api.html#axis-access "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xaxis.html#matplotlib.axes.Axes.xaxis "matplotlib.axes.Axes.xaxis") | The [`XAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.XAxis "matplotlib.axis.XAxis")<br> instance. |
| [`Axes.yaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.yaxis.html#matplotlib.axes.Axes.yaxis "matplotlib.axes.Axes.yaxis") | The [`YAxis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.YAxis "matplotlib.axis.YAxis")<br> instance. |
| [`Axes.get_xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis.html#matplotlib.axes.Axes.get_xaxis "matplotlib.axes.Axes.get_xaxis") | \[_Discouraged_\] Return the XAxis instance. |
| [`Axes.get_yaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis.html#matplotlib.axes.Axes.get_yaxis "matplotlib.axes.Axes.get_yaxis") | \[_Discouraged_\] Return the YAxis instance. |

### [Axis limits and direction](https://matplotlib.org/stable/api/axes_api.html#id19)
[#](https://matplotlib.org/stable/api/axes_api.html#axis-limits-and-direction "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.set_xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | Set whether the xaxis is oriented in the "inverse" direction. |
| [`Axes.get_xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xinverted.html#matplotlib.axes.Axes.get_xinverted "matplotlib.axes.Axes.get_xinverted") | Return whether the xaxis is oriented in the "inverse" direction. |
| [`Axes.invert_xaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_xaxis.html#matplotlib.axes.Axes.invert_xaxis "matplotlib.axes.Axes.invert_xaxis") | \[_Discouraged_\] Invert the x-axis. |
| [`Axes.xaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xaxis_inverted.html#matplotlib.axes.Axes.xaxis_inverted "matplotlib.axes.Axes.xaxis_inverted") | \[_Discouraged_\] Return whether the xaxis is oriented in the "inverse" direction. |
| [`Axes.set_yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | Set whether the yaxis is oriented in the "inverse" direction. |
| [`Axes.get_yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yinverted.html#matplotlib.axes.Axes.get_yinverted "matplotlib.axes.Axes.get_yinverted") | Return whether the yaxis is oriented in the "inverse" direction. |
| [`Axes.invert_yaxis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.invert_yaxis.html#matplotlib.axes.Axes.invert_yaxis "matplotlib.axes.Axes.invert_yaxis") | \[_Discouraged_\] Invert the y-axis. |
| [`Axes.yaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.yaxis_inverted.html#matplotlib.axes.Axes.yaxis_inverted "matplotlib.axes.Axes.yaxis_inverted") | \[_Discouraged_\] Return whether the yaxis is oriented in the "inverse" direction. |
| [`Axes.set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim") | Set the x-axis view limits. |
| [`Axes.get_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlim.html#matplotlib.axes.Axes.get_xlim "matplotlib.axes.Axes.get_xlim") | Return the x-axis view limits. |
| [`Axes.set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim") | Set the y-axis view limits. |
| [`Axes.get_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ylim.html#matplotlib.axes.Axes.get_ylim "matplotlib.axes.Axes.get_ylim") | Return the y-axis view limits. |
| [`Axes.update_datalim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.update_datalim.html#matplotlib.axes.Axes.update_datalim "matplotlib.axes.Axes.update_datalim") | Extend the [`dataLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.dataLim.html#matplotlib.axes.Axes.dataLim "matplotlib.axes.Axes.dataLim")<br> Bbox to include the given points. |
| [`Axes.set_xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound") | Set the lower and upper numerical bounds of the x-axis. |
| [`Axes.get_xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xbound.html#matplotlib.axes.Axes.get_xbound "matplotlib.axes.Axes.get_xbound") | Return the lower and upper x-axis bounds, in increasing order. |
| [`Axes.set_ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound") | Set the lower and upper numerical bounds of the y-axis. |
| [`Axes.get_ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ybound.html#matplotlib.axes.Axes.get_ybound "matplotlib.axes.Axes.get_ybound") | Return the lower and upper y-axis bounds, in increasing order. |

### [Axis labels, title, and legend](https://matplotlib.org/stable/api/axes_api.html#id20)
[#](https://matplotlib.org/stable/api/axes_api.html#axis-labels-title-and-legend "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | Set the label for the x-axis. |
| [`Axes.get_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xlabel.html#matplotlib.axes.Axes.get_xlabel "matplotlib.axes.Axes.get_xlabel") | Get the xlabel text string. |
| [`Axes.set_ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | Set the label for the y-axis. |
| [`Axes.get_ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ylabel.html#matplotlib.axes.Axes.get_ylabel "matplotlib.axes.Axes.get_ylabel") | Get the ylabel text string. |
| [`Axes.label_outer`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.label_outer.html#matplotlib.axes.Axes.label_outer "matplotlib.axes.Axes.label_outer") | Only show "outer" labels and tick labels. |
| [`Axes.set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | Set a title for the Axes. |
| [`Axes.get_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_title.html#matplotlib.axes.Axes.get_title "matplotlib.axes.Axes.get_title") | Get an Axes title. |
| [`Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend") | Place a legend on the Axes. |
| [`Axes.get_legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend.html#matplotlib.axes.Axes.get_legend "matplotlib.axes.Axes.get_legend") | Return the [`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")<br> instance, or None if no legend is defined. |
| [`Axes.get_legend_handles_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_legend_handles_labels.html#matplotlib.axes.Axes.get_legend_handles_labels "matplotlib.axes.Axes.get_legend_handles_labels") | Return handles and labels for legend |

### [Axis scales](https://matplotlib.org/stable/api/axes_api.html#id21)
[#](https://matplotlib.org/stable/api/axes_api.html#axis-scales "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.set_xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | Set the xaxis' scale. |
| [`Axes.get_xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xscale.html#matplotlib.axes.Axes.get_xscale "matplotlib.axes.Axes.get_xscale") | Return the xaxis' scale (as a str). |
| [`Axes.set_yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | Set the yaxis' scale. |
| [`Axes.get_yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yscale.html#matplotlib.axes.Axes.get_yscale "matplotlib.axes.Axes.get_yscale") | Return the yaxis' scale (as a str). |

### [Autoscaling and margins](https://matplotlib.org/stable/api/axes_api.html#id22)
[#](https://matplotlib.org/stable/api/axes_api.html#autoscaling-and-margins "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.use_sticky_edges`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.use_sticky_edges.html#matplotlib.axes.Axes.use_sticky_edges "matplotlib.axes.Axes.use_sticky_edges") | When autoscaling, whether to obey all [`Artist.sticky_edges`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.sticky_edges.html#matplotlib.artist.Artist.sticky_edges "matplotlib.artist.Artist.sticky_edges")<br>. |
| [`Axes.margins`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins") | Set or retrieve margins around the data for autoscaling axis limits. |
| [`Axes.get_xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xmargin.html#matplotlib.axes.Axes.get_xmargin "matplotlib.axes.Axes.get_xmargin") | Retrieve autoscaling margin of the x-axis. |
| [`Axes.get_ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ymargin.html#matplotlib.axes.Axes.get_ymargin "matplotlib.axes.Axes.get_ymargin") | Retrieve autoscaling margin of the y-axis. |
| [`Axes.set_xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | Set padding of X data limits prior to autoscaling. |
| [`Axes.set_ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | Set padding of Y data limits prior to autoscaling. |
| [`Axes.relim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.relim.html#matplotlib.axes.Axes.relim "matplotlib.axes.Axes.relim") | Recompute the data limits based on current artists. |
| [`Axes.autoscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html#matplotlib.axes.Axes.autoscale "matplotlib.axes.Axes.autoscale") | Autoscale the axis view to the data (toggle). |
| [`Axes.autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view") | Autoscale the view limits using the data limits. |
| [`Axes.set_autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | Set whether autoscaling is applied to each axis on the next draw or call to [`Axes.autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")<br>. |
| [`Axes.get_autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_autoscale_on.html#matplotlib.axes.Axes.get_autoscale_on "matplotlib.axes.Axes.get_autoscale_on") | Return True if each axis is autoscaled, False otherwise. |
| [`Axes.set_autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | Set whether the xaxis is autoscaled when drawing or by [`Axes.autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")<br>. |
| [`Axes.get_autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_autoscalex_on.html#matplotlib.axes.Axes.get_autoscalex_on "matplotlib.axes.Axes.get_autoscalex_on") | Return whether the xaxis is autoscaled. |
| [`Axes.set_autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | Set whether the yaxis is autoscaled when drawing or by [`Axes.autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")<br>. |
| [`Axes.get_autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_autoscaley_on.html#matplotlib.axes.Axes.get_autoscaley_on "matplotlib.axes.Axes.get_autoscaley_on") | Return whether the yaxis is autoscaled. |

### [Aspect ratio](https://matplotlib.org/stable/api/axes_api.html#id23)
[#](https://matplotlib.org/stable/api/axes_api.html#aspect-ratio "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.apply_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.apply_aspect.html#matplotlib.axes.Axes.apply_aspect "matplotlib.axes.Axes.apply_aspect") | Adjust the Axes for a specified data aspect ratio. |
| [`Axes.set_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | Set the aspect ratio of the Axes scaling, i.e. y/x-scale. |
| [`Axes.get_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_aspect.html#matplotlib.axes.Axes.get_aspect "matplotlib.axes.Axes.get_aspect") | Return the aspect ratio of the Axes scaling. |
| [`Axes.set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | Set the Axes box aspect, i.e. the ratio of height to width. |
| [`Axes.get_box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_box_aspect.html#matplotlib.axes.Axes.get_box_aspect "matplotlib.axes.Axes.get_box_aspect") | Return the Axes box aspect, i.e. the ratio of height to width. |
| [`Axes.set_adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | Set how the Axes adjusts to achieve the required aspect ratio. |
| [`Axes.get_adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_adjustable.html#matplotlib.axes.Axes.get_adjustable "matplotlib.axes.Axes.get_adjustable") | Return whether the Axes will adjust its physical dimension ('box') or its data limits ('datalim') to achieve the desired aspect ratio. |

### [Ticks and tick labels](https://matplotlib.org/stable/api/axes_api.html#id24)
[#](https://matplotlib.org/stable/api/axes_api.html#ticks-and-tick-labels "Link to this heading")

|     |     |
| --- | --- |
| [`Axes.set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | Set the xaxis' tick locations and optionally tick labels. |
| [`Axes.get_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticks.html#matplotlib.axes.Axes.get_xticks "matplotlib.axes.Axes.get_xticks") | Return the xaxis' tick locations in data coordinates. |
| [`Axes.set_xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | \[_Discouraged_\] Set the xaxis' tick labels with list of string labels. |
| [`Axes.get_xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklabels.html#matplotlib.axes.Axes.get_xticklabels "matplotlib.axes.Axes.get_xticklabels") | Get the xaxis' tick labels. |
| [`Axes.get_xmajorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xmajorticklabels.html#matplotlib.axes.Axes.get_xmajorticklabels "matplotlib.axes.Axes.get_xmajorticklabels") | Return the xaxis' major tick labels, as a list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br>. |
| [`Axes.get_xminorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xminorticklabels.html#matplotlib.axes.Axes.get_xminorticklabels "matplotlib.axes.Axes.get_xminorticklabels") | Return the xaxis' minor tick labels, as a list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br>. |
| [`Axes.get_xgridlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xgridlines.html#matplotlib.axes.Axes.get_xgridlines "matplotlib.axes.Axes.get_xgridlines") | Return the xaxis' grid lines as a list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>. |
| [`Axes.get_xticklines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xticklines.html#matplotlib.axes.Axes.get_xticklines "matplotlib.axes.Axes.get_xticklines") | Return the xaxis' tick lines as a list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>. |
| [`Axes.xaxis_date`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xaxis_date.html#matplotlib.axes.Axes.xaxis_date "matplotlib.axes.Axes.xaxis_date") | Set up axis ticks and labels to treat data along the xaxis as dates. |
| [`Axes.set_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | Set the yaxis' tick locations and optionally tick labels. |
| [`Axes.get_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticks.html#matplotlib.axes.Axes.get_yticks "matplotlib.axes.Axes.get_yticks") | Return the yaxis' tick locations in data coordinates. |
| [`Axes.set_yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | \[_Discouraged_\] Set the yaxis' tick labels with list of string labels. |
| [`Axes.get_yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticklabels.html#matplotlib.axes.Axes.get_yticklabels "matplotlib.axes.Axes.get_yticklabels") | Get the yaxis' tick labels. |
| [`Axes.get_ymajorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ymajorticklabels.html#matplotlib.axes.Axes.get_ymajorticklabels "matplotlib.axes.Axes.get_ymajorticklabels") | Return the yaxis' major tick labels, as a list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br>. |
| [`Axes.get_yminorticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yminorticklabels.html#matplotlib.axes.Axes.get_yminorticklabels "matplotlib.axes.Axes.get_yminorticklabels") | Return the yaxis' minor tick labels, as a list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br>. |
| [`Axes.get_ygridlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ygridlines.html#matplotlib.axes.Axes.get_ygridlines "matplotlib.axes.Axes.get_ygridlines") | Return the yaxis' grid lines as a list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>. |
| [`Axes.get_yticklines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yticklines.html#matplotlib.axes.Axes.get_yticklines "matplotlib.axes.Axes.get_yticklines") | Return the yaxis' tick lines as a list of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>. |
| [`Axes.yaxis_date`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.yaxis_date.html#matplotlib.axes.Axes.yaxis_date "matplotlib.axes.Axes.yaxis_date") | Set up axis ticks and labels to treat data along the yaxis as dates. |
| [`Axes.minorticks_off`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.minorticks_off.html#matplotlib.axes.Axes.minorticks_off "matplotlib.axes.Axes.minorticks_off") | Remove minor ticks from the Axes. |
| [`Axes.minorticks_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.minorticks_on.html#matplotlib.axes.Axes.minorticks_on "matplotlib.axes.Axes.minorticks_on") | Display minor ticks on the Axes. |
| [`Axes.ticklabel_format`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.ticklabel_format.html#matplotlib.axes.Axes.ticklabel_format "matplotlib.axes.Axes.ticklabel_format") | Configure the [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")<br> used by default for linear Axes. |
| [`Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params") | Change the appearance of ticks, tick labels, and gridlines. |
| [`Axes.locator_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.locator_params.html#matplotlib.axes.Axes.locator_params "matplotlib.axes.Axes.locator_params") | Control behavior of major tick locators. |

[Units](https://matplotlib.org/stable/api/axes_api.html#id25)
[#](https://matplotlib.org/stable/api/axes_api.html#units "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.convert_xunits`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.convert_xunits.html#matplotlib.axes.Axes.convert_xunits "matplotlib.axes.Axes.convert_xunits") | Convert _x_ using the unit type of the xaxis. |
| [`Axes.convert_yunits`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.convert_yunits.html#matplotlib.axes.Axes.convert_yunits "matplotlib.axes.Axes.convert_yunits") | Convert _y_ using the unit type of the yaxis. |
| [`Axes.have_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.have_units.html#matplotlib.axes.Axes.have_units "matplotlib.axes.Axes.have_units") | Return whether units are set on any axis. |

[Adding artists](https://matplotlib.org/stable/api/axes_api.html#id26)
[#](https://matplotlib.org/stable/api/axes_api.html#adding-artists "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist") | Add an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br> to the Axes; return the artist. |
| [`Axes.add_child_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_child_axes.html#matplotlib.axes.Axes.add_child_axes "matplotlib.axes.Axes.add_child_axes") | Add an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br> to the Axes' children; return the child Axes. |
| [`Axes.add_collection`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_collection.html#matplotlib.axes.Axes.add_collection "matplotlib.axes.Axes.add_collection") | Add a [`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")<br> to the Axes; return the collection. |
| [`Axes.add_container`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_container.html#matplotlib.axes.Axes.add_container "matplotlib.axes.Axes.add_container") | Add a [`Container`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.Container "matplotlib.container.Container")<br> to the Axes' containers; return the container. |
| [`Axes.add_image`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_image.html#matplotlib.axes.Axes.add_image "matplotlib.axes.Axes.add_image") | Add an [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")<br> to the Axes; return the image. |
| [`Axes.add_line`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_line.html#matplotlib.axes.Axes.add_line "matplotlib.axes.Axes.add_line") | Add a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br> to the Axes; return the line. |
| [`Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch") | Add a [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")<br> to the Axes; return the patch. |
| [`Axes.add_table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_table.html#matplotlib.axes.Axes.add_table "matplotlib.axes.Axes.add_table") | Add a [`Table`](https://matplotlib.org/stable/api/table_api.html#matplotlib.table.Table "matplotlib.table.Table")<br> to the Axes; return the table. |

[Twinning and sharing](https://matplotlib.org/stable/api/axes_api.html#id27)
[#](https://matplotlib.org/stable/api/axes_api.html#twinning-and-sharing "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.twinx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twinx.html#matplotlib.axes.Axes.twinx "matplotlib.axes.Axes.twinx") | Create a twin Axes sharing the xaxis. |
| [`Axes.twiny`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.twiny.html#matplotlib.axes.Axes.twiny "matplotlib.axes.Axes.twiny") | Create a twin Axes sharing the yaxis. |
| [`Axes.sharex`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.sharex.html#matplotlib.axes.Axes.sharex "matplotlib.axes.Axes.sharex") | Share the x-axis with _other_. |
| [`Axes.sharey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.sharey.html#matplotlib.axes.Axes.sharey "matplotlib.axes.Axes.sharey") | Share the y-axis with _other_. |
| [`Axes.get_shared_x_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_shared_x_axes.html#matplotlib.axes.Axes.get_shared_x_axes "matplotlib.axes.Axes.get_shared_x_axes") | Return an immutable view on the shared x-axes Grouper. |
| [`Axes.get_shared_y_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_shared_y_axes.html#matplotlib.axes.Axes.get_shared_y_axes "matplotlib.axes.Axes.get_shared_y_axes") | Return an immutable view on the shared y-axes Grouper. |

[Axes position](https://matplotlib.org/stable/api/axes_api.html#id28)
[#](https://matplotlib.org/stable/api/axes_api.html#axes-position "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.get_anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_anchor.html#matplotlib.axes.Axes.get_anchor "matplotlib.axes.Axes.get_anchor") | Get the anchor location. |
| [`Axes.set_anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | Define the anchor location. |
| [`Axes.get_axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_axes_locator.html#matplotlib.axes.Axes.get_axes_locator "matplotlib.axes.Axes.get_axes_locator") | Return the axes\_locator. |
| [`Axes.set_axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Set the Axes locator. |
| [`Axes.get_subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_subplotspec.html#matplotlib.axes.Axes.get_subplotspec "matplotlib.axes.Axes.get_subplotspec") | Return the [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")<br> associated with the subplot, or None. |
| [`Axes.set_subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | Set the [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")<br>. |
| [`Axes.reset_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.reset_position.html#matplotlib.axes.Axes.reset_position "matplotlib.axes.Axes.reset_position") | Reset the active position to the original position. |
| [`Axes.get_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_position.html#matplotlib.axes.Axes.get_position "matplotlib.axes.Axes.get_position") | Return the position of the Axes within the figure as a [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")<br>. |
| [`Axes.set_position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | Set the Axes position. |

[Async/event based](https://matplotlib.org/stable/api/axes_api.html#id29)
[#](https://matplotlib.org/stable/api/axes_api.html#async-event-based "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.stale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.stale.html#matplotlib.axes.Axes.stale "matplotlib.axes.Axes.stale") | Whether the artist is 'stale' and needs to be re-drawn for the output to match the internal state of the artist. |
| [`Axes.pchanged`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pchanged.html#matplotlib.axes.Axes.pchanged "matplotlib.axes.Axes.pchanged") | Call all of the registered callbacks. |
| [`Axes.add_callback`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_callback.html#matplotlib.axes.Axes.add_callback "matplotlib.axes.Axes.add_callback") | Add a callback function that will be called whenever one of the [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>'s properties changes. |
| [`Axes.remove_callback`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.remove_callback.html#matplotlib.axes.Axes.remove_callback "matplotlib.axes.Axes.remove_callback") | Remove a callback based on its observer id. |

[Interactive](https://matplotlib.org/stable/api/axes_api.html#id30)
[#](https://matplotlib.org/stable/api/axes_api.html#interactive "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.can_pan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.can_pan.html#matplotlib.axes.Axes.can_pan "matplotlib.axes.Axes.can_pan") | Return whether this Axes supports any pan/zoom button functionality. |
| [`Axes.can_zoom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.can_zoom.html#matplotlib.axes.Axes.can_zoom "matplotlib.axes.Axes.can_zoom") | Return whether this Axes supports the zoom box button functionality. |
| [`Axes.get_navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_navigate.html#matplotlib.axes.Axes.get_navigate "matplotlib.axes.Axes.get_navigate") | Get whether the Axes responds to navigation commands. |
| [`Axes.set_navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | Set whether the Axes responds to navigation toolbar commands. |
| [`Axes.get_navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_navigate_mode.html#matplotlib.axes.Axes.get_navigate_mode "matplotlib.axes.Axes.get_navigate_mode") | Get the navigation toolbar button status: 'PAN', 'ZOOM', or None. |
| [`Axes.set_navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | \[_Deprecated_\] Set the navigation toolbar button status. |
| [`Axes.get_forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_forward_navigation_events.html#matplotlib.axes.Axes.get_forward_navigation_events "matplotlib.axes.Axes.get_forward_navigation_events") | Get how pan/zoom events are forwarded to Axes below this one. |
| [`Axes.set_forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | Set how pan/zoom events are forwarded to Axes below this one. |
| [`Axes.start_pan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.start_pan.html#matplotlib.axes.Axes.start_pan "matplotlib.axes.Axes.start_pan") | Called when a pan operation has started. |
| [`Axes.drag_pan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.drag_pan.html#matplotlib.axes.Axes.drag_pan "matplotlib.axes.Axes.drag_pan") | Called when the mouse moves during a pan operation. |
| [`Axes.end_pan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.end_pan.html#matplotlib.axes.Axes.end_pan "matplotlib.axes.Axes.end_pan") | Called when a pan operation completes (when the mouse button is up.) |
| [`Axes.format_coord`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.format_coord.html#matplotlib.axes.Axes.format_coord "matplotlib.axes.Axes.format_coord") | Return a format string formatting the _x_, _y_ coordinates. |
| [`Axes.format_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.format_cursor_data.html#matplotlib.axes.Axes.format_cursor_data "matplotlib.axes.Axes.format_cursor_data") | Return a string representation of _data_. |
| [`Axes.format_xdata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.format_xdata.html#matplotlib.axes.Axes.format_xdata "matplotlib.axes.Axes.format_xdata") | Return _x_ formatted as an x-value. |
| [`Axes.format_ydata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.format_ydata.html#matplotlib.axes.Axes.format_ydata "matplotlib.axes.Axes.format_ydata") | Return _y_ formatted as a y-value. |
| [`Axes.mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.mouseover.html#matplotlib.axes.Axes.mouseover "matplotlib.axes.Axes.mouseover") | Return whether this artist is queried for custom context information when the mouse cursor moves over it. |
| [`Axes.in_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.in_axes.html#matplotlib.axes.Axes.in_axes "matplotlib.axes.Axes.in_axes") | Return whether the given event (in display coords) is in the Axes. |
| [`Axes.contains`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contains.html#matplotlib.axes.Axes.contains "matplotlib.axes.Axes.contains") | Test whether the artist contains the mouse event. |
| [`Axes.contains_point`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contains_point.html#matplotlib.axes.Axes.contains_point "matplotlib.axes.Axes.contains_point") | Return whether _point_ (pair of pixel coordinates) is inside the Axes patch. |
| [`Axes.get_cursor_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_cursor_data.html#matplotlib.axes.Axes.get_cursor_data "matplotlib.axes.Axes.get_cursor_data") | Return the cursor data for a given event. |

[Children](https://matplotlib.org/stable/api/axes_api.html#id31)
[#](https://matplotlib.org/stable/api/axes_api.html#children "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.get_children`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_children.html#matplotlib.axes.Axes.get_children "matplotlib.axes.Axes.get_children") | Return a list of the child [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>s of this [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>. |
| [`Axes.get_images`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_images.html#matplotlib.axes.Axes.get_images "matplotlib.axes.Axes.get_images") | Return a list of [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")<br>s contained by the Axes. |
| [`Axes.get_lines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_lines.html#matplotlib.axes.Axes.get_lines "matplotlib.axes.Axes.get_lines") | Return a list of lines contained by the Axes. |
| [`Axes.findobj`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.findobj.html#matplotlib.axes.Axes.findobj "matplotlib.axes.Axes.findobj") | Find artist objects. |

[Drawing](https://matplotlib.org/stable/api/axes_api.html#id32)
[#](https://matplotlib.org/stable/api/axes_api.html#drawing "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw.html#matplotlib.axes.Axes.draw "matplotlib.axes.Axes.draw") | Draw the Artist (and its children) using the given renderer. |
| [`Axes.draw_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.draw_artist.html#matplotlib.axes.Axes.draw_artist "matplotlib.axes.Axes.draw_artist") | Efficiently redraw a single artist. |
| [`Axes.redraw_in_frame`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.redraw_in_frame.html#matplotlib.axes.Axes.redraw_in_frame "matplotlib.axes.Axes.redraw_in_frame") | Efficiently redraw Axes data, but not axis ticks, labels, etc. |
| [`Axes.get_rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_rasterization_zorder.html#matplotlib.axes.Axes.get_rasterization_zorder "matplotlib.axes.Axes.get_rasterization_zorder") | Return the zorder value below which artists will be rasterized. |
| [`Axes.set_rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | Set the zorder threshold for rasterization for vector graphics output. |
| [`Axes.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_window_extent.html#matplotlib.axes.Axes.get_window_extent "matplotlib.axes.Axes.get_window_extent") | Return the Axes bounding box in display space. |
| [`Axes.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_tightbbox.html#matplotlib.axes.Axes.get_tightbbox "matplotlib.axes.Axes.get_tightbbox") | Return the tight bounding box of the Axes, including axis and their decorators (xlabel, title, etc). |

[Projection](https://matplotlib.org/stable/api/axes_api.html#id33)
[#](https://matplotlib.org/stable/api/axes_api.html#projection "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

Methods used by [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 that must be overridden for non-rectilinear Axes.

|     |     |
| --- | --- |
| [`Axes.name`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.name.html#matplotlib.axes.Axes.name "matplotlib.axes.Axes.name") |     |
| [`Axes.get_xaxis_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_transform.html#matplotlib.axes.Axes.get_xaxis_transform "matplotlib.axes.Axes.get_xaxis_transform") | Get the transformation used for drawing x-axis labels, ticks and gridlines. |
| [`Axes.get_yaxis_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_transform.html#matplotlib.axes.Axes.get_yaxis_transform "matplotlib.axes.Axes.get_yaxis_transform") | Get the transformation used for drawing y-axis labels, ticks and gridlines. |
| [`Axes.get_data_ratio`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_data_ratio.html#matplotlib.axes.Axes.get_data_ratio "matplotlib.axes.Axes.get_data_ratio") | Return the aspect ratio of the scaled data. |
| [`Axes.get_xaxis_text1_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_text1_transform.html#matplotlib.axes.Axes.get_xaxis_text1_transform "matplotlib.axes.Axes.get_xaxis_text1_transform") |     |
| [`Axes.get_xaxis_text2_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_text2_transform.html#matplotlib.axes.Axes.get_xaxis_text2_transform "matplotlib.axes.Axes.get_xaxis_text2_transform") |     |
| [`Axes.get_yaxis_text1_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_text1_transform.html#matplotlib.axes.Axes.get_yaxis_text1_transform "matplotlib.axes.Axes.get_yaxis_text1_transform") |     |
| [`Axes.get_yaxis_text2_transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_text2_transform.html#matplotlib.axes.Axes.get_yaxis_text2_transform "matplotlib.axes.Axes.get_yaxis_text2_transform") |     |

[Other](https://matplotlib.org/stable/api/axes_api.html#id34)
[#](https://matplotlib.org/stable/api/axes_api.html#other "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Axes.zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.zorder.html#matplotlib.axes.Axes.zorder "matplotlib.axes.Axes.zorder") |     |
| [`Axes.get_default_bbox_extra_artists`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_default_bbox_extra_artists.html#matplotlib.axes.Axes.get_default_bbox_extra_artists "matplotlib.axes.Axes.get_default_bbox_extra_artists") | Return a default list of artists that are used for the bounding box calculation. |
| [`Axes.get_transformed_clip_path_and_affine`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_transformed_clip_path_and_affine.html#matplotlib.axes.Axes.get_transformed_clip_path_and_affine "matplotlib.axes.Axes.get_transformed_clip_path_and_affine") | Return the clip path with the non-affine part of its transformation applied, and the remaining affine part of its transformation. |
| [`Axes.has_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.has_data.html#matplotlib.axes.Axes.has_data "matplotlib.axes.Axes.has_data") | Return whether any artists have been added to the Axes. |
| [`Axes.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set") | Set multiple properties at once. |
| [`Axes.get_figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_figure.html#matplotlib.axes.Axes.get_figure "matplotlib.axes.Axes.get_figure") | Return the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")<br> instance the artist belongs to. |
| [`Axes.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.figure.html#matplotlib.axes.Axes.figure "matplotlib.axes.Axes.figure") | The (Sub)Figure that the artist is on. |
| [`Axes.remove`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.remove.html#matplotlib.axes.Axes.remove "matplotlib.axes.Axes.remove") | Remove the artist from the figure if possible. |

class matplotlib.axes.Axes.ArtistList(_axes_, _prop\_name_, _valid\_types\=None_, _invalid\_types\=None_)[#](https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes.ArtistList "Link to this definition")

A sublist of Axes children based on their type.

The type-specific children sublists were made immutable in Matplotlib 3.7. In the future these artist lists may be replaced by tuples. Use as if this is a tuple already.

Parameters:

**axes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The Axes from which this sublist will pull the children Artists.

**prop\_name**str

The property name used to access this sublist from the Axes; used to generate deprecation warnings.

**valid\_types**list of type, optional

A list of types that determine which children will be returned by this sublist. If specified, then the Artists in the sublist must be instances of any of these types. If unspecified, then any type of Artist is valid (unless limited by _invalid\_types_.)

**invalid\_types**tuple, optional

A list of types that determine which children will _not_ be returned by this sublist. If specified, then Artists in the sublist will never be an instance of these types. Otherwise, no types will be excluded.

On this page