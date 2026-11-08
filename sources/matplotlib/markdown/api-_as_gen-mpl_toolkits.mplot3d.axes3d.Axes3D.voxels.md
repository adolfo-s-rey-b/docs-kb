[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.voxels.html#main-content)

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
    

mpl\_toolkits.mplot3d.axes3d.Axes3D.voxels[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.voxels.html#mpl-toolkits-mplot3d-axes3d-axes3d-voxels "Link to this heading")

=========================================================================================================================================================================================================

Axes3D.voxels(\[_x_, _y_, _z_, \]_/_, _filled_, _facecolors\=None_, _edgecolors\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/mplot3d/axes3d.py#L3636-L3849)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.voxels.html#mpl_toolkits.mplot3d.axes3d.Axes3D.voxels "Link to this definition")

Plot a set of filled voxels

All voxels are plotted as 1x1x1 cubes on the axis, with `filled[0, 0, 0]` placed with its lower corner at the origin. Occluded faces are not plotted.

Parameters:

**filled**3D np.array of bool

A 3D array of values, with truthy values indicating which voxels to fill

**x, y, z**3D np.array, optional

The coordinates of the corners of the voxels. This should broadcast to a shape one larger in every dimension than the shape of _filled_. These can be used to plot non-cubic voxels.

If not specified, defaults to increasing integers along each axis, like those returned by [`indices()`](https://numpy.org/doc/stable/reference/generated/numpy.indices.html#numpy.indices "(in NumPy v2.5)")
. As indicated by the `/` in the function signature, these arguments can only be passed positionally.

**facecolors, edgecolors**array-like, optional

The color to draw the faces and edges of the voxels. Can only be passed as keyword arguments. These parameters can be:

*   A single color value, to color all voxels the same color. This can be either a string, or a 1D RGB/RGBA array
    
*   `None`, the default, to use a single color for the faces, and the style default for the edges.
    
*   A 3D [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
     of color names, with each item the color for the corresponding voxel. The size must match the voxels.
    
*   A 4D [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
     of RGB/RGBA data, with the components along the last axis.
    

**shade**bool, default: True

Whether to shade the facecolors.

**lightsource**[`LightSource`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")
, optional

The lightsource to use when _shade_ is True.

**axlim\_clip**bool, default: False

Whether to hide voxels with points outside the axes view limits.

Added in version 3.10.

**\*\*kwargs**

Additional keyword arguments to pass onto [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
.

Returns:

**faces**dict

A dictionary indexed by coordinate, where `faces[i, j, k]` is a [`Poly3DCollection`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html#mpl_toolkits.mplot3d.art3d.Poly3DCollection "mpl_toolkits.mplot3d.art3d.Poly3DCollection")
 of the faces drawn for the voxel `filled[i, j, k]`. If no faces were drawn for a given voxel, either because it was not asked to be drawn, or it is fully occluded, then `(i, j, k) not in faces`.

Examples

([`Source code`](https://matplotlib.org/stable/_downloads/bffc095eda0f4f626d1da8c97178afcd/voxels.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/f271a4c6d2343ace3f6706b2b8b348c6/voxels_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/a803375654259ab28fd5aa2f3c4b5ed7/voxels_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-voxels_00_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-voxels_00_00.2x.png)

([`Source code`](https://matplotlib.org/stable/_downloads/cdcfc69294110306faf86b32bd593a70/voxels_rgb.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/adecec113d7daa4a5a38bbb8f29306af/voxels_rgb_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/9d0fc6204b950dc0225fbe70d12cfe79/voxels_rgb_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-voxels_rgb_00_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-voxels_rgb_00_00.2x.png)

([`Source code`](https://matplotlib.org/stable/_downloads/a22680c5161cae0bae86cebf2222cb71/voxels_torus.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/c204358959a1d5fbf80045d724fa5a72/voxels_torus_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/bbf9ac10c4576b2328858846f1bd4c96/voxels_torus_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-voxels_torus_00_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-voxels_torus_00_00.2x.png)

([`Source code`](https://matplotlib.org/stable/_downloads/3eef910ce113b73e9aaad84106d6a280/voxels_numpy_logo.py)
, [`2x.png`](https://matplotlib.org/stable/_downloads/e90fe51ea8fe605cd1e4097e2afd9d17/voxels_numpy_logo_00_00.2x.png)
, [`png`](https://matplotlib.org/stable/_downloads/0861dde529ac08f413f0498fb46d2cd3/voxels_numpy_logo_00_00.png)
)

[![](https://matplotlib.org/stable/_images/api-_as_gen-voxels_numpy_logo_00_00.2x.png)](https://matplotlib.org/stable/_images/api-_as_gen-voxels_numpy_logo_00_00.2x.png)

Examples using `mpl_toolkits.mplot3d.axes3d.Axes3D.voxels`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.voxels.html#examples-using-mpl-toolkits-mplot3d-axes3d-axes3d-voxels "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_thumb.png)

[3D voxel / volumetric plot](https://matplotlib.org/stable/gallery/mplot3d/voxels.html)

3D voxel / volumetric plot

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_numpy_logo_thumb.png)

[3D voxel plot of the NumPy logo](https://matplotlib.org/stable/gallery/mplot3d/voxels_numpy_logo.html)

3D voxel plot of the NumPy logo

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_rgb_thumb.png)

[3D voxel / volumetric plot with RGB colors](https://matplotlib.org/stable/gallery/mplot3d/voxels_rgb.html)

3D voxel / volumetric plot with RGB colors

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_torus_thumb.png)

[3D voxel / volumetric plot with cylindrical coordinates](https://matplotlib.org/stable/gallery/mplot3d/voxels_torus.html)

3D voxel / volumetric plot with cylindrical coordinates

![](https://matplotlib.org/stable/_images/sphx_glr_voxels_simple_thumb.png)

[voxels(\[x, y, z\], filled)](https://matplotlib.org/stable/plot_types/3D/voxels_simple.html)

voxels(\[x, y, z\], filled)

On this page