[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/lines_with_ticks_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/lines_with_ticks_demo.html#sphx-glr-download-gallery-lines-bars-and-markers-lines-with-ticks-demo-py)
 to download the full example code.

Lines with a ticked patheffect[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/lines_with_ticks_demo.html#lines-with-a-ticked-patheffect "Link to this heading")

=================================================================================================================================================================================

Ticks can be added along a line to mark one side as a barrier using [`TickedStroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.TickedStroke "matplotlib.patheffects.TickedStroke")
. You can control the angle, spacing, and length of the ticks.

The ticks will also appear appropriately in the legend.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import patheffects

\# Plot a straight diagonal line with ticked style path
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 6))
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\[0, 1\], \[0, 1\], label\="Line",
        path\_effects\=\[[patheffects.withTickedStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke "matplotlib.patheffects.withTickedStroke")\
(spacing\=7, angle\=135)\])

\# Plot a curved line with ticked style path
[nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 101
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.0, 1.0, [nx](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.3\*[np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*8) + 0.4
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\="Curve", path\_effects\=\[[patheffects.withTickedStroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke "matplotlib.patheffects.withTickedStroke")\
()\])

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![lines with ticks demo](https://matplotlib.org/stable/_images/sphx_glr_lines_with_ticks_demo_001_2_00x.png)

Tags: [styling: linestyle](https://matplotlib.org/stable/_tags/styling-linestyle.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: lines_with_ticks_demo.ipynb`](https://matplotlib.org/stable/_downloads/0234b09e9a73d4ee840adeb2955c67c3/lines_with_ticks_demo.ipynb)

[`Download Python source code: lines_with_ticks_demo.py`](https://matplotlib.org/stable/_downloads/3269caad4b186ff2ba73f725b2cb5a12/lines_with_ticks_demo.py)

[`Download zipped: lines_with_ticks_demo.zip`](https://matplotlib.org/stable/_downloads/a57a2948749125bcde398081b67f0be1/lines_with_ticks_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)