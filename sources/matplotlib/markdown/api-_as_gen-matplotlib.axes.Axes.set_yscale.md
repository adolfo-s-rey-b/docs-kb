[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#main-content)

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
    

matplotlib.axes.Axes.set\_yscale[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib-axes-axes-set-yscale "Link to this heading")

===========================================================================================================================================================================

Axes.set\_yscale(_value_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_base.py#L74-L75)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "Link to this definition")

Set the yaxis' scale.

Parameters:

**value**str or [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")

The axis scale type to apply. Valid string values are the names of scale classes ("linear", "log", "function",...). These may be the names of any of the [built-in scales](https://matplotlib.org/stable/api/scale_api.html#builtin-scales)
 or of any custom scales registered using [`matplotlib.scale.register_scale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.register_scale "matplotlib.scale.register_scale")
.

**\*\*kwargs**

If _value_ is a string, keywords are passed to the instantiation method of the respective class.

Examples using `matplotlib.axes.Axes.set_yscale`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#examples-using-matplotlib-axes-axes-set-yscale "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_markevery_demo_thumb.png)

[Markevery Demo](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html)

Markevery Demo

![](https://matplotlib.org/stable/_images/sphx_glr_errorbar_features_thumb.png)

[Different ways of specifying error bars](https://matplotlib.org/stable/gallery/statistics/errorbar_features.html)

Different ways of specifying error bars

![](https://matplotlib.org/stable/_images/sphx_glr_boxplot_thumb.png)

[Artist customization in box plots](https://matplotlib.org/stable/gallery/statistics/boxplot.html)

Artist customization in box plots

![](https://matplotlib.org/stable/_images/sphx_glr_scales_thumb.png)

[Scales overview](https://matplotlib.org/stable/gallery/scales/scales.html)

Scales overview

![](https://matplotlib.org/stable/_images/sphx_glr_asinh_demo_thumb.png)

[Asinh scale](https://matplotlib.org/stable/gallery/scales/asinh_demo.html)

Asinh scale

![](https://matplotlib.org/stable/_images/sphx_glr_aspect_loglog_thumb.png)

[Loglog aspect](https://matplotlib.org/stable/gallery/scales/aspect_loglog.html)

Loglog aspect

![](https://matplotlib.org/stable/_images/sphx_glr_log_demo_thumb.png)

[Log scale](https://matplotlib.org/stable/gallery/scales/log_demo.html)

Log scale

![](https://matplotlib.org/stable/_images/sphx_glr_symlog_demo_thumb.png)

[Symlog scale](https://matplotlib.org/stable/gallery/scales/symlog_demo.html)

Symlog scale

![](https://matplotlib.org/stable/_images/sphx_glr_scales3d_thumb.png)

[Scales on 3D (Log, Symlog, etc.)](https://matplotlib.org/stable/gallery/mplot3d/scales3d.html)

Scales on 3D (Log, Symlog, etc.)

![](https://matplotlib.org/stable/_images/sphx_glr_stock_prices_thumb.png)

[Stock prices over 32 years](https://matplotlib.org/stable/gallery/showcase/stock_prices.html)

Stock prices over 32 years

![](https://matplotlib.org/stable/_images/sphx_glr_axes_scales_thumb.png)

[Axis scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html)

Axis scales

![](https://matplotlib.org/stable/_images/sphx_glr_colormapnorms_thumb.png)

[Colormap normalization](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html)

Colormap normalization

On this page