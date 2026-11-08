[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlim.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.get\_zlim[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlim.html#mpl-toolkits-mplot3d-axes3d-axes3d-get-zlim "Link to this heading")

================================================================================================================================================================================================================

Axes3D.get\_zlim()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L1131-L1151)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlim "Link to this definition")

Return the 3D z-axis view limits.

Returns:

**left, right**(float, float)

The current z-axis limits in data coordinates.

See also

[`set_zlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim")

[`set_zbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound")
, [`get_zbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zbound "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zbound")

[`invert_zaxis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.invert_zaxis.html#mpl_toolkits.mplot3d.axes3d.Axes3D.invert_zaxis "mpl_toolkits.mplot3d.axes3d.Axes3D.invert_zaxis")
, [`zaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_inverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_inverted "mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_inverted")

Notes

The z-axis may be inverted, in which case the _left_ value will be greater than the _right_ value.

On this page