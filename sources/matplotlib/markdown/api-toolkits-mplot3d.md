[Skip to main content](https://matplotlib.org/stable/api/toolkits/mplot3d.html#main-content)

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
    

`mpl_toolkits.mplot3d`[#](https://matplotlib.org/stable/api/toolkits/mplot3d.html#mpl-toolkits-mplot3d "Link to this heading")

===============================================================================================================================

The mplot3d toolkit adds simple 3D plotting capabilities (scatter, surface, line, mesh, etc.) to Matplotlib by supplying an Axes object that can create a 2D projection of a 3D scene. The resulting graph will have the same look and feel as regular 2D plots. Not the fastest or most feature complete 3D library out there, but it ships with Matplotlib and thus may be a lighter weight solution for some use cases.

See the [mplot3d tutorial](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html#mplot3d)
 for more information.

![../../_images/demo_mplot3d.png](https://matplotlib.org/stable/_images/demo_mplot3d.png)

The interactive backends also provide the ability to rotate and zoom the 3D scene. One can rotate the 3D scene by simply clicking-and-dragging the scene. Panning is done by clicking the middle mouse button, and zooming is done by right-clicking the scene and dragging the mouse up and down. Unlike 2D plots, the toolbar pan and zoom buttons are not used.

*   [mplot3d FAQ](https://matplotlib.org/stable/api/toolkits/mplot3d/faq.html)
    *   [How is mplot3d different from Mayavi?](https://matplotlib.org/stable/api/toolkits/mplot3d/faq.html#how-is-mplot3d-different-from-mayavi)
        
    *   [My 3D plot doesn't look right at certain viewing angles](https://matplotlib.org/stable/api/toolkits/mplot3d/faq.html#my-3d-plot-doesn-t-look-right-at-certain-viewing-angles)
        
    *   [I don't like how the 3D plot is laid out, how do I change that?](https://matplotlib.org/stable/api/toolkits/mplot3d/faq.html#i-don-t-like-how-the-3d-plot-is-laid-out-how-do-i-change-that)
        
*   [mplot3d View Angles](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html)
    *   [How to define the view angle](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#how-to-define-the-view-angle)
        
    *   [Primary view planes](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#primary-view-planes)
        
    *   [Rotation with mouse](https://matplotlib.org/stable/api/toolkits/mplot3d/view_angles.html#rotation-with-mouse)
        
*   [mpl\_toolkits.mplot3d.axes3d.Axes3D](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html)
    *   [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D)
        
    *   [Plotting](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#plotting)
        
    *   [Text and annotations](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#text-and-annotations)
        
    *   [Clearing](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#clearing)
        
    *   [Appearance](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#appearance)
        
    *   [Axis](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#axis)
        
    *   [Units](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#units)
        
    *   [Adding artists](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#adding-artists)
        
    *   [Sharing](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#sharing)
        
    *   [Interactive](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#interactive)
        
    *   [Projection and perspective](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#projection-and-perspective)
        
    *   [Drawing](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#drawing)
        
    *   [Aliases and deprecated methods](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#aliases-and-deprecated-methods)
        
    *   [Other](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#other)
        
    *   [Sample 3D data](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#sample-3d-data)
        

Note

[`pyplot`](https://matplotlib.org/stable/api/pyplot_summary.html#module-matplotlib.pyplot "matplotlib.pyplot")
 cannot be used to add content to 3D plots, because its function signatures are strictly 2D and cannot handle the additional information needed for 3D. Instead, use the explicit API by calling the respective methods on the [`Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
 object.

[`axes3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html#module-mpl_toolkits.mplot3d.axes3d "mpl_toolkits.mplot3d.axes3d")
[#](https://matplotlib.org/stable/api/toolkits/mplot3d.html#axes3d "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

3D plotting in Matplotlib is still not as mature as the 2D case. Please report any functions that do not behave as expected as a bug. In addition, help and patches would be greatly appreciated!

[`axes3d.Axes3D`](https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html#mpl_toolkits.mplot3d.axes3d.Axes3D "mpl_toolkits.mplot3d.axes3d.Axes3D")
 (fig\[, rect, elev, azim, roll, ...\]) 3D Axes object.

[`axis3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html#module-mpl_toolkits.mplot3d.axis3d "mpl_toolkits.mplot3d.axis3d")
[#](https://matplotlib.org/stable/api/toolkits/mplot3d.html#axis3d "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

See `mpl_toolkits.mplot3d.axis3d._axinfo` for a dictionary containing constants that may be modified for controlling the look and feel of mplot3d axes (e.g., label spacing, font colors and panel colors). Historically, axis3d has suffered from having hard-coded constants that precluded user adjustments, and this dictionary was implemented in version 1.1 as a stop-gap measure.

|     |     |
| --- | --- |
| [`axis3d.Axis`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axis3d.Axis.html#mpl_toolkits.mplot3d.axis3d.Axis "mpl_toolkits.mplot3d.axis3d.Axis")<br>(axes, \*\[, rotate\_label\]) | An Axis class for the 3D plots. |

[`art3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html#module-mpl_toolkits.mplot3d.art3d "mpl_toolkits.mplot3d.art3d")
[#](https://matplotlib.org/stable/api/toolkits/mplot3d.html#art3d "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`art3d.Line3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3D.html#mpl_toolkits.mplot3d.art3d.Line3D "mpl_toolkits.mplot3d.art3d.Line3D")<br>(xs, ys, zs, \*args\[, axlim\_clip\]) | 3D line object. |
| [`art3d.Line3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")<br>(lines\[, axlim\_clip\]) | A collection of 3D lines. |
| [`art3d.Patch3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Patch3D.html#mpl_toolkits.mplot3d.art3d.Patch3D "mpl_toolkits.mplot3d.art3d.Patch3D")<br>(\*args\[, zs, zdir, axlim\_clip\]) | 3D patch object. |
| [`art3d.Patch3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Patch3DCollection.html#mpl_toolkits.mplot3d.art3d.Patch3DCollection "mpl_toolkits.mplot3d.art3d.Patch3DCollection")<br>(\*args\[, zs, zdir, ...\]) | A collection of 3D patches. |
| [`art3d.Path3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection "mpl_toolkits.mplot3d.art3d.Path3DCollection")<br>(\*args\[, zs, zdir, ...\]) | A collection of 3D paths. |
| [`art3d.PathPatch3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.PathPatch3D.html#mpl_toolkits.mplot3d.art3d.PathPatch3D "mpl_toolkits.mplot3d.art3d.PathPatch3D")<br>(path, \*\[, zs, zdir, ...\]) | 3D PathPatch object. |
| [`art3d.Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")<br>(verts, \*args\[, ...\]) | A collection of 3D polygons. |
| [`art3d.Text3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Text3D.html#mpl_toolkits.mplot3d.art3d.Text3D "mpl_toolkits.mplot3d.art3d.Text3D")<br>(\[x, y, z, text, zdir, axlim\_clip\]) | Text object with 3D position and direction. |
| [`art3d.get_dir_vector`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.get_dir_vector.html#mpl_toolkits.mplot3d.art3d.get_dir_vector "mpl_toolkits.mplot3d.art3d.get_dir_vector")<br>(zdir) | Return a direction vector. |
| [`art3d.juggle_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.juggle_axes.html#mpl_toolkits.mplot3d.art3d.juggle_axes "mpl_toolkits.mplot3d.art3d.juggle_axes")<br>(xs, ys, zs, zdir) | Reorder coordinates so that 2D _xs_, _ys_ can be plotted in the plane orthogonal to _zdir_. |
| [`art3d.line_2d_to_3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.line_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.line_2d_to_3d "mpl_toolkits.mplot3d.art3d.line_2d_to_3d")<br>(line\[, zs, zdir, axlim\_clip\]) | Convert a [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")<br> to a [`Line3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3D.html#mpl_toolkits.mplot3d.art3d.Line3D "mpl_toolkits.mplot3d.art3d.Line3D")<br> object. |
| [`art3d.line_collection_2d_to_3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.line_collection_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.line_collection_2d_to_3d "mpl_toolkits.mplot3d.art3d.line_collection_2d_to_3d")<br>(col\[, zs, ...\]) | Convert a [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")<br> to a [`Line3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Line3DCollection.html#mpl_toolkits.mplot3d.art3d.Line3DCollection "mpl_toolkits.mplot3d.art3d.Line3DCollection")<br> object. |
| [`art3d.patch_2d_to_3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.patch_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.patch_2d_to_3d "mpl_toolkits.mplot3d.art3d.patch_2d_to_3d")<br>(patch\[, z, zdir, ...\]) | Convert a [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")<br> to a [`Patch3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Patch3D.html#mpl_toolkits.mplot3d.art3d.Patch3D "mpl_toolkits.mplot3d.art3d.Patch3D")<br> object. |
| [`art3d.patch_collection_2d_to_3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.patch_collection_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.patch_collection_2d_to_3d "mpl_toolkits.mplot3d.art3d.patch_collection_2d_to_3d")<br>(col\[, zs, ...\]) | Convert a [`PatchCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PatchCollection "matplotlib.collections.PatchCollection")<br> into a [`Patch3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Patch3DCollection.html#mpl_toolkits.mplot3d.art3d.Patch3DCollection "mpl_toolkits.mplot3d.art3d.Patch3DCollection")<br> object (or a [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")<br> into a [`Path3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Path3DCollection.html#mpl_toolkits.mplot3d.art3d.Path3DCollection "mpl_toolkits.mplot3d.art3d.Path3DCollection")<br> object). |
| [`art3d.pathpatch_2d_to_3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d "mpl_toolkits.mplot3d.art3d.pathpatch_2d_to_3d")<br>(pathpatch\[, z, zdir\]) | Convert a [`PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")<br> to a [`PathPatch3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.PathPatch3D.html#mpl_toolkits.mplot3d.art3d.PathPatch3D "mpl_toolkits.mplot3d.art3d.PathPatch3D")<br> object. |
| [`art3d.poly_collection_2d_to_3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.poly_collection_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.poly_collection_2d_to_3d "mpl_toolkits.mplot3d.art3d.poly_collection_2d_to_3d")<br>(col\[, zs, ...\]) | Convert a [`PolyCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PolyCollection "matplotlib.collections.PolyCollection")<br> into a [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")<br> object. |
| [`art3d.rotate_axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.rotate_axes.html#mpl_toolkits.mplot3d.art3d.rotate_axes "mpl_toolkits.mplot3d.art3d.rotate_axes")<br>(xs, ys, zs, zdir) | Reorder coordinates so that the axes are rotated with _zdir_ along the original z axis. |
| [`art3d.text_2d_to_3d`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.text_2d_to_3d.html#mpl_toolkits.mplot3d.art3d.text_2d_to_3d "mpl_toolkits.mplot3d.art3d.text_2d_to_3d")<br>(obj\[, z, zdir, axlim\_clip\]) | Convert a [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")<br> to a [`Text3D`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Text3D.html#mpl_toolkits.mplot3d.art3d.Text3D "mpl_toolkits.mplot3d.art3d.Text3D")<br> object. |

[`proj3d`](https://matplotlib.org/stable/api/toolkits/mplot3d.html#module-mpl_toolkits.mplot3d.proj3d "mpl_toolkits.mplot3d.proj3d")
[#](https://matplotlib.org/stable/api/toolkits/mplot3d.html#proj3d "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`proj3d.inv_transform`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.proj3d.inv_transform.html#mpl_toolkits.mplot3d.proj3d.inv_transform "mpl_toolkits.mplot3d.proj3d.inv_transform")<br>(xs, ys, zs, invM) | Transform the points by the inverse of the projection matrix, _invM_. |
| [`proj3d.proj_transform`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.proj3d.proj_transform.html#mpl_toolkits.mplot3d.proj3d.proj_transform "mpl_toolkits.mplot3d.proj3d.proj_transform")<br>(xs, ys, zs, M) | Transform the points by the projection matrix _M_. |
| [`proj3d.proj_transform_clip`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.proj3d.proj_transform_clip.html#mpl_toolkits.mplot3d.proj3d.proj_transform_clip "mpl_toolkits.mplot3d.proj3d.proj_transform_clip")<br>(xs, ys, zs, M) | \[_Deprecated_\] |
| [`proj3d.world_transformation`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.proj3d.world_transformation.html#mpl_toolkits.mplot3d.proj3d.world_transformation "mpl_toolkits.mplot3d.proj3d.world_transformation")<br>(xmin, xmax, ...) | Produce a matrix that scales homogeneous coords in the specified ranges to \[0, 1\], or \[0, pb\_aspect\[i\]\] if the plotbox aspect ratio is specified. |

On this page