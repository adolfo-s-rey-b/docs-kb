[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.patch_collection_2d_to_3d.html#main-content)

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
    

mpl\_toolkits.mplot3d.art3d.patch\_collection\_2d\_to\_3d[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.patch_collection_2d_to_3d.html#mpl-toolkits-mplot3d-art3d-patch-collection-2d-to-3d "Link to this heading")

==============================================================================================================================================================================================================================================

mpl\_toolkits.mplot3d.art3d.patch\_collection\_2d\_to\_3d(_col_, _zs\=0_, _zdir\='z'_, _depthshade\=None_, _axlim\_clip\=False_, _\*args_, _depthshade\_minalpha\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1178-L1226)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.patch_collection_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.patch_collection_2d_to_3d "Link to this definition")

Convert a [`PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
 into a [`Patch3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Patch3DCollection.html#mpl_toolkits.mplot3d.art3d.Patch3DCollection "mpl_toolkits.mplot3d.art3d.Patch3DCollection")
 object (or a [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 into a [`Path3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection "mpl_toolkits.mplot3d.art3d.Path3DCollection")
 object).

Parameters:

**col**[`PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")
 or [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")

The collection to convert.

**zs**float or array of floats

The location or locations to place the patches in the collection along the _zdir_ axis. Default: 0.

**zdir**{'x', 'y', 'z'}

The axis in which to place the patches. Default: "z". See [`get_dir_vector`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.get_dir_vector.html#mpl_toolkits.mplot3d.art3d.get_dir_vector "mpl_toolkits.mplot3d.art3d.get_dir_vector")
 for a description of the values.

**depthshade**bool, default: `[rcParams["axes3d.depthshade"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.depthshade#rcparam-axes3d-depthshade) ` (default: `True`)

Whether to shade the patches to give a sense of depth.

**axlim\_clip**bool, default: False

Whether to hide patches with a vertex outside the axes view limits.

Added in version 3.10.

**depthshade\_minalpha**float, default: `[rcParams["axes3d.depthshade_minalpha"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes3d.depthshade_minalpha#rcparam-axes3d-depthshade-minalpha) ` (default: `0.3`)

Sets the minimum alpha value used by depth-shading.

Added in version 3.11.

On this page