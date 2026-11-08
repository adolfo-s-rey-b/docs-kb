[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.text[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text.html#mpl-toolkits-mplot3d-axes3d-axes3d-text "Link to this heading")

===================================================================================================================================================================================================

Axes3D.text(_x_, _y_, _z_, _s_, _zdir\=None_, _\*_, _axlim\_clip\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L2182-L2219)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text.html#mpl_toolkits.mplot3d.axes3d.Axes3D.text "Link to this definition")

Add the text _s_ to the 3D Axes at location _x_, _y_, _z_ in data coordinates.

Parameters:

**x, y, z**float

The position to place the text.

**s**str

The text.

**zdir**{'x', 'y', 'z', 3-tuple}, optional

The direction to be used as the z-direction. Default: 'z'. See [`get_dir_vector`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.get_dir_vector.html#mpl_toolkits.mplot3d.art3d.get_dir_vector "mpl_toolkits.mplot3d.art3d.get_dir_vector")
 for a description of the values.

**axlim\_clip**bool, default: False

Whether to hide text that is outside the axes view limits.

Added in version 3.10.

**\*\*kwargs**

Other arguments are forwarded to [`matplotlib.axes.Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
.

Returns:

[`Text3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Text3D.html#mpl_toolkits.mplot3d.art3d.Text3D "mpl_toolkits.mplot3d.art3d.Text3D")

The created [`Text3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Text3D.html#mpl_toolkits.mplot3d.art3d.Text3D "mpl_toolkits.mplot3d.art3d.Text3D")
 instance.

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.text`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.text.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-text "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_text3d_thumb.png)

[Text annotations in 3D](https://matplotlib.org/stable/gallery/mplot3d/text3d.html)

Text annotations in 3D

On this page