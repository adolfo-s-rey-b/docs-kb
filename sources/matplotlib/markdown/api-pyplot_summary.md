[Skip to main content](https://matplotlib.org/stable/api/pyplot_summary.html#main-content)

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
    

`matplotlib.pyplot`[#](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "Link to this heading")

==============================================================================================================================

[`matplotlib.pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 is a state-based interface to matplotlib. It provides an implicit, MATLAB-like, way of plotting. It also opens figures on your screen, and acts as the figure GUI manager.

pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation:

import numpy as np
import matplotlib.pyplot as plt

x \= np.arange(0, 5, 0.1)
y \= np.sin(x)
plt.plot(x, y)
plt.show()

The explicit object-oriented API is recommended for complex plots, though pyplot is still usually used to create the figure and often the Axes in the figure. See [`pyplot.figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
, [`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
, and [`pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 to create figures, and [Axes API](https://matplotlib.org/stable/api/axes_api.html)
 for the plotting methods on an Axes:

import numpy as np
import matplotlib.pyplot as plt

x \= np.arange(0, 5, 0.1)
y \= np.sin(x)
fig, ax \= plt.subplots()
ax.plot(x, y)
plt.show()

See [Matplotlib Application Interfaces (APIs)](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#api-interfaces)
 for an explanation of the tradeoffs between the implicit and explicit interfaces.

Managing Figure and Axes[#](https://matplotlib.org/stable/api/pyplot_summary.html#managing-figure-and-axes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes") | Add an Axes to the current figure and make it the current Axes. |
| [`cla`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.cla.html#matplotlib.pyplot.cla "matplotlib.pyplot.cla") | Clear the current Axes. |
| [`clf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clf.html#matplotlib.pyplot.clf "matplotlib.pyplot.clf") | Clear the current figure. |
| [`close`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close") | Close a figure window, and unregister it from pyplot. |
| [`delaxes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.delaxes.html#matplotlib.pyplot.delaxes "matplotlib.pyplot.delaxes") | Remove an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br> (defaulting to the current Axes) from its figure. |
| [`fignum_exists`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fignum_exists.html#matplotlib.pyplot.fignum_exists "matplotlib.pyplot.fignum_exists") | Return whether the figure with the given id exists. |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure") | Create a new figure, or activate an existing figure. |
| [`gca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca") | Get the current Axes. |
| [`gcf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gcf.html#matplotlib.pyplot.gcf "matplotlib.pyplot.gcf") | Get the current figure. |
| [`get_figlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_figlabels.html#matplotlib.pyplot.get_figlabels "matplotlib.pyplot.get_figlabels") | Return a list of existing figure labels. |
| [`get_fignums`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_fignums.html#matplotlib.pyplot.get_fignums "matplotlib.pyplot.get_fignums") | Return a list of existing figure numbers. |
| [`sca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.sca.html#matplotlib.pyplot.sca "matplotlib.pyplot.sca") | Set the current Axes to _ax_ and the current Figure to the parent of _ax_. |
| [`subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot") | Add an Axes to the current figure or retrieve an existing Axes. |
| [`subplot2grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot2grid.html#matplotlib.pyplot.subplot2grid "matplotlib.pyplot.subplot2grid") | Create a subplot at a specific location inside a regular grid. |
| [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic") | Build a layout of Axes based on ASCII art or nested lists. |
| [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots") | Create a figure and a set of subplots. |
| [`twinx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.twinx.html#matplotlib.pyplot.twinx "matplotlib.pyplot.twinx") | Make and return a second Axes that shares the _x_\-axis. |
| [`twiny`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.twiny.html#matplotlib.pyplot.twiny "matplotlib.pyplot.twiny") | Make and return a second Axes that shares the _y_\-axis. |

Adding data to the plot[#](https://matplotlib.org/stable/api/pyplot_summary.html#adding-data-to-the-plot "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

### Basic[#](https://matplotlib.org/stable/api/pyplot_summary.html#basic "Link to this heading")

|     |     |
| --- | --- |
| [`plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot") | Plot y versus x as lines and/or markers. |
| [`errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar") | Plot y versus x as lines and/or markers with attached errorbars. |
| [`scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter "matplotlib.pyplot.scatter") | A scatter plot of _y_ vs. _x_ with varying marker size and/or color. |
| [`step`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.step.html#matplotlib.pyplot.step "matplotlib.pyplot.step") | Make a step plot. |
| [`loglog`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.loglog.html#matplotlib.pyplot.loglog "matplotlib.pyplot.loglog") | Make a plot with log scaling on both the x- and y-axis. |
| [`semilogx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html#matplotlib.pyplot.semilogx "matplotlib.pyplot.semilogx") | Make a plot with log scaling on the x-axis. |
| [`semilogy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogy.html#matplotlib.pyplot.semilogy "matplotlib.pyplot.semilogy") | Make a plot with log scaling on the y-axis. |
| [`fill_between`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html#matplotlib.pyplot.fill_between "matplotlib.pyplot.fill_between") | Fill the area between two horizontal curves. |
| [`fill_betweenx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_betweenx.html#matplotlib.pyplot.fill_betweenx "matplotlib.pyplot.fill_betweenx") | Fill the area between two vertical curves. |
| [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar") | Make a bar plot. |
| [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html#matplotlib.pyplot.barh "matplotlib.pyplot.barh") | Make a horizontal bar plot. |
| [`bar_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar_label.html#matplotlib.pyplot.bar_label "matplotlib.pyplot.bar_label") | Label a bar plot. |
| [`grouped_bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grouped_bar.html#matplotlib.pyplot.grouped_bar "matplotlib.pyplot.grouped_bar") | Make a grouped bar plot. |
| [`stem`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem "matplotlib.pyplot.stem") | Create a stem plot. |
| [`eventplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.eventplot.html#matplotlib.pyplot.eventplot "matplotlib.pyplot.eventplot") | Plot identical parallel lines at the given positions. |
| [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie "matplotlib.pyplot.pie") | Plot a pie chart. |
| [`pie_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie_label.html#matplotlib.pyplot.pie_label "matplotlib.pyplot.pie_label") | Label a pie chart. |
| [`stackplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stackplot.html#matplotlib.pyplot.stackplot "matplotlib.pyplot.stackplot") | Draw a stacked area plot or a streamgraph. |
| [`broken_barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.broken_barh.html#matplotlib.pyplot.broken_barh "matplotlib.pyplot.broken_barh") | Plot a horizontal sequence of rectangles. |
| [`vlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html#matplotlib.pyplot.vlines "matplotlib.pyplot.vlines") | Plot vertical lines at each _x_ from _ymin_ to _ymax_. |
| [`hlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hlines.html#matplotlib.pyplot.hlines "matplotlib.pyplot.hlines") | Plot horizontal lines at each _y_ from _xmin_ to _xmax_. |
| [`fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill.html#matplotlib.pyplot.fill "matplotlib.pyplot.fill") | Plot filled polygons. |
| [`polar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.polar.html#matplotlib.pyplot.polar "matplotlib.pyplot.polar") | Make a polar plot. |

### Spans[#](https://matplotlib.org/stable/api/pyplot_summary.html#spans "Link to this heading")

|     |     |
| --- | --- |
| [`axhline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html#matplotlib.pyplot.axhline "matplotlib.pyplot.axhline") | Add a horizontal line spanning the whole or fraction of the Axes. |
| [`axhspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhspan.html#matplotlib.pyplot.axhspan "matplotlib.pyplot.axhspan") | Add a horizontal span (rectangle) across the Axes. |
| [`axvline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html#matplotlib.pyplot.axvline "matplotlib.pyplot.axvline") | Add a vertical line spanning the whole or fraction of the Axes. |
| [`axvspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvspan.html#matplotlib.pyplot.axvspan "matplotlib.pyplot.axvspan") | Add a vertical span (rectangle) across the Axes. |
| [`axline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axline.html#matplotlib.pyplot.axline "matplotlib.pyplot.axline") | Add an infinitely long straight line. |

### Spectral[#](https://matplotlib.org/stable/api/pyplot_summary.html#spectral "Link to this heading")

|     |     |
| --- | --- |
| [`acorr`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.acorr.html#matplotlib.pyplot.acorr "matplotlib.pyplot.acorr") | Plot the autocorrelation of _x_. |
| [`angle_spectrum`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.angle_spectrum.html#matplotlib.pyplot.angle_spectrum "matplotlib.pyplot.angle_spectrum") | Plot the angle spectrum. |
| [`cohere`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.cohere.html#matplotlib.pyplot.cohere "matplotlib.pyplot.cohere") | Plot the coherence between _x_ and _y_. |
| [`csd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.csd.html#matplotlib.pyplot.csd "matplotlib.pyplot.csd") | Plot the cross-spectral density. |
| [`magnitude_spectrum`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.magnitude_spectrum.html#matplotlib.pyplot.magnitude_spectrum "matplotlib.pyplot.magnitude_spectrum") | Plot the magnitude spectrum. |
| [`phase_spectrum`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.phase_spectrum.html#matplotlib.pyplot.phase_spectrum "matplotlib.pyplot.phase_spectrum") | Plot the phase spectrum. |
| [`psd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.psd.html#matplotlib.pyplot.psd "matplotlib.pyplot.psd") | Plot the power spectral density. |
| [`specgram`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.specgram.html#matplotlib.pyplot.specgram "matplotlib.pyplot.specgram") | Plot a spectrogram. |
| [`xcorr`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xcorr.html#matplotlib.pyplot.xcorr "matplotlib.pyplot.xcorr") | Plot the cross correlation between _x_ and _y_. |

### Statistics[#](https://matplotlib.org/stable/api/pyplot_summary.html#statistics "Link to this heading")

|     |     |
| --- | --- |
| [`ecdf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ecdf.html#matplotlib.pyplot.ecdf "matplotlib.pyplot.ecdf") | Compute and plot the empirical cumulative distribution function of _x_. |
| [`boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot") | Draw a box and whisker plot. |
| [`violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html#matplotlib.pyplot.violinplot "matplotlib.pyplot.violinplot") | Make a violin plot. |

### Binned[#](https://matplotlib.org/stable/api/pyplot_summary.html#binned "Link to this heading")

|     |     |
| --- | --- |
| [`hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hexbin.html#matplotlib.pyplot.hexbin "matplotlib.pyplot.hexbin") | Make a 2D hexagonal binning plot of points _x_, _y_. |
| [`hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist") | Compute and plot a histogram. |
| [`hist2d`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist2d.html#matplotlib.pyplot.hist2d "matplotlib.pyplot.hist2d") | Make a 2D histogram plot. |
| [`stairs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stairs.html#matplotlib.pyplot.stairs "matplotlib.pyplot.stairs") | Draw a stepwise constant function as a line or a filled plot. |

### Contours[#](https://matplotlib.org/stable/api/pyplot_summary.html#contours "Link to this heading")

|     |     |
| --- | --- |
| [`clabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clabel.html#matplotlib.pyplot.clabel "matplotlib.pyplot.clabel") | Label a contour plot. |
| [`contour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html#matplotlib.pyplot.contour "matplotlib.pyplot.contour") | Plot contour lines. |
| [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contourf.html#matplotlib.pyplot.contourf "matplotlib.pyplot.contourf") | Plot filled contours. |

### 2D arrays[#](https://matplotlib.org/stable/api/pyplot_summary.html#d-arrays "Link to this heading")

|     |     |
| --- | --- |
| [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow") | Display data as an image, i.e., on a 2D regular raster. |
| [`matshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html#matplotlib.pyplot.matshow "matplotlib.pyplot.matshow") | Display a 2D array as a matrix in a new figure window. |
| [`pcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolor.html#matplotlib.pyplot.pcolor "matplotlib.pyplot.pcolor") | Create a pseudocolor plot with a non-regular rectangular grid. |
| [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolormesh.html#matplotlib.pyplot.pcolormesh "matplotlib.pyplot.pcolormesh") | Create a pseudocolor plot with a non-regular rectangular grid. |
| [`spy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.spy.html#matplotlib.pyplot.spy "matplotlib.pyplot.spy") | Plot the sparsity pattern of a 2D array. |
| [`figimage`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figimage.html#matplotlib.pyplot.figimage "matplotlib.pyplot.figimage") | Add a non-resampled image to the figure. |

### Unstructured triangles[#](https://matplotlib.org/stable/api/pyplot_summary.html#unstructured-triangles "Link to this heading")

|     |     |
| --- | --- |
| [`triplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.triplot.html#matplotlib.pyplot.triplot "matplotlib.pyplot.triplot") | Draw an unstructured triangular grid as lines and/or markers. |
| [`tripcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tripcolor.html#matplotlib.pyplot.tripcolor "matplotlib.pyplot.tripcolor") | Create a pseudocolor plot of an unstructured triangular grid. |
| [`tricontour`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontour.html#matplotlib.pyplot.tricontour "matplotlib.pyplot.tricontour") | Draw contour lines on an unstructured triangular grid. |
| [`tricontourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tricontourf.html#matplotlib.pyplot.tricontourf "matplotlib.pyplot.tricontourf") | Draw contour regions on an unstructured triangular grid. |

### Text and annotations[#](https://matplotlib.org/stable/api/pyplot_summary.html#text-and-annotations "Link to this heading")

|     |     |
| --- | --- |
| [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate") | Annotate the point _xy_ with text _text_. |
| [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text") | Add text to the Axes. |
| [`figtext`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figtext.html#matplotlib.pyplot.figtext "matplotlib.pyplot.figtext") | Add text to figure. |
| [`table`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.table.html#matplotlib.pyplot.table "matplotlib.pyplot.table") | Add a table to an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br>. |
| [`arrow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.arrow.html#matplotlib.pyplot.arrow "matplotlib.pyplot.arrow") | \[_Discouraged_\] Add an arrow to the Axes. |
| [`figlegend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figlegend.html#matplotlib.pyplot.figlegend "matplotlib.pyplot.figlegend") | Place a legend on the figure. |
| [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend") | Place a legend on the Axes. |

### Vector fields[#](https://matplotlib.org/stable/api/pyplot_summary.html#vector-fields "Link to this heading")

|     |     |
| --- | --- |
| [`barbs`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barbs.html#matplotlib.pyplot.barbs "matplotlib.pyplot.barbs") | Plot a 2D field of wind barbs. |
| [`quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html#matplotlib.pyplot.quiver "matplotlib.pyplot.quiver") | Plot a 2D field of arrows. |
| [`quiverkey`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiverkey.html#matplotlib.pyplot.quiverkey "matplotlib.pyplot.quiverkey") | Add a key to a quiver plot. |
| [`streamplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.streamplot.html#matplotlib.pyplot.streamplot "matplotlib.pyplot.streamplot") | Draw streamlines of a vector flow. |

Axis configuration[#](https://matplotlib.org/stable/api/pyplot_summary.html#axis-configuration "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`autoscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.autoscale.html#matplotlib.pyplot.autoscale "matplotlib.pyplot.autoscale") | Autoscale the axis view to the data (toggle). |
| [`axis`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axis.html#matplotlib.pyplot.axis "matplotlib.pyplot.axis") | Convenience method to get or set some axis properties. |
| [`box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.box.html#matplotlib.pyplot.box "matplotlib.pyplot.box") | Turn the Axes box on or off on the current Axes. |
| [`grid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html#matplotlib.pyplot.grid "matplotlib.pyplot.grid") | Configure the grid lines. |
| [`locator_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.locator_params.html#matplotlib.pyplot.locator_params "matplotlib.pyplot.locator_params") | Control behavior of major tick locators. |
| [`minorticks_off`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.minorticks_off.html#matplotlib.pyplot.minorticks_off "matplotlib.pyplot.minorticks_off") | Remove minor ticks from the Axes. |
| [`minorticks_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.minorticks_on.html#matplotlib.pyplot.minorticks_on "matplotlib.pyplot.minorticks_on") | Display minor ticks on the Axes. |
| [`rgrids`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rgrids.html#matplotlib.pyplot.rgrids "matplotlib.pyplot.rgrids") | Get or set the radial gridlines on the current polar plot. |
| [`thetagrids`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.thetagrids.html#matplotlib.pyplot.thetagrids "matplotlib.pyplot.thetagrids") | Get or set the theta gridlines on the current polar plot. |
| [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tick_params.html#matplotlib.pyplot.tick_params "matplotlib.pyplot.tick_params") | Change the appearance of ticks, tick labels, and gridlines. |
| [`ticklabel_format`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ticklabel_format.html#matplotlib.pyplot.ticklabel_format "matplotlib.pyplot.ticklabel_format") | Configure the [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")<br> used by default for linear Axes. |
| [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html#matplotlib.pyplot.xlabel "matplotlib.pyplot.xlabel") | Set the label for the x-axis. |
| [`xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlim.html#matplotlib.pyplot.xlim "matplotlib.pyplot.xlim") | Get or set the x limits of the current Axes. |
| [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html#matplotlib.pyplot.xscale "matplotlib.pyplot.xscale") | Set the xaxis' scale. |
| [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html#matplotlib.pyplot.xticks "matplotlib.pyplot.xticks") | Get or set the current tick locations and labels of the x-axis. |
| [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html#matplotlib.pyplot.ylabel "matplotlib.pyplot.ylabel") | Set the label for the y-axis. |
| [`ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html#matplotlib.pyplot.ylim "matplotlib.pyplot.ylim") | Get or set the y-limits of the current Axes. |
| [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib.pyplot.yscale "matplotlib.pyplot.yscale") | Set the yaxis' scale. |
| [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html#matplotlib.pyplot.yticks "matplotlib.pyplot.yticks") | Get or set the current tick locations and labels of the y-axis. |
| [`suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html#matplotlib.pyplot.suptitle "matplotlib.pyplot.suptitle") | Add a centered super title to the figure. |
| [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title") | Set a title for the Axes. |

Layout[#](https://matplotlib.org/stable/api/pyplot_summary.html#layout "Link to this heading")

-----------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`margins`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.margins.html#matplotlib.pyplot.margins "matplotlib.pyplot.margins") | Set or retrieve margins around the data for autoscaling axis limits. |
| [`subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust") | Adjust the subplot layout parameters. |
| [`subplot_tool`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_tool.html#matplotlib.pyplot.subplot_tool "matplotlib.pyplot.subplot_tool") | Launch a subplot tool window for a figure. |
| [`tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout") | Adjust the padding between and around subplots. |

Colormapping[#](https://matplotlib.org/stable/api/pyplot_summary.html#colormapping "Link to this heading")

-----------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`clim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clim.html#matplotlib.pyplot.clim "matplotlib.pyplot.clim") | Set the color limits of the current image. |
| [`colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar") | Add a colorbar to a plot. |
| [`gci`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gci.html#matplotlib.pyplot.gci "matplotlib.pyplot.gci") | Get the current colorable artist. |
| [`sci`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.sci.html#matplotlib.pyplot.sci "matplotlib.pyplot.sci") | Set the current image. |
| [`get_cmap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "matplotlib.pyplot.get_cmap") | Get a colormap instance, defaulting to rc values if _name_ is None. |
| [`set_cmap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.set_cmap.html#matplotlib.pyplot.set_cmap "matplotlib.pyplot.set_cmap") | Set the default colormap, and applies it to the current image if any. |
| [`imread`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html#matplotlib.pyplot.imread "matplotlib.pyplot.imread") | Read an image from a file into an array. |
| [`imsave`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imsave.html#matplotlib.pyplot.imsave "matplotlib.pyplot.imsave") | Colormap and save an array as an image file. |

Colormaps are available via the colormap registry [`matplotlib.colormaps`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps "matplotlib.colormaps")
. For convenience this registry is available in `pyplot` as

matplotlib.pyplot.colormaps[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/cm.py)
[#](https://matplotlib.org/stable/api/pyplot_summary.html#matplotlib.pyplot.colormaps "Link to this definition")

Container for colormaps that are known to Matplotlib by name.

The universal registry instance is [`matplotlib.colormaps`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps "matplotlib.colormaps")
. There should be no need for users to instantiate [`ColormapRegistry`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
 themselves.

Read access uses a dict-like interface mapping names to [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
s:

import matplotlib as mpl
cmap \= mpl.colormaps\['viridis'\]

Returned [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
s are copies, so that their modification does not change the global definition of the colormap.

Additional colormaps can be added via [`ColormapRegistry.register`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry.register "matplotlib.cm.ColormapRegistry.register")
:

mpl.colormaps.register(my\_colormap)

To get a list of all registered colormaps, you can do:

from matplotlib import colormaps
list(colormaps)

Additionally, there are shortcut functions to set builtin colormaps; e.g. `plt.viridis()` is equivalent to `plt.set_cmap('viridis')`.

matplotlib.pyplot.color\_sequences[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py)
[#](https://matplotlib.org/stable/api/pyplot_summary.html#matplotlib.pyplot.color_sequences "Link to this definition")

Container for sequences of colors that are known to Matplotlib by name.

The universal registry instance is [`matplotlib.color_sequences`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.color_sequences "matplotlib.color_sequences")
. There should be no need for users to instantiate [`ColorSequenceRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry "matplotlib.colors.ColorSequenceRegistry")
 themselves.

Read access uses a dict-like interface mapping names to lists of colors:

import matplotlib as mpl
colors \= mpl.color\_sequences\['tab10'\]

For a list of built in color sequences, see [Named color sequences](https://matplotlib.org/stable/gallery/color/color_sequences.html)
. The returned lists are copies, so that their modification does not change the global definition of the color sequence.

Additional color sequences can be added via [`ColorSequenceRegistry.register`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry.register "matplotlib.colors.ColorSequenceRegistry.register")
:

mpl.color\_sequences.register('rgb', \['r', 'g', 'b'\])

Configuration[#](https://matplotlib.org/stable/api/pyplot_summary.html#configuration "Link to this heading")

-------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`rc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html#matplotlib.pyplot.rc "matplotlib.pyplot.rc") | Set the current [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")<br>. _group_ is the grouping for the rc, e.g., for `lines.linewidth` the group is `lines`, for `axes.facecolor`, the group is `axes`, and so on. Group may also be a list or tuple of group names, e.g., (_xtick_, _ytick_). _kwargs_ is a dictionary attribute name/value pairs, e.g.,::. |
| [`rc_context`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc_context.html#matplotlib.pyplot.rc_context "matplotlib.pyplot.rc_context") | Return a context manager for temporarily changing rcParams. |
| [`rcdefaults`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rcdefaults.html#matplotlib.pyplot.rcdefaults "matplotlib.pyplot.rcdefaults") | Restore the [`rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")<br> from Matplotlib's internal default style. |

Output[#](https://matplotlib.org/stable/api/pyplot_summary.html#output "Link to this heading")

-----------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.draw.html#matplotlib.pyplot.draw "matplotlib.pyplot.draw") | Redraw the current figure. |
| [`draw_if_interactive`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.draw_if_interactive.html#matplotlib.pyplot.draw_if_interactive "matplotlib.pyplot.draw_if_interactive") | Redraw the current figure if in interactive mode. |
| [`ioff`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ioff.html#matplotlib.pyplot.ioff "matplotlib.pyplot.ioff") | Disable interactive mode. |
| [`ion`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ion.html#matplotlib.pyplot.ion "matplotlib.pyplot.ion") | Enable interactive mode. |
| [`install_repl_displayhook`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.install_repl_displayhook.html#matplotlib.pyplot.install_repl_displayhook "matplotlib.pyplot.install_repl_displayhook") | Connect to the display hook of the current shell. |
| [`isinteractive`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.isinteractive.html#matplotlib.pyplot.isinteractive "matplotlib.pyplot.isinteractive") | Return whether plots are updated after every plotting command. |
| [`pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pause.html#matplotlib.pyplot.pause "matplotlib.pyplot.pause") | Run the GUI event loop for _interval_ seconds. |
| [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig "matplotlib.pyplot.savefig") | Save the current figure as an image or vector graphic to a file. |
| [`show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show") | Display all open figures. |
| [`switch_backend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.switch_backend.html#matplotlib.pyplot.switch_backend "matplotlib.pyplot.switch_backend") | Set the pyplot backend. |
| [`uninstall_repl_displayhook`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.uninstall_repl_displayhook.html#matplotlib.pyplot.uninstall_repl_displayhook "matplotlib.pyplot.uninstall_repl_displayhook") | Disconnect from the display hook of the current shell. |

Other[#](https://matplotlib.org/stable/api/pyplot_summary.html#other "Link to this heading")

---------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`connect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.connect.html#matplotlib.pyplot.connect "matplotlib.pyplot.connect") | Bind function _func_ to event _s_. |
| [`disconnect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.disconnect.html#matplotlib.pyplot.disconnect "matplotlib.pyplot.disconnect") | Disconnect the callback with id _cid_. |
| [`findobj`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.findobj.html#matplotlib.pyplot.findobj "matplotlib.pyplot.findobj") | Find artist objects. |
| [`get`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get.html#matplotlib.pyplot.get "matplotlib.pyplot.get") | Return the value of an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>'s _property_, or print all of them. |
| [`getp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.getp.html#matplotlib.pyplot.getp "matplotlib.pyplot.getp") | Return the value of an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>'s _property_, or print all of them. |
| [`get_current_fig_manager`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_current_fig_manager.html#matplotlib.pyplot.get_current_fig_manager "matplotlib.pyplot.get_current_fig_manager") | Return the figure manager of the current figure. |
| [`ginput`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ginput.html#matplotlib.pyplot.ginput "matplotlib.pyplot.ginput") | Blocking call to interact with a figure. |
| [`new_figure_manager`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.new_figure_manager.html#matplotlib.pyplot.new_figure_manager "matplotlib.pyplot.new_figure_manager") | Create a new figure manager instance. |
| [`set_loglevel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.set_loglevel.html#matplotlib.pyplot.set_loglevel "matplotlib.pyplot.set_loglevel") | Configure Matplotlib's logging levels. |
| [`setp`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.setp.html#matplotlib.pyplot.setp "matplotlib.pyplot.setp") | Set one or more properties on an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br>, or list allowed values. |
| [`waitforbuttonpress`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.waitforbuttonpress.html#matplotlib.pyplot.waitforbuttonpress "matplotlib.pyplot.waitforbuttonpress") | Blocking call to interact with the figure. |
| [`xkcd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html#matplotlib.pyplot.xkcd "matplotlib.pyplot.xkcd") | Turn on [xkcd](https://xkcd.com/)<br> sketch-style drawing mode. |

On this page