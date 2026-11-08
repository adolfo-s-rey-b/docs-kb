[Skip to main content](https://matplotlib.org/stable/gallery/specialty_plots/anscombe.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/specialty_plots/anscombe.html#sphx-glr-download-gallery-specialty-plots-anscombe-py)
 to download the full example code.

Anscombe's quartet[#](https://matplotlib.org/stable/gallery/specialty_plots/anscombe.html#anscombe-s-quartet "Link to this heading")

=====================================================================================================================================

[Anscombe's quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet)
 is a group of datasets (x, y) that have the same mean, standard deviation, and regression line, but which are qualitatively different.

It is often used to illustrate the importance of looking at a set of data graphically and not only relying on basic statistic properties.

import matplotlib.pyplot as plt
import numpy as np

[x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5\]
[y1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68\]
[y2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74\]
[y3](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73\]
[x4](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8\]
[y4](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89\]

[datasets](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    'I': ([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
),
    'II': ([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
),
    'III': ([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y3](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
),
    'IV': ([x4](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y4](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
}

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(2, 2, sharex\=True, sharey\=True, figsize\=(6, 6),
                        gridspec\_kw\={'wspace': 0.08, 'hspace': 0.08})
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set(xlim\=(0, 20), ylim\=(2, 14))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set(xticks\=(0, 10, 20), yticks\=(4, 8, 12))

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, ([label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, ([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)) in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, [datasets](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items()):
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.1, 0.9, [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontsize\=20, transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, va\='top')
    [ax.tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
(direction\='in', top\=True, right\=True)
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, 'o')

    \# linear regression
    [p1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [p0](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [np.polyfit](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")
([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, deg\=1)  \# slope, intercept
    [ax.axline](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html#matplotlib.axes.Axes.axline "matplotlib.axes.Axes.axline")
(xy1\=(0, [p0](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
), slope\=[p1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, color\='r', lw\=2)

    \# add text box for the statistics
    [stats](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= (f'$\\\\mu$ = {[np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
([y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):.2f}\\n'
             f'$\\\\sigma$ = {[np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html#numpy.std "numpy.std")
([y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):.2f}\\n'
             f'$r$ = {[np.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef")
([x](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)\[0\]\[1\]:.2f}')
    [bbox](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(boxstyle\='round', fc\='blanchedalmond', ec\='orange', alpha\=0.5)
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.95, 0.07, [stats](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontsize\=9, [bbox](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\=[bbox](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
,
            transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
, horizontalalignment\='right')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![anscombe](https://matplotlib.org/stable/_images/sphx_glr_anscombe_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.axline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html#matplotlib.axes.Axes.axline "matplotlib.axes.Axes.axline")
     / [`matplotlib.pyplot.axline`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axline.html#matplotlib.pyplot.axline "matplotlib.pyplot.axline")
    
*   [`matplotlib.axes.Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
     / [`matplotlib.pyplot.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
    
*   [`matplotlib.axes.Axes.tick_params`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html#matplotlib.axes.Axes.tick_params "matplotlib.axes.Axes.tick_params")
     / matplotlib.pyplot.tick\_params\`
    

[`Download Jupyter notebook: anscombe.ipynb`](https://matplotlib.org/stable/_downloads/971d06df440941179dfdec3a81a5a048/anscombe.ipynb)

[`Download Python source code: anscombe.py`](https://matplotlib.org/stable/_downloads/a1864552db7c65c7d6ba6abe05cfe4a8/anscombe.py)

[`Download zipped: anscombe.zip`](https://matplotlib.org/stable/_downloads/9e065a96d3e14af21ac5f89e8ad30036/anscombe.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)