[Skip to main content](https://matplotlib.org/stable/gallery/statistics/boxplot_color.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/boxplot_color.html#sphx-glr-download-gallery-statistics-boxplot-color-py)
 to download the full example code.

Box plots with custom fill colors[#](https://matplotlib.org/stable/gallery/statistics/boxplot_color.html#box-plots-with-custom-fill-colors "Link to this heading")

===================================================================================================================================================================

To color each box of a box plot individually:

1.  use the keyword argument `patch_artist=True` to create filled boxes.
    
2.  loop through the created boxes and adapt their color.
    

import matplotlib.pyplot as plt
import numpy as np

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[fruit\_weights](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\
    [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")\
(130, 10, size\=100),\
    [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")\
(125, 20, size\=100),\
    [np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")\
(120, 30, size\=100),\
\]
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['peaches', 'oranges', 'tomatoes'\]
[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['peachpuff', 'orange', 'tomato'\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('fruit weight (g)')

[bplot](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [ax.boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
([fruit\_weights](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
                   patch\_artist\=True,  \# fill with color
                   tick\_labels\=[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)  \# will be used to label x-ticks

\# fill with colors
for [patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
, [color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([bplot](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['boxes'\], [colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [patch.set\_facecolor](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_facecolor "matplotlib.patches.Patch.set_facecolor")
([color](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![boxplot color](https://matplotlib.org/stable/_images/sphx_glr_boxplot_color_001_2_00x.png)

Tags: [styling: color](https://matplotlib.org/stable/_tags/styling-color.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)
 [plot-type: boxplot](https://matplotlib.org/stable/_tags/plot-type-boxplot.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
     / [`matplotlib.pyplot.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")
    

[`Download Jupyter notebook: boxplot_color.ipynb`](https://matplotlib.org/stable/_downloads/cab87f33fe8231420d0cdca293f6b8eb/boxplot_color.ipynb)

[`Download Python source code: boxplot_color.py`](https://matplotlib.org/stable/_downloads/38761f6a99c4cb7b7f91b79f2d3cbea4/boxplot_color.py)

[`Download zipped: boxplot_color.zip`](https://matplotlib.org/stable/_downloads/6bc53a259ab3b6d1f1f2149f5c1c362c/boxplot_color.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)