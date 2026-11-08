[Skip to main content](https://matplotlib.org/stable/gallery/statistics/histogram_bihistogram.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/histogram_bihistogram.html#sphx-glr-download-gallery-statistics-histogram-bihistogram-py)
 to download the full example code.

Bihistogram[#](https://matplotlib.org/stable/gallery/statistics/histogram_bihistogram.html#bihistogram "Link to this heading")

===============================================================================================================================

How to plot a bihistogram with Matplotlib.

import matplotlib.pyplot as plt
import numpy as np

\# Create a random number generator with a fixed seed for reproducibility
[rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
(19680801)

Generate data and plot a bihistogram[#](https://matplotlib.org/stable/gallery/statistics/histogram_bihistogram.html#generate-data-and-plot-a-bihistogram "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To generate a bihistogram we need two datasets (each being a vector of numbers). We will plot both histograms using plt.hist() and set the weights of the second one to be negative. We'll generate data below and plot the bihistogram.

[N\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 10\_000

\# Generate two normal distributions
[dataset1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(0, 1, size\=[N\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[dataset2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")
(1, 2, size\=[N\_points](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

\# Use a constant bin width to make the two histograms easier to compare visually
[bin\_width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.25
[bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min "numpy.min")
(\[[dataset1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [dataset2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\]),
                    [np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max "numpy.max")
(\[[dataset1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [dataset2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\]) + [bin\_width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [bin\_width](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# Plot the first histogram
[ax.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([dataset1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\="Dataset 1")

\# Plot the second histogram
\# (notice the negative weights, which flip the histogram upside down)
[ax.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([dataset2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, weights\=-[np.ones\_like](https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like")
([dataset2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\="Dataset 2")
[ax.axhline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
(0, color\="k")
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![histogram bihistogram](https://matplotlib.org/stable/_images/sphx_glr_histogram_bihistogram_001_2_00x.png)

Tags: [plot-type: histogram](https://matplotlib.org/stable/_tags/plot-type-histogram.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)
 [purpose: showcase](https://matplotlib.org/stable/_tags/purpose-showcase.html)

[`Download Jupyter notebook: histogram_bihistogram.ipynb`](https://matplotlib.org/stable/_downloads/0bf3e2cf1e74c1b07549d595e76d2d97/histogram_bihistogram.ipynb)

[`Download Python source code: histogram_bihistogram.py`](https://matplotlib.org/stable/_downloads/5de653d80bcc9ea35116a0e4d36d75b5/histogram_bihistogram.py)

[`Download zipped: histogram_bihistogram.zip`](https://matplotlib.org/stable/_downloads/2e63fa6040b0d66b789c94205555bf39/histogram_bihistogram.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page