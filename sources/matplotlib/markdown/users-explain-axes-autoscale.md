[Skip to main content](https://matplotlib.org/stable/users/explain/axes/autoscale.html#main-content)

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
    

Note

[Go to the end](https://matplotlib.org/stable/users/explain/axes/autoscale.html#sphx-glr-download-users-explain-axes-autoscale-py)
 to download the full example code.

Axis autoscaling[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#axis-autoscaling "Link to this heading")

=============================================================================================================================

Basic concept[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#basic-concept "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Autoscaling ensures that data is visible within the Axes by automatically adjusting the axis limits. When you plot data, Matplotlib's autoscaling mechanism updates the axis limits accordingly.

import matplotlib.pyplot as plt
import numpy as np

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-6, 6, 201)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sinc](https://numpy.org/doc/stable/reference/generated/numpy.sinc.html#numpy.sinc "numpy.sinc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

![autoscale](https://matplotlib.org/stable/_images/sphx_glr_autoscale_001_2_00x.png)

Margins[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#margins "Link to this heading")

-----------------------------------------------------------------------------------------------------------

To ensure that the data is not at the very edge of the plot, Matplotlib adds a margin around the data limits. Note that the _x_ data range in the above plot is \[-6, 6\], but the x-axis limits are slightly wider due to the margin.

The default margin is 5%, defined via

*   `[rcParams["axes.xmargin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.xmargin#rcparam-axes-xmargin) ` (default: `0.05`)
    
*   `[rcParams["axes.ymargin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.ymargin#rcparam-axes-ymargin) ` (default: `0.05`)
    
*   `[rcParams["axes.zmargin"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.zmargin#rcparam-axes-zmargin) ` (default: `0.05`)
    

print([ax.get\_xmargin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xmargin.html#matplotlib.axes.Axes.get_xmargin "matplotlib.axes.Axes.get_xmargin")
(), [ax.get\_ymargin](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_ymargin.html#matplotlib.axes.Axes.get_ymargin "matplotlib.axes.Axes.get_ymargin")
())

0.05 0.05

The margin size can be overridden to make them smaller or larger using [`margins`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
(0.2, 0.2)

![autoscale](https://matplotlib.org/stable/_images/sphx_glr_autoscale_002_2_00x.png)

In general, margins can be in the range (-0.5, ∞), where negative margins set the axes limits to a subrange of the data range, i.e. they clip data. Using a single number for margins affects both axes, a single margin can be customized using keyword arguments `x` or `y`, but positional and keyword interface cannot be combined.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=-0.2)

![autoscale](https://matplotlib.org/stable/_images/sphx_glr_autoscale_003_2_00x.png)

Sticky edges[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#sticky-edges "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

There are plot elements ([`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
s) that are usually used without margins. For example, false-color images (e.g. created with [`Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
) are not considered in the margins calculation.

[xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[zz](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sinc](https://numpy.org/doc/stable/reference/generated/numpy.sinc.html#numpy.sinc "numpy.sinc")
([np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(([xx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 1)\*\*2 + ([yy](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 1)\*\*2))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(12, 8))
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].imshow([zz](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].set\_title("default margins")
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].imshow([zz](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].margins(0.2)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].set\_title("margins(0.2)")

![default margins, margins(0.2)](https://matplotlib.org/stable/_images/sphx_glr_autoscale_004_2_00x.png)

This override of margins is determined by "sticky edges", a property of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 class that can suppress adding margins to axis limits. The effect of sticky edges can be disabled on an Axes by changing [`use_sticky_edges`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.use_sticky_edges.html#matplotlib.axes.Axes.use_sticky_edges "matplotlib.axes.Axes.use_sticky_edges")
. Artists have a property [`Artist.sticky_edges`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.sticky_edges.html#matplotlib.artist.Artist.sticky_edges "matplotlib.artist.Artist.sticky_edges")
, and the values of sticky edges can be changed by writing to `Artist.sticky_edges.x` or `Artist.sticky_edges.y`.

The following example shows how overriding works and when it is needed.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=3, figsize\=(16, 10))
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].imshow([zz](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].margins(0.2)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].set\_title("default use\_sticky\_edges\\nmargins(0.2)")
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].imshow([zz](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].margins(0.2)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].use\_sticky\_edges \= False
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].set\_title("use\_sticky\_edges=False\\nmargins(0.2)")
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[2\].imshow([zz](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[2\].margins(\-0.2)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[2\].set\_title("default use\_sticky\_edges\\nmargins(-0.2)")

![default use_sticky_edges margins(0.2), use_sticky_edges=False margins(0.2), default use_sticky_edges margins(-0.2)](https://matplotlib.org/stable/_images/sphx_glr_autoscale_005_2_00x.png)

We can see that setting `use_sticky_edges` to _False_ renders the image with requested margins.

While sticky edges don't increase the axis limits through extra margins, negative margins are still taken into account. This can be seen in the reduced limits of the third image.

Controlling autoscale[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#controlling-autoscale "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

By default, the limits are recalculated every time you add a new curve to the plot:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(12, 8))
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].set\_title("Single curve")
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* 2.0, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].set\_title("Two curves")

![Single curve, Two curves](https://matplotlib.org/stable/_images/sphx_glr_autoscale_006_2_00x.png)

If you don't want automatic updates of the axis limits, either deactivate autoscaling with [`autoscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html#matplotlib.axes.Axes.autoscale "matplotlib.axes.Axes.autoscale")
 or set the limits manually with [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
 / [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
.

Let's say that we want to see only a part of the data in greater detail. Setting the `xlim` persists even if we add more curves to the data. Calling [`Axes.autoscale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html#matplotlib.axes.Axes.autoscale "matplotlib.axes.Axes.autoscale")
 will re-enable the autoscaling and recalculate the limits to fit all the data.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(12, 8))
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].set\_xlim(left\=-1, right\=1)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* 0.5, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].set\_title("set\_xlim(left=-1, right=1)\\n")
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].set\_xlim(left\=-1, right\=1)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].plot([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* 0.5, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].autoscale()
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].set\_title("set\_xlim(left=-1, right=1)\\nautoscale()")

![set_xlim(left=-1, right=1) , set_xlim(left=-1, right=1) autoscale()](https://matplotlib.org/stable/_images/sphx_glr_autoscale_007_2_00x.png)

We can check that the first plot has autoscale disabled and that the second plot has it enabled again by using [`Axes.get_autoscale_on()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_autoscale_on.html#matplotlib.axes.Axes.get_autoscale_on "matplotlib.axes.Axes.get_autoscale_on")
:

print([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].get\_autoscale\_on())  \# False means disabled
print([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].get\_autoscale\_on())  \# True means enabled -> recalculated

False
True

Arguments of the autoscale function give us precise control over the process of autoscaling. A combination of arguments `enable`, and `axis` sets the autoscaling feature for the selected axis (or both). The argument `tight` sets the margin of the selected axis to zero. To preserve settings of either `enable` or `tight` you can set the opposite one to _None_, that way it should not be modified. However, setting `enable` to _None_ and tight to _True_ affects both axes regardless of the `axis` argument.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
(0.2, 0.2)
[ax.autoscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale.html#matplotlib.axes.Axes.autoscale "matplotlib.axes.Axes.autoscale")
(enable\=None, axis\="x", tight\=True)

print([ax.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
())

![autoscale](https://matplotlib.org/stable/_images/sphx_glr_autoscale_008_2_00x.png)

(0, 0)

Technical background[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#technical-background "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

This section explains the internal pipeline that runs when autoscaling computes axis limits from data. Understanding the mechanics helps when you encounter surprising behaviour or need to update limits manually.

### Data limits and view limits[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#data-limits-and-view-limits "Link to this heading")

Matplotlib maintains two sets of limits:

*   **Data limits** ([`Axes.dataLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.dataLim.html#matplotlib.axes.Axes.dataLim "matplotlib.axes.Axes.dataLim")
    ): the tight bounding box of the raw data.
    
*   **View limits** ([`Axes.viewLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.viewLim.html#matplotlib.axes.Axes.viewLim "matplotlib.axes.Axes.viewLim")
    ): the displayed axis limits. By default, computed from the data limits through the autoscaling mechanism outlined below, but they can be set independently. View limits can alternatively be set explicitly through [`set_xlim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
     / [`set_ylim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
    , which also disables autoscaling so that the set limits remain fixed.
    

The following shows the input and output of this process — `dataLim` holds the raw data bounds, `viewLim` the final displayed axis limits.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-6, 6, 201)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
print(f"dataLim x: ({[ax.dataLim.x0](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.x0 "matplotlib.transforms.Bbox.x0")
:.3f}, {[ax.dataLim.x1](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.x1 "matplotlib.transforms.Bbox.x1")
:.3f})")
print(f"dataLim y: ({[ax.dataLim.y0](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.y0 "matplotlib.transforms.Bbox.y0")
:.3f}, {[ax.dataLim.y1](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.y1 "matplotlib.transforms.Bbox.y1")
:.3f})")
print(f"viewLim x: ({[ax.viewLim.x0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.viewLim.html#matplotlib.axes.Axes.viewLim "matplotlib.axes.Axes.viewLim")
:.3f}, {[ax.viewLim.x1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.viewLim.html#matplotlib.axes.Axes.viewLim "matplotlib.axes.Axes.viewLim")
:.3f})")
print(f"viewLim y: ({[ax.viewLim.y0](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.viewLim.html#matplotlib.axes.Axes.viewLim "matplotlib.axes.Axes.viewLim")
:.3f}, {[ax.viewLim.y1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.viewLim.html#matplotlib.axes.Axes.viewLim "matplotlib.axes.Axes.viewLim")
:.3f})")

![autoscale](https://matplotlib.org/stable/_images/sphx_glr_autoscale_009_2_00x.png)

dataLim x: (-6.000, 6.000)
dataLim y: (-1.000, 1.000)
viewLim x: (-6.600, 6.600)
viewLim y: (-1.100, 1.100)

The x data range is \[-6, 6\] and the default 5% margin adds roughly 0.6 on each side, widening the view to about \[-6.6, 6.6\]. The same applies to the y axis.

### Update logic[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#update-logic "Link to this heading")

Data and view limit updates are handled as separate stages.

**Data limits**: When an artist is added to an Axes through one of the plotting methods, the data limits are updated through [`Axes.update_datalim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.update_datalim.html#matplotlib.axes.Axes.update_datalim "matplotlib.axes.Axes.update_datalim")
 to include the new data. This only ever increases the data limits. It is also possible to update [`Axes.dataLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.dataLim.html#matplotlib.axes.Axes.dataLim "matplotlib.axes.Axes.dataLim")
 manually, but this is not common. Removal of an artist or change of its data does not trigger any update of the data limits, so they can become out of date. In such cases, it is necessary to explicitly recompute the data limit through [`Axes.relim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.relim.html#matplotlib.axes.Axes.relim "matplotlib.axes.Axes.relim")
.

**View limits**: When autoscaling is enabled, the view limits are automatically computed from the data limit. This update is lazy and only triggered when the view limits are queried or drawn, so that they don't have to be recomputed for every added artist. This is transparent to the user. Explicit changes of the data limits through [`Axes.dataLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.dataLim.html#matplotlib.axes.Axes.dataLim "matplotlib.axes.Axes.dataLim")
 or [`Axes.relim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.relim.html#matplotlib.axes.Axes.relim "matplotlib.axes.Axes.relim")
 do not trigger an update of the view limits, so they can also become out of date. In such cases, it is necessary to explicitly recompute the view limits through [`Axes.autoscale_view`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
.

### View limit calculation[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#view-limit-calculation "Link to this heading")

Given the data limits, the view limits are derived through these steps:

*   scale domain clamping
    
*   margin expansion
    
*   sticky edge clamping
    
*   optional limit rounding
    

### Scale domain clamping[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#scale-domain-clamping "Link to this heading")

Before margins are applied, the data limits are clipped to the valid domain of the axis scale. This matters for scales like log (positive values only) and logit (values strictly between 0 and 1): if a bound lies outside the domain, it is replaced with a value at the domain boundary.

For this purpose, [`Axes.dataLim`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.dataLim.html#matplotlib.axes.Axes.dataLim "matplotlib.axes.Axes.dataLim")
 tracks not just the ordinary min/max of the data but also `minpos` — the smallest strictly positive value seen. A log-scale lower bound of zero or less is replaced with `minpos` rather than the actual minimum, because only positive values can be displayed.

For a logit scale, the upper bound is approximated as `1 - minpos`, since the largest data value below 1 is not tracked separately. This means the autoscaled upper limit may include slightly more headroom than necessary when the data maximum is well below 1.

### Margin expansion[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#margin-expansion "Link to this heading")

The first step is to apply the margins, i.e. widen the view limits beyond the data limits so that data is not at the very edge of the plot. Margins are specified as a fraction of the data span in screen coordinates so that the data-free border area always has the same visual size, irrespective of data ranges or axis scales. The margin is applied symmetrically to both sides of the data limits, so the view is expanded equally in both directions.

This is illustrated in the following example, where the data limits and axis scales are different, but the visual margin is the same in both cases.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(9, 4))
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("Margins are visually constant, "
             "even with different data limits and axis scales")

[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 10\], \[0, 1\])
[ax1.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
(0.2)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(1, 20)
[ax2.semilogy](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogy.html#matplotlib.axes.Axes.semilogy "matplotlib.axes.Axes.semilogy")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[ax2.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
(0.2)

![Margins are visually constant, even with different data limits and axis scales](https://matplotlib.org/stable/_images/sphx_glr_autoscale_010_2_00x.png)

### Sticky edges clamping[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#sticky-edges-clamping "Link to this heading")

Sticky edges are axis values at which margin expansion is clamped. After computing the margin-expanded limits, if an expanded limit would extend beyond a sticky edge, it is pulled back to that edge instead.

Artists register sticky edges to prevent blank margins at natural data boundaries. [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
, for example, registers sticky edges at its four pixel boundaries, which is why images fill the Axes by default without any surrounding margin (as shown in the [Sticky edges](https://matplotlib.org/stable/users/explain/axes/autoscale.html#autoscale-sticky-edges)
 section above). Sticky edges only suppress _outward expansion past the data boundary_ — they never shrink limits into the data, and negative margins are not affected. Setting `Axes.use_sticky_edges = False` disables sticky edge clamping on that Axes.

### Limit rounding[#](https://matplotlib.org/stable/users/explain/axes/autoscale.html#limit-rounding "Link to this heading")

As a final step, the view limits can optionally be expanded outward to the nearest "nice" tick position, so that the axis edges coincide with tick marks. This is disabled by default, but can be turned on with the "round\_numbers" mode of `[rcParams["axes.autolimit_mode"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=axes.autolimit_mode#rcparam-axes-autolimit-mode) ` (default: `'data'`):

*   `'data'` (default): keep the limits at the margin-expanded values.
    
*   `'round_numbers'`: expand the limits outward to the nearest "nice" tick position, so the axis edges coincide with tick marks.
    

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(10, 4))
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0.3, 4.7\], \[0.3, 4.7\])
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("autolimit\_mode='data' (default)")
with [plt.rc\_context](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc_context.html#matplotlib.pyplot.rc_context "matplotlib.pyplot.rc_context")
({'axes.autolimit\_mode': 'round\_numbers'}):
    [ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0.3, 4.7\], \[0.3, 4.7\])
    [ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("autolimit\_mode='round\_numbers'")
    [ax2.autoscale\_view](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.autoscale_view.html#matplotlib.axes.Axes.autoscale_view "matplotlib.axes.Axes.autoscale_view")
()  \# force autoscale while round\_numbers is active

![autolimit_mode='data' (default), autolimit_mode='round_numbers'](https://matplotlib.org/stable/_images/sphx_glr_autoscale_011_2_00x.png)

**Total running time of the script:** (0 minutes 10.169 seconds)

[`Download Jupyter notebook: autoscale.ipynb`](https://matplotlib.org/stable/_downloads/a63f0ce83ad0b644d528e3b40b8614df/autoscale.ipynb)

[`Download Python source code: autoscale.py`](https://matplotlib.org/stable/_downloads/e864ab41236053d6086728793d17eb75/autoscale.py)

[`Download zipped: autoscale.zip`](https://matplotlib.org/stable/_downloads/8825ced79ce887e9d5c427acc997c875/autoscale.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page