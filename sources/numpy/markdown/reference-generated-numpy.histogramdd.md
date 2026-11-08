[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.histogramdd.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.histogramdd.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.histogramdd.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.histogramdd.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.histogramdd.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.histogramdd.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.histogramdd.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.histogramdd.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.histogramdd.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.histogramdd.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.histogramdd.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.histogramdd.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.histogramdd.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.histogramdd.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.histogramdd.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.histogramdd.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.histogramdd.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.histogramdd.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.histogramdd.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.histogramdd.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.histogramdd.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.histogramdd.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.histogramdd[#](https://numpy.org/doc/stable/reference/generated/numpy.histogramdd.html#numpy-histogramdd "Link to this heading")

=======================================================================================================================================

numpy.histogramdd(_sample_, _bins\=10_, _range\=None_, _density\=None_, _weights\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_histograms_impl.py#L913-L1085)
[#](https://numpy.org/doc/stable/reference/generated/numpy.histogramdd.html#numpy.histogramdd "Link to this definition")

Compute the multidimensional histogram of some data.

Parameters:

**sample**(N, D) array, or (N, D) array\_like

The data to be histogrammed.

Note the unusual interpretation of sample when an array\_like:

*   When an array, each row is a coordinate in a D-dimensional space - such as `histogramdd(np.array([p1, p2, p3]))`.
    
*   When an array\_like, each element is the list of values for single coordinate - such as `histogramdd((X, Y, Z))`.
    

The first form should be preferred.

**bins**sequence or int, optional

The bin specification:

*   A sequence of arrays describing the monotonically increasing bin edges along each dimension.
    
*   The number of bins for each dimension (nx, ny, … =bins)
    
*   The number of bins for all dimensions (nx=ny=…=bins).
    

**range**sequence, optional

A sequence of length D, each an optional (lower, upper) tuple giving the outer bin edges to be used if the edges are not given explicitly in _bins_. An entry of None in the sequence results in the minimum and maximum values being used for the corresponding dimension. The default, None, is equivalent to passing a tuple of D None values.

**density**bool, optional

If False, the default, returns the number of samples in each bin. If True, returns the probability _density_ function at the bin, `bin_count / sample_count / bin_volume`.

**weights**(N,) array\_like, optional

An array of values _w\_i_ weighing each sample _(x\_i, y\_i, z\_i, …)_. Weights are normalized to 1 if density is True. If density is False, the values of the returned histogram are equal to the sum of the weights belonging to the samples falling into each bin.

Returns:

**H**ndarray

The multidimensional histogram of sample x. See density and weights for the different possible semantics.

**edges**tuple of ndarrays

A tuple of D arrays describing the bin edges for each dimension.

See also

[`histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")

1-D histogram

[`histogram2d`](https://numpy.org/doc/stable/reference/generated/numpy.histogram2d.html#numpy.histogram2d "numpy.histogram2d")

2-D histogram

Examples

Try it in your browser!

\>>> import numpy as np
\>>> rng \= np.random.default\_rng()
\>>> r \= rng.normal(size\=(100,3))
\>>> H, edges \= np.histogramdd(r, bins \= (5, 8, 4))
\>>> H.shape, edges\[0\].size, edges\[1\].size, edges\[2\].size
((5, 8, 4), 6, 9, 5)

Copy to clipboard

Go BackOpen In Tab

On this page