[Skip to main content](https://matplotlib.org/stable/gallery/statistics/customized_violin.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/customized_violin.html#sphx-glr-download-gallery-statistics-customized-violin-py)
 to download the full example code.

Violin plot customization[#](https://matplotlib.org/stable/gallery/statistics/customized_violin.html#violin-plot-customization "Link to this heading")

=======================================================================================================================================================

This example demonstrates how to fully customize violin plots. The first plot shows the default style by providing only the data. The second plot first limits what Matplotlib draws with additional keyword arguments. Then a simplified representation of a box plot is drawn on top. Lastly, the styles of the artists of the violins are modified.

For more information on violin plots, the scikit-learn docs have a great section: [https://scikit-learn.org/stable/modules/density.html](https://scikit-learn.org/stable/modules/density.html)

import matplotlib.pyplot as plt
import numpy as np

def adjacent\_values(vals, q1, q3):
    upper\_adjacent\_value \= q3 + (q3 \- q1) \* 1.5
    upper\_adjacent\_value \= [np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
(upper\_adjacent\_value, q3, vals\[\-1\])

    lower\_adjacent\_value \= q1 \- (q3 \- q1) \* 1.5
    lower\_adjacent\_value \= [np.clip](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
(lower\_adjacent\_value, vals\[0\], q1)
    return lower\_adjacent\_value, upper\_adjacent\_value

def set\_axis\_style([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ax.set\_xticks](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks "matplotlib.axes.Axes.set_xticks")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1, len([labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
) + 1), [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
    [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0.25, len([labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
) + 0.75)
    [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Sample name')

\# create test data
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[sorted([np.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy.random.normal "numpy.random.normal")\
(0, std, 100)) for std in range(1, 5)\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=1, ncols\=3, figsize\=(9, 3), sharey\=True)

[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Default violin plot')
[ax1.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Observed values')
[ax1.violinplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Set colors of violins')
[ax2.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Observed values')
[ax2.violinplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")
(
    [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
    facecolor\=\[('yellow', 0.3), ('blue', 0.3), ('red', 0.3), ('green', 0.3)\],
    linecolor\='black',
)
\# Note that when passing a sequence of colors, the method will repeat the sequence if
\# less colors are provided than data distributions.

[ax3.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Customized violin plot')
[parts](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [ax3.violinplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")
(
        [data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, showmeans\=False, showmedians\=False, showextrema\=False,
        facecolor\='#D43F3A', linecolor\='black')

for [pc](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.FillBetweenPolyCollection "matplotlib.collections.FillBetweenPolyCollection")
 in [parts](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['bodies'\]:
    [pc.set\_edgecolor](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.FillBetweenPolyCollection.set_edgecolor "matplotlib.collections.FillBetweenPolyCollection.set_edgecolor")
('black')
    [pc.set\_linewidth](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.FillBetweenPolyCollection.set_linewidth "matplotlib.collections.FillBetweenPolyCollection.set_linewidth")
(1)
    [pc.set\_alpha](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.FillBetweenPolyCollection.set_alpha "matplotlib.collections.FillBetweenPolyCollection.set_alpha")
(1)

[quartile1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [medians](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [quartile3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.percentile](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile "numpy.percentile")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, \[25, 50, 75\], axis\=1)
[whiskers](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\
    adjacent\_values(sorted\_array, q1, q3)\
    for sorted\_array, q1, q3 in zip([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
, [quartile1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, [quartile3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
)\])
[whiskers\_min](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [whiskers\_max](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [whiskers](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\], [whiskers](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 1\]

[inds](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(1, len([medians](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) + 1)
[ax3.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([inds](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [medians](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, marker\='o', color\='white', s\=30, zorder\=3)
[ax3.vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib.axes.Axes.vlines "matplotlib.axes.Axes.vlines")
([inds](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [quartile1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [quartile3](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='k', linestyle\='-', lw\=5)
[ax3.vlines](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib.axes.Axes.vlines "matplotlib.axes.Axes.vlines")
([inds](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [whiskers\_min](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [whiskers\_max](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='k', linestyle\='-', lw\=1)

\# set style for the axes
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['A', 'B', 'C', 'D'\]
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in \[[ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
, [ax3](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")\
\]:
    set\_axis\_style([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[plt.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots_adjust.html#matplotlib.pyplot.subplots_adjust "matplotlib.pyplot.subplots_adjust")
(bottom\=0.15, wspace\=0.05)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Default violin plot, Set colors of violins, Customized violin plot](https://matplotlib.org/stable/_images/sphx_glr_customized_violin_001_2_00x.png)

Tags: [plot-type: violin](https://matplotlib.org/stable/_tags/plot-type-violin.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.violinplot.html#matplotlib.axes.Axes.violinplot "matplotlib.axes.Axes.violinplot")
     / [`matplotlib.pyplot.violinplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html#matplotlib.pyplot.violinplot "matplotlib.pyplot.violinplot")
    
*   [`matplotlib.axes.Axes.vlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.vlines.html#matplotlib.axes.Axes.vlines "matplotlib.axes.Axes.vlines")
     / [`matplotlib.pyplot.vlines`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.vlines.html#matplotlib.pyplot.vlines "matplotlib.pyplot.vlines")
    

[`Download Jupyter notebook: customized_violin.ipynb`](https://matplotlib.org/stable/_downloads/d595ac356685e81c555d776a958885b3/customized_violin.ipynb)

[`Download Python source code: customized_violin.py`](https://matplotlib.org/stable/_downloads/b12095cadca065936a22019675f933dd/customized_violin.py)

[`Download zipped: customized_violin.zip`](https://matplotlib.org/stable/_downloads/35a97d1b165fddfc7eac01596acc1727/customized_violin.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)