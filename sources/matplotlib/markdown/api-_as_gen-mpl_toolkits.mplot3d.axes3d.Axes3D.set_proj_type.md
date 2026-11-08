[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.set\_proj\_type[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type.html#mpl-toolkits-mplot3d-axes3d-axes3d-set-proj-type "Link to this heading")

================================================================================================================================================================================================================================

Axes3D.set\_proj\_type(_proj\_type_, _focal\_length\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L1342-L1368)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_proj_type "Link to this definition")

Set the projection type.

Parameters:

**proj\_type**{'persp', 'ortho'}

The projection type.

**focal\_length**float, default: None

For a projection type of 'persp', the focal length of the virtual camera. Must be > 0. If None, defaults to 1. The focal length can be computed from a desired Field Of View via the equation: focal\_length = 1/tan(FOV/2)

On this page