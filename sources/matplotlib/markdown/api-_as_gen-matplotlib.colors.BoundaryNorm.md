[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#main-content)

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
    

matplotlib.colors.BoundaryNorm[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib-colors-boundarynorm "Link to this heading")

=======================================================================================================================================================================

class matplotlib.colors.BoundaryNorm(_boundaries_, _ncolors_, _clip\=False_, _\*_, _extend\='neither'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3208-L3335)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "Link to this definition")

Bases: [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

Generate a colormap index based on discrete intervals.

Unlike [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 or [`LogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")
, [`BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
 maps values to integers instead of to the interval 0-1.

Parameters:

**boundaries**array-like

Monotonically increasing sequence of at least 2 bin edges: data falling in the n-th bin will be mapped to the n-th color. Bins are left-closed and right-open; i.e., the n-th bin is `boundaries[n] <= value < boundaries[n + 1]`.

**ncolors**int

Number of colors in the colormap to be used.

**clip**bool, optional

If clip is `True`, out of range values are mapped to 0 if they are below `boundaries[0]` or mapped to `ncolors - 1` if they are greater than or equal to `boundaries[-1]`.

If clip is `False`, out of range values are mapped to -1 if they are below `boundaries[0]` or mapped to _ncolors_ if they are greater than or equal to `boundaries[-1]`. These are then converted to valid indices by [`Colormap.__call__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.__call__ "matplotlib.colors.Colormap.__call__")
.

**extend**{'neither', 'both', 'min', 'max'}, default: 'neither'

Extend the number of bins to include one or both of the regions beyond the boundaries. For example, if `extend` is 'min', then the color to which the region between the first pair of boundaries is mapped will be distinct from the first color in the colormap, and by default a [`Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")
 will be drawn with the triangle extension on the left or lower end.

Notes

If there are fewer bins (including extensions) than colors, then the color index is chosen by linearly interpolating the `[0, nbins - 1]` range onto the `[0, ncolors - 1]` range, effectively skipping some colors in the middle of the colormap.

\_\_call\_\_(_value_, _clip\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3285-L3325)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm.__call__ "Link to this definition")

This method behaves similarly to [`Normalize.__call__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize.__call__ "matplotlib.colors.Normalize.__call__")
, except that it returns integers or arrays of int16.

inverse(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3327-L3335)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm.inverse "Link to this definition")

Raises:

ValueError

BoundaryNorm is not invertible, so calling this method will always raise an error

Examples using `matplotlib.colors.BoundaryNorm`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#examples-using-matplotlib-colors-boundarynorm "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_image_masked_thumb.png)

[Image with masked values](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html)

Image with masked values

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_levels_thumb.png)

[pcolormesh](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_levels.html)

pcolormesh

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_normalizations_thumb.png)

[Colormap normalizations](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_normalizations.html)

Colormap normalizations

![](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_thumb.png)

[Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)

Annotated heatmap

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_histogram_thumb.png)

[Histogram as colorbar](https://matplotlib.org/stable/gallery/color/colorbar_histogram.html)

Histogram as colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_leftventricle_bullseye_thumb.png)

[Left ventricle bullseye](https://matplotlib.org/stable/gallery/specialty_plots/leftventricle_bullseye.html)

Left ventricle bullseye

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_only_thumb.png)

[Customized Colorbars Tutorial](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html)

Customized Colorbars Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

On this page