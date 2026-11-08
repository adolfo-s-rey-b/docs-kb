[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#main-content)

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
    

mpl\_toolkits.axisartist.grid\_finder.MaxNLocator[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl-toolkits-axisartist-grid-finder-maxnlocator "Link to this heading")

============================================================================================================================================================================================================================

class mpl\_toolkits.axisartist.grid\_finder.MaxNLocator(_nbins\=10_, _steps\=None_, _trim\=True_, _integer\=False_, _symmetric\=False_, _prune\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L270-L283)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl_toolkits.axisartist.grid_finder.MaxNLocator "Link to this definition")

Bases: [`MaxNLocator`](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.MaxNLocator "matplotlib.ticker.MaxNLocator")

Parameters:

**nbins**int or 'auto', default: 10

Maximum number of intervals; one less than max number of ticks. If the string 'auto', the number of bins will be automatically determined based on the length of the axis.

**steps**array-like, optional

Sequence of acceptable tick multiples, starting with 1 and ending with 10. For example, if `steps=[1, 2, 4, 5, 10]`, `20, 40, 60` or `0.4, 0.6, 0.8` would be possible sets of ticks because they are multiples of 2. `30, 60, 90` would not be generated because 3 does not appear in this example list of steps.

**integer**bool, default: False

If True, ticks will take only integer values, provided at least _min\_n\_ticks_ integers are found within the view limits.

**symmetric**bool, default: False

If True, autoscaling will result in a range symmetric about zero.

**prune**{'lower', 'upper', 'both', None}, default: None

Remove the 'lower' tick, the 'upper' tick, or ticks on 'both' sides _if they fall exactly on an axis' edge_ (this typically occurs when `[rcParams["axes.autolimit_mode"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.autolimit_mode#rcparam-axes-autolimit-mode) ` (default: `'data'`) is 'round\_numbers'). Removing such ticks is mostly useful for stacked or ganged plots, where the upper tick of an Axes overlaps with the lower tick of the axes above it.

**min\_n\_ticks**int, default: 2

Relax _nbins_ and _integer_ constraints if necessary to obtain this minimum number of ticks.

\_\_call\_\_(_v1_, _v2_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axisartist/grid_finder.py#L281-L283)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#mpl_toolkits.axisartist.grid_finder.MaxNLocator.__call__ "Link to this definition")

Return the locations of the ticks.

Examples using `mpl_toolkits.axisartist.grid_finder.MaxNLocator`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.grid_finder.MaxNLocator.html#examples-using-mpl-toolkits-axisartist-grid-finder-maxnlocator "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axis_direction_thumb.png)

[axis\_direction demo](https://matplotlib.org/stable/gallery/axisartist/demo_axis_direction.html)

axis\_direction demo

![](https://matplotlib.org/stable/_images/sphx_glr_demo_curvelinear_grid2_thumb.png)

[Demo CurveLinear Grid2](https://matplotlib.org/stable/gallery/axisartist/demo_curvelinear_grid2.html)

Demo CurveLinear Grid2

![](https://matplotlib.org/stable/_images/sphx_glr_demo_floating_axes_thumb.png)

[floating\_axes features](https://matplotlib.org/stable/gallery/axisartist/demo_floating_axes.html)

floating\_axes features

![](https://matplotlib.org/stable/_images/sphx_glr_simple_axis_pad_thumb.png)

[Simple axis pad](https://matplotlib.org/stable/gallery/axisartist/simple_axis_pad.html)

Simple axis pad

On this page