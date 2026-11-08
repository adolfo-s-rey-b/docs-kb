[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.axes\_divider.AxesDivider[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl-toolkits-axes-grid1-axes-divider-axesdivider "Link to this heading")

================================================================================================================================================================================================================================

class mpl\_toolkits.axes\_grid1.axes\_divider.AxesDivider(_axes_, _xref\=None_, _yref\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L335-L477)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider "Link to this definition")

Bases: [`Divider`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.Divider.html#mpl_toolkits.axes_grid1.axes_divider.Divider "mpl_toolkits.axes_grid1.axes_divider.Divider")

Divider based on the preexisting axes.

Parameters:

**axes**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

**xref**

**yref**

append\_axes(_position_, _size_, _pad\=None_, _\*_, _axes\_class\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L419-L451)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.append_axes "Link to this definition")

Add a new axes on a given side of the main axes.

Parameters:

**position**{"left", "right", "bottom", "top"}

Where the new axes is positioned relative to the main axes.

**size**[`axes_size`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#module-mpl_toolkits.axes_grid1.axes_size "mpl_toolkits.axes_grid1.axes_size")
 or float or str

The axes width or height. float or str arguments are interpreted as `axes_size.from_any(size, AxesX(<main_axes>))` for left or right axes, and likewise with `AxesY` for bottom or top axes.

**pad**[`axes_size`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_size.html#module-mpl_toolkits.axes_grid1.axes_size "mpl_toolkits.axes_grid1.axes_size")
 or float or str

Padding between the axes. float or str arguments are interpreted as for _size_. Defaults to `[rcParams["figure.subplot.wspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.wspace#rcparam-figure-subplot-wspace) ` (default: `0.2`) times the main Axes width (left or right axes) or `[rcParams["figure.subplot.hspace"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=figure.subplot.hspace#rcparam-figure-subplot-hspace) ` (default: `0.2`) times the main Axes height (bottom or top axes).

**axes\_class**subclass type of [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, optional

The type of the new axes. Defaults to the type of the main axes.

**\*\*kwargs**

All extra keywords arguments are passed to the created axes.

get\_anchor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L470-L474)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.get_anchor "Link to this definition")

Return the anchor.

get\_aspect()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L453-L461)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.get_aspect "Link to this definition")

Return aspect.

get\_position()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L463-L468)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.get_position "Link to this definition")

Return the position of the rectangle.

get\_subplotspec()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_divider.py#L476-L477)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#mpl_toolkits.axes_grid1.axes_divider.AxesDivider.get_subplotspec "Link to this definition")

Examples using `mpl_toolkits.axes_grid1.axes_divider.AxesDivider`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_divider.AxesDivider.html#examples-using-mpl-toolkits-axes-grid1-axes-divider-axesdivider "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_colorbar_with_axes_divider_thumb.png)

[Colorbar with AxesDivider](https://matplotlib.org/stable/gallery/axes_grid1/demo_colorbar_with_axes_divider.html)

Colorbar with AxesDivider

![](https://matplotlib.org/stable/_images/sphx_glr_make_room_for_ylabel_using_axesgrid_thumb.png)

[Make room for ylabel using axes\_grid](https://matplotlib.org/stable/gallery/axes_grid1/make_room_for_ylabel_using_axesgrid.html)

Make room for ylabel using axes\_grid

![](https://matplotlib.org/stable/_images/sphx_glr_scatter_hist_locatable_axes_thumb.png)

[Align histogram to scatter plot using locatable Axes](https://matplotlib.org/stable/gallery/axes_grid1/scatter_hist_locatable_axes.html)

Align histogram to scatter plot using locatable Axes

![](https://matplotlib.org/stable/_images/sphx_glr_tight_layout_guide_thumb.png)

[Tight layout guide](https://matplotlib.org/stable/users/explain/axes/tight_layout_guide.html)

Tight layout guide

On this page