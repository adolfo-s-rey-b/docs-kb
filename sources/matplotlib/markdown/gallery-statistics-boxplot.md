[Skip to main content](https://matplotlib.org/stable/gallery/statistics/boxplot.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/statistics/boxplot.html#sphx-glr-download-gallery-statistics-boxplot-py)
 to download the full example code.

Artist customization in box plots[#](https://matplotlib.org/stable/gallery/statistics/boxplot.html#artist-customization-in-box-plots "Link to this heading")

=============================================================================================================================================================

This example demonstrates how to use the various keyword arguments to fully customize box plots. The first figure demonstrates how to remove and add individual components (note that the mean is the only value not shown by default). The second figure demonstrates how the styles of the artists can be customized. It also demonstrates how to set the limit of the whiskers to specific percentiles (lower right Axes)

A good general reference on boxplots and their history can be found here: [https://vita.had.co.nz/papers/boxplots.pdf](https://vita.had.co.nz/papers/boxplots.pdf)

import matplotlib.pyplot as plt
import numpy as np

\# fake data
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.lognormal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.lognormal.html#numpy.random.lognormal "numpy.random.lognormal")
(size\=(37, 4), mean\=1.5, sigma\=1.75)
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= list('ABCD')
[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 10  \# fontsize

Demonstrate how to toggle the display of different elements:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=3, figsize\=(6, 6), sharey\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, tick\_labels\=[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_title('Default', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, tick\_labels\=[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, showmeans\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_title('showmeans=True', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, tick\_labels\=[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, showmeans\=True, meanline\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].set\_title('showmeans=True,\\nmeanline=True', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, tick\_labels\=[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, showbox\=False, showcaps\=False)
[tufte\_title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= 'Tufte Style \\n(showbox=False,\\nshowcaps=False)'
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].set\_title([tufte\_title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, tick\_labels\=[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, notch\=True, bootstrap\=10000)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_title('notch=True,\\nbootstrap=10000', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, tick\_labels\=[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, showfliers\=False)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].set\_title('showfliers=False', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [ax.set\_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
('log')
    [ax.set\_yticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels")
(\[\])

[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(hspace\=0.4)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Default, showmeans=True, showmeans=True, meanline=True, Tufte Style  (showbox=False, showcaps=False), notch=True, bootstrap=10000, showfliers=False](https://matplotlib.org/stable/_images/sphx_glr_boxplot_001_2_00x.png)

Demonstrate how to customize the display different elements:

[boxprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(linestyle\='--', linewidth\=3, color\='darkgoldenrod')
[flierprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(marker\='o', markerfacecolor\='green', markersize\=12,
                  markeredgecolor\='none')
[medianprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(linestyle\='-.', linewidth\=2.5, color\='firebrick')
[meanpointprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(marker\='D', markeredgecolor\='black',
                      markerfacecolor\='firebrick')
[meanlineprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(linestyle\='--', linewidth\=2.5, color\='purple')

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, ncols\=3, figsize\=(6, 6), sharey\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [boxprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\=[boxprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].set\_title('Custom boxprops', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [flierprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\=[flierprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, [medianprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\=[medianprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 1\].set\_title('Custom medianprops\\nand flierprops', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, whis\=(0, 100))
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 2\].set\_title('whis=(0, 100)', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, meanprops\=[meanpointprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, meanline\=False,
                  showmeans\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 0\].set\_title('Custom mean\\nas point', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, meanprops\=[meanlineprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, meanline\=True,
                  showmeans\=True)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 1\].set\_title('Custom mean\\nas line', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].boxplot([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, whis\=\[15, 85\])
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1, 2\].set\_title('whis=\[15, 85\]\\n#percentiles', fontsize\=[fs](https://docs.python.org/3/library/functions.html#int "builtins.int")
)

for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
    [ax.set\_yscale](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yscale.html#matplotlib.axes.Axes.set_yscale "matplotlib.axes.Axes.set_yscale")
('log')
    [ax.set\_yticklabels](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html#matplotlib.axes.Axes.set_yticklabels "matplotlib.axes.Axes.set_yticklabels")
(\[\])

[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("I never said they'd be pretty")
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(hspace\=0.4)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![I never said they'd be pretty, Custom boxprops, Custom medianprops and flierprops, whis=(0, 100), Custom mean as point, Custom mean as line, whis=[15, 85] #percentiles](https://matplotlib.org/stable/_images/sphx_glr_boxplot_002_2_00x.png)

Tags: [plot-type: boxplot](https://matplotlib.org/stable/_tags/plot-type-boxplot.html)
 [domain: statistics](https://matplotlib.org/stable/_tags/domain-statistics.html)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot "matplotlib.axes.Axes.boxplot")
     / [`matplotlib.pyplot.boxplot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html#matplotlib.pyplot.boxplot "matplotlib.pyplot.boxplot")
    

**Total running time of the script:** (0 minutes 3.419 seconds)

[`Download Jupyter notebook: boxplot.ipynb`](https://matplotlib.org/stable/_downloads/43dfdc3242d6e3f7d2a54971e771b799/boxplot.ipynb)

[`Download Python source code: boxplot.py`](https://matplotlib.org/stable/_downloads/91eae76e954fa871772e65b23de96ffe/boxplot.py)

[`Download zipped: boxplot.zip`](https://matplotlib.org/stable/_downloads/4a138d640ccc764c6d3a9023ced9b592/boxplot.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)