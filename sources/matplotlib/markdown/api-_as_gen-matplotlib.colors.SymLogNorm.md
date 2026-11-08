[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#main-content)

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
    

matplotlib.colors.SymLogNorm[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib-colors-symlognorm "Link to this heading")

=================================================================================================================================================================

class matplotlib.colors.SymLogNorm(_linthresh_, _linscale\=1.0_, _vmin\=None_, _vmax\=None_, _clip\=False_, _\*_, _base\=10_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2908-L2985)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "Link to this definition")

Bases: [`SymLogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")

The symmetrical logarithmic scale is logarithmic in both the positive and negative directions from the origin.

Since the values close to zero tend toward infinity, there is a need to have a range around zero that is linear. The parameter _linthresh_ allows the user to specify the size of this range (-_linthresh_, _linthresh_).

Parameters:

**linthresh**float

The range within which the plot is linear (to avoid having the plot go to infinity around zero).

**linscale**float, default: 1

This allows the linear range (-_linthresh_ to _linthresh_) to be stretched relative to the logarithmic range. Its value is the number of decades to use for each half of the linear range. For example, when _linscale_ == 1.0 (the default), the space used for the positive and negative halves of the linear range will be equal to one decade in the logarithmic range.

**base**float, default: 10

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
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm.__call__ "Link to this definition")

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
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm.autoscale_None "Link to this definition")

If _vmin_ or _vmax_ are not set, use the min/max of _A_ to set them.

inverse(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2963-L2978)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm.inverse "Link to this definition")

Maps the normalized value (i.e., index in the colormap) back to image data value.

Parameters:

**value**

Normalized value.

Examples using `matplotlib.colors.SymLogNorm`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#examples-using-matplotlib-colors-symlognorm "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_normalizations_thumb.png)

[Colormap normalizations](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_normalizations.html)

Colormap normalizations

![](https://matplotlib.org/stable/_images/sphx_glr_colormap_normalizations_symlognorm_thumb.png)

[Colormap normalizations SymLogNorm](https://matplotlib.org/stable/gallery/images_contours_and_fields/colormap_normalizations_symlognorm.html)

Colormap normalizations SymLogNorm

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

On this page