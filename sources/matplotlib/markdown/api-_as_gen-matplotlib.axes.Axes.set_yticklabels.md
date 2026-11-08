[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#main-content)

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
    

matplotlib.axes.Axes.set\_yticklabels[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib-axes-axes-set-yticklabels "Link to this heading")

==========================================================================================================================================================================================

Axes.set\_yticklabels(_labels_, _\*_, _minor\=False_, _fontdict\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L74-L75)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "Link to this definition")

\[_Discouraged_\] Set the yaxis' tick labels with list of string labels.

Discouraged

The use of this method is discouraged, because of the dependency on tick positions. In most cases, you'll want to use `Axes.set_[x/y/z]ticks(positions, labels)` or `Axes.set_yticks` instead.

If you are using this method, you should always fix the tick positions before, e.g. by using [`Axes.set_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
 or by explicitly setting a [`FixedLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
. Otherwise, ticks are free to move and the labels may end up in unexpected positions.

Parameters:

**labels**sequence of str or of [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
s

Texts for labeling each tick location in the sequence set by [`Axes.set_yticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
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

Examples using `matplotlib.axes.Axes.set_yticklabels`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#examples-using-matplotlib-axes-axes-set-yticklabels "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_thumb.png)

[Artist customization in box plots](https://matplotlib.org/stable/gallery/statistics/boxplot.html)

Artist customization in box plots

![](https://matplotlib.org/stable/_images/sphx_glr_violinplot_thumb.png)

[Violin plot basics](https://matplotlib.org/stable/gallery/statistics/violinplot.html)

Violin plot basics

![](https://matplotlib.org/stable/_images/sphx_glr_tex_demo_thumb.png)

[Render math equations using TeX](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html)

Render math equations using TeX

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

On this page