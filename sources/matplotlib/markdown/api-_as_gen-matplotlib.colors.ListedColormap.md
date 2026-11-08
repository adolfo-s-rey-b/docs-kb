[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#main-content)

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
    

matplotlib.colors.ListedColormap[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib-colors-listedcolormap "Link to this heading")

=============================================================================================================================================================================

class matplotlib.colors.ListedColormap(_colors_, _name\='unnamed'_, _N\=<deprecated parameter>_, _\*_, _bad\=None_, _under\=None_, _over\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1299-L1429)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "Link to this definition")

Bases: [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")

Colormap object generated from a list of colors.

This may be most useful when indexing directly into a colormap, but it can also be used to generate special colormaps for ordinary mapping.

Parameters:

**colors**list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or array

Sequence of Matplotlib color specifications (color names or RGB(A) values).

**name**str, optional

String to identify the colormap.

**N**int, optional

Number of entries in the map. The default is _None_, in which case there is one colormap entry for each element in the list of colors. If

N < len(colors)

the list will be truncated at _N_. If

N \> len(colors)

the list will be extended by repetition.

Deprecated since version 3.11: This parameter will be removed. Please instead ensure that the list of passed colors is the required length.

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

property monochrome[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap.monochrome "Link to this definition")

Return whether all colors in the colormap are identical.

resampled(_lutsize_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1395-L1403)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap.resampled "Link to this definition")

Return a new colormap with _lutsize_ entries.

reversed(_name\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1405-L1429)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap.reversed "Link to this definition")

Return a reversed instance of the Colormap.

Parameters:

**name**str, optional

The name for the reversed colormap. If None, the name is set to `self.name + "_r"`.

Returns:

ListedColormap

A reversed instance of the colormap.

Examples using `matplotlib.colors.ListedColormap`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#examples-using-matplotlib-colors-listedcolormap "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_multivariate_marker_plot_thumb.png)

[Mapping marker properties to multivariate data](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multivariate_marker_plot.html)

Mapping marker properties to multivariate data

![](https://matplotlib.org/stable/_images/sphx_glr_quadmesh_demo_thumb.png)

[QuadMesh Demo](https://matplotlib.org/stable/gallery/images_contours_and_fields/quadmesh_demo.html)

QuadMesh Demo

![](https://matplotlib.org/stable/_images/sphx_glr_time_series_histogram_thumb.png)

[Time Series Histogram](https://matplotlib.org/stable/gallery/statistics/time_series_histogram.html)

Time Series Histogram

![](https://matplotlib.org/stable/_images/sphx_glr_nested_pie_thumb.png)

[Nested pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html)

Nested pie charts

![](https://matplotlib.org/stable/_images/sphx_glr_individual_colors_from_cmap_thumb.png)

[Selecting individual colors from a colormap](https://matplotlib.org/stable/gallery/color/individual_colors_from_cmap.html)

Selecting individual colors from a colormap

![](https://matplotlib.org/stable/_images/sphx_glr_lasso_demo_thumb.png)

[Lasso Demo](https://matplotlib.org/stable/gallery/event_handling/lasso_demo.html)

Lasso Demo

![](https://matplotlib.org/stable/_images/sphx_glr_leftventricle_bullseye_thumb.png)

[Left ventricle bullseye](https://matplotlib.org/stable/gallery/specialty_plots/leftventricle_bullseye.html)

Left ventricle bullseye

![](https://matplotlib.org/stable/_images/sphx_glr_colorbar_only_thumb.png)

[Customized Colorbars Tutorial](https://matplotlib.org/stable/users/explain/colors/colorbar_only.html)

Customized Colorbars Tutorial

![](https://matplotlib.org/stable/_images/sphx_glr_colormap-manipulation_thumb.png)

[Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html)

Creating Colormaps in Matplotlib

On this page