[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.poly_collection_2d_to_3d.html#main-content)

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
    

mpl\_toolkits.mplot3d.art3d.poly\_collection\_2d\_to\_3d[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.poly_collection_2d_to_3d.html#mpl-toolkits-mplot3d-art3d-poly-collection-2d-to-3d "Link to this heading")

===========================================================================================================================================================================================================================================

mpl\_toolkits.mplot3d.art3d.poly\_collection\_2d\_to\_3d(_col_, _zs\=0_, _zdir\='z'_, _axlim\_clip\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1555-L1575)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.poly_collection_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.poly_collection_2d_to_3d "Link to this definition")

Convert a [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")
 into a [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
 object.

Parameters:

**col**[`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")

The collection to convert.

**zs**float or array of floats

The location or locations to place the polygons in the collection along the _zdir_ axis. Default: 0.

**zdir**{'x', 'y', 'z'}

The axis in which to place the patches. Default: 'z'. See [`get_dir_vector`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.get_dir_vector.html#mpl_toolkits.mplot3d.art3d.get_dir_vector "mpl_toolkits.mplot3d.art3d.get_dir_vector")
 for a description of the values.

On this page