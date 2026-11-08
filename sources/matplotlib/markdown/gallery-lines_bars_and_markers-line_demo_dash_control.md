[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html#sphx-glr-download-gallery-lines-bars-and-markers-line-demo-dash-control-py)
 to download the full example code.

Dashed line style configuration[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/line_demo_dash_control.html#dashed-line-style-configuration "Link to this heading")

====================================================================================================================================================================================

The dashing of a line is controlled via a dash sequence. It can be modified using [`Line2D.set_dashes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dashes "matplotlib.lines.Line2D.set_dashes")
.

The dash sequence is a series of on/off lengths in points, e.g. `[3, 1]` would be 3pt long lines separated by 1pt spaces.

Some functions like [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 support passing Line properties as keyword arguments. In such a case, you can already set the dashing when creating the line.

_Note_: The dash style can also be configured via a [property\_cycle](https://matplotlib.org/stable/users/explain/artists/color_cycle.html#color-cycle)
 by passing a list of dash sequences using the keyword _dashes_ to the cycler. This is not shown within this example.

Other attributes of the dash may also be set either with the relevant method ([`set_dash_capstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_capstyle "matplotlib.lines.Line2D.set_dash_capstyle")
, [`set_dash_joinstyle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_joinstyle "matplotlib.lines.Line2D.set_dash_joinstyle")
, [`set_gapcolor`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_gapcolor "matplotlib.lines.Line2D.set_gapcolor")
) or by passing the property through a plotting function.

import matplotlib.pyplot as plt
import numpy as np

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 10, 500)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[plt.rc](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rc.html#matplotlib.pyplot.rc "matplotlib.pyplot.rc")
('lines', linewidth\=2.5)
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# Using set\_dashes() and set\_capstyle() to modify dashing of an existing line.
[line1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, label\='Using set\_dashes() and set\_dash\_capstyle()')
[line1.set\_dashes](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dashes "matplotlib.lines.Line2D.set_dashes")
(\[2, 2, 10, 2\])  \# 2pt line, 2pt break, 10pt line, 2pt break.
[line1.set\_dash\_capstyle](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_dash_capstyle "matplotlib.lines.Line2D.set_dash_capstyle")
('round')

\# Using plot(..., dashes=...) to set the dashing when creating a line.
[line2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 0.2, dashes\=\[6, 2\], label\='Using the dashes parameter')

\# Using plot(..., dashes=..., gapcolor=...) to set the dashing and
\# alternating color when creating a line.
[line3](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \- 0.4, dashes\=\[4, 4\], gapcolor\='tab:pink',
                 label\='Using the dashes and gapcolor parameters')

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(handlelength\=4)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![line demo dash control](https://matplotlib.org/stable/_images/sphx_glr_line_demo_dash_control_001_2_00x.png)

Tags: [styling: linestyle](https://matplotlib.org/stable/_tags/styling-linestyle.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: line_demo_dash_control.ipynb`](https://matplotlib.org/stable/_downloads/4f32bf39e78d4b54b802e1d726030b42/line_demo_dash_control.ipynb)

[`Download Python source code: line_demo_dash_control.py`](https://matplotlib.org/stable/_downloads/1c02700bb13e6571e774c10ba73db267/line_demo_dash_control.py)

[`Download zipped: line_demo_dash_control.zip`](https://matplotlib.org/stable/_downloads/3a1a41f50ed83a37c8bac35c4f86a00c/line_demo_dash_control.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)