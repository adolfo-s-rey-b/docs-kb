[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.juggle_axes.html#main-content)

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
    

mpl\_toolkits.mplot3d.art3d.juggle\_axes[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.juggle_axes.html#mpl-toolkits-mplot3d-art3d-juggle-axes "Link to this heading")

=================================================================================================================================================================================================

mpl\_toolkits.mplot3d.art3d.juggle\_axes(_xs_, _ys_, _zs_, _zdir_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/art3d.py#L1578-L1592)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.juggle_axes.html#mpl_toolkits.mplot3d.art3d.juggle_axes "Link to this definition")

Reorder coordinates so that 2D _xs_, _ys_ can be plotted in the plane orthogonal to _zdir_. _zdir_ is normally 'x', 'y' or 'z'. However, if _zdir_ starts with a '-' it is interpreted as a compensation for [`rotate_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.rotate_axes.html#mpl_toolkits.mplot3d.art3d.rotate_axes "mpl_toolkits.mplot3d.art3d.rotate_axes")
.

On this page