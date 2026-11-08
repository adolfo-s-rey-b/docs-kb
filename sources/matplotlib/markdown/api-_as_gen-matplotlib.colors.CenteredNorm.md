[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#main-content)

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
    

matplotlib.colors.CenteredNorm[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib-colors-centerednorm "Link to this heading")

=======================================================================================================================================================================

class matplotlib.colors.CenteredNorm(_vcenter\=0_, _halfrange\=None_, _clip\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2723-L2838)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib.colors.CenteredNorm "Link to this definition")

Bases: [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")

Normalize symmetrical data around a center (0 by default).

Unlike [`TwoSlopeNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html#matplotlib.colors.TwoSlopeNorm "matplotlib.colors.TwoSlopeNorm")
, [`CenteredNorm`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib.colors.CenteredNorm "matplotlib.colors.CenteredNorm")
 applies an equal rate of change around the center.

Useful when mapping symmetrical data around a conceptual center e.g., data that range from -2 to 4, with 0 as the midpoint, and with equal rates of change around that midpoint.

Parameters:

**vcenter**float, default: 0

The data value that defines `0.5` in the normalization.

**halfrange**float, optional

The range of data values that defines a range of `0.5` in the normalization, so that _vcenter_ - _halfrange_ is `0.0` and _vcenter_ + _halfrange_ is `1.0` in the normalization. Defaults to the largest absolute difference to _vcenter_ for the values in the dataset.

**clip**bool, default: False

Determines the behavior for mapping values outside the range `[vmin, vmax]`.

If clipping is off, values outside the range `[vmin, vmax]` are also transformed, resulting in values outside `[0, 1]`. This behavior is usually desirable, as colormaps can mark these _under_ and _over_ values with specific colors.

If clipping is on, values below _vmin_ are mapped to 0 and values above _vmax_ are mapped to 1. Such values become indistinguishable from regular boundary values, which may cause misinterpretation of the data.

Examples

This maps data values -2 to 0.25, 0 to 0.5, and 4 to 1.0 (assuming equal rates of change above and below 0.0):

\>>> import matplotlib.colors as mcolors
\>>> norm \= mcolors.CenteredNorm(halfrange\=4.0)
\>>> data \= \[\-2., 0., 4.\]
\>>> norm(data)
array(\[0.25, 0.5 , 1.  \])

autoscale(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2775-L2781)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib.colors.CenteredNorm.autoscale "Link to this definition")

Set _halfrange_ to `max(abs(A-vcenter))`, then set _vmin_ and _vmax_.

autoscale\_None(_A_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2783-L2787)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib.colors.CenteredNorm.autoscale_None "Link to this definition")

Set _vmin_ and _vmax_.

property halfrange[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib.colors.CenteredNorm.halfrange "Link to this definition")

property vcenter[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib.colors.CenteredNorm.vcenter "Link to this definition")

property vmax[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib.colors.CenteredNorm.vmax "Link to this definition")

Upper limit of the input data interval; maps to 1.

property vmin[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#matplotlib.colors.CenteredNorm.vmin "Link to this definition")

Lower limit of the input data interval; maps to 0.

Examples using `matplotlib.colors.CenteredNorm`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.CenteredNorm.html#examples-using-matplotlib-colors-centerednorm "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

On this page