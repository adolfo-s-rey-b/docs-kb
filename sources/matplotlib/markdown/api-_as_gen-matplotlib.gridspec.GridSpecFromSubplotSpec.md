[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#main-content)

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
    

matplotlib.gridspec.GridSpecFromSubplotSpec[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib-gridspec-gridspecfromsubplotspec "Link to this heading")

==============================================================================================================================================================================================================

class matplotlib.gridspec.GridSpecFromSubplotSpec(_nrows_, _ncols_, _subplot\_spec_, _wspace\=None_, _hspace\=None_, _height\_ratios\=None_, _width\_ratios\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L471-L528)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec "Link to this definition")

Bases: [`GridSpecBase`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase "matplotlib.gridspec.GridSpecBase")

GridSpec whose subplot layout parameters are inherited from the location specified by a given SubplotSpec.

Parameters:

**nrows, ncols**int

Number of rows and number of columns of the grid.

**subplot\_spec**SubplotSpec

Spec from which the layout parameters are inherited.

**wspace, hspace**float, optional

See [`GridSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html#matplotlib.gridspec.GridSpec "matplotlib.gridspec.GridSpec")
 for more details. If not specified default values (from the figure or rcParams) are used.

**height\_ratios**array-like of length _nrows_, optional

See [`GridSpecBase`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase "matplotlib.gridspec.GridSpecBase")
 for details.

**width\_ratios**array-like of length _ncols_, optional

See [`GridSpecBase`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecBase.html#matplotlib.gridspec.GridSpecBase "matplotlib.gridspec.GridSpecBase")
 for details.

get\_subplot\_params(_figure\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L508-L522)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec.get_subplot_params "Link to this definition")

Return a dictionary of subplot layout parameters.

get\_topmost\_subplotspec()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/gridspec.py#L524-L528)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#matplotlib.gridspec.GridSpecFromSubplotSpec.get_topmost_subplotspec "Link to this definition")

Return the topmost [`SubplotSpec`](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.SubplotSpec.html#matplotlib.gridspec.SubplotSpec "matplotlib.gridspec.SubplotSpec")
 instance associated with the subplot.

Examples using `matplotlib.gridspec.GridSpecFromSubplotSpec`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpecFromSubplotSpec.html#examples-using-matplotlib-gridspec-gridspecfromsubplotspec "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_gridspec_nested_thumb.png)

[Nested Gridspecs](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_nested.html)

Nested Gridspecs

![](https://matplotlib.org/stable/_images/sphx_glr_demo_constrained_layout_thumb.png)

[Resize Axes with constrained layout](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/demo_constrained_layout.html)

Resize Axes with constrained layout

![](https://matplotlib.org/stable/_images/sphx_glr_arranging_axes_thumb.png)

[Arranging multiple Axes in a Figure](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)

Arranging multiple Axes in a Figure

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

On this page