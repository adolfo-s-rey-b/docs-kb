[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#main-content)

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
    

matplotlib.pyplot.get\_cmap[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib-pyplot-get-cmap "Link to this heading")

============================================================================================================================================================

matplotlib.pyplot.get\_cmap(_name\=None_, _lut\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L2707-L2733)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "Link to this definition")

Get a colormap instance, defaulting to rc values if _name_ is None.

Parameters:

**name**[`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 or str or None, default: None

If a [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 instance, it will be returned. Otherwise, the name of a colormap known to Matplotlib, which will be resampled by _lut_. The default, None, means `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`).

**lut**int or None, default: None

If _name_ is not already a Colormap instance and _lut_ is not None, the colormap will be resampled to have _lut_ entries in the lookup table.

Returns:

Colormap

Examples using `matplotlib.pyplot.get_cmap`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#examples-using-matplotlib-pyplot-get-cmap "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_thumb.png)

[Image resampling](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)

Image resampling

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_histogram_thumb.png)

[Histogram as colorbar](https://matplotlib.org/stable/gallery/color/colorbar_histogram.html)

Histogram as colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_imshow3d_thumb.png)

[2D images in 3D](https://matplotlib.org/stable/gallery/mplot3d/imshow3d.html)

2D images in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_intersecting_planes_thumb.png)

[Intersecting planes](https://matplotlib.org/stable/gallery/mplot3d/intersecting_planes.html)

Intersecting planes

![](https://matplotlib.org/stable/_images/sphx_glr_pie_thumb.png)

[pie(x)](https://matplotlib.org/stable/plot_types/stats/pie.html)

pie(x)

On this page