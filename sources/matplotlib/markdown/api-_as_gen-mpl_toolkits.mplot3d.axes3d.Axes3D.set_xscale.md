[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.set\_xscale[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale.html#mpl-toolkits-mplot3d-axes3d-axes3d-set-xscale "Link to this heading")

======================================================================================================================================================================================================================

Axes3D.set\_xscale(_value_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L1183-L1197)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale "Link to this definition")

Set the x-axis scale.

Parameters:

**value**{"linear", "log", "symlog", "logit", ...}

The axis scale type to apply. See [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")
 for the list of available scales.

**\*\*kwargs**

Keyword arguments are forwarded to the scale class. For example, `base=2` can be passed when using a log scale.

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_xscale.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-set-xscale "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_scales3d_thumb.png)

[Scales on 3D (Log, Symlog, etc.)](https://matplotlib.org/stable/gallery/mplot3d/scales3d.html)

Scales on 3D (Log, Symlog, etc.)

On this page