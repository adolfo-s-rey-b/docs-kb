[Skip to main content](https://matplotlib.org/stable/gallery/color/set_alpha.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/color/set_alpha.html#sphx-glr-download-gallery-color-set-alpha-py)
 to download the full example code.

Ways to set a color's alpha value[#](https://matplotlib.org/stable/gallery/color/set_alpha.html#ways-to-set-a-color-s-alpha-value "Link to this heading")

==========================================================================================================================================================

Compare setting alpha by the _alpha_ keyword argument and by one of the Matplotlib color formats. Often, the _alpha_ keyword is the only tool needed to add transparency to a color. In some cases, the _(matplotlib\_color, alpha)_ color format provides an easy way to fine-tune the appearance of a Figure.

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility.
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(ncols\=2, figsize\=(8, 4))

[x\_values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[n for n in range(20)\]
[y\_values](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(20)

[facecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['green' if y \> 0 else 'red' for y in [y\_values](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\]
[edgecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [facecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")

[ax1.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([x\_values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y\_values](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\=[facecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, edgecolor\=[edgecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, alpha\=0.5)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Explicit 'alpha' keyword value\\nshared by all bars and edges")

\# Normalize y values to get distinct face alpha values.
[abs\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[abs(y) for y in [y\_values](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\]
[face\_alphas](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[n / max([abs\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
) for n in [abs\_y](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\]
[edge\_alphas](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[1 \- alpha for alpha in [face\_alphas](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\]

[colors\_with\_alphas](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list(zip([facecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [face\_alphas](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))
[edgecolors\_with\_alphas](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list(zip([edgecolors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [edge\_alphas](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))

[ax2.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([x\_values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [y\_values](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\=[colors\_with\_alphas](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
        edgecolor\=[edgecolors\_with\_alphas](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Normalized alphas for\\neach bar and each edge')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Explicit 'alpha' keyword value shared by all bars and edges, Normalized alphas for each bar and each edge](https://matplotlib.org/stable/_images/sphx_glr_set_alpha_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
    
*   [`matplotlib.pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
    

Tags: [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: set_alpha.ipynb`](https://matplotlib.org/stable/_downloads/3ef845f9a2adcd4ab9114e0f796b40ae/set_alpha.ipynb)

[`Download Python source code: set_alpha.py`](https://matplotlib.org/stable/_downloads/8ac9df75950acff1ebf040a1d2761824/set_alpha.py)

[`Download zipped: set_alpha.zip`](https://matplotlib.org/stable/_downloads/8ce35c0c5f9e0ce890695337afad6ce9/set_alpha.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)