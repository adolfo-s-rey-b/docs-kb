[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#main-content)

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
    

matplotlib.colors.Norm[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib-colors-norm "Link to this heading")

===============================================================================================================================================

class matplotlib.colors.Norm[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2314-L2402)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib.colors.Norm "Link to this definition")

Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC "(in Python v3.14)")

Abstract base class for normalizations.

Subclasses include [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 which maps from a scalar to a scalar. However, this class makes no such requirement, and subclasses may support the normalization of multiple variates simultaneously, with separate normalization for each variate.

abstractmethod \_\_call\_\_(_value_, _clip\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2349-L2369)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib.colors.Norm.__call__ "Link to this definition")

Normalize the data and return the normalized data.

Parameters:

**value**

Data to normalize.

**clip**bool, optional

See the description of the parameter _clip_ in [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
.

If `None`, defaults to `self.clip` (which defaults to `False`).

Notes

If not already initialized, `self.vmin` and `self.vmax` are initialized using `self.autoscale_None(value)`.

abstractmethod autoscale(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2371-L2374)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib.colors.Norm.autoscale "Link to this definition")

Set _vmin_, _vmax_ to min, max of _A_.

abstractmethod autoscale\_None(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2376-L2379)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib.colors.Norm.autoscale_None "Link to this definition")

If _vmin_ or _vmax_ are not set, use the min/max of _A_ to set them.

abstract property clip[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib.colors.Norm.clip "Link to this definition")

Determines the behavior for mapping values outside the range `[vmin, vmax]`.

See the _clip_ parameter in [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
.

abstract property n\_components[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib.colors.Norm.n_components "Link to this definition")

The number of normalized components.

This is the number of elements of the parameter to `__call__` and of _vmin_, _vmax_.

abstractmethod scaled()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2381-L2384)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib.colors.Norm.scaled "Link to this definition")

Return whether _vmin_ and _vmax_ are both set.

abstract property vmax[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib.colors.Norm.vmax "Link to this definition")

Upper limit of the input data interval; maps to 1.

abstract property vmin[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib.colors.Norm.vmin "Link to this definition")

Lower limit of the input data interval; maps to 0.

Examples using `matplotlib.colors.Norm`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#examples-using-matplotlib-colors-norm "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_multivariate_marker_plot_thumb.png)

[Mapping marker properties to multivariate data](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multivariate_marker_plot.html)

Mapping marker properties to multivariate data

![](https://matplotlib.org/stable/_images/sphx_glr_image_masked_thumb.png)

[Image with masked values](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html)

Image with masked values

![](https://matplotlib.org/stable/_images/sphx_glr_multi_image_thumb.png)

[Multiple images with one colorbar](https://matplotlib.org/stable/gallery/images_contours_and_fields/multi_image.html)

Multiple images with one colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_image_transparency_blend_thumb.png)

[Blend transparency with color in 2D images](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_transparency_blend.html)

Blend transparency with color in 2D images

![](https://matplotlib.org/stable/_images/sphx_glr_pcolor_demo_thumb.png)

[pcolor images](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolor_demo.html)

pcolor images

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_levels_thumb.png)

[pcolormesh](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_levels.html)

pcolormesh

![](https://matplotlib.org/stable/_images/sphx_glr_contour_image_thumb.png)

[Contour image](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_image.html)

Contour image

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_normalizations_thumb.png)

[Colormap normalizations](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_normalizations.html)

Colormap normalizations

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_normalizations_symlognorm_thumb.png)

[Colormap normalizations SymLogNorm](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_normalizations_symlognorm.html)

Colormap normalizations SymLogNorm

![](https://matplotlib.org/stable/_images/sphx_glr_image_annotated_heatmap_thumb.png)

[Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html)

Annotated heatmap

![](https://matplotlib.org/stable/_images/sphx_glr_hist_thumb.png)

[Histograms](https://matplotlib.org/stable/gallery/statistics/hist.html)

Histograms

![](https://matplotlib.org/stable/_images/sphx_glr_power_norm_thumb.png)

[Exploring normalizations](https://matplotlib.org/stable/gallery/scales/power_norm.html)

Exploring normalizations

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_histogram_thumb.png)

[Histogram as colorbar](https://matplotlib.org/stable/gallery/color/colorbar_histogram.html)

Histogram as colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_imshow3d_thumb.png)

[2D images in 3D](https://matplotlib.org/stable/gallery/mplot3d/imshow3d.html)

2D images in 3D

![](https://matplotlib.org/stable/_images/sphx_glr_mandelbrot_thumb.png)

[Shaded & power normalized rendering](https://matplotlib.org/stable/gallery/showcase/mandelbrot.html)

Shaded & power normalized rendering

![](https://matplotlib.org/stable/_images/sphx_glr_advanced_hillshading_thumb.png)

[Hillshading](https://matplotlib.org/stable/gallery/specialty_plots/advanced_hillshading.html)

Hillshading

![](https://matplotlib.org/stable/_images/sphx_glr_leftventricle_bullseye_thumb.png)

[Left ventricle bullseye](https://matplotlib.org/stable/gallery/specialty_plots/leftventricle_bullseye.html)

Left ventricle bullseye

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_constrainedlayout_guide_thumb.png)

[Constrained layout guide](https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html)

Constrained layout guide

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_only_thumb.png)

[Customized Colorbars Tutorial](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html)

Customized Colorbars Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

On this page