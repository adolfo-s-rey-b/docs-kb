[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_title.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.set\_title[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_title.html#mpl-toolkits-mplot3d-axes3d-axes3d-set-title "Link to this heading")

===================================================================================================================================================================================================================

Axes3D.set\_title(_label_, _fontdict\=None_, _loc\='center'_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L3499-L3504)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_title.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_title "Link to this definition")

Set a title for the Axes.

Set one of the three available Axes titles. The available titles are positioned above the Axes in the center, flush with the left edge, and flush with the right edge.

Parameters:

**label**str

Text to use for the title

**fontdict**dict

Discouraged

The use of _fontdict_ is discouraged. Parameters should be passed as individual keyword arguments or using dictionary-unpacking `set_title(..., **fontdict)`.

A dictionary controlling the appearance of the title text, the default _fontdict_ is:

{'fontsize': rcParams\['axes.titlesize'\],
 'fontweight': rcParams\['axes.titleweight'\],
 'color': rcParams\['axes.titlecolor'\],
 'verticalalignment': 'baseline',
 'horizontalalignment': loc}

**loc**{'center', 'left', 'right'}, default: `[rcParams["axes.titlelocation"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titlelocation#rcparam-axes-titlelocation) ` (default: `'center'`)

Which title to set.

**y**float, default: `[rcParams["axes.titley"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titley#rcparam-axes-titley) ` (default: `None`)

Vertical Axes location for the title (1.0 is the top). If None (the default) and `[rcParams["axes.titley"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titley#rcparam-axes-titley) ` (default: `None`) is also None, y is determined automatically to avoid decorators on the Axes.

**pad**float, default: `[rcParams["axes.titlepad"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.titlepad#rcparam-axes-titlepad) ` (default: `6.0`)

The offset of the title from the top of the Axes, in points.

Returns:

[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")

The matplotlib text instance representing the title

Other Parameters:

**\*\*kwargs**[`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 properties

Other keyword arguments are text properties, see [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 for a list of valid text properties.

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.set_title`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_title.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-set-title "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_3d_bars_thumb.png)

[Demo of 3D bar charts](https://matplotlib.org/stable/gallery/mplot3d/3d_bars.html)

Demo of 3D bar charts

![](https://matplotlib.org/stable/_images/sphx_glr_lorenz_attractor_thumb.png)

[Lorenz attractor](https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html)

Lorenz attractor

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_zero_stride_thumb.png)

[3D wireframe plots in one direction](https://matplotlib.org/stable/gallery/mplot3d/wire3d_zero_stride.html)

3D wireframe plots in one direction

On this page