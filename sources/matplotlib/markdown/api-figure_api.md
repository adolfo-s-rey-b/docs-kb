[Skip to main content](https://matplotlib.org/stable/api/figure_api.html#main-content)

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
    

`matplotlib.figure`[#](https://matplotlib.org/stable/api/figure_api.html#module-matplotlib.figure "Link to this heading")

==========================================================================================================================

[`matplotlib.figure`](https://matplotlib.org/stable/api/figure_api.html#module-matplotlib.figure "matplotlib.figure")
 implements the following classes:

[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

Top level [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
, which holds all plot elements. Many methods are implemented in [`FigureBase`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase "matplotlib.figure.FigureBase")
.

[`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")

A logical figure inside a figure, usually added to a figure (or parent [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
) with [`Figure.add_subfigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#matplotlib.figure.Figure.add_subfigure "matplotlib.figure.Figure.add_subfigure")
 or [`Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 methods.

Figures are typically created using pyplot methods [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
, [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
, and [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
.

fig, ax \= plt.subplots(figsize\=(2, 2), facecolor\='lightskyblue',
                       layout\='constrained')
fig.suptitle('Figure')
ax.set\_title('Axes', loc\='left', fontstyle\='oblique', fontsize\='medium')

([`Source code`](https://matplotlib.org/stable/_downloads/3928de11b4fbd0ba3f492ed92aebda79/figure_api-1.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/37981875abad13945405683f462a9931/figure_api-1.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/38bf68f42cdd9788ce147da6927a8a7d/figure_api-1.png)
)

[![](https://matplotlib.org/stable/_images/api-figure_api-1.2x.png)](https://matplotlib.org/stable/_images/api-figure_api-1.2x.png)

Some situations call for directly instantiating a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 class, usually inside an application of some sort (see [Embedding Matplotlib in graphical user interfaces](https://matplotlib.org/stable/gallery/user_interfaces/index.html#user-interfaces)
 for a list of examples) . More information about Figures can be found at [Introduction to Figures](https://matplotlib.org/stable/users/explain/figure/figure_intro.html#figure-intro)
.

Figure[#](https://matplotlib.org/stable/api/figure_api.html#figure "Link to this heading")

-------------------------------------------------------------------------------------------

### Figure class[#](https://matplotlib.org/stable/api/figure_api.html#figure-class "Link to this heading")

|     |     |
| --- | --- |
| [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure") | The top level container for all the plot elements. |

### Adding Axes and SubFigures[#](https://matplotlib.org/stable/api/figure_api.html#adding-axes-and-subfigures "Link to this heading")

|     |     |
| --- | --- |
| [`Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes") | Add an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br> to the figure. |
| [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot") | Add an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br> to the figure as part of a subplot arrangement. |
| [`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots") | Add a set of subplots to this figure. |
| [`Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic") | Build a layout of Axes based on ASCII art or nested lists. |
| [`Figure.add_gridspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_gridspec.html#matplotlib.figure.Figure.add_gridspec "matplotlib.figure.Figure.add_gridspec") | Low-level API for creating a [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")<br> that has this figure as a parent. |
| [`Figure.get_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_axes.html#matplotlib.figure.Figure.get_axes "matplotlib.figure.Figure.get_axes") | List of Axes in the Figure. |
| [`Figure.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.axes.html#matplotlib.figure.Figure.axes "matplotlib.figure.Figure.axes") | List of Axes in the Figure. |
| [`Figure.delaxes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.delaxes.html#matplotlib.figure.Figure.delaxes "matplotlib.figure.Figure.delaxes") | Remove the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br> _ax_ from the figure; update the current Axes. |
| [`Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures") | Add a set of subfigures to this figure or subfigure. |
| [`Figure.add_subfigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subfigure.html#matplotlib.figure.Figure.add_subfigure "matplotlib.figure.Figure.add_subfigure") | Add a [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")<br> to the figure as part of a subplot arrangement. |

### Saving[#](https://matplotlib.org/stable/api/figure_api.html#saving "Link to this heading")

|     |     |
| --- | --- |
| [`Figure.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig") | Save the current figure as an image or vector graphic to a file. |

### Annotating[#](https://matplotlib.org/stable/api/figure_api.html#annotating "Link to this heading")

|     |     |
| --- | --- |
| [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar") | Add a colorbar to a plot. |
| [`Figure.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend") | Place a legend on the figure. |
| [`Figure.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text") | Add text to figure. |
| [`Figure.suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle") | Add a centered super title to the figure. |
| [`Figure.get_suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_suptitle.html#matplotlib.figure.Figure.get_suptitle "matplotlib.figure.Figure.get_suptitle") | Return the suptitle as string or an empty string if not set. |
| [`Figure.supxlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supxlabel.html#matplotlib.figure.Figure.supxlabel "matplotlib.figure.Figure.supxlabel") | Add a centered super xlabel to the figure. |
| [`Figure.get_supxlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_supxlabel.html#matplotlib.figure.Figure.get_supxlabel "matplotlib.figure.Figure.get_supxlabel") | Return the supxlabel as string or an empty string if not set. |
| [`Figure.supylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.supylabel.html#matplotlib.figure.Figure.supylabel "matplotlib.figure.Figure.supylabel") | Add a centered super ylabel to the figure. |
| [`Figure.get_supylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_supylabel.html#matplotlib.figure.Figure.get_supylabel "matplotlib.figure.Figure.get_supylabel") | Return the supylabel as string or an empty string if not set. |
| [`Figure.align_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_labels.html#matplotlib.figure.Figure.align_labels "matplotlib.figure.Figure.align_labels") | Align the xlabels and ylabels of subplots with the same subplots row or column (respectively) if label alignment is being done automatically (i.e. the label position is not manually set). |
| [`Figure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels") | Align the xlabels of subplots in the same subplot row if label alignment is being done automatically (i.e. the label position is not manually set). |
| [`Figure.align_ylabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "matplotlib.figure.Figure.align_ylabels") | Align the ylabels of subplots in the same subplot column if label alignment is being done automatically (i.e. the label position is not manually set). |
| [`Figure.align_titles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_titles.html#matplotlib.figure.Figure.align_titles "matplotlib.figure.Figure.align_titles") | Align the titles of subplots in the same subplot row if title alignment is being done automatically (i.e. the title position is not manually set). |
| [`Figure.autofmt_xdate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.autofmt_xdate.html#matplotlib.figure.Figure.autofmt_xdate "matplotlib.figure.Figure.autofmt_xdate") | Date ticklabels often overlap, so it is useful to rotate them and right align them. |

### Figure geometry[#](https://matplotlib.org/stable/api/figure_api.html#figure-geometry "Link to this heading")

|     |     |
| --- | --- |
| [`Figure.set_size_inches`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_size_inches.html#matplotlib.figure.Figure.set_size_inches "matplotlib.figure.Figure.set_size_inches") | Set the figure size in inches. |
| [`Figure.get_size_inches`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_size_inches.html#matplotlib.figure.Figure.get_size_inches "matplotlib.figure.Figure.get_size_inches") | Return the current size of the figure in inches. |
| [`Figure.set_figheight`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figheight.html#matplotlib.figure.Figure.set_figheight "matplotlib.figure.Figure.set_figheight") | Set the height of the figure in inches. |
| [`Figure.get_figheight`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_figheight.html#matplotlib.figure.Figure.get_figheight "matplotlib.figure.Figure.get_figheight") | Return the figure height in inches. |
| [`Figure.set_figwidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figwidth.html#matplotlib.figure.Figure.set_figwidth "matplotlib.figure.Figure.set_figwidth") | Set the width of the figure in inches. |
| [`Figure.get_figwidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_figwidth.html#matplotlib.figure.Figure.get_figwidth "matplotlib.figure.Figure.get_figwidth") | Return the figure width in inches. |
| [`Figure.dpi`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.dpi.html#matplotlib.figure.Figure.dpi "matplotlib.figure.Figure.dpi") | The resolution in dots per inch. |
| [`Figure.set_dpi`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_dpi.html#matplotlib.figure.Figure.set_dpi "matplotlib.figure.Figure.set_dpi") | Set the resolution of the figure in dots-per-inch. |
| [`Figure.get_dpi`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_dpi.html#matplotlib.figure.Figure.get_dpi "matplotlib.figure.Figure.get_dpi") | Return the resolution in dots per inch as a float. |

### Subplot layout[#](https://matplotlib.org/stable/api/figure_api.html#subplot-layout "Link to this heading")

|     |     |
| --- | --- |
| [`Figure.subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust") | Adjust the subplot layout parameters. |
| [`Figure.set_layout_engine`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html#matplotlib.figure.Figure.set_layout_engine "matplotlib.figure.Figure.set_layout_engine") | Set the layout engine for this figure. |
| [`Figure.get_layout_engine`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_layout_engine.html#matplotlib.figure.Figure.get_layout_engine "matplotlib.figure.Figure.get_layout_engine") |     |

#### Discouraged or deprecated[#](https://matplotlib.org/stable/api/figure_api.html#discouraged-or-deprecated "Link to this heading")

|     |     |
| --- | --- |
| [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout") | Adjust the padding between and around subplots. |
| [`Figure.set_tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_tight_layout.html#matplotlib.figure.Figure.set_tight_layout "matplotlib.figure.Figure.set_tight_layout") | \[_Deprecated_\] Set whether and how [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")<br> is called when drawing. |
| [`Figure.get_tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_tight_layout.html#matplotlib.figure.Figure.get_tight_layout "matplotlib.figure.Figure.get_tight_layout") | Return whether [`Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")<br> is called when drawing. |
| [`Figure.set_constrained_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout.html#matplotlib.figure.Figure.set_constrained_layout "matplotlib.figure.Figure.set_constrained_layout") | \[_Deprecated_\] Set whether `constrained_layout` is used upon drawing. |
| [`Figure.get_constrained_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_constrained_layout.html#matplotlib.figure.Figure.get_constrained_layout "matplotlib.figure.Figure.get_constrained_layout") | Return whether constrained layout is being used. |
| [`Figure.set_constrained_layout_pads`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_constrained_layout_pads.html#matplotlib.figure.Figure.set_constrained_layout_pads "matplotlib.figure.Figure.set_constrained_layout_pads") | \[_Deprecated_\] Set padding for `constrained_layout`. |
| [`Figure.get_constrained_layout_pads`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_constrained_layout_pads.html#matplotlib.figure.Figure.get_constrained_layout_pads "matplotlib.figure.Figure.get_constrained_layout_pads") | \[_Deprecated_\] Get padding for `constrained_layout`. |

### Interactive[#](https://matplotlib.org/stable/api/figure_api.html#interactive "Link to this heading")

See also

*   [Event handling and picking](https://matplotlib.org/stable/users/explain/figure/event_handling.html#event-handling)
    

|     |     |
| --- | --- |
| [`Figure.ginput`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.ginput.html#matplotlib.figure.Figure.ginput "matplotlib.figure.Figure.ginput") | Blocking call to interact with a figure. |
| [`Figure.add_axobserver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axobserver.html#matplotlib.figure.Figure.add_axobserver "matplotlib.figure.Figure.add_axobserver") | Whenever the Axes state change, `func(self)` will be called. |
| [`Figure.waitforbuttonpress`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.waitforbuttonpress.html#matplotlib.figure.Figure.waitforbuttonpress "matplotlib.figure.Figure.waitforbuttonpress") | Blocking call to interact with the figure. |
| [`Figure.pick`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.pick.html#matplotlib.figure.Figure.pick "matplotlib.figure.Figure.pick") | Process a pick event. |

### Modifying appearance[#](https://matplotlib.org/stable/api/figure_api.html#modifying-appearance "Link to this heading")

|     |     |
| --- | --- |
| [`Figure.set_frameon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_frameon.html#matplotlib.figure.Figure.set_frameon "matplotlib.figure.Figure.set_frameon") | Set the figure's background patch visibility, i.e. whether the figure background will be drawn. |
| [`Figure.get_frameon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_frameon.html#matplotlib.figure.Figure.get_frameon "matplotlib.figure.Figure.get_frameon") | Return the figure's background patch visibility, i.e. whether the figure background will be drawn. |
| [`Figure.set_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_linewidth.html#matplotlib.figure.Figure.set_linewidth "matplotlib.figure.Figure.set_linewidth") | Set the line width of the Figure rectangle. |
| [`Figure.get_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_linewidth.html#matplotlib.figure.Figure.get_linewidth "matplotlib.figure.Figure.get_linewidth") | Get the line width of the Figure rectangle. |
| [`Figure.set_facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_facecolor.html#matplotlib.figure.Figure.set_facecolor "matplotlib.figure.Figure.set_facecolor") | Set the face color of the Figure rectangle. |
| [`Figure.get_facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_facecolor.html#matplotlib.figure.Figure.get_facecolor "matplotlib.figure.Figure.get_facecolor") | Get the face color of the Figure rectangle. |
| [`Figure.set_edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_edgecolor.html#matplotlib.figure.Figure.set_edgecolor "matplotlib.figure.Figure.set_edgecolor") | Set the edge color of the Figure rectangle. |
| [`Figure.get_edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_edgecolor.html#matplotlib.figure.Figure.get_edgecolor "matplotlib.figure.Figure.get_edgecolor") | Get the edge color of the Figure rectangle. |

### Adding and getting Artists[#](https://matplotlib.org/stable/api/figure_api.html#adding-and-getting-artists "Link to this heading")

|     |     |
| --- | --- |
| [`Figure.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_artist.html#matplotlib.figure.Figure.add_artist "matplotlib.figure.Figure.add_artist") | Add an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br> to the figure. |
| [`Figure.get_children`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_children.html#matplotlib.figure.Figure.get_children "matplotlib.figure.Figure.get_children") | Get a list of artists contained in the figure. |
| [`Figure.figimage`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.figimage.html#matplotlib.figure.Figure.figimage "matplotlib.figure.Figure.figimage") | Add a non-resampled image to the figure. |

### Getting and modifying state[#](https://matplotlib.org/stable/api/figure_api.html#getting-and-modifying-state "Link to this heading")

See also

*   [Interactive figures](https://matplotlib.org/stable/users/explain/figure/interactive.html#interactive-figures)
    

|     |     |
| --- | --- |
| [`Figure.clear`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.clear.html#matplotlib.figure.Figure.clear "matplotlib.figure.Figure.clear") | Clear the figure. |
| [`Figure.gca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.gca.html#matplotlib.figure.Figure.gca "matplotlib.figure.Figure.gca") | Get the current Axes. |
| [`Figure.sca`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.sca.html#matplotlib.figure.Figure.sca "matplotlib.figure.Figure.sca") | Set the current Axes to be _a_ and return _a_. |
| [`Figure.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_tightbbox.html#matplotlib.figure.Figure.get_tightbbox "matplotlib.figure.Figure.get_tightbbox") | Return a (tight) bounding box of the figure _in inches_. |
| [`Figure.get_window_extent`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_window_extent.html#matplotlib.figure.Figure.get_window_extent "matplotlib.figure.Figure.get_window_extent") | Get the artist's bounding box in display space, ignoring clipping. |
| [`Figure.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.show.html#matplotlib.figure.Figure.show "matplotlib.figure.Figure.show") | If using a GUI backend with pyplot, display the figure window. |
| [`Figure.set_canvas`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_canvas.html#matplotlib.figure.Figure.set_canvas "matplotlib.figure.Figure.set_canvas") | Set the canvas that contains the figure |
| [`Figure.draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw.html#matplotlib.figure.Figure.draw "matplotlib.figure.Figure.draw") | Draw the Artist (and its children) using the given renderer. |
| [`Figure.draw_without_rendering`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html#matplotlib.figure.Figure.draw_without_rendering "matplotlib.figure.Figure.draw_without_rendering") | Draw the figure with no output. |
| [`Figure.draw_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_artist.html#matplotlib.figure.Figure.draw_artist "matplotlib.figure.Figure.draw_artist") | Draw [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br> _a_ only. |

SubFigure[#](https://matplotlib.org/stable/api/figure_api.html#subfigure "Link to this heading")

-------------------------------------------------------------------------------------------------

Matplotlib has the concept of a [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
, which is a logical figure inside a parent [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
. It has many of the same methods as the parent. See [Nested Axes layouts](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html#nested-axes-layouts)
.

([`Source code`](https://matplotlib.org/stable/_downloads/382c9b85341197b76d986e481c645d41/figure_api-2.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/da916275b47491944b59f7675d56ce3e/figure_api-2.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/6d2d947373c1c37fbc4b6d0d0e4f83d9/figure_api-2.png)
)

[![](https://matplotlib.org/stable/_images/api-figure_api-2.2x.png)](https://matplotlib.org/stable/_images/api-figure_api-2.2x.png)

### SubFigure class[#](https://matplotlib.org/stable/api/figure_api.html#subfigure-class "Link to this heading")

|     |     |
| --- | --- |
| [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") | Logical figure that can be placed inside a figure. |

### Adding Axes and SubFigures[#](https://matplotlib.org/stable/api/figure_api.html#id1 "Link to this heading")

|     |     |
| --- | --- |
| [`SubFigure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_axes.html#matplotlib.figure.SubFigure.add_axes "matplotlib.figure.SubFigure.add_axes") | Add an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br> to the figure. |
| [`SubFigure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_subplot.html#matplotlib.figure.SubFigure.add_subplot "matplotlib.figure.SubFigure.add_subplot") | Add an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br> to the figure as part of a subplot arrangement. |
| [`SubFigure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplots.html#matplotlib.figure.SubFigure.subplots "matplotlib.figure.SubFigure.subplots") | Add a set of subplots to this figure. |
| [`SubFigure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subplot_mosaic.html#matplotlib.figure.SubFigure.subplot_mosaic "matplotlib.figure.SubFigure.subplot_mosaic") | Build a layout of Axes based on ASCII art or nested lists. |
| [`SubFigure.add_gridspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_gridspec.html#matplotlib.figure.SubFigure.add_gridspec "matplotlib.figure.SubFigure.add_gridspec") | Low-level API for creating a [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")<br> that has this figure as a parent. |
| [`SubFigure.delaxes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.delaxes.html#matplotlib.figure.SubFigure.delaxes "matplotlib.figure.SubFigure.delaxes") | Remove the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br> _ax_ from the figure; update the current Axes. |
| [`SubFigure.add_subfigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_subfigure.html#matplotlib.figure.SubFigure.add_subfigure "matplotlib.figure.SubFigure.add_subfigure") | Add a [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")<br> to the figure as part of a subplot arrangement. |
| [`SubFigure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.subfigures.html#matplotlib.figure.SubFigure.subfigures "matplotlib.figure.SubFigure.subfigures") | Add a set of subfigures to this figure or subfigure. |

### Annotating[#](https://matplotlib.org/stable/api/figure_api.html#id2 "Link to this heading")

|     |     |
| --- | --- |
| [`SubFigure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.colorbar.html#matplotlib.figure.SubFigure.colorbar "matplotlib.figure.SubFigure.colorbar") | Add a colorbar to a plot. |
| [`SubFigure.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.legend.html#matplotlib.figure.SubFigure.legend "matplotlib.figure.SubFigure.legend") | Place a legend on the figure. |
| [`SubFigure.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.text.html#matplotlib.figure.SubFigure.text "matplotlib.figure.SubFigure.text") | Add text to figure. |
| [`SubFigure.suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.suptitle.html#matplotlib.figure.SubFigure.suptitle "matplotlib.figure.SubFigure.suptitle") | Add a centered super title to the figure. |
| [`SubFigure.get_suptitle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.get_suptitle.html#matplotlib.figure.SubFigure.get_suptitle "matplotlib.figure.SubFigure.get_suptitle") | Return the suptitle as string or an empty string if not set. |
| [`SubFigure.supxlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.supxlabel.html#matplotlib.figure.SubFigure.supxlabel "matplotlib.figure.SubFigure.supxlabel") | Add a centered super xlabel to the figure. |
| [`SubFigure.get_supxlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.get_supxlabel.html#matplotlib.figure.SubFigure.get_supxlabel "matplotlib.figure.SubFigure.get_supxlabel") | Return the supxlabel as string or an empty string if not set. |
| [`SubFigure.supylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.supylabel.html#matplotlib.figure.SubFigure.supylabel "matplotlib.figure.SubFigure.supylabel") | Add a centered super ylabel to the figure. |
| [`SubFigure.get_supylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.get_supylabel.html#matplotlib.figure.SubFigure.get_supylabel "matplotlib.figure.SubFigure.get_supylabel") | Return the supylabel as string or an empty string if not set. |
| [`SubFigure.align_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.align_labels.html#matplotlib.figure.SubFigure.align_labels "matplotlib.figure.SubFigure.align_labels") | Align the xlabels and ylabels of subplots with the same subplots row or column (respectively) if label alignment is being done automatically (i.e. the label position is not manually set). |
| [`SubFigure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.align_xlabels.html#matplotlib.figure.SubFigure.align_xlabels "matplotlib.figure.SubFigure.align_xlabels") | Align the xlabels of subplots in the same subplot row if label alignment is being done automatically (i.e. the label position is not manually set). |
| [`SubFigure.align_ylabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.align_ylabels.html#matplotlib.figure.SubFigure.align_ylabels "matplotlib.figure.SubFigure.align_ylabels") | Align the ylabels of subplots in the same subplot column if label alignment is being done automatically (i.e. the label position is not manually set). |
| [`SubFigure.align_titles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.align_titles.html#matplotlib.figure.SubFigure.align_titles "matplotlib.figure.SubFigure.align_titles") | Align the titles of subplots in the same subplot row if title alignment is being done automatically (i.e. the title position is not manually set). |

### Adding and getting Artists[#](https://matplotlib.org/stable/api/figure_api.html#id3 "Link to this heading")

|     |     |
| --- | --- |
| [`SubFigure.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.add_artist.html#matplotlib.figure.SubFigure.add_artist "matplotlib.figure.SubFigure.add_artist") | Add an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br> to the figure. |
| [`SubFigure.get_children`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.get_children.html#matplotlib.figure.SubFigure.get_children "matplotlib.figure.SubFigure.get_children") | Get a list of artists contained in the figure. |

### Modifying appearance[#](https://matplotlib.org/stable/api/figure_api.html#id4 "Link to this heading")

|     |     |
| --- | --- |
| [`SubFigure.set_frameon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.set_frameon.html#matplotlib.figure.SubFigure.set_frameon "matplotlib.figure.SubFigure.set_frameon") | Set the figure's background patch visibility, i.e. whether the figure background will be drawn. |
| [`SubFigure.get_frameon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.get_frameon.html#matplotlib.figure.SubFigure.get_frameon "matplotlib.figure.SubFigure.get_frameon") | Return the figure's background patch visibility, i.e. whether the figure background will be drawn. |
| [`SubFigure.set_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.set_linewidth.html#matplotlib.figure.SubFigure.set_linewidth "matplotlib.figure.SubFigure.set_linewidth") | Set the line width of the Figure rectangle. |
| [`SubFigure.get_linewidth`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.get_linewidth.html#matplotlib.figure.SubFigure.get_linewidth "matplotlib.figure.SubFigure.get_linewidth") | Get the line width of the Figure rectangle. |
| [`SubFigure.set_facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.set_facecolor.html#matplotlib.figure.SubFigure.set_facecolor "matplotlib.figure.SubFigure.set_facecolor") | Set the face color of the Figure rectangle. |
| [`SubFigure.get_facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.get_facecolor.html#matplotlib.figure.SubFigure.get_facecolor "matplotlib.figure.SubFigure.get_facecolor") | Get the face color of the Figure rectangle. |
| [`SubFigure.set_edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.set_edgecolor.html#matplotlib.figure.SubFigure.set_edgecolor "matplotlib.figure.SubFigure.set_edgecolor") | Set the edge color of the Figure rectangle. |
| [`SubFigure.get_edgecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.get_edgecolor.html#matplotlib.figure.SubFigure.get_edgecolor "matplotlib.figure.SubFigure.get_edgecolor") | Get the edge color of the Figure rectangle. |

### Passthroughs[#](https://matplotlib.org/stable/api/figure_api.html#passthroughs "Link to this heading")

|     |     |
| --- | --- |
| [`SubFigure.set_dpi`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.set_dpi.html#matplotlib.figure.SubFigure.set_dpi "matplotlib.figure.SubFigure.set_dpi") | Set the resolution of parent figure in dots-per-inch. |
| [`SubFigure.get_dpi`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.get_dpi.html#matplotlib.figure.SubFigure.get_dpi "matplotlib.figure.SubFigure.get_dpi") | Return the resolution of the parent figure in dots-per-inch as a float. |

FigureBase parent class[#](https://matplotlib.org/stable/api/figure_api.html#figurebase-parent-class "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

class matplotlib.figure.FigureBase(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L118-L2219)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase "Link to this definition")

Base class for [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 and [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 containing the methods that add artists to the figure or subfigure, create Axes, etc.

add\_artist(_artist_, _clip\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L503-L536)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.add_artist "Link to this definition")

Add an [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 to the figure.

Usually artists are added to [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 objects using [`Axes.add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
; this method can be used in the rare cases where one needs to add artists directly to the figure instead.

Parameters:

**artist**[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

The artist to add to the figure. If the added artist has no transform previously set, its transform will be set to `figure.transSubfigure`.

**clip**bool, default: False

Whether the added artist should be clipped by the figure patch.

Returns:

[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")

The added artist.

add\_axes(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L538-L649)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.add_axes "Link to this definition")

Add an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to the figure.

Call signatures:

add\_axes(rect, projection\=None, polar\=False, \*\*kwargs)
add\_axes(ax)

Parameters:

**rect**tuple (left, bottom, width, height)

The dimensions (left, bottom, width, height) of the new [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. All quantities are in fractions of figure width and height.

**projection**{None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str}, optional

The projection type of the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
. _str_ is the name of a custom projection, see [`projections`](https://matplotlib.org/stable/api/projections_api.html#module-matplotlib.projections "matplotlib.projections")
. The default None results in a 'rectilinear' projection.

**polar**bool, default: False

If True, equivalent to projection='polar'.

**axes\_class**subclass type of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

The [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 subclass that is instantiated. This parameter is incompatible with _projection_ and _polar_. See [axisartist](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#axisartist-users-guide-index)
 for examples.

**sharex, sharey**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

Share the x or y [`axis`](https://matplotlib.org/stable/api/axis_api.html#module-matplotlib.axis "matplotlib.axis")
 with sharex and/or sharey. The axis will have the same limits, ticks, and scale as the axis of the shared Axes.

**label**str

A label for the returned Axes.

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, or a subclass of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The returned Axes class depends on the projection used. It is [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 if rectilinear projection is used and [`projections.polar.PolarAxes`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes "matplotlib.projections.polar.PolarAxes")
 if polar projection is used.

Other Parameters:

**\*\*kwargs**

This method also takes the keyword arguments for the returned Axes class. The keyword arguments for the rectilinear Axes class [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 can be found in the following table but there might also be other keyword arguments if another projection is used, see the actual Axes class.

| Property | Description |
| --- | --- |
| [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
| [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
| [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
| [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
| [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
| [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
| [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
| [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
| [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
| [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
| [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
| [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound") | (lower: float, upper: float) |
| [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
| [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
| [`xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim") | (left: float, right: float) |
| [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
| [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
| [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
| [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
| [`ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound") | (lower: float, upper: float) |
| [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
| [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
| [`ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim") | (bottom: float, top: float) |
| [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
| [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
| [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
| [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

See also

[`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")

[`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")

[`pyplot.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")

[`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")

[`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")

Notes

In rare circumstances, [`add_axes`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.add_axes "matplotlib.figure.FigureBase.add_axes")
 may be called with a single argument, an Axes instance already created in the present figure but not in the figure's list of Axes.

Examples

Some simple examples:

rect \= l, b, w, h
fig \= plt.figure()
fig.add\_axes(rect)
fig.add\_axes(rect, frameon\=False, facecolor\='g')
fig.add\_axes(rect, polar\=True)
ax \= fig.add\_axes(rect, projection\='polar')
fig.delaxes(ax)
fig.add\_axes(ax)

add\_gridspec(_nrows\=1_, _ncols\=1_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1564-L1609)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.add_gridspec "Link to this definition")

Low-level API for creating a [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 that has this figure as a parent.

This is a low-level API, allowing you to create a gridspec and subsequently add subplots based on the gridspec. Most users do not need that freedom and should use the higher-level methods [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
 or [`subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
.

Parameters:

**nrows**int, default: 1

Number of rows in grid.

**ncols**int, default: 1

Number of columns in grid.

Returns:

[`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")

Other Parameters:

**\*\*kwargs**

Keyword arguments are passed to [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
.

See also

[`matplotlib.pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")

Examples

Adding a subplot that spans two rows:

fig \= plt.figure()
gs \= fig.add\_gridspec(2, 2)
ax1 \= fig.add\_subplot(gs\[0, 0\])
ax2 \= fig.add\_subplot(gs\[1, 0\])
\# spans two rows:
ax3 \= fig.add\_subplot(gs\[:, 1\])

add\_subfigure(_subplotspec_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1680-L1708)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.add_subfigure "Link to this definition")

Add a [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 to the figure as part of a subplot arrangement.

Parameters:

**subplotspec**[`gridspec.SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")

Defines the region in a parent gridspec where the subfigure will be placed.

Returns:

[`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")

Other Parameters:

**\*\*kwargs**

Are passed to the [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 object.

See also

[`Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")

add\_subplot(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L651-L777)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.add_subplot "Link to this definition")

Add an [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to the figure as part of a subplot arrangement.

Call signatures:

add\_subplot(nrows, ncols, index, \*\*kwargs)
add\_subplot(pos, \*\*kwargs)
add\_subplot(ax)
add\_subplot()

Parameters:

**\*args**int, (int, int, _index_), or [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
, default: (1, 1, 1)

The position of the subplot described by one of

*   Three integers (_nrows_, _ncols_, _index_). The subplot will take the _index_ position on a grid with _nrows_ rows and _ncols_ columns. _index_ starts at 1 in the upper left corner and increases to the right. _index_ can also be a two-tuple specifying the (_first_, _last_) indices (1-based, and including _last_) of the subplot, e.g., `fig.add_subplot(3, 1, (1, 2))` makes a subplot that spans the upper 2/3 of the figure.
    
*   A 3-digit integer. The digits are interpreted as if given separately as three single-digit integers, i.e. `fig.add_subplot(235)` is the same as `fig.add_subplot(2, 3, 5)`. Note that this can only be used if there are no more than 9 subplots.
    
*   A [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
    .
    

In rare circumstances, [`add_subplot`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.add_subplot "matplotlib.figure.FigureBase.add_subplot")
 may be called with a single argument, a subplot Axes instance already created in the present figure but not in the figure's list of Axes.

**projection**{None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str}, optional

The projection type of the subplot ([`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
). _str_ is the name of a custom projection, see [`projections`](https://matplotlib.org/stable/api/projections_api.html#module-matplotlib.projections "matplotlib.projections")
. The default None results in a 'rectilinear' projection.

**polar**bool, default: False

If True, equivalent to projection='polar'.

**axes\_class**subclass type of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

The [`axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 subclass that is instantiated. This parameter is incompatible with _projection_ and _polar_. See [axisartist](https://matplotlib.org/stable/users/explain/toolkits/axisartist.html#axisartist-users-guide-index)
 for examples.

**sharex, sharey**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

Share the x or y [`axis`](https://matplotlib.org/stable/api/axis_api.html#module-matplotlib.axis "matplotlib.axis")
 with sharex and/or sharey. The axis will have the same limits, ticks, and scale as the axis of the shared Axes.

**label**str

A label for the returned Axes.

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

The Axes of the subplot. The returned Axes can actually be an instance of a subclass, such as [`projections.polar.PolarAxes`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes "matplotlib.projections.polar.PolarAxes")
 for polar projections.

Other Parameters:

**\*\*kwargs**

This method also takes the keyword arguments for the returned Axes base class; except for the _figure_ argument. The keyword arguments for the rectilinear base class [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 can be found in the following table but there might also be other keyword arguments if another projection is used.

| Property | Description |
| --- | --- |
| [`adjustable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_adjustable.html#matplotlib.axes.Axes.set_adjustable "matplotlib.axes.Axes.set_adjustable") | {'box', 'datalim'} |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`anchor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_anchor.html#matplotlib.axes.Axes.set_anchor "matplotlib.axes.Axes.set_anchor") | (float, float) or {'C', 'SW', 'S', 'SE', 'E', 'NE', ...} |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect") | {'auto', 'equal'} or float |
| [`autoscale_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscale_on.html#matplotlib.axes.Axes.set_autoscale_on "matplotlib.axes.Axes.set_autoscale_on") | bool |
| [`autoscalex_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscalex_on.html#matplotlib.axes.Axes.set_autoscalex_on "matplotlib.axes.Axes.set_autoscalex_on") | unknown |
| [`autoscaley_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_autoscaley_on.html#matplotlib.axes.Axes.set_autoscaley_on "matplotlib.axes.Axes.set_autoscaley_on") | unknown |
| [`axes_locator`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axes_locator.html#matplotlib.axes.Axes.set_axes_locator "matplotlib.axes.Axes.set_axes_locator") | Callable\[\[Axes, Renderer\], Bbox\] |
| [`axisbelow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axisbelow.html#matplotlib.axes.Axes.set_axisbelow "matplotlib.axes.Axes.set_axisbelow") | bool or 'line' |
| [`box_aspect`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_box_aspect.html#matplotlib.axes.Axes.set_box_aspect "matplotlib.axes.Axes.set_box_aspect") | float or None |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
| [`facecolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor")<br> or [`fc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_facecolor.html#matplotlib.axes.Axes.set_facecolor "matplotlib.axes.Axes.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`forward_navigation_events`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_forward_navigation_events.html#matplotlib.axes.Axes.set_forward_navigation_events "matplotlib.axes.Axes.set_forward_navigation_events") | bool or "auto" |
| [`frame_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_frame_on.html#matplotlib.axes.Axes.set_frame_on "matplotlib.axes.Axes.set_frame_on") | bool |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`navigate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate.html#matplotlib.axes.Axes.set_navigate "matplotlib.axes.Axes.set_navigate") | bool |
| [`navigate_mode`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_navigate_mode.html#matplotlib.axes.Axes.set_navigate_mode "matplotlib.axes.Axes.set_navigate_mode") | unknown |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`position`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_position.html#matplotlib.axes.Axes.set_position "matplotlib.axes.Axes.set_position") | \[left, bottom, width, height\] or [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox") |
| [`prop_cycle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_prop_cycle.html#matplotlib.axes.Axes.set_prop_cycle "matplotlib.axes.Axes.set_prop_cycle") | [`Cycler`](https://matplotlib.org/cycler/generated/cycler.Cycler.html#cycler.Cycler "(in cycler v0.12)") |
| [`rasterization_zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_rasterization_zorder.html#matplotlib.axes.Axes.set_rasterization_zorder "matplotlib.axes.Axes.set_rasterization_zorder") | float or None |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`subplotspec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_subplotspec.html#matplotlib.axes.Axes.set_subplotspec "matplotlib.axes.Axes.set_subplotspec") | unknown |
| [`title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title") | str |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`xbound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xbound.html#matplotlib.axes.Axes.set_xbound "matplotlib.axes.Axes.set_xbound") | (lower: float, upper: float) |
| [`xinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xinverted.html#matplotlib.axes.Axes.set_xinverted "matplotlib.axes.Axes.set_xinverted") | unknown |
| [`xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel") | str |
| [`xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim") | (left: float, right: float) |
| [`xmargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xmargin.html#matplotlib.axes.Axes.set_xmargin "matplotlib.axes.Axes.set_xmargin") | float greater than -0.5 |
| [`xscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale") | unknown |
| [`xticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels") | unknown |
| [`xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks") | unknown |
| [`ybound`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ybound.html#matplotlib.axes.Axes.set_ybound "matplotlib.axes.Axes.set_ybound") | (lower: float, upper: float) |
| [`yinverted`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yinverted.html#matplotlib.axes.Axes.set_yinverted "matplotlib.axes.Axes.set_yinverted") | unknown |
| [`ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel") | str |
| [`ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim") | (bottom: float, top: float) |
| [`ymargin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ymargin.html#matplotlib.axes.Axes.set_ymargin "matplotlib.axes.Axes.set_ymargin") | float greater than -0.5 |
| [`yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale") | unknown |
| [`yticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels") | unknown |
| [`yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks") | unknown |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

See also

[`Figure.add_axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")

[`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")

[`pyplot.axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes "matplotlib.pyplot.axes")

[`Figure.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")

[`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")

Examples

fig \= plt.figure()

fig.add\_subplot(231)
ax1 \= fig.add\_subplot(2, 3, 1)  \# equivalent but more general

fig.add\_subplot(232, frameon\=False)  \# subplot with no frame
fig.add\_subplot(233, projection\='polar')  \# polar subplot
fig.add\_subplot(234, sharex\=ax1)  \# subplot sharing x-axis with ax1
fig.add\_subplot(235, facecolor\="red")  \# red subplot

ax1.remove()  \# delete ax1 from the figure
fig.add\_subplot(ax1)  \# add ax1 back to the figure

align\_labels(_axs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1535-L1562)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.align_labels "Link to this definition")

Align the xlabels and ylabels of subplots with the same subplots row or column (respectively) if label alignment is being done automatically (i.e. the label position is not manually set).

Alignment persists for draw events after this is called.

Parameters:

**axs**list of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Optional list (or [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
) of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to align the labels. Default is to align all Axes on the figure.

See also

[`matplotlib.figure.Figure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels")

[`matplotlib.figure.Figure.align_ylabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "matplotlib.figure.Figure.align_ylabels")

[`matplotlib.figure.Figure.align_titles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_titles.html#matplotlib.figure.Figure.align_titles "matplotlib.figure.Figure.align_titles")

Notes

This assumes that all Axes in `axs` are from the same [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
, so that their [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 positions correspond to figure positions.

align\_titles(_axs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1488-L1533)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.align_titles "Link to this definition")

Align the titles of subplots in the same subplot row if title alignment is being done automatically (i.e. the title position is not manually set).

Alignment persists for draw events after this is called.

Parameters:

**axs**list of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Optional list of (or ndarray) [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to align the titles. Default is to align all Axes on the figure.

See also

[`matplotlib.figure.Figure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels")

[`matplotlib.figure.Figure.align_ylabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "matplotlib.figure.Figure.align_ylabels")

[`matplotlib.figure.Figure.align_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_labels.html#matplotlib.figure.Figure.align_labels "matplotlib.figure.Figure.align_labels")

Notes

This assumes that all Axes in `axs` are from the same [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
, so that their [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 positions correspond to figure positions.

Examples

Example with titles:

fig, axs \= plt.subplots(1, 2)
axs\[0\].set\_aspect('equal')
axs\[0\].set\_title('Title 0')
axs\[1\].set\_title('Title 1')
fig.align\_titles()

align\_xlabels(_axs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1366-L1425)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.align_xlabels "Link to this definition")

Align the xlabels of subplots in the same subplot row if label alignment is being done automatically (i.e. the label position is not manually set).

Alignment persists for draw events after this is called.

If a label is on the bottom, it is aligned with labels on Axes that also have their label on the bottom and that have the same bottom-most subplot row. If the label is on the top, it is aligned with labels on Axes with the same top-most row.

Parameters:

**axs**list of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Optional list of (or [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
) [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to align the xlabels. Default is to align all Axes on the figure.

See also

[`matplotlib.figure.Figure.align_ylabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_ylabels.html#matplotlib.figure.Figure.align_ylabels "matplotlib.figure.Figure.align_ylabels")

[`matplotlib.figure.Figure.align_titles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_titles.html#matplotlib.figure.Figure.align_titles "matplotlib.figure.Figure.align_titles")

[`matplotlib.figure.Figure.align_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_labels.html#matplotlib.figure.Figure.align_labels "matplotlib.figure.Figure.align_labels")

Notes

This assumes that all Axes in `axs` are from the same [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
, so that their [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 positions correspond to figure positions.

Examples

Example with rotated xtick labels:

fig, axs \= plt.subplots(1, 2)
axs\[0\].tick\_params(axis\='x', rotation\=55)
axs\[0\].set\_xlabel('XLabel 0')
axs\[1\].set\_xlabel('XLabel 1')
fig.align\_xlabels()

align\_ylabels(_axs\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1427-L1486)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.align_ylabels "Link to this definition")

Align the ylabels of subplots in the same subplot column if label alignment is being done automatically (i.e. the label position is not manually set).

Alignment persists for draw events after this is called.

If a label is on the left, it is aligned with labels on Axes that also have their label on the left and that have the same left-most subplot column. If the label is on the right, it is aligned with labels on Axes with the same right-most column.

Parameters:

**axs**list of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Optional list (or [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
) of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 to align the ylabels. Default is to align all Axes on the figure.

See also

[`matplotlib.figure.Figure.align_xlabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_xlabels.html#matplotlib.figure.Figure.align_xlabels "matplotlib.figure.Figure.align_xlabels")

[`matplotlib.figure.Figure.align_titles`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_titles.html#matplotlib.figure.Figure.align_titles "matplotlib.figure.Figure.align_titles")

[`matplotlib.figure.Figure.align_labels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.align_labels.html#matplotlib.figure.Figure.align_labels "matplotlib.figure.Figure.align_labels")

Notes

This assumes that all Axes in `axs` are from the same [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
, so that their [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 positions correspond to figure positions.

Examples

Example with large yticks labels:

fig, axs \= plt.subplots(2, 1)
axs\[0\].plot(np.arange(0, 1000, 50))
axs\[0\].set\_ylabel('YLabel 0')
axs\[1\].set\_ylabel('YLabel 1')
fig.align\_ylabels()

autofmt\_xdate(_bottom\=0.2_, _rotation\=30_, _ha\='right'_, _which\='major'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L175-L218)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.autofmt_xdate "Link to this definition")

Date ticklabels often overlap, so it is useful to rotate them and right align them. Also, a common use case is a number of subplots with shared x-axis where the x-axis is date data. The ticklabels are often long, and it helps to rotate them on the bottom subplot and turn them off on other subplots, as well as turn off xlabels.

Parameters:

**bottom**float, default: 0.2

The bottom of the subplots for [`subplots_adjust`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.subplots_adjust "matplotlib.figure.FigureBase.subplots_adjust")
.

**rotation**float, default: 30 degrees

The rotation angle of the xtick labels in degrees.

**ha**{'left', 'center', 'right'}, default: 'right'

The horizontal alignment of the xticklabels.

**which**{'major', 'minor', 'both'}, default: 'major'

Selects which ticklabels to rotate.

clear(_keep\_observers\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L972-L1006)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.clear "Link to this definition")

Clear the figure.

Parameters:

**keep\_observers**bool, default: False

Set _keep\_observers_ to True if, for example, a gui widget is tracking the Axes in the figure.

clf(_keep\_observers\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1009-L1023)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.clf "Link to this definition")

\[_Discouraged_\] Alias for the [`clear()`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.clear "matplotlib.figure.FigureBase.clear")
 method.

Discouraged

The use of `clf()` is discouraged. Use `clear()` instead.

Parameters:

**keep\_observers**bool, default: False

Set _keep\_observers_ to True if, for example, a gui widget is tracking the Axes in the figure.

colorbar(_mappable_, _cax\=None_, _ax\=None_, _use\_gridspec\=True_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1201-L1320)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.colorbar "Link to this definition")

Add a colorbar to a plot.

Parameters:

**mappable**

The [`matplotlib.colorizer.ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
 (i.e., [`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
, etc.) described by this colorbar. This argument is mandatory for the [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
 method but optional for the [`pyplot.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.colorbar.html#matplotlib.pyplot.colorbar "matplotlib.pyplot.colorbar")
 function, which sets the default to the current image.

Note that one can create a [`colorizer.ColorizingArtist`](https://matplotlib.org/stable/api/colorizer_api.html#matplotlib.colorizer.ColorizingArtist "matplotlib.colorizer.ColorizingArtist")
 "on-the-fly" to generate colorbars not attached to a previously drawn artist, e.g.

cr \= colorizer.Colorizer(norm\=norm, cmap\=cmap)
fig.colorbar(colorizer.ColorizingArtist(cr), ax\=ax)

**cax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

Axes into which the colorbar will be drawn. If [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
, then a new Axes is created and the space for it will be stolen from the Axes(s) specified in _ax_.

**ax**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or iterable or [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 of Axes, optional

The one or more parent Axes from which space for a new colorbar Axes will be stolen. This parameter is only used if _cax_ is not set.

Defaults to the Axes that contains the mappable used to create the colorbar.

**use\_gridspec**bool, optional

If _cax_ is `None`, a new _cax_ is created as an instance of Axes. If _ax_ is positioned with a subplotspec and _use\_gridspec_ is `True`, then _cax_ is also positioned with a subplotspec.

Returns:

**colorbar**[`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")

Other Parameters:

**location**None or {'left', 'right', 'top', 'bottom'}

The location, relative to the parent Axes, where the colorbar Axes is created. It also determines the _orientation_ of the colorbar (colorbars on the left and right are vertical, colorbars at the top and bottom are horizontal). If None, the location will come from the _orientation_ if it is set (vertical colorbars on the right, horizontal ones at the bottom), or default to 'right' if _orientation_ is unset.

**orientation**None or {'vertical', 'horizontal'}

The orientation of the colorbar. It is preferable to set the _location_ of the colorbar, as that also determines the _orientation_; passing incompatible values for _location_ and _orientation_ raises an exception.

**fraction**float, default: 0.15

Fraction of original Axes to use for colorbar.

**shrink**float, default: 1.0

Fraction by which to multiply the size of the colorbar.

**aspect**float, default: 20

Ratio of long to short dimensions.

**pad**float, default: 0.05 if vertical, 0.15 if horizontal

Fraction of original Axes between colorbar and new image Axes.

**anchor**(float, float), optional

The anchor point of the colorbar Axes. Defaults to (0.0, 0.5) if vertical; (0.5, 1.0) if horizontal.

**panchor**(float, float), or _False_, optional

The anchor point of the colorbar parent Axes. If _False_, the parent axes' anchor will be unchanged. Defaults to (1.0, 0.5) if vertical; (0.5, 0.0) if horizontal.

**extend**{'neither', 'both', 'min', 'max'}

Make pointed end(s) for out-of-range values (unless 'neither'). These are set for a given colormap using the colormap set\_under and set\_over methods.

**extendfrac**{_None_, 'auto', length, lengths}

If set to _None_, both the minimum and maximum triangular colorbar extensions will have a length of 5% of the interior colorbar length (this is the default setting).

If set to 'auto', makes the triangular colorbar extensions the same lengths as the interior boxes (when _spacing_ is set to 'uniform') or the same lengths as the respective adjacent interior boxes (when _spacing_ is set to 'proportional').

If a scalar, indicates the length of both the minimum and maximum triangular colorbar extensions as a fraction of the interior colorbar length. A two-element sequence of fractions may also be given, indicating the lengths of the minimum and maximum colorbar extensions respectively as a fraction of the interior colorbar length.

**extendrect**bool

If _False_ the minimum and maximum colorbar extensions will be triangular (the default). If _True_ the extensions will be rectangular.

**ticks**None or list of ticks or Locator

If None, ticks are determined automatically from the input.

**format**None or str or Formatter

If None, [`ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 is used. Format strings, e.g., `"%4.2e"` or `"{x:.2e}"`, are supported. An alternative [`Formatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.Formatter "matplotlib.ticker.Formatter")
 may be given instead.

**drawedges**bool

Whether to draw lines at color boundaries.

**label**str

The label on the colorbar's long axis.

**boundaries, values**None or a sequence

If unset, the colormap will be displayed on a 0-1 scale. If sequences, _values_ must have a length 1 less than _boundaries_. For each region delimited by adjacent entries in _boundaries_, the color mapped to the corresponding value in _values_ will be used. The size of each region is determined by the _spacing_ parameter. Normally only useful for indexed colors (i.e. `norm=NoNorm()`) or other unusual circumstances.

**spacing**{'uniform', 'proportional'}

For discrete colorbars ([`BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 or contours), 'uniform' gives each color the same space; 'proportional' makes the space proportional to the data interval.

Notes

If _mappable_ is a [`ContourSet`](https://matplotlib.org/stable/api/contour_api.html#matplotlib.contour.ContourSet "matplotlib.contour.ContourSet")
, its _extend_ kwarg is included automatically.

The _shrink_ kwarg provides a simple way to scale the colorbar with respect to the Axes. Note that if _cax_ is specified, it determines the size of the colorbar, and _shrink_ and _aspect_ are ignored.

For more precise control, you can manually specify the positions of the axes objects in which the mappable and the colorbar are drawn. In this case, do not use any of the Axes properties kwargs.

It is known that some vector graphics viewers (svg and pdf) render white gaps between segments of the colorbar. This is due to bugs in the viewers, not Matplotlib. As a workaround, the colorbar can be rendered with overlapping segments:

cbar \= colorbar()
cbar.solids.set\_edgecolor("face")
draw()

However, this has negative consequences in other circumstances, e.g. with semi-transparent images (alpha < 1) and colorbar extensions; therefore, this workaround is not used by default (see issue #1188).

contains(_mouseevent_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L293-L304)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.contains "Link to this definition")

Test whether the mouse event occurred on the figure.

Returns:

bool, {}

delaxes(_ax_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L930-L934)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.delaxes "Link to this definition")

Remove the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 _ax_ from the figure; update the current Axes.

draw(_renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L1044-L1061)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.draw "Link to this definition")

Draw the Artist (and its children) using the given renderer.

This has no effect if the artist is not visible ([`Artist.get_visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_visible.html#matplotlib.artist.Artist.get_visible "matplotlib.artist.Artist.get_visible")
 returns False).

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass.

Notes

This method is overridden in the Artist subclasses.

property figure[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.figure "Link to this definition")

The root [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
. To get the parent of a [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
, use the [`get_figure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_figure "matplotlib.figure.FigureBase.get_figure")
 method.

property frameon[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.frameon "Link to this definition")

Return the figure's background patch visibility, i.e. whether the figure background will be drawn. Equivalent to `Figure.patch.get_visible()`.

gca()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1716-L1727)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.gca "Link to this definition")

Get the current Axes.

If there is currently no Axes on this Figure, a new one is created using [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
. (To test whether there is currently an Axes on a Figure, check whether `figure.axes` is empty. To test whether there is currently a Figure on the pyplot figure stack, check whether [`pyplot.get_fignums()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_fignums.html#matplotlib.pyplot.get_fignums "matplotlib.pyplot.get_fignums")
 is empty.)

get\_children()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L220-L230)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_children "Link to this definition")

Get a list of artists contained in the figure.

get\_default\_bbox\_extra\_artists()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1797-L1806)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_default_bbox_extra_artists "Link to this definition")

Return a list of Artists typically used in [`Figure.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.get_tightbbox.html#matplotlib.figure.Figure.get_tightbbox "matplotlib.figure.Figure.get_tightbbox")
.

get\_edgecolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L436-L438)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_edgecolor "Link to this definition")

Get the edge color of the Figure rectangle.

get\_facecolor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L440-L442)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_facecolor "Link to this definition")

Get the face color of the Figure rectangle.

get\_figure(_root\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L232-L269)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_figure "Link to this definition")

Return the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 instance the (Sub)Figure belongs to.

Parameters:

**root**bool, default=True

If False, return the (Sub)Figure this artist is on. If True, return the root Figure for a nested tree of SubFigures.

Deprecated since version 3.10: From version 3.12 _root_ will default to False.

get\_frameon()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L444-L450)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_frameon "Link to this definition")

Return the figure's background patch visibility, i.e. whether the figure background will be drawn. Equivalent to `Figure.patch.get_visible()`.

get\_linewidth()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L462-L466)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_linewidth "Link to this definition")

Get the line width of the Figure rectangle.

get\_suptitle()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L400-L403)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_suptitle "Link to this definition")

Return the suptitle as string or an empty string if not set.

get\_supxlabel()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L415-L418)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_supxlabel "Link to this definition")

Return the supxlabel as string or an empty string if not set.

get\_supylabel()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L431-L434)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_supylabel "Link to this definition")

Return the supylabel as string or an empty string if not set.

get\_tightbbox(_renderer\=None_, _\*_, _bbox\_extra\_artists\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1808-L1879)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_tightbbox "Link to this definition")

Return a (tight) bounding box of the figure _in inches_.

Note that [`FigureBase`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase "matplotlib.figure.FigureBase")
 differs from all other artists, which return their [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
 in pixels.

Artists that have `artist.set_in_layout(False)` are not included in the bbox.

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass

Renderer that will be used to draw the figures (i.e. `fig.canvas.get_renderer()`)

**bbox\_extra\_artists**list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 or `None`

List of artists to include in the tight bounding box. If `None` (default), then all artist children of each Axes are included in the tight bounding box.

Returns:

[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")

containing the bounding box (in figure inches).

get\_window\_extent(_renderer\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L306-L308)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.get_window_extent "Link to this definition")

Get the artist's bounding box in display space, ignoring clipping.

The bounding box's width and height are non-negative.

Subclasses should override for inclusion in the bounding box "tight" calculation. Default is to return an empty bounding box at 0, 0.

Warning

The extent can change due to any changes in the transform stack, such as changing the Axes limits, the figure size, the canvas used (as is done when saving a figure), or the DPI.

Relying on a once-retrieved window extent can lead to unexpected behavior in various cases such as interactive figures being resized or moved to a screen with different dpi, or figures that look fine on screen render incorrectly when saved to file.

To get accurate results you may need to manually call [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 or [`draw_without_rendering`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw_without_rendering.html#matplotlib.figure.Figure.draw_without_rendering "matplotlib.figure.Figure.draw_without_rendering")
 to have Matplotlib compute the rendered size.

Parameters:

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
, optional

Renderer used to draw the figure (i.e. `fig.canvas.get_renderer()`).

See also

[`Artist.get_tightbbox`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_tightbbox.html#matplotlib.artist.Artist.get_tightbbox "matplotlib.artist.Artist.get_tightbbox")

Get the artist bounding box, taking clipping into account.

legend(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1031-L1149)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.legend "Link to this definition")

Place a legend on the figure.

Call signatures:

legend()
legend(handles, labels)
legend(handles\=handles)
legend(labels)

The call signatures correspond to the following different ways to use this method:

**1\. Automatic detection of elements to be shown in the legend**

The elements to be added to the legend are automatically determined, when you do not pass in any extra arguments.

In this case, the labels are taken from the artist. You can specify them either at artist creation or by calling the [`set_label()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label")
 method on the artist:

ax.plot(\[1, 2, 3\], label\='Inline label')
fig.legend()

or:

line, \= ax.plot(\[1, 2, 3\])
line.set\_label('Label via method')
fig.legend()

Specific lines can be excluded from the automatic legend element selection by defining a label starting with an underscore. This is default for all artists, so calling [`Figure.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.legend.html#matplotlib.figure.Figure.legend "matplotlib.figure.Figure.legend")
 without any arguments and without setting the labels manually will result in no legend being drawn.

**2\. Explicitly listing the artists and labels in the legend**

For full control of which artists have a legend entry, it is possible to pass an iterable of legend artists followed by an iterable of legend labels respectively:

fig.legend(\[line1, line2, line3\], \['label1', 'label2', 'label3'\])

**3\. Explicitly listing the artists in the legend**

This is similar to 2, but the labels are taken from the artists' label properties. Example:

line1, \= ax1.plot(\[1, 2, 3\], label\='label1')
line2, \= ax2.plot(\[1, 2, 3\], label\='label2')
fig.legend(handles\=\[line1, line2\])

**4\. Labeling existing plot elements**

Discouraged

This call signature is discouraged, because the relation between plot elements and labels is only implicit by their order and can easily be mixed up.

To make a legend for all artists on all Axes, call this function with an iterable of strings, one for each legend item. For example:

fig, (ax1, ax2) \= plt.subplots(1, 2)
ax1.plot(\[1, 3, 5\], color\='blue')
ax2.plot(\[2, 4, 6\], color\='red')
fig.legend(\['the blues', 'the reds'\])

Parameters:

**handles**list of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
, optional

A list of Artists (lines, patches) to be added to the legend. Use this together with _labels_, if you need full control on what is shown in the legend and the automatic mechanism described above is not sufficient.

The length of handles and labels should be the same in this case. If they are not, they are truncated to the smaller length.

**labels**list of str, optional

A list of labels to show next to the artists. Use this together with _handles_, if you need full control on what is shown in the legend and the automatic mechanism described above is not sufficient.

Returns:

[`Legend`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend "matplotlib.legend.Legend")

Other Parameters:

**loc**str or pair of floats, default: 'upper right'

The location of the legend.

The string locations place the legend at the corresponding position within the bounding box, which by default is the full figure area. The bounding box can be changed via _bbox\_to\_anchor_.

The positions are visualized below:

+--------------+--------------+---------------+
| 'upper left' |'upper center'| 'upper right' |
+--------------+--------------+---------------+
|'center left' |   'center'   |'center right' |
+--------------+--------------+---------------+
| 'lower left' |'lower center'| 'lower right' |
+--------------+--------------+---------------+

The location can also be a 2-tuple giving the coordinates of the lower-left corner of the legend in figure coordinates (in which case _bbox\_to\_anchor_ will be ignored).

For back-compatibility, `'center right'` (but no other location) can also be spelled `'right'`, and each "string" location can also be given as a numeric value:

| Location String | Location Code |
| --- | --- |
| 'best' (Axes only) | 0   |
| 'upper right' | 1   |
| 'upper left' | 2   |
| 'lower left' | 3   |
| 'lower right' | 4   |
| 'right' | 5   |
| 'center left' | 6   |
| 'center right' | 7   |
| 'lower center' | 8   |
| 'upper center' | 9   |
| 'center' | 10  |

If a figure is using the constrained layout manager, the string codes of the _loc_ keyword argument can get better layout behaviour using the prefix 'outside'. There is ambiguity at the corners, so 'outside upper right' will make space for the legend above the rest of the axes in the layout, and 'outside right upper' will make space on the right side of the layout. In addition to the values of _loc_ listed above, we have 'outside right upper', 'outside right lower', 'outside left upper', and 'outside left lower'. See [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 for more details.

**bbox\_to\_anchor**[`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")
, 2-tuple, or 4-tuple of floats

Box that is used to position the legend in conjunction with _loc_. This is an advanced option for free placement of the legend. For most use cases, _loc_ alone is sufficient.

Defaults to `axes.bbox` (if called as a method to [`Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
) or `figure.bbox` (if `figure.legend`).

Bbox coordinates are interpreted in the coordinate system given by _bbox\_transform_, with the default transform Axes or Figure coordinates, depending on which `legend` is called.

If a 4-tuple or [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")
 is given, then it specifies the bbox `(x, y, width, height)` that the legend is placed in. To put the legend in the best location in the bottom right quadrant of the Axes (or figure):

loc\='best', bbox\_to\_anchor\=(0.5, 0., 0.5, 0.5)

A 2-tuple `(x, y)` places the corner of the legend specified by _loc_ at x, y. For example, to put the legend's upper right-hand corner in the center of the Axes (or figure) the following keywords can be used:

loc\='upper right', bbox\_to\_anchor\=(0.5, 0.5)

For more details on legend positioning, see the [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
.

**ncols**int, default: 1

The number of columns that the legend has.

For backward compatibility, the spelling _ncol_ is also supported but it is discouraged. If both are given, _ncols_ takes precedence.

**prop**None or [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 or dict

The font properties of the legend. If None (default), the current [`matplotlib.rcParams`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams "matplotlib.rcParams")
 will be used.

**fontsize**int or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}

The font size of the legend. If the value is numeric the size will be the absolute font size in points. String values are relative to the current default font size. This argument is only used if _prop_ is not specified.

**labelcolor**str or list, default: `[rcParams["legend.labelcolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.labelcolor#rcparam-legend-labelcolor) ` (default: `'None'`)

The color of the text in the legend. Either a valid color string (for example, 'red'), or a list of color strings. The labelcolor can also be made to match the color of the line or marker using 'linecolor', 'markerfacecolor' (or 'mfc'), or 'markeredgecolor' (or 'mec').

Labelcolor can be set globally using `[rcParams["legend.labelcolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.labelcolor#rcparam-legend-labelcolor) ` (default: `'None'`). If None, use `[rcParams["text.color"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.color#rcparam-text-color) ` (default: `'black'`).

**numpoints**int, default: `[rcParams["legend.numpoints"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.numpoints#rcparam-legend-numpoints) ` (default: `1`)

The number of marker points in the legend when creating a legend entry for a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 (line).

**scatterpoints**int, default: `[rcParams["legend.scatterpoints"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.scatterpoints#rcparam-legend-scatterpoints) ` (default: `1`)

The number of marker points in the legend when creating a legend entry for a [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 (scatter plot).

**scatteryoffsets**iterable of floats, default: `[0.375, 0.5, 0.3125]`

The vertical offset (relative to the font size) for the markers created for a scatter plot legend entry. 0.0 is at the base the legend text, and 1.0 is at the top. To draw all markers at the same height, set to `[0.5]`.

**markerscale**float, default: `[rcParams["legend.markerscale"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.markerscale#rcparam-legend-markerscale) ` (default: `1.0`)

The relative size of legend markers compared to the originally drawn ones.

**markerfirst**bool, default: True

If _True_, legend marker is placed to the left of the legend label. If _False_, legend marker is placed to the right of the legend label.

**reverse**bool, default: False

If _True_, the legend labels are displayed in reverse order from the input. If _False_, the legend labels are displayed in the same order as the input.

Added in version 3.7.

**frameon**bool, default: `[rcParams["legend.frameon"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.frameon#rcparam-legend-frameon) ` (default: `True`)

Whether the legend should be drawn on a patch (frame).

**fancybox**bool, default: `[rcParams["legend.fancybox"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.fancybox#rcparam-legend-fancybox) ` (default: `True`)

Whether round edges should be enabled around the [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")
 which makes up the legend's background.

**shadow**None, bool or dict, default: `[rcParams["legend.shadow"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.shadow#rcparam-legend-shadow) ` (default: `False`)

Whether to draw a shadow behind the legend. The shadow can be configured using [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
 keywords. Customization via `[rcParams["legend.shadow"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.shadow#rcparam-legend-shadow) ` (default: `False`) is currently not supported.

**framealpha**float, default: `[rcParams["legend.framealpha"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.framealpha#rcparam-legend-framealpha) ` (default: `0.8`)

The alpha transparency of the legend's background. If _shadow_ is activated and _framealpha_ is `None`, the default value is ignored.

**facecolor**"inherit" or color, default: `[rcParams["legend.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.facecolor#rcparam-legend-facecolor) ` (default: `'inherit'`)

The legend's background color. If `"inherit"`, use `[rcParams["axes.facecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.facecolor#rcparam-axes-facecolor) ` (default: `'white'`).

**edgecolor**"inherit" or color, default: `[rcParams["legend.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.edgecolor#rcparam-legend-edgecolor) ` (default: `'0.8'`)

The legend's background patch edge color. If `"inherit"`, use `[rcParams["axes.edgecolor"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.edgecolor#rcparam-axes-edgecolor) ` (default: `'black'`).

**linewidth**float or None, default: `[rcParams["legend.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.linewidth#rcparam-legend-linewidth) ` (default: `None`)

The legend's background patch edge linewidth. If `None`, use `[rcParams["patch.linewidth"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=patch.linewidth#rcparam-patch-linewidth) ` (default: `1.0`).

Added in version 3.11.

**mode**{"expand", None}

If _mode_ is set to `"expand"` the legend will be horizontally expanded to fill the Axes area (or _bbox\_to\_anchor_ if defines the legend's size).

**bbox\_transform**None or [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

The transform for the bounding box (_bbox\_to\_anchor_). For a value of `None` (default) the Axes' `matplotlib.axes.Axes.transAxes` transform will be used.

**title**str or None

The legend's title. Default is no title (`None`).

**title\_fontproperties**None or [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 or dict

The font properties of the legend's title. If None (default), the _title\_fontsize_ argument will be used if present; if _title\_fontsize_ is also None, the current `[rcParams["legend.title_fontsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.title_fontsize#rcparam-legend-title-fontsize) ` (default: `None`) will be used.

**title\_fontsize**int or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}, default: `[rcParams["legend.title_fontsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.title_fontsize#rcparam-legend-title-fontsize) ` (default: `None`)

The font size of the legend's title. Note: This cannot be combined with _title\_fontproperties_. If you want to set the fontsize alongside other font properties, use the _size_ parameter in _title\_fontproperties_.

**alignment**{'center', 'left', 'right'}, default: 'center'

The alignment of the legend title and the box of entries. The entries are aligned as a single block, so that markers always lined up.

**borderpad**float, default: `[rcParams["legend.borderpad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.borderpad#rcparam-legend-borderpad) ` (default: `0.4`)

The fractional whitespace inside the legend border, in font-size units.

**labelspacing**float, default: `[rcParams["legend.labelspacing"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.labelspacing#rcparam-legend-labelspacing) ` (default: `0.5`)

The vertical space between the legend entries, in font-size units.

**handlelength**float, default: `[rcParams["legend.handlelength"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.handlelength#rcparam-legend-handlelength) ` (default: `2.0`)

The length of the legend handles, in font-size units.

**handleheight**float, default: `[rcParams["legend.handleheight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.handleheight#rcparam-legend-handleheight) ` (default: `0.7`)

The height of the legend handles, in font-size units.

**handletextpad**float, default: `[rcParams["legend.handletextpad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.handletextpad#rcparam-legend-handletextpad) ` (default: `0.8`)

The pad between the legend handle and text, in font-size units.

**borderaxespad**float, default: `[rcParams["legend.borderaxespad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.borderaxespad#rcparam-legend-borderaxespad) ` (default: `0.5`)

The pad between the Axes and legend border, in font-size units.

**columnspacing**float, default: `[rcParams["legend.columnspacing"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=legend.columnspacing#rcparam-legend-columnspacing) ` (default: `2.0`)

The spacing between columns, in font-size units.

**handler\_map**dict or None

The custom dictionary mapping instances or types to a legend handler. This _handler\_map_ updates the default handler map found at [`matplotlib.legend.Legend.get_legend_handler_map`](https://matplotlib.org/stable/api/legend_api.html#matplotlib.legend.Legend.get_legend_handler_map "matplotlib.legend.Legend.get_legend_handler_map")
.

**draggable**bool, default: False

Whether the legend can be dragged with the mouse.

See also

[`Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")

Notes

Some artists are not supported by this function. See [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html#legend-guide)
 for details.

sca(_a_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1710-L1714)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.sca "Link to this definition")

Set the current Axes to be _a_ and return _a_.

set(_\*_, _agg\_filter\=<UNSET>_, _alpha\=<UNSET>_, _animated\=<UNSET>_, _clip\_box\=<UNSET>_, _clip\_on\=<UNSET>_, _clip\_path\=<UNSET>_, _edgecolor\=<UNSET>_, _facecolor\=<UNSET>_, _frameon\=<UNSET>_, _gid\=<UNSET>_, _in\_layout\=<UNSET>_, _label\=<UNSET>_, _linewidth\=<UNSET>_, _mouseover\=<UNSET>_, _path\_effects\=<UNSET>_, _picker\=<UNSET>_, _rasterized\=<UNSET>_, _sketch\_params\=<UNSET>_, _snap\=<UNSET>_, _transform\=<UNSET>_, _url\=<UNSET>_, _visible\=<UNSET>_, _zorder\=<UNSET>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/artist.py#L140-L140)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set "Link to this definition")

Set multiple properties at once.

a.set(a\=A, b\=B, c\=C)

is equivalent to

a.set\_a(A)
a.set\_b(B)
a.set\_c(C)

In addition to the full property names, aliases are also supported, e.g. `set(lw=2)` is equivalent to `set(linewidth=2)`, but it is an error to pass both simultaneously.

The order of the individual setter calls matches the order of parameters in `set()`. However, most properties do not depend on each other so that order is rarely relevant.

Supported properties are

> | Property | Description |
> | --- | --- |
> | [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
> | [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
> | [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
> | [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | [`BboxBase`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxBase "matplotlib.transforms.BboxBase")<br> or None |
> | [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | bool |
> | [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | Patch or (Path, Transform) or None |
> | [`edgecolor`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_edgecolor "matplotlib.figure.FigureBase.set_edgecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`facecolor`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_facecolor "matplotlib.figure.FigureBase.set_facecolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
> | [`figure`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_figure "matplotlib.figure.FigureBase.set_figure") | unknown |
> | [`frameon`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_frameon "matplotlib.figure.FigureBase.set_frameon") | bool |
> | [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
> | [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
> | [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
> | [`linewidth`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_linewidth "matplotlib.figure.FigureBase.set_linewidth") | number |
> | [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
> | [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
> | [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
> | [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
> | [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
> | [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
> | [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
> | [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
> | [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
> | [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

set\_edgecolor(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L468-L476)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_edgecolor "Link to this definition")

Set the edge color of the Figure rectangle.

Parameters:

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

set\_facecolor(_color_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L478-L486)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_facecolor "Link to this definition")

Set the face color of the Figure rectangle.

Parameters:

**color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

set\_figure(_fig_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L271-L287)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_figure "Link to this definition")

Deprecated since version 3.10: Currently this method will raise an exception if _fig_ is anything other than the root [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 this (Sub)Figure is on. In future it will always raise an exception.

set\_frameon(_b_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L488-L499)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_frameon "Link to this definition")

Set the figure's background patch visibility, i.e. whether the figure background will be drawn. Equivalent to `Figure.patch.set_visible()`.

Parameters:

**b**bool

set\_linewidth(_linewidth_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L452-L460)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.set_linewidth "Link to this definition")

Set the line width of the Figure rectangle.

Parameters:

**linewidth**number

subfigures(_nrows\=1_, _ncols\=1_, _squeeze\=True_, _wspace\=None_, _hspace\=None_, _width\_ratios\=None_, _height\_ratios\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1611-L1678)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.subfigures "Link to this definition")

Add a set of subfigures to this figure or subfigure.

A subfigure has the same artist methods as a figure, and is logically the same as a figure, but cannot print itself. See [Figure subfigures](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subfigures.html)
.

Changed in version 3.10: subfigures are now added in row-major order.

Parameters:

**nrows, ncols**int, default: 1

Number of rows/columns of the subfigure grid.

**squeeze**bool, default: True

If True, extra dimensions are squeezed out from the returned array of subfigures.

**wspace, hspace**float, default: None

The amount of width/height reserved for space between subfigures, expressed as a fraction of the average subfigure width/height. If not given, the values will be inferred from rcParams if using constrained layout (see [`ConstrainedLayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine "matplotlib.layout_engine.ConstrainedLayoutEngine")
), or zero if not using a layout engine.

**width\_ratios**array-like of length _ncols_, optional

Defines the relative widths of the columns. Each column gets a relative width of `width_ratios[i] / sum(width_ratios)`. If not given, all columns will have the same width.

**height\_ratios**array-like of length _nrows_, optional

Defines the relative heights of the rows. Each row gets a relative height of `height_ratios[i] / sum(height_ratios)`. If not given, all rows will have the same height.

subplot\_mosaic(_mosaic_, _\*_, _sharex\=False_, _sharey\=False_, _width\_ratios\=None_, _height\_ratios\=None_, _empty\_sentinel\='.'_, _subplot\_kw\=None_, _per\_subplot\_kw\=None_, _gridspec\_kw\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1906-L2213)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.subplot_mosaic "Link to this definition")

Build a layout of Axes based on ASCII art or nested lists.

This is a helper function to build complex GridSpec layouts visually.

See [Complex and semantic figure composition (subplot\_mosaic)](https://matplotlib.org/stable/users/explain/axes/mosaic.html#mosaic)
 for an example and full API documentation

Parameters:

**mosaic**list of list of {hashable or nested} or str

A visual layout of how you want your Axes to be arranged labeled as strings. For example

x \= \[\['A panel', 'A panel', 'edge'\],\
     \['C panel', '.',       'edge'\]\]

produces 4 Axes:

*   'A panel' which is 1 row high and spans the first two columns
    
*   'edge' which is 2 rows high and is on the right edge
    
*   'C panel' which in 1 row and 1 column wide in the bottom left
    
*   a blank space 1 row and 1 column wide in the bottom center
    

Any of the entries in the layout can be a list of lists of the same form to create nested layouts.

If input is a str, then it can either be a multi-line string of the form

'''
AAE
C.E
'''

where each character is a column and each line is a row. Or it can be a single-line string where rows are separated by `;`:

'AB;CC'

The string notation allows only single character Axes labels and does not support nesting but is very terse.

The Axes identifiers may be [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")
 or a non-iterable hashable object (e.g. [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")
 s may not be used).

**sharex, sharey**bool, default: False

If True, the x-axis (_sharex_) or y-axis (_sharey_) will be shared among all subplots. In that case, tick label visibility and axis units behave as for [`subplots`](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.subplots "matplotlib.figure.FigureBase.subplots")
. If False, each subplot's x- or y-axis will be independent.

**width\_ratios**array-like of length _ncols_, optional

Defines the relative widths of the columns. Each column gets a relative width of `width_ratios[i] / sum(width_ratios)`. If not given, all columns will have the same width. Equivalent to `gridspec_kw={'width_ratios': [...]}`. In the case of nested layouts, this argument applies only to the outer layout.

**height\_ratios**array-like of length _nrows_, optional

Defines the relative heights of the rows. Each row gets a relative height of `height_ratios[i] / sum(height_ratios)`. If not given, all rows will have the same height. Equivalent to `gridspec_kw={'height_ratios': [...]}`. In the case of nested layouts, this argument applies only to the outer layout.

**subplot\_kw**dict, optional

Dictionary with keywords passed to the [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 call used to create each subplot. These values may be overridden by values in _per\_subplot\_kw_.

**per\_subplot\_kw**dict, optional

A dictionary mapping the Axes identifiers or tuples of identifiers to a dictionary of keyword arguments to be passed to the [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 call used to create each subplot. The values in these dictionaries have precedence over the values in _subplot\_kw_.

If _mosaic_ is a string, and thus all keys are single characters, it is possible to use a single string instead of a tuple as keys; i.e. `"AB"` is equivalent to `("A", "B")`.

Added in version 3.7.

**gridspec\_kw**dict, optional

Dictionary with keywords passed to the [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 constructor used to create the grid the subplots are placed on. In the case of nested layouts, this argument applies only to the outer layout. For more complex layouts, users should use [`Figure.subfigures`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
 to create the nesting.

**empty\_sentinel**object, optional

Entry in the layout to mean "leave this space empty". Defaults to `'.'`. Note, if _layout_ is a string, it is processed via [`inspect.cleandoc`](https://docs.python.org/3/library/inspect.html#inspect.cleandoc "(in Python v3.14)")
 to remove leading white space, which may interfere with using white-space as the empty sentinel.

Returns:

dict\[label, Axes\]

A dictionary mapping the labels to the Axes objects. The order of the Axes is left-to-right and top-to-bottom of their position in the total layout.

subplots(_nrows\=1_, _ncols\=1_, _\*_, _sharex\=False_, _sharey\=False_, _squeeze\=True_, _width\_ratios\=None_, _height\_ratios\=None_, _subplot\_kw\=None_, _gridspec\_kw\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L792-L928)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.subplots "Link to this definition")

Add a set of subplots to this figure.

This utility wrapper makes it convenient to create common layouts of subplots in a single call.

Parameters:

**nrows, ncols**int, default: 1

Number of rows/columns of the subplot grid.

**sharex, sharey**bool or {'none', 'all', 'row', 'col'}, default: False

Controls sharing of x-axis (_sharex_) or y-axis (_sharey_):

*   True or 'all': x- or y-axis will be shared among all subplots.
    
*   False or 'none': each subplot x- or y-axis will be independent.
    
*   'row': each subplot row will share an x- or y-axis.
    
*   'col': each subplot column will share an x- or y-axis.
    

When subplots have a shared x-axis along a column, only the x tick labels of the bottom subplot are created. Similarly, when subplots have a shared y-axis along a row, only the y tick labels of the first column subplot are created. To later turn other subplots' ticklabels on, use [`tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
.

When subplots have a shared axis that has units, calling [`Axis.set_units`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_units.html#matplotlib.axis.Axis.set_units "matplotlib.axis.Axis.set_units")
 will update each axis with the new units.

Note that it is not possible to unshare axes.

**squeeze**bool, default: True

*   If True, extra dimensions are squeezed out from the returned array of Axes:
    
    *   if only one subplot is constructed (nrows=ncols=1), the resulting single Axes object is returned as a scalar.
        
    *   for Nx1 or 1xM subplots, the returned object is a 1D numpy object array of Axes objects.
        
    *   for NxM, subplots with N>1 and M>1 are returned as a 2D array.
        
*   If False, no squeezing at all is done: the returned Axes object is always a 2D array containing Axes instances, even if it ends up being 1x1.
    

**width\_ratios**array-like of length _ncols_, optional

Defines the relative widths of the columns. Each column gets a relative width of `width_ratios[i] / sum(width_ratios)`. If not given, all columns will have the same width. Equivalent to `gridspec_kw={'width_ratios': [...]}`.

**height\_ratios**array-like of length _nrows_, optional

Defines the relative heights of the rows. Each row gets a relative height of `height_ratios[i] / sum(height_ratios)`. If not given, all rows will have the same height. Equivalent to `gridspec_kw={'height_ratios': [...]}`.

**subplot\_kw**dict, optional

Dict with keywords passed to the [`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
 call used to create each subplot.

**gridspec\_kw**dict, optional

Dict with keywords passed to the [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 constructor used to create the grid the subplots are placed on.

Returns:

[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or array of Axes

Either a single [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 object or an array of Axes objects if more than one subplot was created. The dimensions of the resulting array can be controlled with the _squeeze_ keyword, see above.

See also

[`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")

[`Figure.add_subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")

[`pyplot.subplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot "matplotlib.pyplot.subplot")

Examples

\# First create some toy data:
x \= np.linspace(0, 2\*np.pi, 400)
y \= np.sin(x\*\*2)

\# Create a figure
fig \= plt.figure()

\# Create a subplot
ax \= fig.subplots()
ax.plot(x, y)
ax.set\_title('Simple plot')

\# Create two subplots and unpack the output array immediately
ax1, ax2 \= fig.subplots(1, 2, sharey\=True)
ax1.plot(x, y)
ax1.set\_title('Sharing Y axis')
ax2.scatter(x, y)

\# Create four polar Axes and access them through the returned array
axes \= fig.subplots(2, 2, subplot\_kw\=dict(projection\='polar'))
axes\[0, 0\].plot(x, y)
axes\[1, 1\].scatter(x, y)

\# Share an X-axis with each column of subplots
fig.subplots(2, 2, sharex\='col')

\# Share a Y-axis with each row of subplots
fig.subplots(2, 2, sharey\='row')

\# Share both X- and Y-axes with all subplots
fig.subplots(2, 2, sharex\='all', sharey\='all')

\# Note that this is the same as
fig.subplots(2, 2, sharex\=True, sharey\=True)

subplots\_adjust(_left\=None_, _bottom\=None_, _right\=None_, _top\=None_, _wspace\=None_, _hspace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1322-L1364)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.subplots_adjust "Link to this definition")

Adjust the subplot layout parameters.

Unset parameters are left unmodified; initial values are given by `[rcParams["figure.subplot.[name]"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.[name]#rcparam-figure-subplot-left) `.

([`Source code`](https://matplotlib.org/stable/_downloads/01c30d8647018decc739b3ad375ac00c/figure_subplots_adjust.py)
, [`png`](https://matplotlib.org/stable/_downloads/362a080aae6b1dfd85262cfa1d98085f/figure_subplots_adjust.png)
)

[![](https://matplotlib.org/stable/_images/api-figure_subplots_adjust.2x.png)](https://matplotlib.org/stable/_images/api-figure_subplots_adjust.2x.png)

Parameters:

**left**float, optional

The position of the left edge of the subplots, as a fraction of the figure width.

**right**float, optional

The position of the right edge of the subplots, as a fraction of the figure width.

**bottom**float, optional

The position of the bottom edge of the subplots, as a fraction of the figure height.

**top**float, optional

The position of the top edge of the subplots, as a fraction of the figure height.

**wspace**float, optional

The width of the padding between subplots, as a fraction of the average Axes width.

**hspace**float, optional

The height of the padding between subplots, as a fraction of the average Axes height.

suptitle(_t_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L390-L398)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.suptitle "Link to this definition")

Add a centered super title to the figure.

Parameters:

**t**str

The super title text.

**x**float, default: 0.5

The x location of the text in figure coordinates.

**y**float, default: 0.98

The y location of the text in figure coordinates.

**horizontalalignment, ha**{'center', 'left', 'right'}, default: center

The horizontal alignment of the text relative to (_x_, _y_).

**verticalalignment, va**{'top', 'center', 'bottom', 'baseline'}, default: top

The vertical alignment of the text relative to (_x_, _y_).

**fontsize, size**default: `[rcParams["figure.titlesize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titlesize#rcparam-figure-titlesize) ` (default: `'large'`)

The font size of the text. See [`Text.set_size`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_size "matplotlib.text.Text.set_size")
 for possible values.

**fontweight, weight**default: `[rcParams["figure.titleweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titleweight#rcparam-figure-titleweight) ` (default: `'normal'`)

The font weight of the text. See [`Text.set_weight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_weight "matplotlib.text.Text.set_weight")
 for possible values.

Returns:

text

The [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance of the super title.

Other Parameters:

**fontproperties**None or dict, optional

A dict of font properties. If _fontproperties_ is given the default values for font size and weight are taken from the [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 defaults. `[rcParams["figure.titlesize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titlesize#rcparam-figure-titlesize) ` (default: `'large'`) and `[rcParams["figure.titleweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.titleweight#rcparam-figure-titleweight) ` (default: `'normal'`) are ignored in this case.

**\*\*kwargs**

Additional kwargs are [`matplotlib.text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties.

supxlabel(_t_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L405-L413)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.supxlabel "Link to this definition")

Add a centered super xlabel to the figure.

Parameters:

**t**str

The super xlabel text.

**x**float, default: 0.5

The x location of the text in figure coordinates.

**y**float, default: 0.01

The y location of the text in figure coordinates.

**horizontalalignment, ha**{'center', 'left', 'right'}, default: center

The horizontal alignment of the text relative to (_x_, _y_).

**verticalalignment, va**{'top', 'center', 'bottom', 'baseline'}, default: bottom

The vertical alignment of the text relative to (_x_, _y_).

**fontsize, size**default: `[rcParams["figure.labelsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.labelsize#rcparam-figure-labelsize) ` (default: `'large'`)

The font size of the text. See [`Text.set_size`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_size "matplotlib.text.Text.set_size")
 for possible values.

**fontweight, weight**default: `[rcParams["figure.labelweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.labelweight#rcparam-figure-labelweight) ` (default: `'normal'`)

The font weight of the text. See [`Text.set_weight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_weight "matplotlib.text.Text.set_weight")
 for possible values.

Returns:

text

The [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance of the super xlabel.

Other Parameters:

**fontproperties**None or dict, optional

A dict of font properties. If _fontproperties_ is given the default values for font size and weight are taken from the [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 defaults. `[rcParams["figure.labelsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.labelsize#rcparam-figure-labelsize) ` (default: `'large'`) and `[rcParams["figure.labelweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.labelweight#rcparam-figure-labelweight) ` (default: `'normal'`) are ignored in this case.

**\*\*kwargs**

Additional kwargs are [`matplotlib.text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties.

supylabel(_t_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L420-L429)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.supylabel "Link to this definition")

Add a centered super ylabel to the figure.

Parameters:

**t**str

The super ylabel text.

**x**float, default: 0.02

The x location of the text in figure coordinates.

**y**float, default: 0.5

The y location of the text in figure coordinates.

**horizontalalignment, ha**{'center', 'left', 'right'}, default: left

The horizontal alignment of the text relative to (_x_, _y_).

**verticalalignment, va**{'top', 'center', 'bottom', 'baseline'}, default: center

The vertical alignment of the text relative to (_x_, _y_).

**fontsize, size**default: `[rcParams["figure.labelsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.labelsize#rcparam-figure-labelsize) ` (default: `'large'`)

The font size of the text. See [`Text.set_size`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_size "matplotlib.text.Text.set_size")
 for possible values.

**fontweight, weight**default: `[rcParams["figure.labelweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.labelweight#rcparam-figure-labelweight) ` (default: `'normal'`)

The font weight of the text. See [`Text.set_weight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_weight "matplotlib.text.Text.set_weight")
 for possible values.

Returns:

text

The [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 instance of the super ylabel.

Other Parameters:

**fontproperties**None or dict, optional

A dict of font properties. If _fontproperties_ is given the default values for font size and weight are taken from the [`FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
 defaults. `[rcParams["figure.labelsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.labelsize#rcparam-figure-labelsize) ` (default: `'large'`) and `[rcParams["figure.labelweight"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.labelweight#rcparam-figure-labelweight) ` (default: `'normal'`) are ignored in this case.

**\*\*kwargs**

Additional kwargs are [`matplotlib.text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties.

text(_x_, _y_, _s_, _fontdict\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L1151-L1199)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.FigureBase.text "Link to this definition")

Add text to figure.

Parameters:

**x, y**float

The position to place the text. By default, this is in figure coordinates, floats in \[0, 1\]. The coordinate system can be changed using the _transform_ keyword.

**s**str

The text string.

**fontdict**dict, optional

A dictionary to override the default text properties. If not given, the defaults are determined by `[rcParams["font.*"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=font.*#rcparam-font-family) `. Properties passed as _kwargs_ override the corresponding ones given in _fontdict_.

Returns:

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

Other Parameters:

**\*\*kwargs**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties

Other miscellaneous text parameters.

| Property | Description |
| --- | --- |
| [`agg_filter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_agg_filter.html#matplotlib.artist.Artist.set_agg_filter "matplotlib.artist.Artist.set_agg_filter") | a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array and two offsets from the bottom left corner of the image |
| [`alpha`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_alpha.html#matplotlib.artist.Artist.set_alpha "matplotlib.artist.Artist.set_alpha") | float or None |
| [`animated`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_animated.html#matplotlib.artist.Artist.set_animated "matplotlib.artist.Artist.set_animated") | bool |
| [`antialiased`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_antialiased "matplotlib.text.Text.set_antialiased") | bool |
| [`backgroundcolor`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_backgroundcolor "matplotlib.text.Text.set_backgroundcolor") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`bbox`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_bbox "matplotlib.text.Text.set_bbox") | dict with properties for [`FancyBboxPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.FancyBboxPatch.html#matplotlib.patches.FancyBboxPatch "matplotlib.patches.FancyBboxPatch")<br> or None |
| [`clip_box`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_box.html#matplotlib.artist.Artist.set_clip_box "matplotlib.artist.Artist.set_clip_box") | unknown |
| [`clip_on`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_on.html#matplotlib.artist.Artist.set_clip_on "matplotlib.artist.Artist.set_clip_on") | unknown |
| [`clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path") | unknown |
| [`color`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color")<br> or [`c`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_color "matplotlib.text.Text.set_color") | [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def) |
| [`figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_figure.html#matplotlib.artist.Artist.set_figure "matplotlib.artist.Artist.set_figure") | [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> or [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure") |
| [`fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")<br> or [`family`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily")<br> or [`fontname`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfamily "matplotlib.text.Text.set_fontfamily") | {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'} |
| [`fontfeatures`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontfeatures "matplotlib.text.Text.set_fontfeatures") | list of str, or tuple of str, or None |
| [`fontproperties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties")<br> or [`font`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties")<br> or [`font_properties`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontproperties "matplotlib.text.Text.set_fontproperties") | [`font_manager.FontProperties`](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")<br> or [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")<br> or [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "(in Python v3.14)") |
| [`fontsize`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize")<br> or [`size`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontsize "matplotlib.text.Text.set_fontsize") | float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'} |
| [`fontstretch`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch "matplotlib.text.Text.set_fontstretch")<br> or [`stretch`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstretch "matplotlib.text.Text.set_fontstretch") | {a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'} |
| [`fontstyle`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "matplotlib.text.Text.set_fontstyle")<br> or [`style`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontstyle "matplotlib.text.Text.set_fontstyle") | {'normal', 'italic', 'oblique'} |
| [`fontvariant`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant "matplotlib.text.Text.set_fontvariant")<br> or [`variant`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontvariant "matplotlib.text.Text.set_fontvariant") | {'normal', 'small-caps'} |
| [`fontweight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "matplotlib.text.Text.set_fontweight")<br> or [`weight`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_fontweight "matplotlib.text.Text.set_fontweight") | {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'} |
| [`gid`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_gid.html#matplotlib.artist.Artist.set_gid "matplotlib.artist.Artist.set_gid") | str |
| [`horizontalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment")<br> or [`ha`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_horizontalalignment "matplotlib.text.Text.set_horizontalalignment") | {'left', 'center', 'right'} |
| [`in_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_in_layout.html#matplotlib.artist.Artist.set_in_layout "matplotlib.artist.Artist.set_in_layout") | bool |
| [`label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_label.html#matplotlib.artist.Artist.set_label "matplotlib.artist.Artist.set_label") | object |
| [`language`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_language "matplotlib.text.Text.set_language") | str or None |
| [`linespacing`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_linespacing "matplotlib.text.Text.set_linespacing") | 'normal' or float, default: 'normal' |
| [`math_fontfamily`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_math_fontfamily "matplotlib.text.Text.set_math_fontfamily") | str |
| [`mouseover`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_mouseover.html#matplotlib.artist.Artist.set_mouseover "matplotlib.artist.Artist.set_mouseover") | bool |
| [`multialignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment")<br> or [`ma`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_multialignment "matplotlib.text.Text.set_multialignment") | {'left', 'right', 'center'} |
| [`parse_math`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_parse_math "matplotlib.text.Text.set_parse_math") | bool |
| [`path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects") | list of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect") |
| [`picker`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_picker.html#matplotlib.artist.Artist.set_picker "matplotlib.artist.Artist.set_picker") | None or bool or float or callable |
| [`position`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_position "matplotlib.text.Text.set_position") | (float, float) |
| [`rasterized`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_rasterized.html#matplotlib.artist.Artist.set_rasterized "matplotlib.artist.Artist.set_rasterized") | bool |
| [`rotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation "matplotlib.text.Text.set_rotation") | float or {'vertical', 'horizontal'} |
| [`rotation_mode`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_rotation_mode "matplotlib.text.Text.set_rotation_mode") | {None, 'default', 'anchor', 'xtick', 'ytick'} |
| [`sketch_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_sketch_params.html#matplotlib.artist.Artist.set_sketch_params "matplotlib.artist.Artist.set_sketch_params") | (scale: float, length: float, randomness: float) |
| [`snap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_snap.html#matplotlib.artist.Artist.set_snap "matplotlib.artist.Artist.set_snap") | bool or None |
| [`text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text") | object |
| [`transform`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_transform.html#matplotlib.artist.Artist.set_transform "matplotlib.artist.Artist.set_transform") | [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform") |
| [`transform_rotates_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_transform_rotates_text "matplotlib.text.Text.set_transform_rotates_text") | bool |
| [`url`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_url.html#matplotlib.artist.Artist.set_url "matplotlib.artist.Artist.set_url") | str |
| [`usetex`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_usetex "matplotlib.text.Text.set_usetex") | bool, default: `[rcParams["text.usetex"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=text.usetex#rcparam-text-usetex) ` (default: `False`) |
| [`verticalalignment`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment")<br> or [`va`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_verticalalignment "matplotlib.text.Text.set_verticalalignment") | {'baseline', 'bottom', 'center', 'center\_baseline', 'top'} |
| [`visible`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_visible.html#matplotlib.artist.Artist.set_visible "matplotlib.artist.Artist.set_visible") | bool |
| [`wrap`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_wrap "matplotlib.text.Text.set_wrap") | bool |
| [`x`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_x "matplotlib.text.Text.set_x") | float |
| [`y`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_y "matplotlib.text.Text.set_y") | float |
| [`zorder`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_zorder.html#matplotlib.artist.Artist.set_zorder "matplotlib.artist.Artist.set_zorder") | float |

See also

[`Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")

[`pyplot.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")

Helper functions[#](https://matplotlib.org/stable/api/figure_api.html#helper-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------

matplotlib.figure.figaspect(_arg_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/figure.py#L3674-L3751)
[#](https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.figaspect "Link to this definition")

Calculate the width and height for a figure with a specified aspect ratio.

While the height is taken from `[rcParams["figure.figsize"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.figsize#rcparam-figure-figsize) ` (default: `[6.4, 4.8]`), the width is adjusted to match the desired aspect ratio. Additionally, it is ensured that the width is in the range \[4., 16.\] and the height is in the range \[2., 16.\]. If necessary, the default height is adjusted to ensure this.

Parameters:

**arg**float or 2D array

If a float, this defines the aspect ratio (i.e. the ratio height / width). In case of an array the aspect ratio is number of rows / number of columns, so that the array could be fitted in the figure undistorted.

Returns:

**size**(2,) array

The width and height of the figure in inches.

Notes

If you want to create an Axes within the figure, that still preserves the aspect ratio, be sure to create it with equal width and height. See examples below.

Thanks to Fernando Perez for this function.

Examples

Make a figure twice as tall as it is wide:

w, h \= figaspect(2.)
fig \= Figure(figsize\=(w, h))
ax \= fig.add\_axes((0.1, 0.1, 0.8, 0.8))
ax.imshow(A, \*\*kwargs)

Make a figure with the proper aspect for an array:

A \= rand(5, 3)
w, h \= figaspect(A)
fig \= Figure(figsize\=(w, h))
ax \= fig.add\_axes((0.1, 0.1, 0.8, 0.8))
ax.imshow(A, \*\*kwargs)

On this page