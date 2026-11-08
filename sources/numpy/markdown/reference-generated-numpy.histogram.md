[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.histogram.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.histogram.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.histogram.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.histogram.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.histogram.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.histogram.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.histogram.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.histogram.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.histogram.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.histogram.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.histogram.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.histogram.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.histogram.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.histogram.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.histogram.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.histogram.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.histogram.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.histogram.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.histogram.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.histogram.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.histogram[#](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy-histogram "Link to this heading")

=================================================================================================================================

numpy.histogram(_a_, _bins\=10_, _range\=None_, _density\=None_, _weights\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_histograms_impl.py#L685-L899)
[#](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "Link to this definition")

Compute the histogram of a dataset.

Parameters:

**a**array\_like

Input data. The histogram is computed over the flattened array.

**bins**int or sequence of scalars or str, optional

If _bins_ is an int, it defines the number of equal-width bins in the given range (10, by default). If _bins_ is a sequence, it defines a monotonically increasing array of bin edges, including the rightmost edge, allowing for non-uniform bin widths.

If _bins_ is a string, it defines the method used to calculate the optimal bin width, as defined by [`histogram_bin_edges`](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges "numpy.histogram_bin_edges")
.

**range**(float, float), optional

The lower and upper range of the bins. If not provided, range is simply `(a.min(), a.max())`. Values outside the range are ignored. The first element of the range must be less than or equal to the second. _range_ affects the automatic bin computation as well. While bin width is computed to be optimal based on the actual data within _range_, the bin count will fill the entire range including portions containing no data.

**weights**array\_like, optional

An array of weights, of the same shape as _a_. Each value in _a_ only contributes its associated weight towards the bin count (instead of 1). If _density_ is True, the weights are normalized, so that the integral of the density over the range remains 1. Please note that the `dtype` of _weights_ will also become the `dtype` of the returned accumulator (_hist_), so it must be large enough to hold accumulated values as well.

**density**bool, optional

If `False`, the result will contain the number of samples in each bin. If `True`, the result is the value of the probability _density_ function at the bin, normalized such that the _integral_ over the range is 1. Note that the sum of the histogram values will not be equal to 1 unless bins of unity width are chosen; it is not a probability _mass_ function.

Returns:

**hist**array

The values of the histogram. See _density_ and _weights_ for a description of the possible semantics. If _weights_ are given, `hist.dtype` will be taken from _weights_.

**bin\_edges**array of dtype float

Return the bin edges `(length(hist)+1)`.

See also

[`histogramdd`](https://numpy.org/doc/stable/reference/generated/numpy.histogramdd.html#numpy.histogramdd "numpy.histogramdd")
, [`bincount`](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html#numpy.bincount "numpy.bincount")
, [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")
, [`digitize`](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html#numpy.digitize "numpy.digitize")
, [`histogram_bin_edges`](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges "numpy.histogram_bin_edges")

Notes

All but the last (righthand-most) bin is half-open. In other words, if _bins_ is:

\[1, 2, 3, 4\]

Copy to clipboard

then the first bin is `[1, 2)` (including 1, but excluding 2) and the second `[2, 3)`. The last bin, however, is `[3, 4]`, which _includes_ 4.\
\
Examples\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> np.histogram(\[1, 2, 1\], bins\=\[0, 1, 2, 3\])\
(array(\[0, 2, 1\]), array(\[0, 1, 2, 3\]))\
\>>> np.histogram(np.arange(4), bins\=np.arange(5), density\=True)\
(array(\[0.25, 0.25, 0.25, 0.25\]), array(\[0, 1, 2, 3, 4\]))\
\>>> np.histogram(\[\[1, 2, 1\], \[1, 0, 1\]\], bins\=\[0,1,2,3\])\
(array(\[1, 4, 1\]), array(\[0, 1, 2, 3\]))\
\
Copy to clipboard\
\
\>>> a \= np.arange(5)\
\>>> hist, bin\_edges \= np.histogram(a, density\=True)\
\>>> hist\
array(\[0.5, 0. , 0.5, 0. , 0. , 0.5, 0. , 0.5, 0. , 0.5\])\
\>>> hist.sum()\
2.4999999999999996\
\>>> np.sum(hist \* np.diff(bin\_edges))\
1.0\
\
Copy to clipboard\
\
Automated Bin Selection Methods example, using 2 peak random data with 2000 points.\
\
import matplotlib.pyplot as plt\
import numpy as np\
\
rng \= np.random.RandomState(10)  \# deterministic random data\
a \= np.hstack((rng.normal(size\=1000),\
               rng.normal(loc\=5, scale\=2, size\=1000)))\
plt.hist(a, bins\='auto')  \# arguments are passed to np.histogram\
plt.title("Histogram with 'auto' bins")\
plt.show()\
\
Copy to clipboard\
\
![../../_images/numpy-histogram-1.png](https://numpy.org/doc/stable/_images/numpy-histogram-1.png)\
\
Go BackOpen In Tab\
\
On this page