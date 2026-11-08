[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axhspan_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axhspan_demo.html#sphx-glr-download-gallery-subplots-axes-and-figures-axhspan-demo-py)
 to download the full example code.

Draw regions that span an Axes[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axhspan_demo.html#draw-regions-that-span-an-axes "Link to this heading")

===========================================================================================================================================================================

[`axhspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html#matplotlib.axes.Axes.axhspan "matplotlib.axes.Axes.axhspan")
 and [`axvspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvspan.html#matplotlib.axes.Axes.axvspan "matplotlib.axes.Axes.axvspan")
 draw rectangles that span the Axes in either the horizontal or vertical direction and are bounded in the other direction. They are often used to highlight data regions.

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(7, 3))

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 2.9 \* [np.convolve](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "numpy.convolve")
([np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(500), [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(30) / 30, mode\='valid')
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax1.axhspan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html#matplotlib.axes.Axes.axhspan "matplotlib.axes.Axes.axhspan")
(\-1, 1, alpha\=0.1)
[ax1.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(ylim\=(\-1.5, 1.5), title\="axhspan")

[mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 8
[sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 2
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 16, 401)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-(([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\-[mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
)\*\*2)/(2\*[sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
\*\*2))
[ax2.axvspan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvspan.html#matplotlib.axes.Axes.axvspan "matplotlib.axes.Axes.axvspan")
([mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
\-2\*[sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
\-[sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
, color\='0.95')
[ax2.axvspan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvspan.html#matplotlib.axes.Axes.axvspan "matplotlib.axes.Axes.axvspan")
([mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
\-[sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
+[sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
, color\='0.9')
[ax2.axvspan](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvspan.html#matplotlib.axes.Axes.axvspan "matplotlib.axes.Axes.axvspan")
([mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
+[sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
+2\*[sigma](https://docs.python.org/3/library/functions.html#int "builtins.int")
, color\='0.95')
[ax2.axvline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
([mu](https://docs.python.org/3/library/functions.html#int "builtins.int")
, color\='darkgrey', linestyle\='--')
[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax2.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(title\="axvspan")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![axhspan, axvspan](https://matplotlib.org/stable/_images/sphx_glr_axhspan_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.axhspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html#matplotlib.axes.Axes.axhspan "matplotlib.axes.Axes.axhspan")
     / [`matplotlib.pyplot.axhspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhspan.html#matplotlib.pyplot.axhspan "matplotlib.pyplot.axhspan")
    
*   [`matplotlib.axes.Axes.axvspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvspan.html#matplotlib.axes.Axes.axvspan "matplotlib.axes.Axes.axvspan")
     / [`matplotlib.pyplot.axvspan`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvspan.html#matplotlib.pyplot.axvspan "matplotlib.pyplot.axvspan")
    

See also

[`axhline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
, [`axvline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
, [`axline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html#matplotlib.axes.Axes.axline "matplotlib.axes.Axes.axline")
 draw infinite lines.

Tags: [styling: shape](https://matplotlib.org/stable/_tags/styling-shape.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: axhspan_demo.ipynb`](https://matplotlib.org/stable/_downloads/fb74c75146177c4b4ad37e0cee639902/axhspan_demo.ipynb)

[`Download Python source code: axhspan_demo.py`](https://matplotlib.org/stable/_downloads/e24e3e0db408a967fe1592ecb628b5d1/axhspan_demo.py)

[`Download zipped: axhspan_demo.zip`](https://matplotlib.org/stable/_downloads/9d6cfa03c318e16e30a4dc17f1017ee8/axhspan_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)