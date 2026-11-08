[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.thetagrids.html#main-content)

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
    

matplotlib.pyplot.thetagrids[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.thetagrids.html#matplotlib-pyplot-thetagrids "Link to this heading")

=================================================================================================================================================================

matplotlib.pyplot.thetagrids(_angles\=None_, _labels\=None_, _fmt\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2564-L2637)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.thetagrids.html#matplotlib.pyplot.thetagrids "Link to this definition")

Get or set the theta gridlines on the current polar plot.

Call signatures:

lines, labels \= thetagrids()
lines, labels \= thetagrids(angles, labels\=None, fmt\=None, \*\*kwargs)

When called with no arguments, [`thetagrids`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.thetagrids.html#matplotlib.pyplot.thetagrids "matplotlib.pyplot.thetagrids")
 simply returns the tuple (_lines_, _labels_). When called with arguments, the labels will appear at the specified angles.

Parameters:

**angles**tuple with floats, degrees

The angles of the theta gridlines.

**labels**tuple with strings or None

The labels to use at each radial gridline. The [`projections.polar.ThetaFormatter`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.ThetaFormatter "matplotlib.projections.polar.ThetaFormatter")
 will be used if None.

**fmt**str or None

Format string used in [`matplotlib.ticker.FormatStrFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "matplotlib.ticker.FormatStrFormatter")
. For example '%f'. Note that the angle in radians will be used.

Returns:

**lines**list of [`lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The theta gridlines.

**labels**list of [`text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The tick labels.

Other Parameters:

**\*\*kwargs**

_kwargs_ are optional [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties for the labels.

See also

[`pyplot.rgrids`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rgrids.html#matplotlib.pyplot.rgrids "matplotlib.pyplot.rgrids")

[`projections.polar.PolarAxes.set_thetagrids`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_thetagrids "matplotlib.projections.polar.PolarAxes.set_thetagrids")

[`Axis.get_gridlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_gridlines.html#matplotlib.axis.Axis.get_gridlines "matplotlib.axis.Axis.get_gridlines")

[`Axis.get_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklabels.html#matplotlib.axis.Axis.get_ticklabels "matplotlib.axis.Axis.get_ticklabels")

Examples

\# set the locations of the angular gridlines
lines, labels \= thetagrids(range(45, 360, 90))

\# set the locations and labels of the angular gridlines
lines, labels \= thetagrids(range(45, 360, 90), ('NE', 'NW', 'SW', 'SE'))

On this page