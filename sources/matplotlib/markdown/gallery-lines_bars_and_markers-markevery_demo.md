[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html#sphx-glr-download-gallery-lines-bars-and-markers-markevery-demo-py)
 to download the full example code.

Markevery Demo[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html#markevery-demo "Link to this heading")

==========================================================================================================================================

The `markevery` property of [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 allows drawing markers at a subset of data points.

The list of possible parameters is specified at [`Line2D.set_markevery`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_markevery "matplotlib.lines.Line2D.set_markevery")
. In short:

*   A single integer N draws every N-th marker.
    
*   A tuple of integers (start, N) draws every N-th marker, starting at data index _start_.
    
*   A list of integers draws the markers at the specified indices.
    
*   A slice draws the markers at the sliced indices.
    
*   A float specifies the distance between markers as a fraction of the Axes diagonal in screen space. This will lead to a visually uniform distribution of the points along the line, irrespective of scales and zooming.
    

import matplotlib.pyplot as plt
import numpy as np

\# define a list of markevery cases to plot
[cases](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    None,\
    8,\
    (30, 8),\
    \[16, 24, 32\],\
    \[0, \-1\],\
    slice(100, 200, 3),\
    0.1,\
    0.4,\
    (0.2, 0.4)\
\]

\# data points
[delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.11
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10 \- 2 \* [delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 200) + [delta](https://docs.python.org/3/library/functions.html#float "builtins.float")
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) + 1.0 + [delta](https://docs.python.org/3/library/functions.html#float "builtins.float")

markevery with linear scales[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html#markevery-with-linear-scales "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 3, figsize\=(10, 6), layout\='constrained')
for ax, [markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [cases](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f'markevery={[markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
}')
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o', ls\='-', ms\=4, [markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

![markevery=None, markevery=8, markevery=(30, 8), markevery=[16, 24, 32], markevery=[0, -1], markevery=slice(100, 200, 3), markevery=0.1, markevery=0.4, markevery=(0.2, 0.4)](https://matplotlib.org/stable/_images/sphx_glr_markevery_demo_001_2_00x.png)

markevery with log scales[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html#markevery-with-log-scales "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Note that the log scale causes a visual asymmetry in the marker distance for when subsampling the data using an integer. In contrast, subsampling on fraction of figure size creates even distributions, because it's based on fractions of the Axes diagonal, not on data coordinates or data indices.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 3, figsize\=(10, 6), layout\='constrained')
for ax, [markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [cases](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f'markevery={[markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
}')
    [ax.set\_xscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
('log')
    [ax.set\_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
('log')
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o', ls\='-', ms\=4, [markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

![markevery=None, markevery=8, markevery=(30, 8), markevery=[16, 24, 32], markevery=[0, -1], markevery=slice(100, 200, 3), markevery=0.1, markevery=0.4, markevery=(0.2, 0.4)](https://matplotlib.org/stable/_images/sphx_glr_markevery_demo_002_2_00x.png)

markevery on zoomed plots[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html#markevery-on-zoomed-plots "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Integer-based _markevery_ specifications select points from the underlying data and are independent on the view. In contrast, float-based specifications are related to the Axes diagonal. While zooming does not change the Axes diagonal, it changes the displayed data range, and more points will be displayed when zooming.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 3, figsize\=(10, 6), layout\='constrained')
for ax, [markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [cases](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f'markevery={[markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
}')
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o', ls\='-', ms\=4, [markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(6, 6.7)
    [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(1.1, 1.7)

![markevery=None, markevery=8, markevery=(30, 8), markevery=[16, 24, 32], markevery=[0, -1], markevery=slice(100, 200, 3), markevery=0.1, markevery=0.4, markevery=(0.2, 0.4)](https://matplotlib.org/stable/_images/sphx_glr_markevery_demo_003_2_00x.png)

markevery on polar plots[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html#markevery-on-polar-plots "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 3.0, 200)
[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(3, 3, figsize\=(10, 6), layout\='constrained',
                        subplot\_kw\={'projection': 'polar'})
for ax, [markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [cases](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f'markevery={[markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
}')
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'o', ls\='-', ms\=4, [markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[markevery](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![markevery=None, markevery=8, markevery=(30, 8), markevery=[16, 24, 32], markevery=[0, -1], markevery=slice(100, 200, 3), markevery=0.1, markevery=0.4, markevery=(0.2, 0.4)](https://matplotlib.org/stable/_images/sphx_glr_markevery_demo_004_2_00x.png)

Tags: [component: marker](https://matplotlib.org/stable/_tags/component-marker.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 16.466 seconds)

[`Download Jupyter notebook: markevery_demo.ipynb`](https://matplotlib.org/stable/_downloads/97d182004997b17b767f4c217261ded9/markevery_demo.ipynb)

[`Download Python source code: markevery_demo.py`](https://matplotlib.org/stable/_downloads/d4832f59edf5628fed3ec2eee2cecbf9/markevery_demo.py)

[`Download zipped: markevery_demo.zip`](https://matplotlib.org/stable/_downloads/b64b2ecc0930bd80fee0e5e32252bd60/markevery_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page