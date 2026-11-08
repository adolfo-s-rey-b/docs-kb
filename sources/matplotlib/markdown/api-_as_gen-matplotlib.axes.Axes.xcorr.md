[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xcorr.html#main-content)

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
    

matplotlib.axes.Axes.xcorr[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xcorr.html#matplotlib-axes-axes-xcorr "Link to this heading")

===========================================================================================================================================================

Axes.xcorr(_x_, _y_, _\*_, _normed\=True_, _detrend\=<function detrend\_none>_, _usevlines\=True_, _maxlags\=10_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/axes/_axes.py#L2023-L2133)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xcorr.html#matplotlib.axes.Axes.xcorr "Link to this definition")

Plot the cross correlation between _x_ and _y_.

The correlation with lag k is defined as \\(\\sum\_n x\[n+k\] \\cdot y^\*\[n\]\\), where \\(y^\*\\) is the complex conjugate of \\(y\\).

Parameters:

**x, y**array-like of length n

Neither _x_ nor _y_ are run through Matplotlib's unit conversion, so these should be unit-less arrays.

**detrend**callable, default: [`mlab.detrend_none`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_none "matplotlib.mlab.detrend_none")
 (no detrending)

A detrending function applied to _x_ and _y_. It must have the signature

detrend(x: np.ndarray) \-> np.ndarray

**normed**bool, default: True

If `True`, input vectors are normalised to unit length.

**usevlines**bool, default: True

Determines the plot style.

If `True`, vertical lines are plotted from 0 to the xcorr value using [`Axes.vlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib.axes.Axes.vlines "matplotlib.axes.Axes.vlines")
. Additionally, a horizontal line is plotted at y=0 using [`Axes.axhline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
.

If `False`, markers are plotted at the xcorr values using [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
.

**maxlags**int, default: 10

Number of lags to show. If None, will return all `2 * len(x) - 1` lags.

Returns:

**lags**array (length `2*maxlags+1`)

The lag vector.

**c**array (length `2*maxlags+1`)

The auto correlation vector.

**line**[`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
 or [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")

[`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 added to the Axes of the correlation:

*   [`LineCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection "matplotlib.collections.LineCollection")
     if _usevlines_ is True.
    
*   [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
     if _usevlines_ is False.
    

**b**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 or None

Horizontal line at 0 if _usevlines_ is True None _usevlines_ is False.

Other Parameters:

**linestyle**[`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 property, optional

The linestyle for plotting the data points. Only used if _usevlines_ is `False`.

**marker**str, default: 'o'

The marker for plotting the data points. Only used if _usevlines_ is `False`.

**data**indexable object, optional

If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:

_x_, _y_

**\*\*kwargs**

Additional parameters are passed to [`Axes.vlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib.axes.Axes.vlines "matplotlib.axes.Axes.vlines")
 and [`Axes.axhline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
 if _usevlines_ is `True`; otherwise they are passed to [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
.

Notes

The cross correlation is performed with [`numpy.correlate`](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#numpy.correlate "(in NumPy v2.5)")
 with `mode = "full"`.

Examples using `matplotlib.axes.Axes.xcorr`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xcorr.html#examples-using-matplotlib-axes-axes-xcorr "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_xcorr_acorr_demo_thumb.png)

[Cross- and auto-correlation](https://matplotlib.org/stable/gallery/statistics/xcorr_acorr_demo.html)

Cross- and auto-correlation

On this page