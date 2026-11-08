[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.histogram2d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.histogram2d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.histogram2d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.histogram2d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.histogram2d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.histogram2d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.histogram2d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.histogram2d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.histogram2d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.histogram2d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.histogram2d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.histogram2d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.histogram2d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.histogram2d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.histogram2d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.histogram2d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.histogram2d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.histogram2d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.histogram2d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.histogram2d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.histogram2d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.histogram2d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.histogram2d[#](https://numpy.org/doc/stable/reference/generated/numpy.histogram2d.html#numpy-histogram2d "Link to this heading")

=======================================================================================================================================

numpy.histogram2d(_x_, _y_, _bins\=10_, _range\=None_, _density\=None_, _weights\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L695-L862)
[#](https://numpy.org/doc/stable/reference/generated/numpy.histogram2d.html#numpy.histogram2d "Link to this definition")

Compute the bi-dimensional histogram of two data samples.

Parameters:

**x**array\_like, shape (N,)

An array containing the x coordinates of the points to be histogrammed.

**y**array\_like, shape (N,)

An array containing the y coordinates of the points to be histogrammed.

**bins**int or array\_like or \[int, int\] or \[array, array\], optional

The bin specification:

*   If int, the number of bins for the two dimensions (nx=ny=bins).
    
*   If array\_like, the bin edges for the two dimensions (x\_edges=y\_edges=bins).
    
*   If \[int, int\], the number of bins in each dimension (nx, ny = bins).
    
*   If \[array, array\], the bin edges in each dimension (x\_edges, y\_edges = bins).
    
*   A combination \[int, array\] or \[array, int\], where int is the number of bins and array is the bin edges.
    

**range**array\_like, shape(2,2), optional

The leftmost and rightmost edges of the bins along each dimension (if not specified explicitly in the _bins_ parameters): `[[xmin, xmax], [ymin, ymax]]`. All values outside of this range will be considered outliers and not tallied in the histogram.

**density**bool, optional

If False, the default, returns the number of samples in each bin. If True, returns the probability _density_ function at the bin, `bin_count / sample_count / bin_area`.

**weights**array\_like, shape(N,), optional

An array of values `w_i` weighing each sample `(x_i, y_i)`. Weights are normalized to 1 if _density_ is True. If _density_ is False, the values of the returned histogram are equal to the sum of the weights belonging to the samples falling into each bin.

Returns:

**H**ndarray, shape(nx, ny)

The bi-dimensional histogram of samples _x_ and _y_. Values in _x_ are histogrammed along the first dimension and values in _y_ are histogrammed along the second dimension.

**xedges**ndarray, shape(nx+1,)

The bin edges along the first dimension.

**yedges**ndarray, shape(ny+1,)

The bin edges along the second dimension.

See also

[`histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")

1D histogram

[`histogramdd`](https://numpy.org/doc/stable/reference/generated/numpy.histogramdd.html#numpy.histogramdd "numpy.histogramdd")

Multidimensional histogram

Notes

When _density_ is True, then the returned histogram is the sample density, defined such that the sum over bins of the product `bin_value * bin_area` is 1.

Please note that the histogram does not follow the Cartesian convention where _x_ values are on the abscissa and _y_ values on the ordinate axis. Rather, _x_ is histogrammed along the first dimension of the array (vertical), and _y_ along the second dimension of the array (horizontal). This ensures compatibility with [`histogramdd`](https://numpy.org/doc/stable/reference/generated/numpy.histogramdd.html#numpy.histogramdd "numpy.histogramdd")
.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from matplotlib.image import NonUniformImage
\>>> import matplotlib.pyplot as plt

Copy to clipboard

Construct a 2-D histogram with variable bin width. First define the bin edges:

\>>> xedges \= \[0, 1, 3, 5\]
\>>> yedges \= \[0, 2, 3, 4, 6\]

Copy to clipboard

Next we create a histogram H with random bin content:

\>>> x \= np.random.normal(2, 1, 100)
\>>> y \= np.random.normal(1, 1, 100)
\>>> H, xedges, yedges \= np.histogram2d(x, y, bins\=(xedges, yedges))
\>>> \# Histogram does not follow Cartesian convention (see Notes),
\>>> \# therefore transpose H for visualization purposes.
\>>> H \= H.T

Copy to clipboard

[`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "(in Matplotlib v3.11.0)")
 can only display square bins:

\>>> fig \= plt.figure(figsize\=(7, 3))
\>>> ax \= fig.add\_subplot(131, title\='imshow: square bins')
\>>> plt.imshow(H, interpolation\='nearest', origin\='lower',
...         extent\=\[xedges\[0\], xedges\[\-1\], yedges\[0\], yedges\[\-1\]\])
<matplotlib.image.AxesImage object at 0x...>

Copy to clipboard

[`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolormesh.html#matplotlib.pyplot.pcolormesh "(in Matplotlib v3.11.0)")
 can display actual edges:

\>>> ax \= fig.add\_subplot(132, title\='pcolormesh: actual edges',
...         aspect\='equal')
\>>> X, Y \= np.meshgrid(xedges, yedges)
\>>> ax.pcolormesh(X, Y, H)
<matplotlib.collections.QuadMesh object at 0x...>

Copy to clipboard

[`NonUniformImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.NonUniformImage "(in Matplotlib v3.11.0)")
 can be used to display actual bin edges with interpolation:

\>>> ax \= fig.add\_subplot(133, title\='NonUniformImage: interpolated',
...         aspect\='equal', xlim\=xedges\[\[0, \-1\]\], ylim\=yedges\[\[0, \-1\]\])
\>>> im \= NonUniformImage(ax, interpolation\='bilinear')
\>>> xcenters \= (xedges\[:\-1\] + xedges\[1:\]) / 2
\>>> ycenters \= (yedges\[:\-1\] + yedges\[1:\]) / 2
\>>> im.set\_data(xcenters, ycenters, H)
\>>> ax.add\_image(im)
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-histogram2d-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-histogram2d-1_00_00.png)

It is also possible to construct a 2-D histogram without specifying bin edges:

\>>> \# Generate non-symmetric test data
\>>> n \= 10000
\>>> x \= np.linspace(1, 100, n)
\>>> y \= 2\*np.log(x) + np.random.rand(n) \- 0.5
\>>> \# Compute 2d histogram. Note the order of x/y and xedges/yedges
\>>> H, yedges, xedges \= np.histogram2d(y, x, bins\=20)

Copy to clipboard

Now we can plot the histogram using [`pcolormesh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolormesh.html#matplotlib.pyplot.pcolormesh "(in Matplotlib v3.11.0)")
, and a [`hexbin`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hexbin.html#matplotlib.pyplot.hexbin "(in Matplotlib v3.11.0)")
 for comparison.

\>>> \# Plot histogram using pcolormesh
\>>> fig, (ax1, ax2) \= plt.subplots(ncols\=2, sharey\=True)
\>>> ax1.pcolormesh(xedges, yedges, H, cmap\='rainbow')
\>>> ax1.plot(x, 2\*np.log(x), 'k-')
\>>> ax1.set\_xlim(x.min(), x.max())
\>>> ax1.set\_ylim(y.min(), y.max())
\>>> ax1.set\_xlabel('x')
\>>> ax1.set\_ylabel('y')
\>>> ax1.set\_title('histogram2d')
\>>> ax1.grid()

Copy to clipboard

\>>> \# Create hexbin plot for comparison
\>>> ax2.hexbin(x, y, gridsize\=20, cmap\='rainbow')
\>>> ax2.plot(x, 2\*np.log(x), 'k-')
\>>> ax2.set\_title('hexbin')
\>>> ax2.set\_xlim(x.min(), x.max())
\>>> ax2.set\_xlabel('x')
\>>> ax2.grid()

Copy to clipboard

\>>> plt.show()

Copy to clipboard

![../../_images/numpy-histogram2d-1_01_00.png](https://numpy.org/doc/stable/_images/numpy-histogram2d-1_01_00.png)

Go BackOpen In Tab

On this page