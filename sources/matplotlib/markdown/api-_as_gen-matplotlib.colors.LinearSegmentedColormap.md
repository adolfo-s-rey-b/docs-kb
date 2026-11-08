[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#main-content)

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
    

matplotlib.colors.LinearSegmentedColormap[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib-colors-linearsegmentedcolormap "Link to this heading")

========================================================================================================================================================================================================

class matplotlib.colors.LinearSegmentedColormap(_name_, _segmentdata_, _N\=256_, _gamma\=1.0_, _\*_, _bad\=None_, _under\=None_, _over\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1087-L1296)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "Link to this definition")

Bases: [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")

Colormap objects based on lookup tables using linear segments.

The lookup table is generated using linear interpolation for each primary color, with the 0-1 domain divided into any number of segments.

Create colormap from linear mapping segments.

Parameters:

**name**str

The name of the colormap.

**segmentdata**dict

A dictionary with keys "red", "green", "blue" for the color channels. Each entry should be a list of _x_, _y0_, _y1_ tuples, forming rows in a table. Entries for alpha are optional.

Example: suppose you want red to increase from 0 to 1 over the bottom half, green to do the same over the middle half, and blue over the top half. Then you would use:

{
    'red':   \[(0.0,  0.0, 0.0),\
              (0.5,  1.0, 1.0),\
              (1.0,  1.0, 1.0)\],
    'green': \[(0.0,  0.0, 0.0),\
              (0.25, 0.0, 0.0),\
              (0.75, 1.0, 1.0),\
              (1.0,  1.0, 1.0)\],
    'blue':  \[(0.0,  0.0, 0.0),\
              (0.5,  0.0, 0.0),\
              (1.0,  1.0, 1.0)\]
}

Each row in the table for a given color is a sequence of _x_, _y0_, _y1_ tuples. In each sequence, _x_ must increase monotonically from 0 to 1. For any input value _z_ falling between _x\[i\]_ and _x\[i+1\]_, the output value of a given color will be linearly interpolated between _y1\[i\]_ and _y0\[i+1\]_:

row i:   x  y0  y1
               /
              /
row i+1: x  y0  y1

Hence, y0 in the first row and y1 in the last row are never used.

**N**int

The number of RGB quantization levels.

**gamma**float

Gamma correction factor for input distribution x of the mapping. See also [https://en.wikipedia.org/wiki/Gamma\_correction](https://en.wikipedia.org/wiki/Gamma_correction)
.

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

See also

[`LinearSegmentedColormap.from_list`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.from_list "matplotlib.colors.LinearSegmentedColormap.from_list")

Static method; factory function for generating a smoothly-varying LinearSegmentedColormap.

static from\_list(_name_, _colors_, _N\=256_, _gamma\=1.0_, _\*_, _bad\=None_, _under\=None_, _over\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1193-L1251)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.from_list "Link to this definition")

Create a [`LinearSegmentedColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 from a list of colors.

Parameters:

**name**str

The name of the colormap.

**colors**list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of (value, color)

If only colors are given, they are equidistantly mapped from the range \\(\[0, 1\]\\); i.e. 0 maps to `colors[0]` and 1 maps to `colors[-1]`. If (value, color) pairs are given, the mapping is from _value_ to _color_. This can be used to divide the range unevenly. The values must increase monotonically from 0 to 1.

**N**int

The number of RGB quantization levels.

**gamma**float

**bad**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: transparent

The color for invalid values (NaN or masked).

**under**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: color of the lowest value

The color for low out-of-range values.

**over**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: color of the highest value

The color for high out-of-range values.

resampled(_lutsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1253-L1260)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.resampled "Link to this definition")

Return a new colormap with _lutsize_ entries.

reversed(_name\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1267-L1296)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.reversed "Link to this definition")

Return a reversed instance of the Colormap.

Parameters:

**name**str, optional

The name for the reversed colormap. If None, the name is set to `self.name + "_r"`.

Returns:

LinearSegmentedColormap

The reversed colormap.

set\_gamma(_gamma_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1188-L1191)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap.set_gamma "Link to this definition")

Set a new gamma value and regenerate colormap.

Examples using `matplotlib.colors.LinearSegmentedColormap`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#examples-using-matplotlib-colors-linearsegmentedcolormap "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_image_masked_thumb.png)

[Image with masked values](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_masked.html)

Image with masked values

![](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_thumb.png)

[Image resampling](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html)

Image resampling

![](https://matplotlib.org/stable/_images/sphx_glr_pcolormesh_levels_thumb.png)

[pcolormesh](https://matplotlib.org/stable/gallery/images_contours_and_fields/pcolormesh_levels.html)

pcolormesh

![](https://matplotlib.org/stable/_images/sphx_glr_contourf_demo_thumb.png)

[Contourf demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_demo.html)

Contourf demo

![](https://matplotlib.org/stable/_images/sphx_glr_contour_image_thumb.png)

[Contour image](https://matplotlib.org/stable/gallery/images_contours_and_fields/contour_image.html)

Contour image

![](https://matplotlib.org/stable/_images/sphx_glr_custom_legends_thumb.png)

[Compose custom legends](https://matplotlib.org/stable/gallery/text_labels_and_annotations/custom_legends.html)

Compose custom legends

![](https://matplotlib.org/stable/_images/sphx_glr_hatchcolor_demo_thumb.png)

[Hatchcolor Demo](https://matplotlib.org/stable/gallery/shapes_and_collections/hatchcolor_demo.html)

Hatchcolor Demo

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_histogram_thumb.png)

[Histogram as colorbar](https://matplotlib.org/stable/gallery/color/colorbar_histogram.html)

Histogram as colorbar

![](https://matplotlib.org/stable/_images/sphx_glr_custom_cmap_thumb.png)

[Create a colormap from a list of colors](https://matplotlib.org/stable/gallery/color/custom_cmap.html)

Create a colormap from a list of colors

![](https://matplotlib.org/stable/_images/sphx_glr_logos2_thumb.png)

[Matplotlib logo](https://matplotlib.org/stable/gallery/misc/logos2.html)

Matplotlib logo

![](https://matplotlib.org/stable/_images/sphx_glr_leftventricle_bullseye_thumb.png)

[Left ventricle bullseye](https://matplotlib.org/stable/gallery/specialty_plots/leftventricle_bullseye.html)

Left ventricle bullseye

![](https://matplotlib.org/stable/_images/sphx_glr_topographic_hillshading_thumb.png)

[Topographic hillshading](https://matplotlib.org/stable/gallery/specialty_plots/topographic_hillshading.html)

Topographic hillshading

![](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_thumb.png)

[Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html)

Creating Colormaps in Matplotlib

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

On this page