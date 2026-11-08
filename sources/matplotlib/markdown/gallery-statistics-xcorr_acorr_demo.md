[Skip to main content](https://matplotlib.org/stable/gallery/statistics/xcorr_acorr_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/xcorr_acorr_demo.html#sphx-glr-download-gallery-statistics-xcorr-acorr-demo-py)
 to download the full example code.

Cross- and auto-correlation[#](https://matplotlib.org/stable/gallery/statistics/xcorr_acorr_demo.html#cross-and-auto-correlation "Link to this heading")

=========================================================================================================================================================

Example use of cross-correlation ([`xcorr`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xcorr.html#matplotlib.axes.Axes.xcorr "matplotlib.axes.Axes.xcorr")
) and auto-correlation ([`acorr`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.acorr.html#matplotlib.axes.Axes.acorr "matplotlib.axes.Axes.acorr")
) plots.

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(2, 100)
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, \[[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\] \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 1, sharex\=True)
[ax1.xcorr](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xcorr.html#matplotlib.axes.Axes.xcorr "matplotlib.axes.Axes.xcorr")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, usevlines\=True, maxlags\=50, normed\=True, lw\=2)
[ax1.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(True)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Cross-correlation (xcorr)')

[ax2.acorr](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.acorr.html#matplotlib.axes.Axes.acorr "matplotlib.axes.Axes.acorr")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, usevlines\=True, normed\=True, maxlags\=50, lw\=2)
[ax2.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html#matplotlib.axes.Axes.grid "matplotlib.axes.Axes.grid")
(True)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Auto-correlation (acorr)')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Cross-correlation (xcorr), Auto-correlation (acorr)](https://matplotlib.org/stable/_images/sphx_glr_xcorr_acorr_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.acorr`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.acorr.html#matplotlib.axes.Axes.acorr "matplotlib.axes.Axes.acorr")
     / [`matplotlib.pyplot.acorr`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.acorr.html#matplotlib.pyplot.acorr "matplotlib.pyplot.acorr")
    
*   [`matplotlib.axes.Axes.xcorr`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xcorr.html#matplotlib.axes.Axes.xcorr "matplotlib.axes.Axes.xcorr")
     / [`matplotlib.pyplot.xcorr`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xcorr.html#matplotlib.pyplot.xcorr "matplotlib.pyplot.xcorr")
    

Tags: [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: xcorr_acorr_demo.ipynb`](https://matplotlib.org/stable/_downloads/a95967eaf6f6e1c9caf8dc0e9e980f4d/xcorr_acorr_demo.ipynb)

[`Download Python source code: xcorr_acorr_demo.py`](https://matplotlib.org/stable/_downloads/422be99b36c9fb41febce9e1f21a5401/xcorr_acorr_demo.py)

[`Download zipped: xcorr_acorr_demo.zip`](https://matplotlib.org/stable/_downloads/d7b365fd19270eef537c574f32a0e007/xcorr_acorr_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)