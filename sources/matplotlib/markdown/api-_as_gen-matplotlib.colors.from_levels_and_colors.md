[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.from_levels_and_colors.html#main-content)

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
    

matplotlib.colors.from\_levels\_and\_colors[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.from_levels_and_colors.html#matplotlib-colors-from-levels-and-colors "Link to this heading")

========================================================================================================================================================================================================

matplotlib.colors.from\_levels\_and\_colors(_levels_, _colors_, _extend\='neither'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L4233-L4282)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.from_levels_and_colors.html#matplotlib.colors.from_levels_and_colors "Link to this definition")

A helper routine to generate a cmap and a norm instance which behave similar to contourf's levels and colors arguments.

Parameters:

**levels**sequence of numbers

The quantization levels used to construct the [`BoundaryNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html#matplotlib.colors.BoundaryNorm "matplotlib.colors.BoundaryNorm")
. Value `v` is quantized to level `i` if `lev[i] <= v < lev[i+1]`.

**colors**sequence of colors

The fill color to use for each level. If _extend_ is "neither" there must be `n_level - 1` colors. For an _extend_ of "min" or "max" add one extra color, and for an _extend_ of "both" add two colors.

**extend**{'neither', 'min', 'max', 'both'}, optional

The behaviour when a value falls out of range of the given levels. See [`contourf`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contourf.html#matplotlib.axes.Axes.contourf "matplotlib.axes.Axes.contourf")
 for details.

Returns:

**cmap**[`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")

**norm**[`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

On this page