[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_betweenx_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_betweenx_demo.html#sphx-glr-download-gallery-lines-bars-and-markers-fill-betweenx-demo-py)
 to download the full example code.

Fill the area between two vertical lines[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/fill_betweenx_demo.html#fill-the-area-between-two-vertical-lines "Link to this heading")

==================================================================================================================================================================================================

Using [`fill_betweenx`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
 to color along the horizontal direction between two curves.

import matplotlib.pyplot as plt
import numpy as np

[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 2, 0.01)
[x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= 1.2 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(4 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, \[[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\] \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 3, sharey\=True, figsize\=(6, 6))

[ax1.fill\_betweenx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 0, [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('between (x1, 0)')

[ax2.fill\_betweenx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 1)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('between (x1, 1)')
[ax2.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('x')

[ax3.fill\_betweenx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
)
[ax3.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('between (x1, x2)')

![between (x1, 0), between (x1, 1), between (x1, x2)](https://matplotlib.org/stable/_images/sphx_glr_fill_betweenx_demo_001_2_00x.png)

Now fill between x1 and x2 where a logical condition is met. Note this is different than calling:

fill\_between([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[where\], [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[where\], [x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
\[where\])

because of edge effects over multiple contiguous regions.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, \[[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\] \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, sharey\=True, figsize\=(6, 6))
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='black')
[ax.fill\_betweenx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, where\=[x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \>= [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, facecolor\='green')
[ax.fill\_betweenx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, where\=[x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 <= [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, facecolor\='red')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('fill\_betweenx where')

\# Test support for masked arrays.
[x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \= [np.ma.masked\_greater](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_greater.html#numpy.ma.masked_greater "numpy.ma.masked_greater")
([x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, 1.0)
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='black')
[ax1.fill\_betweenx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, where\=[x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 \>= [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, facecolor\='green')
[ax1.fill\_betweenx](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill_betweenx.html#matplotlib.axes.Axes.fill_betweenx "matplotlib.axes.Axes.fill_betweenx")
([y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, where\=[x2](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 <= [x1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, facecolor\='red')
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('regions with x2 > 1 are masked')

![fill_betweenx where, regions with x2 > 1 are masked](https://matplotlib.org/stable/_images/sphx_glr_fill_betweenx_demo_002_2_00x.png)

This example illustrates a problem; because of the data gridding, there are undesired unfilled triangles at the crossover points. A brute-force solution would be to interpolate all arrays to a very fine grid before plotting.

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Tags: [plot-type: fill\_between](https://matplotlib.org/stable/_tags/plot-type-fill_between.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 1.515 seconds)

[`Download Jupyter notebook: fill_betweenx_demo.ipynb`](https://matplotlib.org/stable/_downloads/7e406faa61604cc10c30a781440a6802/fill_betweenx_demo.ipynb)

[`Download Python source code: fill_betweenx_demo.py`](https://matplotlib.org/stable/_downloads/25520da3172b0ab1766f2f0bd31a49f6/fill_betweenx_demo.py)

[`Download zipped: fill_betweenx_demo.zip`](https://matplotlib.org/stable/_downloads/db6965a28e99aee03ea9631bca850d9e/fill_betweenx_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)