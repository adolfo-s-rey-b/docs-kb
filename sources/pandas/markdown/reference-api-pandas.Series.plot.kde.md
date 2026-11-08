[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.kde.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.plot.kde.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.kde.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.plot.kde.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.plot.kde.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.plot.kde.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.plot.kde.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.plot.kde.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.plot.kde.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.plot.kde.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.plot.kde.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.plot.kde.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.plot.kde.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.plot.kde.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.plot.kde[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.kde.html#pandas-series-plot-kde "Link to this heading")

==================================================================================================================================================

Series.plot.kde(_bw\_method\=None_, _ind\=None_, _weights\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/plotting/_core.py#L1968-L2092)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.kde.html#pandas.Series.plot.kde "Link to this definition")

Make a Kernel Density Estimate plot using Gaussian kernels.

In statistics, [kernel density estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation)
 (KDE) is a non-parametric way to estimate the probability density function (PDF) of a random variable. This function uses Gaussian kernels and includes automatic bandwidth determination.

Parameters:

**bw\_method**str, scalar or callable, optional

The method used to calculate the estimator bandwidth. This can be ‘scott’, ‘silverman’, a scalar constant or a callable. If None (default), ‘scott’ is used. See `scipy.stats.gaussian_kde` for more information.

**ind**NumPy array or int, optional

Evaluation points for the estimated PDF. If None (default), 1000 equally spaced points are used. If ind is a NumPy array, the KDE is evaluated at the points passed. If ind is an integer, ind number of equally spaced points are used.

**weights**NumPy array, optional

Weights of datapoints. This must be the same shape as datapoints. If None (default), the samples are assumed to be equally weighted.

**\*\*kwargs**

Additional keyword arguments, such as `ax`, `figsize`, `title` and `legend`, are documented in [`DataFrame.plot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")
.

Returns:

matplotlib.axes.Axes or numpy.ndarray of them

An ndarray of [`matplotlib.axes.Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "(in Matplotlib v3.11.2)")
 is returned when `subplots=True`.

See also

[`DataFrame.plot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")

Make plots of a DataFrame.

`scipy.stats.gaussian_kde`

Representation of a kernel-density estimate using Gaussian kernels. This is the function used internally to estimate the PDF.

Examples

Given a Series of points randomly sampled from an unknown distribution, estimate its PDF using KDE with automatic bandwidth determination and plot the results, evaluating them at 1000 equally spaced points (default):

\>>> s \= pd.Series(\[1, 2, 2.5, 3, 3.5, 4, 5\])
\>>> ax \= s.plot.kde()

Copy to clipboard

![../../_images/pandas-Series-plot-kde-1.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-kde-1.png)

A scalar bandwidth can be specified. Using a small bandwidth value can lead to over-fitting, while using a large bandwidth value may result in under-fitting:

\>>> ax \= s.plot.kde(bw\_method\=0.3)

Copy to clipboard

![../../_images/pandas-Series-plot-kde-2.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-kde-2.png)

\>>> ax \= s.plot.kde(bw\_method\=3)

Copy to clipboard

![../../_images/pandas-Series-plot-kde-3.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-kde-3.png)

Finally, the ind parameter determines the evaluation points for the plot of the estimated PDF:

\>>> ax \= s.plot.kde(ind\=\[1, 2, 3, 4, 5\])

Copy to clipboard

![../../_images/pandas-Series-plot-kde-4.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-kde-4.png)

For DataFrame, it works in the same way:

\>>> df \= pd.DataFrame(
...     {
...         "x": \[1, 2, 2.5, 3, 3.5, 4, 5\],
...         "y": \[4, 4, 4.5, 5, 5.5, 6, 6\],
...     }
... )
\>>> ax \= df.plot.kde()

Copy to clipboard

![../../_images/pandas-Series-plot-kde-5.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-kde-5.png)

A scalar bandwidth can be specified. Using a small bandwidth value can lead to over-fitting, while using a large bandwidth value may result in under-fitting:

\>>> ax \= df.plot.kde(bw\_method\=0.3)

Copy to clipboard

![../../_images/pandas-Series-plot-kde-6.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-kde-6.png)

\>>> ax \= df.plot.kde(bw\_method\=3)

Copy to clipboard

![../../_images/pandas-Series-plot-kde-7.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-kde-7.png)

Finally, the ind parameter determines the evaluation points for the plot of the estimated PDF:

\>>> ax \= df.plot.kde(ind\=\[1, 2, 3, 4, 5, 6\])

Copy to clipboard

![../../_images/pandas-Series-plot-kde-8.png](https://pandas.pydata.org/docs/_images/pandas-Series-plot-kde-8.png)

On this page