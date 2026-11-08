[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba_array.html#main-content)

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
    

matplotlib.colors.to\_rgba\_array[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba_array.html#matplotlib-colors-to-rgba-array "Link to this heading")

============================================================================================================================================================================

matplotlib.colors.to\_rgba\_array(_c_, _alpha\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L446-L551)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba_array.html#matplotlib.colors.to_rgba_array "Link to this definition")

Convert _c_ to a (n, 4) array of RGBA colors.

Parameters:

**c**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or list of [color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
 or RGB(A) array

If _c_ is a masked array, an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
 is returned with a (0, 0, 0, 0) row for each masked value or row in _c_.

**alpha**float or sequence of floats, optional

If _alpha_ is given, force the alpha value of the returned RGBA tuple to _alpha_.

If None, the alpha value from _c_ is used. If _c_ does not have an alpha channel, then alpha defaults to 1.

_alpha_ is ignored for the color value `"none"` (case-insensitive), which always maps to `(0, 0, 0, 0)`.

If _alpha_ is a sequence and _c_ is a single color, _c_ will be repeated to match the length of _alpha_.

Returns:

array

(n, 4) array of RGBA colors, where each channel (red, green, blue, alpha) can assume values between 0 and 1.

Examples using `matplotlib.colors.to_rgba_array`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.to_rgba_array.html#examples-using-matplotlib-colors-to-rgba-array "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_colors_thumb.png)

[Specifying colors](https://matplotlib.org/stable/users/explain/colors/colors.html)

Specifying colors

On this page