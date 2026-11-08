[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.html#main-content)

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
    

mpl\_toolkits.axisartist.axis\_artist[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.html#module-mpl_toolkits.axisartist.axis_artist "Link to this heading")

===============================================================================================================================================================================================

The [`axis_artist`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.html#module-mpl_toolkits.axisartist.axis_artist "mpl_toolkits.axisartist.axis_artist")
 module implements custom artists to draw axis elements (axis lines and labels, tick lines and labels, grid lines).

Axis lines and labels and tick lines and labels are managed by the [`AxisArtist`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.axis_artist.AxisArtist")
 class; grid lines are managed by the [`GridlinesCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl_toolkits.axisartist.axis_artist.GridlinesCollection "mpl_toolkits.axisartist.axis_artist.GridlinesCollection")
 class.

There is one [`AxisArtist`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.axis_artist.AxisArtist")
 per Axis; it can be accessed through the `axis` dictionary of the parent Axes (which should be a [`Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes "mpl_toolkits.axisartist.axislines.Axes")
), e.g. `ax.axis["bottom"]`.

Children of the AxisArtist are accessed as attributes: `.line` and `.label` for the axis line and label, `.major_ticks`, `.major_ticklabels`, `.minor_ticks`, `.minor_ticklabels` for the tick lines and labels (e.g. `ax.axis["bottom"].line`).

Children properties (colors, fonts, line widths, etc.) can be set using setters, e.g.

\# Make the major ticks of the bottom axis red.
ax.axis\["bottom"\].major\_ticks.set\_color("red")

However, things like the locations of ticks, and their ticklabels need to be changed from the side of the grid\_helper.

axis\_direction[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.html#axis-direction "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

[`AxisArtist`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.axis_artist.AxisArtist")
, [`AxisLabel`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel "mpl_toolkits.axisartist.axis_artist.AxisLabel")
, [`TickLabels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels "mpl_toolkits.axisartist.axis_artist.TickLabels")
 have an _axis\_direction_ attribute, which adjusts the location, angle, etc. The _axis\_direction_ must be one of "left", "right", "bottom", "top", and follows the Matplotlib convention for rectangular axis.

For example, for the _bottom_ axis (the left and right is relative to the direction of the increasing coordinate),

*   ticklabels and axislabel are on the right
    
*   ticklabels and axislabel have text angle of 0
    
*   ticklabels are baseline, center-aligned
    
*   axislabel is top, center-aligned
    

The text angles are actually relative to (90 + angle of the direction to the ticklabel), which gives 0 for bottom axis.

| Property | left | bottom | right | top |
| --- | --- | --- | --- | --- |
| ticklabel location | left | right | right | left |
| axislabel location | left | right | right | left |
| ticklabel angle | 90  | 0   | \-90 | 180 |
| axislabel angle | 180 | 0   | 0   | 180 |
| ticklabel va | center | baseline | center | baseline |
| axislabel va | center | top | center | bottom |
| ticklabel ha | right | center | right | center |
| axislabel ha | right | center | right | center |

Tick orientation is controlled by `[rcParams["xtick.direction"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=xtick.direction#rcparam-xtick-direction) ` (default: `'out'`) and `[rcParams["ytick.direction"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=ytick.direction#rcparam-ytick-direction) ` (default: `'out'`); they can be manually adjusted using

ax.axis\["bottom"\].major\_ticks.set\_tick\_direction("in")  \# or "out", "inout"

The following attributes can be customized (use the `set_xxx` methods):

*   [`Ticks`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.Ticks.html#mpl_toolkits.axisartist.axis_artist.Ticks "mpl_toolkits.axisartist.axis_artist.Ticks")
    : ticksize, tick\_direction
    
*   [`TickLabels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels "mpl_toolkits.axisartist.axis_artist.TickLabels")
    : pad
    
*   [`AxisLabel`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel "mpl_toolkits.axisartist.axis_artist.AxisLabel")
    : pad
    

Classes[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.html#classes "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`AttributeCopier`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AttributeCopier.html#mpl_toolkits.axisartist.axis_artist.AttributeCopier "mpl_toolkits.axisartist.axis_artist.AttributeCopier")<br>() |     |
| [`AxisArtist`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisArtist.html#mpl_toolkits.axisartist.axis_artist.AxisArtist "mpl_toolkits.axisartist.axis_artist.AxisArtist")<br>(axes, helper\[, offset, ...\]) | An artist which draws axis (a line along which the n-th axes coord is constant) line, ticks, tick labels, and axis label. |
| [`AxisLabel`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel "mpl_toolkits.axisartist.axis_artist.AxisLabel")<br>(\*args\[, axis\_direction, axis\]) | Axis label. |
| [`GridlinesCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.GridlinesCollection.html#mpl_toolkits.axisartist.axis_artist.GridlinesCollection "mpl_toolkits.axisartist.axis_artist.GridlinesCollection")<br>(\*args\[, which, axis\]) | Collection of grid lines. |
| [`LabelBase`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.LabelBase.html#mpl_toolkits.axisartist.axis_artist.LabelBase "mpl_toolkits.axisartist.axis_artist.LabelBase")<br>(\*args, \*\*kwargs) | A base class for [`AxisLabel`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.AxisLabel.html#mpl_toolkits.axisartist.axis_artist.AxisLabel "mpl_toolkits.axisartist.axis_artist.AxisLabel")<br> and [`TickLabels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels "mpl_toolkits.axisartist.axis_artist.TickLabels")<br>. |
| [`TickLabels`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.TickLabels.html#mpl_toolkits.axisartist.axis_artist.TickLabels "mpl_toolkits.axisartist.axis_artist.TickLabels")<br>(\*\[, axis\_direction\]) | Tick labels. |
| [`Ticks`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axis_artist.Ticks.html#mpl_toolkits.axisartist.axis_artist.Ticks "mpl_toolkits.axisartist.axis_artist.Ticks")<br>(ticksize\[, tick\_out, axis\]) | Ticks are derived from [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br>, and note that ticks themselves are markers. |

On this page