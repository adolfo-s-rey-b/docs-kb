[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.add\_collection3d[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d.html#mpl-toolkits-mplot3d-axes3d-axes3d-add-collection3d "Link to this heading")

========================================================================================================================================================================================================================================

Axes3D.add\_collection3d(_col_, _zs\=0_, _zdir\='z'_, _autolim\=True_, _\*_, _axlim\_clip\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L3097-L3166)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d "Link to this definition")

Add a 3D collection object to the plot.

2D collection types are converted to a 3D version by modifying the object and adding z coordinate information, _zs_ and _zdir_.

Supported 2D collection types are:

*   [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
    
*   [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
    
*   [`PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
     (currently not supporting _autolim_)
    

Parameters:

**col**[`Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")

A 2D collection object.

**zs**float or array-like, default: 0

The z-positions to be used for the 2D objects.

**zdir**{'x', 'y', 'z'}, default: 'z'

The direction to use for the z-positions.

**autolim**bool, default: True

Whether to update the data limits.

**axlim\_clip**bool, default: False

Whether to hide the scatter points outside the axes view limits.

Added in version 3.10.

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-add-collection3d "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_polys3d_thumb.png)

[Generate 3D polygons](https://matplotlib.org/stable/gallery/mplot3d/polys3d.html)

Generate 3D polygons

On this page