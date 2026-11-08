[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#main-content)

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
    

matplotlib.colors.Colormap[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib-colors-colormap "Link to this heading")

===========================================================================================================================================================

class matplotlib.colors.Colormap(_name_, _N\=256_, _\*_, _bad\=None_, _under\=None_, _over\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L713-L1084)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Baseclass for all scalar to RGBA mappings.

Typically, Colormap instances are used to convert data values (floats) from the interval `[0, 1]` to the RGBA color that the respective Colormap represents. For scaling of data into the `[0, 1]` interval see [`matplotlib.colors.Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
. Subclasses of [`matplotlib.cm.ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
 make heavy use of this `data -> normalize -> map-to-color` processing chain.

Parameters:

**name**str

The name of the colormap.

**N**int

The number of RGB quantization levels.

**bad**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: transparent

The color for invalid values (NaN or masked).

Added in version 3.11.

**under**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: color of the lowest value

The color for low out-of-range values.

Added in version 3.11.

**over**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: color of the highest value

The color for high out-of-range values.

Added in version 3.11.

\_\_call\_\_(_X_, _alpha\=None_, _bytes\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L764-L790)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.__call__ "Link to this definition")

Parameters:

**X**float or int or array-like

The data value(s) to convert to RGBA. For floats, _X_ should be in the interval `[0.0, 1.0]` to return the RGBA values `X*100` percent along the Colormap line. For integers, _X_ should be in the interval `[0, Colormap.N)` to return RGBA values _indexed_ from the Colormap with index `X`.\
\
**alpha**float or array-like or None\
\
Alpha must be a scalar between 0 and 1, a sequence of such floats with shape matching X, or None.\
\
**bytes**bool, default: False\
\
If False (default), the returned RGBA values will be floats in the interval `[0, 1]` otherwise they will be [`numpy.uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")\
s in the interval `[0, 255]`.\
\
Returns:\
\
Tuple of RGBA values if X is scalar, otherwise an array of\
\
RGBA values with a shape of `X.shape + (4, )`.\
\
colorbar\_extend[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.colorbar_extend "Link to this definition")\
\
When this colormap exists on a scalar mappable and colorbar\_extend is not False, colorbar creation will pick up `colorbar_extend` as the default value for the `extend` keyword in the [`matplotlib.colorbar.Colorbar`](https://matplotlib.org/stable/api/colorbar_api.html#matplotlib.colorbar.Colorbar "matplotlib.colorbar.Colorbar")\
 constructor.\
\
copy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1082-L1084)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.copy "Link to this definition")\
\
Return a copy of the colormap.\
\
get\_bad()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L878-L881)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.get_bad "Link to this definition")\
\
Get the color for masked values.\
\
get\_over()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L904-L907)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.get_over "Link to this definition")\
\
Get the color for high out-of-range values.\
\
get\_under()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L891-L894)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.get_under "Link to this definition")\
\
Get the color for low out-of-range values.\
\
is\_gray()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L992-L996)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.is_gray "Link to this definition")\
\
Return whether the colormap is grayscale.\
\
resampled(_lutsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L998-L1009)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.resampled "Link to this definition")\
\
Return a new colormap with _lutsize_ entries.\
\
reversed(_name\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1011-L1028)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.reversed "Link to this definition")\
\
Return a reversed instance of the Colormap.\
\
Note\
\
This function is not implemented for the base class.\
\
Parameters:\
\
**name**str, optional\
\
The name for the reversed colormap. If None, the name is set to `self.name + "_r"`.\
\
See also\
\
[`LinearSegmentedColormap.reversed`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.reversed "matplotlib.colors.LinearSegmentedColormap.reversed")\
\
[`ListedColormap.reversed`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap.reversed "matplotlib.colors.ListedColormap.reversed")\
\
set\_bad(_color\='k'_, _alpha\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L883-L889)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_bad "Link to this definition")\
\
\[_Deprecated_\] Set the color for masked values.\
\
Notes\
\
Deprecated since version 3.11: Use cmap.with\_extremes(bad=...) or Colormap(bad=...) instead.\
\
set\_extremes(_\*_, _bad\=None_, _under\=None_, _over\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L917-L927)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_extremes "Link to this definition")\
\
\[_Deprecated_\] Set the colors for masked (_bad_) values and, when `norm.clip = False`, low (_under_) and high (_over_) out-of-range values.\
\
Notes\
\
Deprecated since version 3.11: Use cmap.with\_extremes(bad=..., under=..., over=...) or Colormap(bad=..., under=..., over=...) instead.\
\
set\_over(_color\='k'_, _alpha\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L909-L915)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_over "Link to this definition")\
\
\[_Deprecated_\] Set the color for high out-of-range values.\
\
Notes\
\
Deprecated since version 3.11: Use cmap.with\_extremes(over=...) or Colormap(over=...) instead.\
\
set\_under(_color\='k'_, _alpha\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L896-L902)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_under "Link to this definition")\
\
\[_Deprecated_\] Set the color for low out-of-range values.\
\
Notes\
\
Deprecated since version 3.11: Use cmap.with\_extremes(under=...) or Colormap(under=...) instead.\
\
with\_alpha(_alpha_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L966-L982)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.with_alpha "Link to this definition")\
\
Return a copy of the colormap with a new uniform transparency.\
\
Parameters:\
\
**alpha**float\
\
The alpha blending value, between 0 (transparent) and 1 (opaque).\
\
with\_extremes(_\*_, _bad\=None_, _under\=None_, _over\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L929-L937)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.with_extremes "Link to this definition")\
\
Return a copy of the colormap, for which the colors for masked (_bad_) values and, when `norm.clip = False`, low (_under_) and high (_over_) out-of-range values, have been set accordingly.\
\
Examples using `matplotlib.colors.Colormap`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#examples-using-matplotlib-colors-colormap "Link to this heading")\
\
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
![](https://matplotlib.org/stable/_images/sphx_glr_contourf_demo_thumb.png)\
\
[Contourf demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_demo.html)\
\
Contourf demo\
\
![](https://matplotlib.org/stable/_images/sphx_glr_custom_cmap_thumb.png)\
\
[Create a colormap from a list of colors](https://matplotlib.org/stable/gallery/color/custom_cmap.html)\
\
Create a colormap from a list of colors\
\
![](https://matplotlib.org/stable/_images/sphx_glr_individual_colors_from_cmap_thumb.png)\
\
[Selecting individual colors from a colormap](https://matplotlib.org/stable/gallery/color/individual_colors_from_cmap.html)\
\
Selecting individual colors from a colormap\
\
![](https://matplotlib.org/stable/_images/sphx_glr_lasso_demo_thumb.png)\
\
[Lasso Demo](https://matplotlib.org/stable/gallery/event_handling/lasso_demo.html)\
\
Lasso Demo\
\
![](https://matplotlib.org/stable/_images/sphx_glr_leftventricle_bullseye_thumb.png)\
\
[Left ventricle bullseye](https://matplotlib.org/stable/gallery/specialty_plots/leftventricle_bullseye.html)\
\
Left ventricle bullseye\
\
![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_only_thumb.png)\
\
[Customized Colorbars Tutorial](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html)\
\
Customized Colorbars Tutorial\
\
![](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_thumb.png)\
\
[Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html)\
\
Creating Colormaps in Matplotlib\
\
On this page