[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#main-content)

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
    

matplotlib.gridspec.SubplotParams[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib-gridspec-subplotparams "Link to this heading")

================================================================================================================================================================================

class matplotlib.gridspec.SubplotParams(_left\=None_, _bottom\=None_, _right\=None_, _top\=None_, _wspace\=None_, _hspace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L741-L807)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Parameters defining the positioning of a subplots grid in a figure.

Defaults are given by `[rcParams["figure.subplot.[name]"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.[name]#rcparam-figure-subplot-left) `.

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

reset()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L800-L803)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams.reset "Link to this definition")

Restore the subplot positioning parameters to the default rcParams values

to\_dict()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L805-L807)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams.to_dict "Link to this definition")

Return a copy of the subplot parameters as a dict.

update(_left\=None_, _bottom\=None_, _right\=None_, _top\=None_, _wspace\=None_, _hspace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L776-L798)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#matplotlib.gridspec.SubplotParams.update "Link to this definition")

Update the dimensions of the passed parameters. _None_ means unchanged.

Examples using `matplotlib.gridspec.SubplotParams`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotParams.html#examples-using-matplotlib-gridspec-subplotparams "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_auto_subplots_adjust_thumb.png)

[Programmatically control subplot adjustment](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/auto_subplots_adjust.html)

Programmatically control subplot adjustment

On this page