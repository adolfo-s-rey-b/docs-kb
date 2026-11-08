[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-download-gallery-lines-bars-and-markers-categorical-variables-py)
 to download the full example code.

Plotting categorical variables[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#plotting-categorical-variables "Link to this heading")

=================================================================================================================================================================================

You can pass categorical values (i.e. strings) directly as x- or y-values to many plotting functions:

import matplotlib.pyplot as plt

[data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
[names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list([data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.keys())
[values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list([data](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.[values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
())

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 3, figsize\=(9, 3), sharey\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].bar([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].scatter([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\].plot([names](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [values](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
('Categorical Plotting')

![Categorical Plotting](https://matplotlib.org/stable/_images/sphx_glr_categorical_variables_001_2_00x.png)

Categorical values are a mapping from names to positions. This means that values that occur multiple times are mapped to the same position. See the `cat` and `dog` values "happy" and "bored" on the y-axis in the following example.

[cat](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["bored", "happy", "bored", "bored", "happy", "bored"\]
[dog](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["happy", "happy", "happy", "happy", "bored", "bored"\]
[activity](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["combing", "drinking", "feeding", "napping", "playing", "washing"\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([activity](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [dog](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\="dog")
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([activity](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [cat](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, label\="cat")
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![categorical variables](https://matplotlib.org/stable/_images/sphx_glr_categorical_variables_002_2_00x.png)

Tags: [plot-type: specialty](https://matplotlib.org/stable/_tags/plot-type-specialty.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 1.250 seconds)

[`Download Jupyter notebook: categorical_variables.ipynb`](https://matplotlib.org/stable/_downloads/d1c8c37ff80ab9e3bf629e2b952c89a1/categorical_variables.ipynb)

[`Download Python source code: categorical_variables.py`](https://matplotlib.org/stable/_downloads/1cca3eedfb7940413267d0c7ae15d169/categorical_variables.py)

[`Download zipped: categorical_variables.zip`](https://matplotlib.org/stable/_downloads/d1680faf43cc055f3db7bf337ffac326/categorical_variables.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)