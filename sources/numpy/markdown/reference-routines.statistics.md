[Skip to main content](https://numpy.org/doc/stable/reference/routines.statistics.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.statistics.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.statistics.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.statistics.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.statistics.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.statistics.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.statistics.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.statistics.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.statistics.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.statistics.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.statistics.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.statistics.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.statistics.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.statistics.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.statistics.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.statistics.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.statistics.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.statistics.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.statistics.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.statistics.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.statistics.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.statistics.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Statistics[#](https://numpy.org/doc/stable/reference/routines.statistics.html#statistics "Link to this heading")

=================================================================================================================

Order statistics[#](https://numpy.org/doc/stable/reference/routines.statistics.html#order-statistics "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")<br>(a\[, axis, out, keepdims\]) | Range of values (maximum - minimum) along an axis. |
| [`percentile`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "numpy.percentile")<br>(a, q\[, axis, out, ...\]) | Compute the q-th percentile of the data along the specified axis. |
| [`nanpercentile`](https://numpy.org/doc/stable/reference/generated/numpy.nanpercentile.html#numpy.nanpercentile "numpy.nanpercentile")<br>(a, q\[, axis, out, ...\]) | Compute the qth percentile of the data along the specified axis, while ignoring nan values. |
| [`quantile`](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy.quantile "numpy.quantile")<br>(a, q\[, axis, out, overwrite\_input, ...\]) | Compute the q-th quantile of the data along the specified axis. |
| [`nanquantile`](https://numpy.org/doc/stable/reference/generated/numpy.nanquantile.html#numpy.nanquantile "numpy.nanquantile")<br>(a, q\[, axis, out, ...\]) | Compute the qth quantile of the data along the specified axis, while ignoring nan values. |

Averages and variances[#](https://numpy.org/doc/stable/reference/routines.statistics.html#averages-and-variances "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`median`](https://numpy.org/doc/stable/reference/generated/numpy.median.html#numpy.median "numpy.median")<br>(a\[, axis, out, overwrite\_input, keepdims\]) | Compute the median along the specified axis. |
| [`average`](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")<br>(a\[, axis, weights, returned, keepdims\]) | Compute the weighted average along the specified axis. |
| [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")<br>(a\[, axis, dtype, out, keepdims, where\]) | Compute the arithmetic mean along the specified axis. |
| [`std`](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")<br>(a\[, axis, dtype, out, ddof, keepdims, ...\]) | Compute the standard deviation along the specified axis. |
| [`var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "numpy.var")<br>(a\[, axis, dtype, out, ddof, keepdims, ...\]) | Compute the variance along the specified axis. |
| [`nanmedian`](https://numpy.org/doc/stable/reference/generated/numpy.nanmedian.html#numpy.nanmedian "numpy.nanmedian")<br>(a\[, axis, out, overwrite\_input, ...\]) | Compute the median along the specified axis, while ignoring NaNs. |
| [`nanmean`](https://numpy.org/doc/stable/reference/generated/numpy.nanmean.html#numpy.nanmean "numpy.nanmean")<br>(a\[, axis, dtype, out, keepdims, where\]) | Compute the arithmetic mean along the specified axis, ignoring NaNs. |
| [`nanstd`](https://numpy.org/doc/stable/reference/generated/numpy.nanstd.html#numpy.nanstd "numpy.nanstd")<br>(a\[, axis, dtype, out, ddof, ...\]) | Compute the standard deviation along the specified axis, while ignoring NaNs. |
| [`nanvar`](https://numpy.org/doc/stable/reference/generated/numpy.nanvar.html#numpy.nanvar "numpy.nanvar")<br>(a\[, axis, dtype, out, ddof, ...\]) | Compute the variance along the specified axis, while ignoring NaNs. |

Correlating[#](https://numpy.org/doc/stable/reference/routines.statistics.html#correlating "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`corrcoef`](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")<br>(x\[, y, rowvar, dtype\]) | Return Pearson product-moment correlation coefficients. |
| [`correlate`](https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#numpy.correlate "numpy.correlate")<br>(a, v\[, mode\]) | Cross-correlation of two 1-dimensional sequences. |
| [`cov`](https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov "numpy.cov")<br>(m\[, y, rowvar, bias, ddof, fweights, ...\]) | Estimate a covariance matrix, given data and weights. |

Histograms[#](https://numpy.org/doc/stable/reference/routines.statistics.html#histograms "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")<br>(a\[, bins, range, density, weights\]) | Compute the histogram of a dataset. |
| [`histogram2d`](https://numpy.org/doc/stable/reference/generated/numpy.histogram2d.html#numpy.histogram2d "numpy.histogram2d")<br>(x, y\[, bins, range, density, ...\]) | Compute the bi-dimensional histogram of two data samples. |
| [`histogramdd`](https://numpy.org/doc/stable/reference/generated/numpy.histogramdd.html#numpy.histogramdd "numpy.histogramdd")<br>(sample\[, bins, range, density, ...\]) | Compute the multidimensional histogram of some data. |
| [`bincount`](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html#numpy.bincount "numpy.bincount")<br>(x, /\[, weights, minlength\]) | Count number of occurrences of each value in array of non-negative ints. |
| [`histogram_bin_edges`](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges "numpy.histogram_bin_edges")<br>(a\[, bins, range, weights\]) | Function to calculate only the edges of the bins used by the [`histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")<br> function. |
| [`digitize`](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html#numpy.digitize "numpy.digitize")<br>(x, bins\[, right\]) | Return the indices of the bins to which each value in input array belongs. |

On this page