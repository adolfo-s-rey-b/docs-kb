[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.histogram_bin_edges.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.histogram_bin_edges.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.histogram_bin_edges.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.histogram_bin_edges.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.histogram_bin_edges.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.histogram_bin_edges.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.histogram_bin_edges.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.histogram_bin_edges.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.histogram_bin_edges.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.histogram_bin_edges.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.histogram_bin_edges.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.histogram_bin_edges.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.histogram_bin_edges.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.histogram_bin_edges.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.histogram_bin_edges.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.histogram_bin_edges.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.histogram_bin_edges.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.histogram_bin_edges.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.histogram_bin_edges.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.histogram_bin_edges.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.histogram\_bin\_edges[#](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy-histogram-bin-edges "Link to this heading")

=================================================================================================================================================================

numpy.histogram\_bin\_edges(_a_, _bins\=10_, _range\=None_, _weights\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_histograms_impl.py#L473-L677)
[#](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges "Link to this definition")

Function to calculate only the edges of the bins used by the [`histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")
 function.

Parameters:

**a**array\_like

Input data. The histogram is computed over the flattened array.

**bins**int or sequence of scalars or str, optional

If _bins_ is an int, it defines the number of equal-width bins in the given range (10, by default). If _bins_ is a sequence, it defines the bin edges, including the rightmost edge, allowing for non-uniform bin widths.

If _bins_ is a string from the list below, [`histogram_bin_edges`](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges "numpy.histogram_bin_edges")
 will use the method chosen to calculate the optimal bin width and consequently the number of bins (see the Notes section for more detail on the estimators) from the data that falls within the requested range. While the bin width will be optimal for the actual data in the range, the number of bins will be computed to fill the entire range, including the empty portions. For visualisation, using the ‘auto’ option is suggested. Weighted data is not supported for automated bin size selection.

‘auto’

Minimum bin width between the ‘sturges’ and ‘fd’ estimators. Provides good all-around performance.

‘fd’ (Freedman Diaconis Estimator)

Robust (resilient to outliers) estimator that takes into account data variability and data size.

‘doane’

An improved version of Sturges’ estimator that works better with non-normal datasets.

‘scott’

Less robust estimator that takes into account data variability and data size.

‘stone’

Estimator based on leave-one-out cross-validation estimate of the integrated squared error. Can be regarded as a generalization of Scott’s rule.

‘rice’

Estimator does not take variability into account, only data size. Commonly overestimates number of bins required.

‘sturges’

R’s default method, only accounts for data size. Only optimal for gaussian data and underestimates number of bins for large non-gaussian datasets.

‘sqrt’

Square root (of data size) estimator, used by Excel and other programs for its speed and simplicity.

**range**(float, float), optional

The lower and upper range of the bins. If not provided, range is simply `(a.min(), a.max())`. Values outside the range are ignored. The first element of the range must be less than or equal to the second. _range_ affects the automatic bin computation as well. While bin width is computed to be optimal based on the actual data within _range_, the bin count will fill the entire range including portions containing no data.

**weights**array\_like, optional

An array of weights, of the same shape as _a_. Each value in _a_ only contributes its associated weight towards the bin count (instead of 1). This is currently not used by any of the bin estimators, but may be in the future.

Returns:

**bin\_edges**array of dtype float

The edges to pass into [`histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")

See also

[`histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")

Notes

The methods to estimate the optimal number of bins are well founded in literature, and are inspired by the choices R provides for histogram visualisation. Note that having the number of bins proportional to \\(n^{1/3}\\) is asymptotically optimal, which is why it appears in most estimators. These are simply plug-in methods that give good starting points for number of bins. In the equations below, \\(h\\) is the binwidth and \\(n\_h\\) is the number of bins. All estimators that compute bin counts are recast to bin width using the [`ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")
 of the data. The final bin count is obtained from `np.round(np.ceil(range / h))`. The final bin width is often less than what is returned by the estimators below.

‘auto’ (minimum bin width of the ‘sturges’ and ‘fd’ estimators)

A compromise to get a good value. For small datasets the Sturges value will usually be chosen, while larger datasets will usually default to FD. Avoids the overly conservative behaviour of FD and Sturges for small and large datasets respectively. Switchover point is usually \\(a.size \\approx 1000\\).

‘fd’ (Freedman Diaconis Estimator)

\\\[h = 2 \\frac{IQR}{n^{1/3}}\\\]

The binwidth is proportional to the interquartile range (IQR) and inversely proportional to cube root of a.size. Can be too conservative for small datasets, but is quite good for large datasets. The IQR is very robust to outliers.

‘scott’

\\\[h = \\sigma \\sqrt\[3\]{\\frac{24 \\sqrt{\\pi}}{n}}\\\]

The binwidth is proportional to the standard deviation of the data and inversely proportional to cube root of `x.size`. Can be too conservative for small datasets, but is quite good for large datasets. The standard deviation is not very robust to outliers. Values are very similar to the Freedman-Diaconis estimator in the absence of outliers.

‘rice’

\\\[n\_h = 2n^{1/3}\\\]

The number of bins is only proportional to cube root of `a.size`. It tends to overestimate the number of bins and it does not take into account data variability.

‘sturges’

\\\[n\_h = \\log \_{2}(n) + 1\\\]

The number of bins is the base 2 log of `a.size`. This estimator assumes normality of data and is too conservative for larger, non-normal datasets. This is the default method in R’s `hist` method.

‘doane’

\\\[ \\begin{align}\\begin{aligned}n\_h = 1 + \\log\_{2}(n) + \\log\_{2}\\left(1 + \\frac{|g\_1|}{\\sigma\_{g\_1}}\\right)\\\\g\_1 = mean\\left\[\\left(\\frac{x - \\mu}{\\sigma}\\right)^3\\right\]\\\\\\sigma\_{g\_1} = \\sqrt{\\frac{6(n - 2)}{(n + 1)(n + 3)}}\\end{aligned}\\end{align} \\\]

An improved version of Sturges’ formula that produces better estimates for non-normal datasets. This estimator attempts to account for the skew of the data.

‘sqrt’

\\\[n\_h = \\sqrt n\\\]

The simplest and fastest estimator. Only takes into account the data size.

Additionally, if the data is of integer dtype, then the binwidth will never be less than 1.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> arr \= np.array(\[0, 0, 0, 1, 2, 3, 3, 4, 5\])
\>>> np.histogram\_bin\_edges(arr, bins\='auto', range\=(0, 1))
array(\[0.  , 0.25, 0.5 , 0.75, 1.  \])
\>>> np.histogram\_bin\_edges(arr, bins\=2)
array(\[0. , 2.5, 5. \])

Copy to clipboard

For consistency with histogram, an array of pre-computed bins is passed through unmodified:

\>>> np.histogram\_bin\_edges(arr, \[1, 2\])
array(\[1, 2\])

Copy to clipboard

This function allows one set of bins to be computed, and reused across multiple histograms:

\>>> shared\_bins \= np.histogram\_bin\_edges(arr, bins\='auto')
\>>> shared\_bins
array(\[0., 1., 2., 3., 4., 5.\])

Copy to clipboard

\>>> group\_id \= np.array(\[0, 1, 1, 0, 1, 1, 0, 1, 1\])
\>>> hist\_0, \_ \= np.histogram(arr\[group\_id \== 0\], bins\=shared\_bins)
\>>> hist\_1, \_ \= np.histogram(arr\[group\_id \== 1\], bins\=shared\_bins)

Copy to clipboard

\>>> hist\_0; hist\_1
array(\[1, 1, 0, 1, 0\])
array(\[2, 0, 1, 1, 2\])

Copy to clipboard

Which gives more easily comparable results than using separate bins for each histogram:

\>>> hist\_0, bins\_0 \= np.histogram(arr\[group\_id \== 0\], bins\='auto')
\>>> hist\_1, bins\_1 \= np.histogram(arr\[group\_id \== 1\], bins\='auto')
\>>> hist\_0; hist\_1
array(\[1, 1, 1\])
array(\[2, 1, 1, 2\])
\>>> bins\_0; bins\_1
array(\[0., 1., 2., 3.\])
array(\[0.  , 1.25, 2.5 , 3.75, 5.  \])

Copy to clipboard

Go BackOpen In Tab

On this page