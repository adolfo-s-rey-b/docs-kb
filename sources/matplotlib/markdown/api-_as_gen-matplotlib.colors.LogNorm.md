[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#main-content)

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
    

matplotlib.colors.LogNorm[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib-colors-lognorm "Link to this heading")

========================================================================================================================================================

class matplotlib.colors.LogNorm(_vmin\=None_, _vmax\=None_, _clip\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2908-L2985)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "Link to this definition")

Bases: [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

Normalize a given value to the 0-1 range on a log scale.

Parameters:

**vmin, vmax**float or None

Values within the range `[vmin, vmax]` from the input data will be linearly mapped to `[0, 1]`. If either _vmin_ or _vmax_ is not provided, they default to the minimum and maximum values of the input, respectively.

**clip**bool, default: False

Determines the behavior for mapping values outside the range `[vmin, vmax]`.

If clipping is off, values outside the range `[vmin, vmax]` are also transformed, resulting in values outside `[0, 1]`. This behavior is usually desirable, as colormaps can mark these _under_ and _over_ values with specific colors.

If clipping is on, values below _vmin_ are mapped to 0 and values above _vmax_ are mapped to 1. Such values become indistinguishable from regular boundary values, which may cause misinterpretation of the data.

Notes

If `vmin == vmax`, input data will be mapped to 0.

\_\_call\_\_(_value_, _clip\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2942-L2961)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm.__call__ "Link to this definition")

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

autoscale\_None(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2980-L2985)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm.autoscale_None "Link to this definition")

If _vmin_ or _vmax_ are not set, use the min/max of _A_ to set them.

inverse(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2963-L2978)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm.inverse "Link to this definition")

Maps the normalized value (i.e., index in the colormap) back to image data value.

Parameters:

**value**

Normalized value.

Examples using `matplotlib.colors.LogNorm`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#examples-using-matplotlib-colors-lognorm "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_pcolor_demo_thumb.png)

[pcolor images](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolor_demo.html)

pcolor images

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_normalizations_thumb.png)

[Colormap normalizations](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_normalizations.html)

Colormap normalizations

![](https://matplotlib.org/stable/_images/sphx_glr_hist_thumb.png)

[Histograms](https://matplotlib.org/stable/gallery/statistics/hist.html)

Histograms

![](https://matplotlib.org/stable/_images/sphx_glr_quick_start_thumb.png)

[Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html)

Quick start guide

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

On this page