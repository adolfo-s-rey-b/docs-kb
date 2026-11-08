[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html#main-content)

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
    

matplotlib.pyplot.yscale[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib-pyplot-yscale "Link to this heading")

=====================================================================================================================================================

matplotlib.pyplot.yscale(_value_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4620-L4622)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html#matplotlib.pyplot.yscale "Link to this definition")

Set the yaxis' scale.

Parameters:

**value**str or [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")

The axis scale type to apply. Valid string values are the names of scale classes ("linear", "log", "function",...). These may be the names of any of the [built-in scales](https://matplotlib.org/stable/api/scale_api.html#builtin-scales)
 or of any custom scales registered using [`matplotlib.scale.register_scale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.register_scale "matplotlib.scale.register_scale")
.

**\*\*kwargs**

If _value_ is a string, keywords are passed to the instantiation method of the respective class.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.set_yscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
.

Examples using `matplotlib.pyplot.yscale`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html#examples-using-matplotlib-pyplot-yscale "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_custom_scale_thumb.png)

[Custom scale](https://matplotlib.org/stable/gallery/scales/custom_scale.html)

Custom scale

![](https://matplotlib.org/stable/_images/sphx_glr_pyplot_thumb.png)

[Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)

Pyplot tutorial

On this page