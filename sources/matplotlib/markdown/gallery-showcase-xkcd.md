[Skip to main content](https://matplotlib.org/stable/gallery/showcase/xkcd.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/showcase/xkcd.html#sphx-glr-download-gallery-showcase-xkcd-py)
 to download the full example code.

XKCD[#](https://matplotlib.org/stable/gallery/showcase/xkcd.html#xkcd "Link to this heading")

==============================================================================================

Shows how to create an xkcd-like plot.

import matplotlib.pyplot as plt
import numpy as np

with [plt.xkcd](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html#matplotlib.pyplot.xkcd "matplotlib.pyplot.xkcd")
():
    \# Based on "Stove Ownership" from XKCD by Randall Munroe
    \# https://xkcd.com/418/

    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.1, 0.2, 0.8, 0.7))
    [ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['top', 'right'\]\].set\_visible(False)
    [ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(\[\])
    [ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[\])
    [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-30, 10)

    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(100)
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[70:\] \-= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(30)

    [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
        'THE DAY I REALIZED\\nI COULD COOK BACON\\nWHENEVER I WANTED',
        xy\=(70, 1), arrowprops\=dict(arrowstyle\='->'), xytext\=(15, \-10))

    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

    [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('time')
    [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('my overall health')
    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(
        0.5, 0.05,
        '"Stove Ownership" from xkcd by Randall Munroe',
        ha\='center')

![xkcd](https://matplotlib.org/stable/_images/sphx_glr_xkcd_001_2_00x.png)

with [plt.xkcd](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html#matplotlib.pyplot.xkcd "matplotlib.pyplot.xkcd")
():
    \# Based on "The Data So Far" from XKCD by Randall Munroe
    \# https://xkcd.com/373/

    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0.1, 0.2, 0.8, 0.7))
    [ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
(\[0, 1\], \[0, 100\], 0.25)
    [ax.spines](https://matplotlib.org/stable/api/spines_api.html#matplotlib.spines.Spines "matplotlib.spines.Spines")
\[\['top', 'right'\]\].set\_visible(False)
    [ax.xaxis.set\_ticks\_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_ticks_position.html#matplotlib.axis.XAxis.set_ticks_position "matplotlib.axis.XAxis.set_ticks_position")
('bottom')
    [ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
(\[0, 1\])
    [ax.set\_xticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html#matplotlib.axes.Axes.set_xticklabels "matplotlib.axes.Axes.set_xticklabels")
(\['CONFIRMED BY\\nEXPERIMENT', 'REFUTED BY\\nEXPERIMENT'\])
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\-0.5, 1.5)
    [ax.set\_yticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html#matplotlib.axes.Axes.set_yticks "matplotlib.axes.Axes.set_yticks")
(\[\])
    [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0, 110)

    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("CLAIMS OF SUPERNATURAL POWERS")

    [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(
        0.5, 0.05,
        '"The Data So Far" from xkcd by Randall Munroe',
        ha\='center')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

#

![CLAIMS OF SUPERNATURAL POWERS](https://matplotlib.org/stable/_images/sphx_glr_xkcd_002_2_00x.png)

Tags: [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)
 [purpose: fun](https://matplotlib.org/stable/_tags/purpose-fun.html)

**Total running time of the script:** (0 minutes 1.119 seconds)

[`Download Jupyter notebook: xkcd.ipynb`](https://matplotlib.org/stable/_downloads/131d158e81b262ebc937088478d60b25/xkcd.ipynb)

[`Download Python source code: xkcd.py`](https://matplotlib.org/stable/_downloads/8a2ff25ab36d899da6c1187a40d64075/xkcd.py)

[`Download zipped: xkcd.zip`](https://matplotlib.org/stable/_downloads/160adb8d85384e90401ae9fb0d00972b/xkcd.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)