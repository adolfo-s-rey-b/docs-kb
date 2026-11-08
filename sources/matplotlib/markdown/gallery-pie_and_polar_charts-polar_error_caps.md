[Skip to main content](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_error_caps.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_error_caps.html#sphx-glr-download-gallery-pie-and-polar-charts-polar-error-caps-py)
 to download the full example code.

Error bar rendering on polar axis[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_error_caps.html#error-bar-rendering-on-polar-axis "Link to this heading")

================================================================================================================================================================================

Demo of error bar plot in polar coordinates. Theta error bars are curved lines ended with caps oriented towards the center. Radius error bars are straight lines oriented towards center with perpendicular caps.

import matplotlib.pyplot as plt
import numpy as np

[theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 4)
[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2 + 0.5

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 10))
ax \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\='polar')
[ax.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, xerr\=0.25, yerr\=0.1, capsize\=7, fmt\="o", c\="seagreen")
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Pretty polar error bars")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Pretty polar error bars](https://matplotlib.org/stable/_images/sphx_glr_polar_error_caps_001_2_00x.png)

Please acknowledge that large theta error bars will be overlapping. This may reduce readability of the output plot. See example figure below:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 10))
ax \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\='polar')
[ax.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, xerr\=5.25, yerr\=0.1, capsize\=7, fmt\="o", c\="darkred")
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Overlapping theta error bars")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Overlapping theta error bars](https://matplotlib.org/stable/_images/sphx_glr_polar_error_caps_002_2_00x.png)

On the other hand, large radius error bars will never overlap, they just lead to unwanted scale in the data, reducing the displayed range.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(10, 10))
ax \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(projection\='polar')
[ax.errorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
([theta](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, xerr\=0.25, yerr\=10.1, capsize\=7, fmt\="o", c\="orangered")
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Large radius error bars")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Large radius error bars](https://matplotlib.org/stable/_images/sphx_glr_polar_error_caps_003_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.errorbar.html#matplotlib.axes.Axes.errorbar "matplotlib.axes.Axes.errorbar")
     / [`matplotlib.pyplot.errorbar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html#matplotlib.pyplot.errorbar "matplotlib.pyplot.errorbar")
    
*   [`matplotlib.projections.polar`](https://matplotlib.org/stable/api/projections/polar.html#module-matplotlib.projections.polar "matplotlib.projections.polar")
    

Tags: [component: error](https://matplotlib.org/stable/_tags/component-error.html)
 [plot-type: errorbar](https://matplotlib.org/stable/_tags/plot-type-errorbar.html)
 [plot-type: polar](https://matplotlib.org/stable/_tags/plot-type-polar.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 3.913 seconds)

[`Download Jupyter notebook: polar_error_caps.ipynb`](https://matplotlib.org/stable/_downloads/122ae47afe79631d03542f6649990d9d/polar_error_caps.ipynb)

[`Download Python source code: polar_error_caps.py`](https://matplotlib.org/stable/_downloads/3a181fd218a35ba7aa01a74c98e3a9c6/polar_error_caps.py)

[`Download zipped: polar_error_caps.zip`](https://matplotlib.org/stable/_downloads/798c7e176cb4a3364f8fd57866e96209/polar_error_caps.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)