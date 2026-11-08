[Skip to main content](https://matplotlib.org/stable/gallery/statistics/histogram_normalization.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/statistics/histogram_normalization.html#sphx-glr-download-gallery-statistics-histogram-normalization-py)
 to download the full example code.

Histogram bins, density, and weight[#](https://matplotlib.org/stable/gallery/statistics/histogram_normalization.html#histogram-bins-density-and-weight "Link to this heading")

===============================================================================================================================================================================

The [`Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
 method can flexibly create histograms in a few different ways, which is flexible and helpful, but can also lead to confusion. In particular, you can:

*   bin the data as you want, either with an automatically chosen number of bins, or with fixed bin edges,
    
*   normalize the histogram so that its integral is one,
    
*   and assign weights to the data points, so that each data point affects the count in its bin differently.
    

The Matplotlib `hist` method calls [`numpy.histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "(in NumPy v2.5)")
 and plots the results, therefore users should consult the numpy documentation for a definitive guide.

Histograms are created by defining bin edges, and taking a dataset of values and sorting them into the bins, and counting or summing how much data is in each bin. In this simple example, 9 numbers between 1 and 4 are sorted into 3 bins:

import matplotlib.pyplot as plt
import numpy as np

[rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
(19680801)

[xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[1.2, 2.3, 3.3, 3.1, 1.7, 3.4, 2.1, 1.25, 1.3\])
[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[1, 2, 3, 4\])

\# changing the style of the histogram bars just to make it
\# very clear where the boundaries of the bins are:
[style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'facecolor': 'none', 'edgecolor': 'C0', 'linewidth': 3}

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.hist](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

\# plot the xdata locations on the x axis:
[ax.plot](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 0\*[xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'd')
[ax.set\_ylabel](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
('Number per bin')
[ax.set\_xlabel](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
('x bins (dx=1.0)')

![histogram normalization](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_001_2_00x.png)

Modifying bins[#](https://matplotlib.org/stable/gallery/statistics/histogram_normalization.html#modifying-bins "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

Changing the bin size changes the shape of this sparse histogram, so its a good idea to choose bins with some care with respect to your data. Here we make the bins half as wide.

[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1, 4.5, 0.5)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.hist](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[ax.plot](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 0\*[xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'd')
[ax.set\_ylabel](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
('Number per bin')
[ax.set\_xlabel](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
('x bins (dx=0.5)')

![histogram normalization](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_002_2_00x.png)

We can also let numpy (via Matplotlib) choose the bins automatically, or specify a number of bins to choose automatically:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['auto', 'n4'\]\],
                             sharex\=True, sharey\=True, layout\='constrained')

[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['auto'\].hist([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \*\*[style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['auto'\].plot([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 0\*[xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'd')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['auto'\].set\_ylabel('Number per bin')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['auto'\].set\_xlabel('x bins (auto)')

[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['n4'\].hist([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=4, \*\*[style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['n4'\].plot([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 0\*[xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'd')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['n4'\].set\_xlabel('x bins ("bins=4")')

![histogram normalization](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_003_2_00x.png)

Normalizing histograms: density and weight[#](https://matplotlib.org/stable/gallery/statistics/histogram_normalization.html#normalizing-histograms-density-and-weight "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Counts-per-bin is the default length of each bar in the histogram. However, we can also normalize the bar lengths as a probability density function using the `density` parameter:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.hist](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, density\=True, \*\*[style](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[ax.set\_ylabel](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
('Probability density \[$V^{-1}$\])')
[ax.set\_xlabel](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
('x bins (dx=0.5 $V$)')

![histogram normalization](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_004_2_00x.png)

This normalization can be a little hard to interpret when just exploring the data. The value attached to each bar is divided by the total number of data points _and_ the width of the bin, and thus the values \_integrate\_ to one when integrating across the full range of data. e.g.

density \= counts / (sum(counts) \* np.diff(bins))
np.sum(density \* np.diff(bins)) \== 1

This normalization is how [probability density functions](https://en.wikipedia.org/wiki/Probability_density_function)
 are defined in statistics. If \\(X\\) is a random variable on \\(x\\), then \\(f\_X\\) is is the probability density function if \\(P\[a<X<b\] = \\int\_a^b f\_X dx\\). If the units of x are Volts, then the units of \\(f\_X\\) are \\(V^{-1}\\) or probability per change in voltage.

The usefulness of this normalization is a little more clear when we draw from a known distribution and try to compare with theory. So, choose 1000 points from a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)
, and also calculate the known probability density function:

[xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [rng.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal "numpy.random.Generator.normal")
(size\=1000)
[xpdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-4, 4, 0.1)
[pdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 1 / ([np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
)) \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[xpdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 / 2)

If we don't use `density=True`, we need to scale the expected probability distribution function by both the length of the data and the width of the bins:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['False', 'True'\]\], layout\='constrained')
[dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.1
[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-4, 4, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].hist([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, density\=False, histtype\='step', label\='Counts')

\# scale and plot the expected pdf:
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].plot([xpdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [pdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* len([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, label\=r'$N\\,f\_X(x)\\,\\delta x$')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].set\_ylabel('Count per bin')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].set\_xlabel('x bins \[V\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].legend()

[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].hist([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, density\=True, histtype\='step', label\='density')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].plot([xpdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [pdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\='$f\_X(x)$')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].set\_ylabel('Probability density \[$V^{-1}$\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].set\_xlabel('x bins \[$V$\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].legend()

![histogram normalization](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_005_2_00x.png)

One advantage of using the density is therefore that the shape and amplitude of the histogram does not depend on the size of the bins. Consider an extreme case where the bins do not have the same width. In this example, the bins below `x=-1.25` are six times wider than the rest of the bins. By normalizing by density, we preserve the shape of the distribution, whereas if we do not, then the wider bins have much higher counts than the thinner bins:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['False', 'True'\]\], layout\='constrained')
[dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.1
[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.hstack](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
(\[[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(\-4, \-1.25, 6\*[dx](https://docs.python.org/3/library/functions.html#float "builtins.float")\
), [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")\
(\-1.25, 4, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")\
)\])
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].hist([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, density\=False, histtype\='step', label\='Counts')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].plot([xpdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [pdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \* len([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, label\=r'$N\\,f\_X(x)\\,\\delta x\_0$')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].set\_ylabel('Count per bin')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].set\_xlabel('x bins \[V\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].legend()

[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].hist([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, density\=True, histtype\='step', label\='density')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].plot([xpdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [pdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\='$f\_X(x)$')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].set\_ylabel('Probability density \[$V^{-1}$\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].set\_xlabel('x bins \[$V$\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].legend()

![histogram normalization](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_006_2_00x.png)

Similarly, if we want to compare histograms with different bin widths, we may want to use `density=True`:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['False', 'True'\]\], layout\='constrained')

\# expected PDF
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].plot([xpdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [pdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, '--', label\='$f\_X(x)$', color\='k')

for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
 in enumerate(\[0.1, 0.4, 1.2\]):
    [xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-4, 4, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
    \# expected histogram:
    [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].plot([xpdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [pdf](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*1000\*[dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, '--', color\=f'C{[nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
}')
    [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].hist([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, density\=False, histtype\='step')

    [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].hist([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, density\=True, histtype\='step', label\=[dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

\# Labels:
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].set\_xlabel('x bins \[$V$\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['False'\].set\_ylabel('Count per bin')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].set\_ylabel('Probability density \[$V^{-1}$\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].set\_xlabel('x bins \[$V$\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['True'\].legend(fontsize\='small', title\='bin width:')

![histogram normalization](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_007_2_00x.png)

Sometimes people want to normalize so that the sum of counts is one. This is analogous to a [probability mass function](https://en.wikipedia.org/wiki/Probability_mass_function)
 for a discrete variable where the sum of probabilities for all the values equals one. Using `hist`, we can get this normalization if we set the _weights_ to 1/N. Note that the amplitude of this normalized histogram still depends on width and/or number of the bins:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(layout\='constrained', figsize\=(3.5, 3))

for [nn](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
 in enumerate(\[0.1, 0.4, 1.2\]):
    [xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-4, 4, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
    [ax.hist](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, weights\=1/len([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(len([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)),
                   histtype\='step', label\=f'{[dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
}')
[ax.set\_xlabel](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
('x bins \[$V$\]')
[ax.set\_ylabel](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
('Bin count / N')
[ax.legend](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
(fontsize\='small', title\='bin width:')

![histogram normalization](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_008_2_00x.png)

The value of normalizing histograms is comparing two distributions that have different sized populations. Here we compare the distribution of `xdata` with a population of 1000, and `xdata2` with 100 members.

[xdata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [rng.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal "numpy.random.Generator.normal")
(size\=100)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['no\_norm', 'density', 'weight'\]\],
                             layout\='constrained', figsize\=(8, 4))

[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(\-4, 4, 0.25)

[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['no\_norm'\].hist([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, histtype\='step')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['no\_norm'\].hist([xdata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, histtype\='step')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['no\_norm'\].set\_ylabel('Counts')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['no\_norm'\].set\_xlabel('x bins \[$V$\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['no\_norm'\].set\_title('No normalization')

[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['density'\].hist([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, histtype\='step', density\=True)
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['density'\].hist([xdata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, histtype\='step', density\=True)
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['density'\].set\_ylabel('Probability density \[$V^{-1}$\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['density'\].set\_title('Density=True')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['density'\].set\_xlabel('x bins \[$V$\]')

[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['weight'\].hist([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, histtype\='step',
                  weights\=1 / len([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(len([xdata](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)),
                  label\='N=1000')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['weight'\].hist([xdata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[xbins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, histtype\='step',
                  weights\=1 / len([xdata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(len([xdata2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)),
                  label\='N=100')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['weight'\].set\_xlabel('x bins \[$V$\]')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['weight'\].set\_ylabel('Counts / N')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['weight'\].legend(fontsize\='small')
[ax](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['weight'\].set\_title('Weight = 1/N')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![No normalization, Density=True, Weight = 1/N](https://matplotlib.org/stable/_images/sphx_glr_histogram_normalization_009_2_00x.png)

Tags: [plot-type: histogram](https://matplotlib.org/stable/_tags/plot-type-histogram.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
     / [`matplotlib.pyplot.hist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist "matplotlib.pyplot.hist")
    
*   [`matplotlib.axes.Axes.set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
    
*   [`matplotlib.axes.Axes.set_xlabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
    
*   [`matplotlib.axes.Axes.set_ylabel`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
    
*   [`matplotlib.axes.Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
    

**Total running time of the script:** (0 minutes 7.232 seconds)

[`Download Jupyter notebook: histogram_normalization.ipynb`](https://matplotlib.org/stable/_downloads/12169718046ea2615f3f512dfd44a9f5/histogram_normalization.ipynb)

[`Download Python source code: histogram_normalization.py`](https://matplotlib.org/stable/_downloads/53dc4031905590e5af06cab7e2cdb32d/histogram_normalization.py)

[`Download zipped: histogram_normalization.zip`](https://matplotlib.org/stable/_downloads/7124922c393f1777456a3a86e4a9d24b/histogram_normalization.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page