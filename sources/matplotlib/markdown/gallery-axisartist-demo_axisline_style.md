[Skip to main content](https://matplotlib.org/stable/gallery/axisartist/demo_axisline_style.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/axisartist/demo_axisline_style.html#sphx-glr-download-gallery-axisartist-demo-axisline-style-py)
 to download the full example code.

Axis line styles[#](https://matplotlib.org/stable/gallery/axisartist/demo_axisline_style.html#axis-line-styles "Link to this heading")

=======================================================================================================================================

This example shows some configurations for axis style.

Note: The [`mpl_toolkits.axisartist`](https://matplotlib.org/stable/api/toolkits/axisartist.html#module-mpl_toolkits.axisartist "mpl_toolkits.axisartist")
 Axes classes may be confusing for new users. If the only aim is to obtain arrow heads at the ends of the axes, rather check out the [Centered spines with arrows](https://matplotlib.org/stable/gallery/spines/centered_spines_with_arrows.html)
 example.

![demo axisline style](https://matplotlib.org/stable/_images/sphx_glr_demo_axisline_style_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

from mpl\_toolkits.axisartist.axislines import [AxesZero](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxesZero.html#mpl_toolkits.axisartist.axislines.AxesZero "mpl_toolkits.axisartist.AxesZero")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
[ax](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxesZero.html#mpl_toolkits.axisartist.axislines.AxesZero "mpl_toolkits.axisartist.AxesZero")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(axes\_class\=[AxesZero](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.AxesZero.html#mpl_toolkits.axisartist.axislines.AxesZero "mpl_toolkits.axisartist.AxesZero")
)

for [direction](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in \["xzero", "yzero"\]:
    \# adds arrows at the ends of each axis
    [ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\[[direction](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_axisline\_style("-|>")

    \# adds X and Y-axis from the origin
    [ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\[[direction](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_visible(True)

for [direction](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in \["left", "right", "bottom", "top"\]:
    \# hides borders
    [ax.axis](https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.axisartist.axislines.Axes.html#mpl_toolkits.axisartist.axislines.Axes.axis "mpl_toolkits.axisartist.Axes.axis")
\[[direction](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\].set\_visible(False)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(\-0.5, 1., 100)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
))

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[`Download Jupyter notebook: demo_axisline_style.ipynb`](https://matplotlib.org/stable/_downloads/568063a054e4068b855cef34d3b037b5/demo_axisline_style.ipynb)

[`Download Python source code: demo_axisline_style.py`](https://matplotlib.org/stable/_downloads/2efbf158321b6ee9b59fa6e4e5367de6/demo_axisline_style.py)

[`Download zipped: demo_axisline_style.zip`](https://matplotlib.org/stable/_downloads/7ead436ada2af17b58cf66744f0ae202/demo_axisline_style.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)