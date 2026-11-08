[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.get_dir_vector.html#main-content)

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
    

mpl\_toolkits.mplot3d.art3d.get\_dir\_vector[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.get_dir_vector.html#mpl-toolkits-mplot3d-art3d-get-dir-vector "Link to this heading")

===========================================================================================================================================================================================================

mpl\_toolkits.mplot3d.art3d.get\_dir\_vector(_zdir_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L41-L72)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.get_dir_vector.html#mpl_toolkits.mplot3d.art3d.get_dir_vector "Link to this definition")

Return a direction vector.

Parameters:

**zdir**{'x', 'y', 'z', None, 3-tuple}

The direction. Possible values are:

*   'x': equivalent to (1, 0, 0)
    
*   'y': equivalent to (0, 1, 0)
    
*   'z': equivalent to (0, 0, 1)
    
*   _None_: equivalent to (0, 0, 0)
    
*   an iterable (x, y, z) is converted to an array
    

Returns:

**x, y, z**array

The direction vector.

On this page