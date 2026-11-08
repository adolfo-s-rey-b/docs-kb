[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.plotting.radviz.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.plotting.radviz.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.plotting.radviz.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.plotting.radviz.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.plotting.radviz.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.plotting.radviz.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.plotting.radviz.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.plotting.radviz.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.plotting.radviz.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.plotting.radviz.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.plotting.radviz.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.plotting.radviz.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.plotting.radviz.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.plotting.radviz.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.plotting.radviz[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.radviz.html#pandas-plotting-radviz "Link to this heading")

==================================================================================================================================================

pandas.plotting.radviz(_frame_, _class\_column_, _ax\=None_, _color\=None_, _colormap\=None_, _\*\*kwds_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_misc.py#L274-L360)
[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.radviz.html#pandas.plotting.radviz "Link to this definition")

Plot a multidimensional dataset in 2D.

Each Series in the DataFrame is represented as an evenly distributed slice on a circle. Each data point is rendered in the circle according to the value on each Series. Highly correlated Series in the DataFrame are placed closer on the unit circle.

RadViz allows you to project an N-dimensional data set into a 2D space where the influence of each dimension can be interpreted as a balance between the influence of all dimensions.

More info available at the [original article](https://doi.org/10.1145/331770.331775)
 describing RadViz.

Parameters:

**frame**DataFrame

Object holding the data.

**class\_column**str

Column name containing the name of the data point category.

**ax**[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.11.2)")
, optional

A plot instance to which to add the information.

**color**list\[str\] or tuple\[str\], optional

Assign a color to each category. Example: \[‘blue’, ‘green’\].

**colormap**str or [`matplotlib.colors.Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "(in Matplotlib v3.11.2)")
, default None

Colormap to select colors from. If string, load colormap with that name from matplotlib.

**\*\*kwds**

Options to pass to matplotlib scatter plotting method.

Returns:

[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.11.2)")

The Axes object from Matplotlib.

See also

`plotting.andrews_curves`

Plot clustering visualization.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "SepalLength": \[6.5, 7.7, 5.1, 5.8, 7.6, 5.0, 5.4, 4.6, 6.7, 4.6\],
...         "SepalWidth": \[3.0, 3.8, 3.8, 2.7, 3.0, 2.3, 3.0, 3.2, 3.3, 3.6\],
...         "PetalLength": \[5.5, 6.7, 1.9, 5.1, 6.6, 3.3, 4.5, 1.4, 5.7, 1.0\],
...         "PetalWidth": \[1.8, 2.2, 0.4, 1.9, 2.1, 1.0, 1.5, 0.2, 2.1, 0.2\],
...         "Category": \[\
...             "virginica",\
...             "virginica",\
...             "setosa",\
...             "virginica",\
...             "virginica",\
...             "versicolor",\
...             "versicolor",\
...             "setosa",\
...             "virginica",\
...             "setosa",\
...         \],
...     }
... )
\>>> pd.plotting.radviz(df, "Category")

Copy to clipboard

![../../_images/pandas-plotting-radviz-1.png](https://pandas.pydata.org/docs/_images/pandas-plotting-radviz-1.png)

On this page