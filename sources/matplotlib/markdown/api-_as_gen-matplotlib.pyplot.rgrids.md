[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rgrids.html#main-content)

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
    

matplotlib.pyplot.rgrids[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rgrids.html#matplotlib-pyplot-rgrids "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.rgrids(_radii\=None_, _labels\=None_, _angle\=None_, _fmt\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2485-L2561)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rgrids.html#matplotlib.pyplot.rgrids "Link to this definition")

Get or set the radial gridlines on the current polar plot.

Call signatures:

lines, labels \= rgrids()
lines, labels \= rgrids(radii, labels\=None, angle\=22.5, fmt\=None, \*\*kwargs)

When called with no arguments, [`rgrids`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rgrids.html#matplotlib.pyplot.rgrids "matplotlib.pyplot.rgrids")
 simply returns the tuple (_lines_, _labels_). When called with arguments, the labels will appear at the specified radial distances and angle.

Parameters:

**radii**tuple with floats

The radii for the radial gridlines

**labels**tuple with strings or None

The labels to use at each radial gridline. The [`matplotlib.ticker.ScalarFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.ScalarFormatter "matplotlib.ticker.ScalarFormatter")
 will be used if None.

**angle**float

The angular position of the radius labels in degrees.

**fmt**str or None

Format string used in [`matplotlib.ticker.FormatStrFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FormatStrFormatter "matplotlib.ticker.FormatStrFormatter")
. For example '%f'.

Returns:

**lines**list of [`lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

The radial gridlines.

**labels**list of [`text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The tick labels.

Other Parameters:

**\*\*kwargs**

_kwargs_ are optional [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties for the labels.

See also

[`pyplot.thetagrids`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.thetagrids.html#matplotlib.pyplot.thetagrids "matplotlib.pyplot.thetagrids")

[`projections.polar.PolarAxes.set_rgrids`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.set_rgrids "matplotlib.projections.polar.PolarAxes.set_rgrids")

[`Axis.get_gridlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_gridlines.html#matplotlib.axis.Axis.get_gridlines "matplotlib.axis.Axis.get_gridlines")

[`Axis.get_ticklabels`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.get_ticklabels.html#matplotlib.axis.Axis.get_ticklabels "matplotlib.axis.Axis.get_ticklabels")

Examples

\# set the locations of the radial gridlines
lines, labels \= rgrids( (0.25, 0.5, 1.0) )

\# set the locations and labels of the radial gridlines
lines, labels \= rgrids( (0.25, 0.5, 1.0), ('Tom', 'Dick', 'Harry' ))

On this page