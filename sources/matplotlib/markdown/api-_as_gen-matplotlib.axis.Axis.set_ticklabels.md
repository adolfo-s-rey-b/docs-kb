[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticklabels.html#main-content)

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
    

matplotlib.axis.Axis.set\_ticklabels[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticklabels.html#matplotlib-axis-axis-set-ticklabels "Link to this heading")

=======================================================================================================================================================================================

Axis.set\_ticklabels(_labels_, _\*_, _minor\=False_, _fontdict\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axis.py#L2177-L2307)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticklabels.html#matplotlib.axis.Axis.set_ticklabels "Link to this definition")

\[_Discouraged_\] Set this Axis' tick labels with list of string labels.

Discouraged

The use of this method is discouraged, because of the dependency on tick positions. In most cases, you'll want to use `Axes.set_[x/y/z]ticks(positions, labels)` or `Axis.set_ticks` instead.

If you are using this method, you should always fix the tick positions before, e.g. by using [`Axis.set_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks")
 or by explicitly setting a [`FixedLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
. Otherwise, ticks are free to move and the labels may end up in unexpected positions.

Parameters:

**labels**sequence of str or of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
s

Texts for labeling each tick location in the sequence set by [`Axis.set_ticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_ticks.html#matplotlib.axis.Axis.set_ticks "matplotlib.axis.Axis.set_ticks")
; the number of labels must match the number of locations. The labels are used as is, via a [`FixedFormatter`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter "matplotlib.ticker.FixedFormatter")
 (without further formatting).

**minor**bool

If True, set minor ticks instead of major ticks.

**fontdict**dict, optional

Discouraged

The use of _fontdict_ is discouraged. Parameters should be passed as individual keyword arguments or using dictionary-unpacking `set_ticklabels(..., **fontdict)`.

A dictionary controlling the appearance of the ticklabels. The default _fontdict_ is:

{'fontsize': rcParams\['axes.titlesize'\],
 'fontweight': rcParams\['axes.titleweight'\],
 'verticalalignment': 'baseline',
 'horizontalalignment': loc}

**\*\*kwargs**

Text properties.

Warning

This only sets the properties of the current ticks, which is only sufficient for static plots.

Ticks are not guaranteed to be persistent. Various operations can create, delete and modify the Tick instances. There is an imminent risk that these settings can get lost if you work on the figure further (including also panning/zooming on a displayed figure).

Use [`set_tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
 instead if possible.

Returns:

list of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
s

For each tick, includes `tick.label1` if it is visible, then `tick.label2` if it is visible, in that order.

On this page