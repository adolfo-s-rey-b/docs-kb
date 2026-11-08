[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.line_2d_to_3d.html#main-content)

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
    

mpl\_toolkits.mplot3d.art3d.line\_2d\_to\_3d[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.line_2d_to_3d.html#mpl-toolkits-mplot3d-art3d-line-2d-to-3d "Link to this heading")

=========================================================================================================================================================================================================

mpl\_toolkits.mplot3d.art3d.line\_2d\_to\_3d(_line_, _zs\=0_, _zdir\='z'_, _axlim\_clip\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L375-L393)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.line_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.line_2d_to_3d "Link to this definition")

Convert a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 to a [`Line3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3D.html#mpl_toolkits.mplot3d.art3d.Line3D "mpl_toolkits.mplot3d.art3d.Line3D")
 object.

Parameters:

**zs**float

The location along the _zdir_ axis in 3D space to position the line.

**zdir**{'x', 'y', 'z'}

Plane to plot line orthogonal to. Default: 'z'. See [`get_dir_vector`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.get_dir_vector.html#mpl_toolkits.mplot3d.art3d.get_dir_vector "mpl_toolkits.mplot3d.art3d.get_dir_vector")
 for a description of the values.

**axlim\_clip**bool, default: False

Whether to hide lines with an endpoint outside the axes view limits.

Added in version 3.10.

On this page