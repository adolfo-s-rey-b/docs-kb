[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.set\_zlim[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl-toolkits-mplot3d-axes3d-axes3d-set-zlim "Link to this heading")

================================================================================================================================================================================================================

Axes3D.set\_zlim(_bottom\=None_, _top\=None_, _\*_, _emit\=True_, _auto\=False_, _view\_margin\=None_, _zmin\=None_, _zmax\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L1046-L1117)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim "Link to this definition")

Set the 3D z-axis view limits.

Parameters:

**bottom**float, optional

The bottom zlim in data coordinates. Passing _None_ leaves the limit unchanged.

The bottom and top zlims may also be passed as the tuple (_bottom_, _top_) as the first positional argument (or as the _bottom_ keyword argument).

**top**float, optional

The top zlim in data coordinates. Passing _None_ leaves the limit unchanged.

**emit**bool, default: True

Whether to notify observers of limit change.

**auto**bool or None, default: False

Whether to turn on autoscaling of the z-axis. _True_ turns on, _False_ turns off, _None_ leaves unchanged.

**view\_margin**float, optional

The additional margin to apply to the limits.

**zmin, zmax**float, optional

They are equivalent to bottom and top respectively, and it is an error to pass both _zmin_ and _bottom_ or _zmax_ and _top_.

Returns:

**bottom, top**(float, float)

The new z-axis limits in data coordinates.

See also

[`get_zlim`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlim.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlim "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zlim")

[`set_zbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound "mpl_toolkits.mplot3d.axes3d.Axes3D.set_zbound")
, [`get_zbound`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.get_zbound.html#mpl_toolkits.mplot3d.axes3d.Axes3D.get_zbound "mpl_toolkits.mplot3d.axes3d.Axes3D.get_zbound")

[`invert_zaxis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.invert_zaxis.html#mpl_toolkits.mplot3d.axes3d.Axes3D.invert_zaxis "mpl_toolkits.mplot3d.axes3d.Axes3D.invert_zaxis")
, [`zaxis_inverted`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_inverted.html#mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_inverted "mpl_toolkits.mplot3d.axes3d.Axes3D.zaxis_inverted")

Notes

The _bottom_ value may be greater than the _top_ value, in which case the z-axis values will decrease from _bottom_ to _top_.

Examples

\>>> set\_zlim(bottom, top)
\>>> set\_zlim((bottom, top))
\>>> bottom, top \= set\_zlim(bottom, top)

One limit may be left unchanged.

\>>> set\_zlim(top\=top\_lim)

Limits may be passed in reverse order to flip the direction of the z-axis. For example, suppose `z` represents depth of the ocean in m. The z-axis limits might be set like the following so 5000 m depth is at the bottom of the plot and the surface, 0 m, is at the top.

\>>> set\_zlim(5000, 0)

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlim.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-set-zlim "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_2dcollections3d_thumb.png)

[Plot 2D data on 3D plot](https://matplotlib.org/stable/gallery/mplot3d/2dcollections3d.html)

Plot 2D data on 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_mixed_subplots_thumb.png)

[2D and 3D Axes in same figure](https://matplotlib.org/stable/gallery/mplot3d/mixed_subplots.html)

2D and 3D Axes in same figure

![](https://matplotlib.org/stable/_images/sphx_glr_offset_thumb.png)

[Automatic text offsetting](https://matplotlib.org/stable/gallery/mplot3d/offset.html)

Automatic text offsetting

![](https://matplotlib.org/stable/_images/sphx_glr_pathpatch3d_thumb.png)

[Draw flat objects in 3D plot](https://matplotlib.org/stable/gallery/mplot3d/pathpatch3d.html)

Draw flat objects in 3D plot

![](https://matplotlib.org/stable/_images/sphx_glr_subplot3d_thumb.png)

[3D plots as subplots](https://matplotlib.org/stable/gallery/mplot3d/subplot3d.html)

3D plots as subplots

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_thumb.png)

[3D surface (colormap)](https://matplotlib.org/stable/gallery/mplot3d/surface3d.html)

3D surface (colormap)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_3_thumb.png)

[3D surface (checkerboard)](https://matplotlib.org/stable/gallery/mplot3d/surface3d_3.html)

3D surface (checkerboard)

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_radial_thumb.png)

[3D surface with polar coordinates](https://matplotlib.org/stable/gallery/mplot3d/surface3d_radial.html)

3D surface with polar coordinates

![](https://matplotlib.org/stable/_images/sphx_glr_text3d_thumb.png)

[Text annotations in 3D](https://matplotlib.org/stable/gallery/mplot3d/text3d.html)

Text annotations in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_trisurf3d_2_thumb.png)

[More triangular 3D surfaces](https://matplotlib.org/stable/gallery/mplot3d/trisurf3d_2.html)

More triangular 3D surfaces

![](https://matplotlib.org/stable/_images/sphx_glr_wire3d_animation_thumb.gif)

[Animate a 3D wireframe plot](https://matplotlib.org/stable/gallery/mplot3d/wire3d_animation.html)

Animate a 3D wireframe plot

On this page