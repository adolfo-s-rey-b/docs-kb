[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hexbin.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.plot.hexbin.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hexbin.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.plot.hexbin.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.plot.hexbin.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.plot.hexbin.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.plot.hexbin.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.plot.hexbin.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.plot.hexbin.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.plot.hexbin.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.plot.hexbin.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.plot.hexbin.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.plot.hexbin.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.plot.hexbin.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.plot.hexbin[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hexbin.html#pandas-dataframe-plot-hexbin "Link to this heading")

====================================================================================================================================================================

DataFrame.plot.hexbin(_x_, _y_, _C\=None_, _reduce\_C\_function\=None_, _gridsize\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_core.py#L2342-L2449)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hexbin.html#pandas.DataFrame.plot.hexbin "Link to this definition")

Make a hexagonal binning plot.

Generate a hexagonal binning plot of x versus y. If C is None (the default), this is a histogram of the number of occurrences of the observations at `(x[i], y[i])`.

If C is specified, specifies values at given coordinates `(x[i], y[i])`. These values are accumulated for each hexagonal bin and then reduced according to reduce\_C\_function, having as default the NumPy’s mean function (`numpy.mean()`). (If C is specified, it must also be a 1-D sequence of the same length as x and y, or a column label.)

Parameters:

**x**int or str

The column label or position for x points.

**y**int or str

The column label or position for y points.

**C**int or str, optional

The column label or position for the value of (x, y) point.

**reduce\_C\_function**callable, default np.mean

Function of one argument that reduces all the values in a bin to a single number (e.g. np.mean, np.max, np.sum, np.std).

**gridsize**int or tuple of (int, int), default 100

The number of hexagons in the x-direction. The corresponding number of hexagons in the y-direction is chosen in a way that the hexagons are approximately regular. Alternatively, gridsize can be a tuple with two elements specifying the number of hexagons in the x-direction and the y-direction. The hexagons tile only the extent of the data, so for a fixed gridsize their apparent size varies with the range of the data and the axis limits. To control the area covered by the hexagons, pass matplotlib’s `extent` keyword via `**kwargs`.

**\*\*kwargs**

Additional keyword arguments, such as `ax`, `figsize`, `title` and `grid`, are documented in [`DataFrame.plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")
.

Returns:

matplotlib.axes.Axes or numpy.ndarray of them

A one-element ndarray is returned when `subplots=True`.

See also

[`DataFrame.plot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")

Make plots of a DataFrame.

[`matplotlib.pyplot.hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hexbin.html#matplotlib.pyplot.hexbin "(in Matplotlib v3.11.2)")

Hexagonal binning plot using matplotlib, the matplotlib function that is used under the hood.

Examples

The following examples are generated with random data from a normal distribution.

\>>> n \= 10000
\>>> rng \= np.random.default\_rng(42)
\>>> df \= pd.DataFrame(
...     {"x": rng.standard\_normal(n), "y": rng.standard\_normal(n)}
... )
\>>> ax \= df.plot.hexbin(x\="x", y\="y", gridsize\=20)

Copy to clipboard

![../../_images/pandas-DataFrame-plot-hexbin-1.png](https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-hexbin-1.png)

The next example uses C and np.sum as reduce\_C\_function. Note that ‘observations’ values ranges from 1 to 5 but the result plot shows values up to more than 25. This is because of the reduce\_C\_function.

\>>> n \= 500
\>>> rng \= np.random.default\_rng(42)
\>>> df \= pd.DataFrame(
...     {
...         "coord\_x": rng.uniform(\-3, 3, size\=n),
...         "coord\_y": rng.uniform(30, 50, size\=n),
...         "observations": rng.integers(1, 5, size\=n),
...     }
... )
\>>> ax \= df.plot.hexbin(
...     x\="coord\_x",
...     y\="coord\_y",
...     C\="observations",
...     reduce\_C\_function\=np.sum,
...     gridsize\=10,
...     cmap\="viridis",
... )

Copy to clipboard

![../../_images/pandas-DataFrame-plot-hexbin-2.png](https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-hexbin-2.png)

On this page