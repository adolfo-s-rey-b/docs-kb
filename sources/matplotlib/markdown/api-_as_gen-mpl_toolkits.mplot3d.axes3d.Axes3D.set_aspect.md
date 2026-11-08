[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.set\_aspect[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect.html#mpl-toolkits-mplot3d-axes3d-axes3d-set-aspect "Link to this heading")

======================================================================================================================================================================================================================

Axes3D.set\_aspect(_aspect_, _adjustable\=None_, _anchor\=<deprecated parameter>_, _share\=<deprecated parameter>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L296-L393)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect "Link to this definition")

Set the aspect ratios.

Parameters:

**aspect**{'auto', 'equal', 'equalxy', 'equalxz', 'equalyz'}

Possible values:

| value | description |
| --- | --- |
| 'auto' | automatic; fill the position rectangle with data. |
| 'equal' | adapt all the axes to have equal aspect ratios. |
| 'equalxy' | adapt the x and y axes to have equal aspect ratios. |
| 'equalxz' | adapt the x and z axes to have equal aspect ratios. |
| 'equalyz' | adapt the y and z axes to have equal aspect ratios. |

**adjustable**{'box', 'datalim'}, default: 'box'

Defines which parameter to adjust to meet the aspect ratio.

*   'box': Change the physical dimensions of the axes bounding box.
    
*   'datalim': Change the x, y, or z data limits.
    

**anchor**None or str or 2-tuple of float, optional

Deprecated since version 3.11: This parameter has no effect.

**share**bool, default: False

Deprecated since version 3.11: This parameter has no effect.

See also

[`mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect.html#mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect "mpl_toolkits.mplot3d.axes3d.Axes3D.set_box_aspect")

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_aspect.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-set-aspect "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_polys3d_thumb.png)

[Generate 3D polygons](https://matplotlib.org/stable/gallery/mplot3d/polys3d.html)

Generate 3D polygons

![](https://matplotlib.org/stable/_images/sphx_glr_surface3d_2_thumb.png)

[3D surface (solid color)](https://matplotlib.org/stable/gallery/mplot3d/surface3d_2.html)

3D surface (solid color)

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_numpy_logo_thumb.png)

[3D voxel plot of the NumPy logo](https://matplotlib.org/stable/gallery/mplot3d/voxels_numpy_logo.html)

3D voxel plot of the NumPy logo

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_rgb_thumb.png)

[3D voxel / volumetric plot with RGB colors](https://matplotlib.org/stable/gallery/mplot3d/voxels_rgb.html)

3D voxel / volumetric plot with RGB colors

On this page