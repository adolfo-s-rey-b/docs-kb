[Skip to main content](https://matplotlib.org/stable/api/layout_engine_api.html#main-content)

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
    

`matplotlib.layout_engine`[#](https://matplotlib.org/stable/api/layout_engine_api.html#module-matplotlib.layout_engine "Link to this heading")

===============================================================================================================================================

Classes to layout elements in a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
.

Figures have a `layout_engine` property that holds a subclass of [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
 defined here (or _None_ for no layout). At draw time `figure.get_layout_engine().execute()` is called, the goal of which is usually to rearrange Axes on the figure to produce a pleasing layout. This is like a `draw` callback but with two differences. First, when printing we disable the layout engine for the final draw. Second, it is useful to know the layout engine while the figure is being created. In particular, colorbars are made differently with different layout engines (for historical reasons).

Matplotlib has two built-in layout engines:

*   [`TightLayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.TightLayoutEngine "matplotlib.layout_engine.TightLayoutEngine")
     was the first layout engine added to Matplotlib. See also [Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide)
    .
    
*   [`ConstrainedLayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine "matplotlib.layout_engine.ConstrainedLayoutEngine")
     is more modern and generally gives better results. See also [Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
    .
    

Third parties can create their own layout engine by subclassing [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
.

class matplotlib.layout\_engine.ConstrainedLayoutEngine(_\*_, _h\_pad\=None_, _w\_pad\=None_, _hspace\=None_, _wspace\=None_, _rect\=(0, 0, 1, 1)_, _compress\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L216-L309)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine "Link to this definition")

Implements the `constrained_layout` geometry management. See [Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#constrainedlayout-guide)
 for details.

Initialize `constrained_layout` settings.

Parameters:

**h\_pad, w\_pad**float

Padding around the Axes elements in inches. Default to `[rcParams["figure.constrained_layout.h_pad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.h_pad#rcparam-figure-constrained-layout-h-pad) ` (default: `0.04167`) and `[rcParams["figure.constrained_layout.w_pad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.w_pad#rcparam-figure-constrained-layout-w-pad) ` (default: `0.04167`).

**hspace, wspace**float

Fraction of the figure to dedicate to space between the axes. These are evenly spread between the gaps between the Axes. A value of 0.2 for a three-column layout would have a space of 0.1 of the figure width between each column. If h/wspace < h/w\_pad, then the pads are used instead. Default to `[rcParams["figure.constrained_layout.hspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.hspace#rcparam-figure-constrained-layout-hspace) ` (default: `0.02`) and `[rcParams["figure.constrained_layout.wspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.wspace#rcparam-figure-constrained-layout-wspace) ` (default: `0.02`).

**rect**tuple of 4 floats

Rectangle in figure coordinates to perform constrained layout in (left, bottom, width, height), each from 0-1.

**compress**bool

Whether to shift Axes so that white space in between them is removed. This is useful for simple grids of fixed-aspect Axes (e.g. a grid of images). See [Grids of fixed aspect-ratio Axes: "compressed" layout](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html#compressed-layout)
.

property adjust\_compatible[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine.adjust_compatible "Link to this definition")

Return a boolean if the layout engine is compatible with [`subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
.

property colorbar\_gridspec[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine.colorbar_gridspec "Link to this definition")

Return a boolean if the layout engine creates colorbars using a gridspec.

execute(_fig_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L265-L282)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine.execute "Link to this definition")

Perform constrained\_layout and move and resize Axes accordingly.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 to perform layout on.

get()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L97-L101)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine.get "Link to this definition")

Return copy of the parameters for the layout engine.

set(_\*_, _h\_pad\=None_, _w\_pad\=None_, _hspace\=None_, _wspace\=None_, _rect\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L284-L309)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.ConstrainedLayoutEngine.set "Link to this definition")

Set the pads for constrained\_layout.

Parameters:

**h\_pad, w\_pad**float

Padding around the Axes elements in inches. Default to `[rcParams["figure.constrained_layout.h_pad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.h_pad#rcparam-figure-constrained-layout-h-pad) ` (default: `0.04167`) and `[rcParams["figure.constrained_layout.w_pad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.w_pad#rcparam-figure-constrained-layout-w-pad) ` (default: `0.04167`).

**hspace, wspace**float

Fraction of the figure to dedicate to space between the axes. These are evenly spread between the gaps between the Axes. A value of 0.2 for a three-column layout would have a space of 0.1 of the figure width between each column. If h/wspace < h/w\_pad, then the pads are used instead. Default to `[rcParams["figure.constrained_layout.hspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.hspace#rcparam-figure-constrained-layout-hspace) ` (default: `0.02`) and `[rcParams["figure.constrained_layout.wspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.constrained_layout.wspace#rcparam-figure-constrained-layout-wspace) ` (default: `0.02`).

**rect**tuple of 4 floats

Rectangle in figure coordinates to perform constrained layout in (left, bottom, width, height), each from 0-1.

class matplotlib.layout\_engine.LayoutEngine(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L32-L108)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "Link to this definition")

Base class for Matplotlib layout engines.

A layout engine can be passed to a figure at instantiation or at any time with [`set_layout_engine`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html#matplotlib.figure.Figure.set_layout_engine "matplotlib.figure.Figure.set_layout_engine")
. Once attached to a figure, the layout engine `execute` function is called at draw time by [`draw`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.draw.html#matplotlib.figure.Figure.draw "matplotlib.figure.Figure.draw")
, providing a special draw-time hook.

Note

However, note that layout engines affect the creation of colorbars, so [`set_layout_engine`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_layout_engine.html#matplotlib.figure.Figure.set_layout_engine "matplotlib.figure.Figure.set_layout_engine")
 should be called before any colorbars are created.

Currently, there are two properties of [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
 classes that are consulted while manipulating the figure:

*   `engine.colorbar_gridspec` tells [`Figure.colorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
     whether to make the
    
    axes using the gridspec method (see [`colorbar.make_axes_gridspec`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes_gridspec "matplotlib.colorbar.make_axes_gridspec")
    ) or not (see [`colorbar.make_axes`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.make_axes "matplotlib.colorbar.make_axes")
    );
    
*   `engine.adjust_compatible` stops [`Figure.subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
     from being
    
    run if it is not compatible with the layout engine.
    

To implement a custom [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
:

1.  override `_adjust_compatible` and `_colorbar_gridspec`
    
2.  override [`LayoutEngine.set`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine.set "matplotlib.layout_engine.LayoutEngine.set")
     to update _self.\_params_
    
3.  override [`LayoutEngine.execute`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine.execute "matplotlib.layout_engine.LayoutEngine.execute")
     with your implementation
    

property adjust\_compatible[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine.adjust_compatible "Link to this definition")

Return a boolean if the layout engine is compatible with [`subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
.

property colorbar\_gridspec[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine.colorbar_gridspec "Link to this definition")

Return a boolean if the layout engine creates colorbars using a gridspec.

execute(_fig_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L103-L108)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine.execute "Link to this definition")

Execute the layout on the figure given by _fig_.

get()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L97-L101)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine.get "Link to this definition")

Return copy of the parameters for the layout engine.

set(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L71-L75)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine.set "Link to this definition")

Set the parameters for the layout engine.

class matplotlib.layout\_engine.PlaceHolderLayoutEngine(_adjust\_compatible_, _colorbar\_gridspec_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L111-L134)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.PlaceHolderLayoutEngine "Link to this definition")

This layout engine does not adjust the figure layout at all.

The purpose of this [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
 is to act as a placeholder when the user removes a layout engine to ensure an incompatible [`LayoutEngine`](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.LayoutEngine "matplotlib.layout_engine.LayoutEngine")
 cannot be set later.

Parameters:

**adjust\_compatible, colorbar\_gridspec**bool

Allow the PlaceHolderLayoutEngine to mirror the behavior of whatever layout engine it is replacing.

property adjust\_compatible[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.PlaceHolderLayoutEngine.adjust_compatible "Link to this definition")

Return a boolean if the layout engine is compatible with [`subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
.

property colorbar\_gridspec[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.PlaceHolderLayoutEngine.colorbar_gridspec "Link to this definition")

Return a boolean if the layout engine creates colorbars using a gridspec.

execute(_fig_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L130-L134)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.PlaceHolderLayoutEngine.execute "Link to this definition")

Do nothing.

get()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L97-L101)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.PlaceHolderLayoutEngine.get "Link to this definition")

Return copy of the parameters for the layout engine.

set(_\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L71-L75)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.PlaceHolderLayoutEngine.set "Link to this definition")

Set the parameters for the layout engine.

class matplotlib.layout\_engine.TightLayoutEngine(_\*_, _pad\=1.08_, _h\_pad\=None_, _w\_pad\=None_, _rect\=(0, 0, 1, 1)_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L137-L213)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.TightLayoutEngine "Link to this definition")

Implements the `tight_layout` geometry management. See [Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html#tight-layout-guide)
 for details.

Initialize tight\_layout engine.

Parameters:

**pad**float, default: 1.08

Padding between the figure edge and the edges of subplots, as a fraction of the font size.

**h\_pad, w\_pad**float

Padding (height/width) between edges of adjacent subplots. Defaults to _pad_.

**rect**tuple (left, bottom, right, top), default: (0, 0, 1, 1).

rectangle in normalized figure coordinates that the subplots (including labels) will fit into.

property adjust\_compatible[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.TightLayoutEngine.adjust_compatible "Link to this definition")

Return a boolean if the layout engine is compatible with [`subplots_adjust`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
.

property colorbar\_gridspec[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.TightLayoutEngine.colorbar_gridspec "Link to this definition")

Return a boolean if the layout engine creates colorbars using a gridspec.

execute(_fig_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L168-L193)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.TightLayoutEngine.execute "Link to this definition")

Execute tight\_layout.

This decides the subplot parameters given the padding that will allow the Axes labels to not be covered by other labels and Axes.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 to perform layout on.

See also

[`figure.Figure.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")

[`pyplot.tight_layout`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html#matplotlib.pyplot.tight_layout "matplotlib.pyplot.tight_layout")

get()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L97-L101)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.TightLayoutEngine.get "Link to this definition")

Return copy of the parameters for the layout engine.

set(_\*_, _pad\=None_, _w\_pad\=None_, _h\_pad\=None_, _rect\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/layout_engine.py#L195-L213)
[#](https://matplotlib.org/stable/api/layout_engine_api.html#matplotlib.layout_engine.TightLayoutEngine.set "Link to this definition")

Set the pads for tight\_layout.

Parameters:

**pad**float

Padding between the figure edge and the edges of subplots, as a fraction of the font size.

**w\_pad, h\_pad**float

Padding (width/height) between edges of adjacent subplots. Defaults to _pad_.

**rect**tuple (left, bottom, right, top)

rectangle in normalized figure coordinates that the subplots (including labels) will fit into.

On this page