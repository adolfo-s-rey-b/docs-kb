[Skip to main content](https://matplotlib.org/stable/api/colors_api.html#main-content)

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
    

`matplotlib.colors`[#](https://matplotlib.org/stable/api/colors_api.html#matplotlib-colors "Link to this heading")

===================================================================================================================

Note

The Color [tutorials](https://matplotlib.org/stable/users/explain/colors/index.html#tutorials-colors)
 and [examples](https://matplotlib.org/stable/gallery/color/index.html#color-examples)
 demonstrate how to set colors and colormaps. You may want to read those instead.

A module for converting numbers or color arguments to _RGB_ or _RGBA_.

_RGB_ and _RGBA_ are sequences of, respectively, 3 or 4 floats in the range 0-1.

This module includes functions and classes for color specification conversions, and for mapping numbers to colors in a 1-D array of colors called a colormap.

Mapping data onto colors using a colormap typically involves two steps: a data array is first mapped onto the range 0-1 using a subclass of [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
, then this number is mapped to a color using a subclass of [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
. Two subclasses of [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 provided here: [`LinearSegmentedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
, which uses piecewise-linear interpolation to define colormaps, and [`ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
, which makes a colormap from a list of colors.

See also

[Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#colormap-manipulation)
 for examples of how to make colormaps and

[Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html#colormaps)
 for a list of built-in colormaps.

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html#colormapnorms)
 for more details about data normalization

More colormaps are available at [palettable](https://jiffyclub.github.io/palettable/)
.

The module also provides functions for checking whether an object can be interpreted as a color ([`is_color_like`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.is_color_like.html#matplotlib.colors.is_color_like "matplotlib.colors.is_color_like")
), for converting such an object to an RGBA tuple ([`to_rgba`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba.html#matplotlib.colors.to_rgba "matplotlib.colors.to_rgba")
) or to an HTML-like hex string in the "#rrggbb" format ([`to_hex`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_hex.html#matplotlib.colors.to_hex "matplotlib.colors.to_hex")
), and a sequence of colors to an (n, 4) RGBA array ([`to_rgba_array`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba_array.html#matplotlib.colors.to_rgba_array "matplotlib.colors.to_rgba_array")
). Caching is used for efficiency.

Colors that Matplotlib recognizes are listed at [Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
.

Color norms[#](https://matplotlib.org/stable/api/colors_api.html#color-norms "Link to this heading")

-----------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Norm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Norm.html#matplotlib.colors.Norm "matplotlib.colors.Norm")<br>() | Abstract base class for normalizations. |
| [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br>(\[vmin, vmax, clip\]) | A class which, when called, maps values within the interval `[vmin, vmax]` linearly to the interval `[0.0, 1.0]`. |
| [`NoNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.NoNorm.html#matplotlib.colors.NoNorm "matplotlib.colors.NoNorm")<br>(\[vmin, vmax, clip\]) | Dummy replacement for [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br>, for the case where we want to use indices directly in a [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")<br>. |
| [`AsinhNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.AsinhNorm.html#matplotlib.colors.AsinhNorm "matplotlib.colors.AsinhNorm")<br>(\[linear\_width, vmin, vmax, clip\]) | The inverse hyperbolic sine scale is approximately linear near the origin, but becomes logarithmic for larger positive or negative values. |
| [`BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")<br>(boundaries, ncolors\[, clip, extend\]) | Generate a colormap index based on discrete intervals. |
| [`CenteredNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib.colors.CenteredNorm "matplotlib.colors.CenteredNorm")<br>(\[vcenter, halfrange, clip\]) | Normalize symmetrical data around a center (0 by default). |
| [`FuncNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.FuncNorm.html#matplotlib.colors.FuncNorm "matplotlib.colors.FuncNorm")<br>(functions\[, vmin, vmax, clip\]) | Arbitrary normalization using functions for the forward and inverse. |
| [`LogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LogNorm.html#matplotlib.colors.LogNorm "matplotlib.colors.LogNorm")<br>(\[vmin, vmax, clip\]) | Normalize a given value to the 0-1 range on a log scale. |
| [`PowerNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.PowerNorm.html#matplotlib.colors.PowerNorm "matplotlib.colors.PowerNorm")<br>(gamma\[, vmin, vmax, clip\]) | Linearly map a given value to the 0-1 range and then apply a power-law normalization over that range. |
| [`SymLogNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SymLogNorm.html#matplotlib.colors.SymLogNorm "matplotlib.colors.SymLogNorm")<br>(linthresh\[, linscale, vmin, ...\]) | The symmetrical logarithmic scale is logarithmic in both the positive and negative directions from the origin. |
| [`TwoSlopeNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib.colors.TwoSlopeNorm "matplotlib.colors.TwoSlopeNorm")<br>(vcenter\[, vmin, vmax\]) | Normalize data with a set center. |
| [`MultiNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.MultiNorm.html#matplotlib.colors.MultiNorm "matplotlib.colors.MultiNorm")<br>(norms\[, vmin, vmax, clip\]) | A class which contains multiple scalar norms. |

Univariate Colormaps[#](https://matplotlib.org/stable/api/colors_api.html#univariate-colormaps "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")<br>(name\[, N, bad, under, over\]) | Baseclass for all scalar to RGBA mappings. |
| [`LinearSegmentedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")<br>(name, segmentdata\[, ...\]) | Colormap objects based on lookup tables using linear segments. |
| [`ListedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")<br>(colors\[, name, N, bad, ...\]) | Colormap object generated from a list of colors. |

Multivariate Colormaps[#](https://matplotlib.org/stable/api/colors_api.html#multivariate-colormaps "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`BivarColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap "matplotlib.colors.BivarColormap")<br>(\[N, M, shape, origin, name\]) | Base class for all bivariate to RGBA mappings. |
| [`SegmentedBivarColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.SegmentedBivarColormap.html#matplotlib.colors.SegmentedBivarColormap "matplotlib.colors.SegmentedBivarColormap")<br>(patch\[, N, shape, ...\]) | BivarColormap object generated by supersampling a regular grid. |
| [`BivarColormapFromImage`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormapFromImage.html#matplotlib.colors.BivarColormapFromImage "matplotlib.colors.BivarColormapFromImage")<br>(lut\[, shape, origin, ...\]) | BivarColormap object generated by supersampling a regular grid. |

Other classes[#](https://matplotlib.org/stable/api/colors_api.html#other-classes "Link to this heading")

---------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`ColorSequenceRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry "matplotlib.colors.ColorSequenceRegistry")<br>() | Container for sequences of colors that are known to Matplotlib by name. |
| [`LightSource`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "matplotlib.colors.LightSource")<br>(\[azdeg, altdeg, hsv\_min\_val, ...\]) | Create a light source coming from the specified azimuth and elevation. |

Functions[#](https://matplotlib.org/stable/api/colors_api.html#functions "Link to this heading")

-------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`from_levels_and_colors`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.from_levels_and_colors.html#matplotlib.colors.from_levels_and_colors "matplotlib.colors.from_levels_and_colors")<br>(levels, colors\[, extend\]) | A helper routine to generate a cmap and a norm instance which behave similar to contourf's levels and colors arguments. |
| [`hsv_to_rgb`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.hsv_to_rgb.html#matplotlib.colors.hsv_to_rgb "matplotlib.colors.hsv_to_rgb")<br>(hsv) | Convert HSV values to RGB. |
| [`rgb_to_hsv`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.rgb_to_hsv.html#matplotlib.colors.rgb_to_hsv "matplotlib.colors.rgb_to_hsv")<br>(arr) | Convert an array of float RGB values (in the range \[0, 1\]) to HSV values. |
| [`to_hex`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_hex.html#matplotlib.colors.to_hex "matplotlib.colors.to_hex")<br>(c\[, keep\_alpha\]) | Convert _c_ to a hex color. |
| [`to_rgb`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgb.html#matplotlib.colors.to_rgb "matplotlib.colors.to_rgb")<br>(c) | Convert the [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> _c_ to an RGB color tuple. |
| [`to_rgba`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba.html#matplotlib.colors.to_rgba "matplotlib.colors.to_rgba")<br>(c\[, alpha\]) | Convert _c_ to an RGBA color. |
| [`to_rgba_array`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba_array.html#matplotlib.colors.to_rgba_array "matplotlib.colors.to_rgba_array")<br>(c\[, alpha\]) | Convert _c_ to a (n, 4) array of RGBA colors. |
| [`is_color_like`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.is_color_like.html#matplotlib.colors.is_color_like "matplotlib.colors.is_color_like")<br>(c) | Return whether _c_ as a valid Matplotlib [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)<br> specifier. |
| [`same_color`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.same_color.html#matplotlib.colors.same_color "matplotlib.colors.same_color")<br>(c1, c2) | Return whether the colors _c1_ and _c2_ are the same. |
| [`get_named_colors_mapping`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.get_named_colors_mapping.html#matplotlib.colors.get_named_colors_mapping "matplotlib.colors.get_named_colors_mapping")<br>() | Return the global mapping of names to named colors. |
| [`make_norm_from_scale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.make_norm_from_scale.html#matplotlib.colors.make_norm_from_scale "matplotlib.colors.make_norm_from_scale")<br>(scale\_cls\[, ...\]) | Decorator for building a [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")<br> subclass from a [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")<br> subclass. |

Exported colors[#](https://matplotlib.org/stable/api/colors_api.html#exported-colors "Link to this heading")

-------------------------------------------------------------------------------------------------------------

The data used to populate the [List of named colors](https://matplotlib.org/stable/gallery/color/named_colors.html)
 are exposed as dictionaries that map color names to hex strings.

matplotlib.colors.BASE\_COLORS[#](https://matplotlib.org/stable/api/colors_api.html#matplotlib.colors.BASE_COLORS "Link to this definition")

matplotlib.colors.TABLEAU\_COLORS[#](https://matplotlib.org/stable/api/colors_api.html#matplotlib.colors.TABLEAU_COLORS "Link to this definition")

matplotlib.colors.CSS4\_COLORS[#](https://matplotlib.org/stable/api/colors_api.html#matplotlib.colors.CSS4_COLORS "Link to this definition")

matplotlib.colors.XKCD\_COLORS[#](https://matplotlib.org/stable/api/colors_api.html#matplotlib.colors.XKCD_COLORS "Link to this definition")

On this page