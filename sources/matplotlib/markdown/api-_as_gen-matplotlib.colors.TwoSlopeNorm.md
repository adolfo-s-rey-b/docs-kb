[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#main-content)

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
    

matplotlib.colors.TwoSlopeNorm[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib-colors-twoslopenorm "Link to this heading")

=======================================================================================================================================================================

class matplotlib.colors.TwoSlopeNorm(_vcenter_, _vmin\=None_, _vmax\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2628-L2720)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib.colors.TwoSlopeNorm "Link to this definition")

Bases: [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

Normalize data with a set center.

Useful when mapping data with an unequal rates of change around a conceptual center, e.g., data that range from -2 to 4, with 0 as the midpoint.

Parameters:

**vcenter**float

The data value that defines `0.5` in the normalization.

**vmin**float, optional

The data value that defines `0.0` in the normalization. Defaults to the min value of the dataset.

**vmax**float, optional

The data value that defines `1.0` in the normalization. Defaults to the max value of the dataset.

Examples

This maps data value -4000 to 0., 0 to 0.5, and +10000 to 1.0; data between is linearly interpolated:

\>>> import matplotlib.colors as mcolors
\>>> offset \= mcolors.TwoSlopeNorm(vmin\=-4000.,
...                               vcenter\=0., vmax\=10000)
\>>> data \= \[\-4000., \-2000., 0., 2500., 5000., 7500., 10000.\]
\>>> offset(data)
array(\[0., 0.25, 0.5, 0.625, 0.75, 0.875, 1.0\])

\_\_call\_\_(_value_, _clip\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2694-L2710)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib.colors.TwoSlopeNorm.__call__ "Link to this definition")

Map value to the interval \[0, 1\]. The _clip_ argument is unused.

autoscale\_None(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2680-L2692)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib.colors.TwoSlopeNorm.autoscale_None "Link to this definition")

Get vmin and vmax.

If vcenter isn't in the range \[vmin, vmax\], either vmin or vmax is expanded so that vcenter lies in the middle of the modified range \[vmin, vmax\].

inverse(_value_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2712-L2720)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib.colors.TwoSlopeNorm.inverse "Link to this definition")

Maps the normalized value (i.e., index in the colormap) back to image data value.

Parameters:

**value**

Normalized value.

property vcenter[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib.colors.TwoSlopeNorm.vcenter "Link to this definition")

Examples using `matplotlib.colors.TwoSlopeNorm`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#examples-using-matplotlib-colors-twoslopenorm "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

On this page