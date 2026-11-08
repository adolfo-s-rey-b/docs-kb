[Skip to main content](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/shared_axis_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/shared_axis_demo.html#sphx-glr-download-gallery-subplots-axes-and-figures-shared-axis-demo-py)
 to download the full example code.

Shared axis[#](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/shared_axis_demo.html#shared-axis "Link to this heading")

=========================================================================================================================================

Use axis sharing when you want to compare data across multiple subplots, and want to ensure they are on the same scale. To do so, pass `sharex=True` and/or `sharey=True` to [`subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
.

This ensures the x- or y-axis limits are synchronized across the subplots. Autoscaling considers the data on all Axes; therefore, any limit changes, including interactive zoom and pan, will affect all shared axes.

The plot below illustrates this by showing two different time-series and using _sharex_ to ensure the times are aligned.

For more info see [Sharing axes](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html#sharing-axes)
.

import matplotlib.pyplot as plt
import numpy as np

[t1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 8, 201)
[y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [t1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(2, 10, 201)
[y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 20 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)\*\*2 \* [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-0.3\*[t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, sharex\=True)

[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax1.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("Signal 1")

[ax2.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax2.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
("Signal 2")
[ax2.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
("Time (s)")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![shared axis demo](https://matplotlib.org/stable/_images/sphx_glr_shared_axis_demo_001_2_00x.png)

Tags: [component: axis](https://matplotlib.org/stable/_tags/component-axis.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: shared_axis_demo.ipynb`](https://matplotlib.org/stable/_downloads/b4898889a201346ffdd44885896b2ec2/shared_axis_demo.ipynb)

[`Download Python source code: shared_axis_demo.py`](https://matplotlib.org/stable/_downloads/268bf2a830c1140e907940f9c32a672b/shared_axis_demo.py)

[`Download zipped: shared_axis_demo.zip`](https://matplotlib.org/stable/_downloads/d585d59595980230bf07fa1beccf741f/shared_axis_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)