[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.text_gradient.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.text_gradient.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.text\_gradient[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.text_gradient.html#pandas-io-formats-style-styler-text-gradient "Link to this heading")

=====================================================================================================================================================================================================================

Styler.text\_gradient(_cmap\='PuBu'_, _low\=0_, _high\=0_, _axis\=0_, _subset\=None_, _vmin\=None_, _vmax\=None_, _gmap\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L3279-L3425)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.text_gradient.html#pandas.io.formats.style.Styler.text_gradient "Link to this definition")

Color the text in a gradient style.

The text color is determined according to the data in each column, row or frame, or by a given gradient map. Requires matplotlib.

Parameters:

**cmap**str or colormap

Matplotlib colormap.

**low**float

Compress the color range at the low end. This is a multiple of the data range to extend below the minimum; good values usually in \[0, 1\], defaults to 0.

**high**float

Compress the color range at the high end. This is a multiple of the data range to extend above the maximum; good values usually in \[0, 1\], defaults to 0.

**axis**{0, 1, “index”, “columns”, None}, default 0

Apply to each column (`axis=0` or `'index'`), to each row (`axis=1` or `'columns'`), or to the entire DataFrame at once with `axis=None`.

**subset**label, array-like, IndexSlice, optional

A valid 2d input to DataFrame.loc\[<subset>\], or, in the case of a 1d input or single key, to DataFrame.loc\[:, <subset>\] where the columns are prioritised, to limit `data` to _before_ applying the function.

**vmin**float, optional

Minimum data value that corresponds to colormap minimum value. If not specified the minimum value of the data (or gmap) will be used.

**vmax**float, optional

Maximum data value that corresponds to colormap maximum value. If not specified the maximum value of the data (or gmap) will be used.

**gmap**array-like, optional

Gradient map for determining the text colors. If not supplied will use the underlying data from rows, columns or frame. If given as an ndarray or list-like must be an identical shape to the underlying data considering `axis` and `subset`. If given as DataFrame or Series must have same index and column labels considering `axis` and `subset`. If supplied, `vmin` and `vmax` should be given relative to this gradient map.

Returns:

Styler

Instance of class with background colored in gradient style.

See also

[`Styler.background_gradient`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.background_gradient.html#pandas.io.formats.style.Styler.background_gradient "pandas.io.formats.style.Styler.background_gradient")

Color the background in a gradient style.

Notes

When using `low` and `high` the range of the gradient, given by the data if `gmap` is not given or by `gmap`, is extended at the low end effectively by map.min - low \* map.range and at the high end by map.max + high \* map.range before the colors are normalized and determined.

If combining with `vmin` and `vmax` the map.min, map.max and map.range are replaced by values according to the values derived from `vmin` and `vmax`.

This method will preselect numeric columns and ignore non-numeric columns unless a `gmap` is supplied in which case no preselection occurs.

Examples

\>>> df \= pd.DataFrame(
...     columns\=\["City", "Temp (c)", "Rain (mm)", "Wind (m/s)"\],
...     data\=\[\
...         \["Stockholm", 21.6, 5.0, 3.2\],\
...         \["Oslo", 22.4, 13.3, 3.1\],\
...         \["Copenhagen", 24.5, 0.0, 6.7\],\
...     \],
... )

Copy to clipboard

Shading the values column-wise, with `axis=0`, preselecting numeric columns

\>>> df.style.text\_gradient(axis\=0)

Copy to clipboard

![../../_images/tg_ax0.png](https://pandas.pydata.org/docs/_images/tg_ax0.png)

Shading all values collectively using `axis=None`

\>>> df.style.text\_gradient(axis\=None)

Copy to clipboard

![../../_images/tg_axNone.png](https://pandas.pydata.org/docs/_images/tg_axNone.png)

Compress the color map from the both `low` and `high` ends

\>>> df.style.text\_gradient(axis\=None, low\=0.75, high\=1.0)

Copy to clipboard

![../../_images/tg_axNone_lowhigh.png](https://pandas.pydata.org/docs/_images/tg_axNone_lowhigh.png)

Manually setting `vmin` and `vmax` gradient thresholds

\>>> df.style.text\_gradient(axis\=None, vmin\=6.7, vmax\=21.6)

Copy to clipboard

![../../_images/tg_axNone_vminvmax.png](https://pandas.pydata.org/docs/_images/tg_axNone_vminvmax.png)

Setting a `gmap` and applying to all columns with another `cmap`

\>>> df.style.text\_gradient(axis\=0, gmap\=df\["Temp (c)"\], cmap\="YlOrRd")
...

Copy to clipboard

![../../_images/tg_gmap.png](https://pandas.pydata.org/docs/_images/tg_gmap.png)

Setting the gradient map for a dataframe (i.e. `axis=None`), we need to explicitly state `subset` to match the `gmap` shape

\>>> gmap \= np.array(\[\[1, 2, 3\], \[2, 3, 4\], \[3, 4, 5\]\])
\>>> df.style.text\_gradient(
...     axis\=None,
...     gmap\=gmap,
...     cmap\="YlOrRd",
...     subset\=\["Temp (c)", "Rain (mm)", "Wind (m/s)"\],
... )

Copy to clipboard

![../../_images/tg_axNone_gmap.png](https://pandas.pydata.org/docs/_images/tg_axNone_gmap.png)

On this page