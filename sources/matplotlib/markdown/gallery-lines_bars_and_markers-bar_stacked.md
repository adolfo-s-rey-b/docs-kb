[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-download-gallery-lines-bars-and-markers-bar-stacked-py)
 to download the full example code.

Stacked bar chart[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#stacked-bar-chart "Link to this heading")

=============================================================================================================================================

This is an example of creating a stacked bar plot using [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
.

import matplotlib.pyplot as plt
import numpy as np

\# data from https://allisonhorst.github.io/palmerpenguins/

[species](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (
    "Adelie\\n $\\\\mu=$3700.66g",
    "Chinstrap\\n $\\\\mu=$3733.09g",
    "Gentoo\\n $\\\\mu=5076.02g$",
)
[weight\_counts](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {
    "Below": [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[70, 31, 58\]),
    "Above": [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[82, 37, 66\]),
}
[width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.5

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.zeros](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")
(3)

for [boolean](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [weight\_count](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 in [weight\_counts](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():
    [p](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 \= [ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
([species](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [weight\_count](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, label\=[boolean](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=[bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    [bottom](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 += [weight\_count](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Number of penguins with above average body mass")
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
(loc\="upper right")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Number of penguins with above average body mass](https://matplotlib.org/stable/_images/sphx_glr_bar_stacked_001_2_00x.png)

Tags: [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: bar_stacked.ipynb`](https://matplotlib.org/stable/_downloads/1bc85d47f3eb5c94245f86588b29de05/bar_stacked.ipynb)

[`Download Python source code: bar_stacked.py`](https://matplotlib.org/stable/_downloads/2ac62a2edbb00a99e8a853b17387ef14/bar_stacked.py)

[`Download zipped: bar_stacked.zip`](https://matplotlib.org/stable/_downloads/8c5451baed7a91246da43e1aa7328c3e/bar_stacked.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)