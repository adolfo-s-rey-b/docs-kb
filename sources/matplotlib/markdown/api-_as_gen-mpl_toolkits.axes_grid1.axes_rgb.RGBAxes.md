[Skip to main content](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.RGBAxes.html#main-content)

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
    

mpl\_toolkits.axes\_grid1.axes\_rgb.RGBAxes[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.RGBAxes.html#mpl-toolkits-axes-grid1-axes-rgb-rgbaxes "Link to this heading")

========================================================================================================================================================================================================

class mpl\_toolkits.axes\_grid1.axes\_rgb.RGBAxes(_\*args_, _pad\=0_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_rgb.py#L62-L157)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.RGBAxes.html#mpl_toolkits.axes_grid1.axes_rgb.RGBAxes "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

4-panel [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 (RGB, R, G, B).

Layout:

┌───────────────┬─────┐
│               │  R  │
│               ├─────┤
│      RGB      │  G  │
│               ├─────┤
│               │  B  │
└───────────────┴─────┘

Subclasses can override the `_defaultAxesClass` attribute. By default RGBAxes uses [`mpl_axes.Axes`](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.mpl_axes.Axes.html#mpl_toolkits.axes_grid1.mpl_axes.Axes "mpl_toolkits.axes_grid1.mpl_axes.Axes")
.

Attributes:

**RGB**`_defaultAxesClass`

The Axes object for the three-channel [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
.

**R**`_defaultAxesClass`

The Axes object for the red channel [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
.

**G**`_defaultAxesClass`

The Axes object for the green channel [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
.

**B**`_defaultAxesClass`

The Axes object for the blue channel [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
.

Parameters:

**pad**float, default: 0

Fraction of the Axes height to put as padding.

**axes\_class**[`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")

Axes class to use. If not provided, `_defaultAxesClass` is used.

**\*args**

Forwarded to _axes\_class_ init for the RGB Axes

**\*\*kwargs**

Forwarded to _axes\_class_ init for the RGB, R, G, and B Axes

imshow\_rgb(_r_, _g_, _b_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/mpl_toolkits/axes_grid1/axes_rgb.py#L125-L157)
[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.RGBAxes.html#mpl_toolkits.axes_grid1.axes_rgb.RGBAxes.imshow_rgb "Link to this definition")

Create the four images {rgb, r, g, b}.

Parameters:

**r, g, b**array-like

The red, green, and blue arrays.

**\*\*kwargs**

Forwarded to [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 calls for the four images.

Returns:

**rgb**[`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")

**r**[`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")

**g**[`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")

**b**[`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")

Examples using `mpl_toolkits.axes_grid1.axes_rgb.RGBAxes`[#](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axes_grid1.axes_rgb.RGBAxes.html#examples-using-mpl-toolkits-axes-grid1-axes-rgb-rgbaxes "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_demo_axes_rgb_thumb.png)

[Show RGB channels using RGBAxes](https://matplotlib.org/stable/gallery/axes_grid1/demo_axes_rgb.html)

Show RGB channels using RGBAxes

On this page