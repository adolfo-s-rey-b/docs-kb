[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.quiver.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.quiver[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.quiver.html#mpl-toolkits-mplot3d-axes3d-axes3d-quiver "Link to this heading")

=========================================================================================================================================================================================================

Axes3D.quiver(_X_, _Y_, _Z_, _U_, _V_, _W_, _\*_, _length\=1_, _arrow\_length\_ratio\=0.3_, _pivot\='tail'_, _normalize\=False_, _axlim\_clip\=False_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L3506-L3632)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.quiver.html#mpl_toolkits.mplot3d.axes3d.Axes3D.quiver "Link to this definition")

Plot a 3D field of arrows.

The arguments can be array-like or scalars, so long as they can be broadcast together. The arguments can also be masked arrays. If an element in any of argument is masked, then that corresponding quiver element will not be plotted.

Parameters:

**X, Y, Z**array-like

The x, y and z coordinates of the arrow locations (default is tail of arrow; see _pivot_ kwarg).

**U, V, W**array-like

The x, y and z components of the arrow vectors.

**length**float, default: 1

The length of each quiver.

**arrow\_length\_ratio**float, default: 0.3

The ratio of the arrow head with respect to the quiver.

**pivot**{'tail', 'middle', 'tip'}, default: 'tail'

The part of the arrow that is at the grid point; the arrow rotates about this point, hence the name _pivot_.

**normalize**bool, default: False

Whether all arrows are normalized to have the same length, or keep the lengths defined by _u_, _v_, and _w_.

**axlim\_clip**bool, default: False

Whether to hide arrows with points outside the axes view limits.

Added in version 3.10.

**data**indexable object, optional

If given, all parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`.

**\*\*kwargs**

Any additional keyword arguments are delegated to [`Line3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.quiver`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.quiver.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-quiver "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_quiver3d_thumb.png)

[3D quiver plot](https://matplotlib.org/stable/gallery/mplot3d/quiver3d.html)

3D quiver plot

![](https://matplotlib.org/stable/_images/sphx_glr_quiver3d_simple_thumb.png)

[quiver(X, Y, Z, U, V, W)](https://matplotlib.org/stable/plot_types/3D/quiver3d_simple.html)

quiver(X, Y, Z, U, V, W)

On this page