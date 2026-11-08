[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.view\_init[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html#mpl-toolkits-mplot3d-axes3d-axes3d-view-init "Link to this heading")

===================================================================================================================================================================================================================

Axes3D.view\_init(_elev\=None_, _azim\=None_, _roll\=None_, _vertical\_axis\='z'_, _share\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L1265-L1340)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html#mpl_toolkits.mplot3d.axes3d.Axes3D.view_init "Link to this definition")

Set the elevation and azimuth of the Axes in degrees (not radians).

This can be used to rotate the Axes programmatically.

To look normal to the primary planes, the following elevation and azimuth angles can be used. A roll angle of 0, 90, 180, or 270 deg will rotate these views while keeping the axes at right angles.

| view plane | elev | azim |
| --- | --- | --- |
| XY  | 90  | \-90 |
| XZ  | 0   | \-90 |
| YZ  | 0   | 0   |
| \-XY | \-90 | 90  |
| \-XZ | 0   | 90  |
| \-YZ | 0   | 180 |

Parameters:

**elev**float, default: None

The elevation angle in degrees rotates the camera above the plane pierced by the vertical axis, with a positive angle corresponding to a location above that plane. For example, with the default vertical axis of 'z', the elevation defines the angle of the camera location above the x-y plane. If None, then the initial value as specified in the [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
 constructor is used.

**azim**float, default: None

The azimuthal angle in degrees rotates the camera about the vertical axis, with a positive angle corresponding to a right-handed rotation. For example, with the default vertical axis of 'z', a positive azimuth rotates the camera about the origin from its location along the +x axis towards the +y axis. If None, then the initial value as specified in the [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
 constructor is used.

**roll**float, default: None

The roll angle in degrees rotates the camera about the viewing axis. A positive angle spins the camera clockwise, causing the scene to rotate counter-clockwise. If None, then the initial value as specified in the [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
 constructor is used.

**vertical\_axis**{"z", "x", "y"}, default: "z"

The axis to align vertically. _azim_ rotates about this axis.

**share**bool, default: False

If `True`, apply the settings to all Axes with shared views.

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.view_init`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.view_init.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-view-init "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_2dcollections3d_thumb.png)

[Plot 2D data on 3D plot](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html)

Plot 2D data on 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_box3d_thumb.png)

[3D box surface plot](https://matplotlib.org/stable/gallery/mplot3d/box3d.html)

3D box surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_tricontour3d_thumb.png)

[Triangular 3D contour plot](https://matplotlib.org/stable/gallery/mplot3d/tricontour3d.html)

Triangular 3D contour plot

![](https://matplotlib.org/stable/_images/sphx_glr_tricontourf3d_thumb.png)

[Triangular 3D filled contour plot](https://matplotlib.org/stable/gallery/mplot3d/tricontourf3d.html)

Triangular 3D filled contour plot

On this page