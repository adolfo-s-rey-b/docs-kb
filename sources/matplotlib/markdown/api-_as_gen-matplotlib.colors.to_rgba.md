[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba.html#main-content)

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
    

matplotlib.colors.to\_rgba[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba.html#matplotlib-colors-to-rgba "Link to this heading")

=========================================================================================================================================================

matplotlib.colors.to\_rgba(_c_, _alpha\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L314-L358)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba.html#matplotlib.colors.to_rgba "Link to this definition")

Convert _c_ to an RGBA color.

Parameters:

**c**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or `np.ma.masked`

**alpha**float, optional

If _alpha_ is given, force the alpha value of the returned RGBA tuple to _alpha_.

If None, the alpha value from _c_ is used. If _c_ does not have an alpha channel, then alpha defaults to 1.

_alpha_ is ignored for the color value `"none"` (case-insensitive), which always maps to `(0, 0, 0, 0)`.

Returns:

tuple

Tuple of floats `(r, g, b, a)`, where each channel (red, green, blue, alpha) can assume values between 0 and 1.

Examples using `matplotlib.colors.to_rgba`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba.html#examples-using-matplotlib-colors-to-rgba "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_named_colors_thumb.png)

[List of named colors](https://matplotlib.org/stable/gallery/color/named_colors.html)

List of named colors

On this page