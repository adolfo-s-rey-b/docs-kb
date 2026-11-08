[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.plotting.andrews_curves.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.plotting.andrews_curves.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.plotting.andrews_curves.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.plotting.andrews_curves.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.plotting.andrews_curves.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.plotting.andrews_curves.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.plotting.andrews_curves.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.plotting.andrews_curves.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.plotting.andrews_curves.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.plotting.andrews_curves.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.plotting.andrews_curves.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.plotting.andrews_curves.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.plotting.andrews_curves.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.plotting.andrews_curves.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.plotting.andrews\_curves[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.andrews_curves.html#pandas-plotting-andrews-curves "Link to this heading")

===========================================================================================================================================================================

pandas.plotting.andrews\_curves(_frame_, _class\_column_, _ax\=None_, _samples\=200_, _color\=None_, _colormap\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_misc.py#L363-L452)
[#](https://pandas.pydata.org/docs/reference/api/pandas.plotting.andrews_curves.html#pandas.plotting.andrews_curves "Link to this definition")

Generate a matplotlib plot for visualizing clusters of multivariate data.

Andrews curves have the functional form:

𝑓⁡(𝑡)\=𝑥1√2+𝑥2⁢sin⁡(𝑡)+𝑥3⁢cos⁡(𝑡)+𝑥4⁢sin⁡(2⁢𝑡)+𝑥5⁢cos⁡(2⁢𝑡)+⋯

Where 𝑥 coefficients correspond to the values of each dimension and 𝑡 is linearly spaced between −𝜋 and +𝜋. Each row of frame then corresponds to a single curve.

Parameters:

**frame**DataFrame

Data to be plotted, preferably normalized to (0.0, 1.0).

**class\_column**label

Name of the column containing class names.

**ax**axes object, default None

Axes to use.

**samples**int

Number of points to plot in each curve.

**color**str, list\[str\] or tuple\[str\], optional

Colors to use for the different classes. Colors can be strings or 3-element floating point RGB values.

**colormap**str or matplotlib colormap object, default None

Colormap to select colors from. If a string, load colormap with that name from matplotlib.

**\*\*kwargs**

Options to pass to matplotlib plotting method.

Returns:

[`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.11.2)")

The matplotlib Axes object with the plot.

See also

`plotting.parallel_coordinates`

Plot parallel coordinates chart.

`DataFrame.plot`

Make plots of Series or DataFrame.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "SepalLength": \[6.5, 7.7, 5.1, 5.8, 7.6, 5.0, 5.4, 4.6, 6.7, 4.6\],
...         "SepalWidth": \[3.0, 3.8, 3.8, 2.7, 3.0, 2.3, 3.0, 3.2, 3.3, 3.6\],
...         "PetalLength": \[5.5, 6.7, 1.9, 5.1, 6.6, 3.3, 4.5, 1.4, 5.7, 1.0\],
...         "PetalWidth": \[1.8, 2.2, 0.4, 1.9, 2.1, 1.0, 1.5, 0.2, 2.1, 0.2\],
...         "Name": \[\
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
\>>> pd.plotting.andrews\_curves(df, "Name")

Copy to clipboard

![../../_images/pandas-plotting-andrews_curves-1.png](https://pandas.pydata.org/docs/_images/pandas-plotting-andrews_curves-1.png)

On this page