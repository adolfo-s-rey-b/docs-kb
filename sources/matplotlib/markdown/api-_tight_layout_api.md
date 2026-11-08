[Skip to main content](https://matplotlib.org/stable/api/_tight_layout_api.html#main-content)

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
    

`matplotlib._tight_layout`[#](https://matplotlib.org/stable/api/_tight_layout_api.html#module-matplotlib._tight_layout "Link to this heading")

===============================================================================================================================================

Routines to adjust subplot params so that subplots are nicely fit in the figure. In doing so, only axis labels, tick labels, Axes titles and offsetboxes that are anchored to Axes are currently considered.

Internally, this module assumes that the margins (left margin, etc.) which are differences between `Axes.get_tightbbox` and `Axes.bbox` are independent of Axes position. This may fail if `Axes.adjustable` is `datalim` as well as such cases as when left or right margin are affected by xlabel.

matplotlib.\_tight\_layout.get\_subplotspec\_list(_axes\_list_, _grid\_spec\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_tight_layout.py#L160-L191)
[#](https://matplotlib.org/stable/api/_tight_layout_api.html#matplotlib._tight_layout.get_subplotspec_list "Link to this definition")

Return a list of subplotspec from the given list of Axes.

For an instance of Axes that does not support subplotspec, None is inserted in the list.

If grid\_spec is given, None is inserted for those not from the given grid\_spec.

matplotlib.\_tight\_layout.get\_tight\_layout\_figure(_fig_, _axes\_list_, _subplotspec\_list_, _renderer_, _pad\=1.08_, _h\_pad\=None_, _w\_pad\=None_, _rect\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_tight_layout.py#L194-L301)
[#](https://matplotlib.org/stable/api/_tight_layout_api.html#matplotlib._tight_layout.get_tight_layout_figure "Link to this definition")

Return subplot parameters for tight-layouted-figure with specified padding.

Parameters:

**fig**Figure

**axes\_list**list of Axes

**subplotspec\_list**list of [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")

The subplotspecs of each Axes.

**renderer**renderer

**pad**float

Padding between the figure edge and the edges of subplots, as a fraction of the font size.

**h\_pad, w\_pad**float

Padding (height/width) between edges of adjacent subplots. Defaults to _pad_.

**rect**tuple (left, bottom, right, top), default: None.

rectangle in normalized figure coordinates that the whole subplots area (including labels) will fit into. Defaults to using the entire figure.

Returns:

subplotspec or None

subplotspec kwargs to be passed to [`Figure.subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
 or None if tight\_layout could not be accomplished.

On this page