[Skip to main content](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html#sphx-glr-download-gallery-pie-and-polar-charts-nested-pie-py)
 to download the full example code.

Nested pie charts[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html#nested-pie-charts "Link to this heading")

==========================================================================================================================================

The following examples show two ways to build a nested pie chart in Matplotlib. Such charts are often referred to as donut charts.

See also the [Left ventricle bullseye](https://matplotlib.org/stable/gallery/specialty_plots/leftventricle_bullseye.html)
 example.

import matplotlib.pyplot as plt
import numpy as np

The most straightforward way to build a pie chart is to use the [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
 method.

In this case, pie takes values corresponding to counts in a group. We'll first generate some fake data, corresponding to three groups. In the inner circle, we'll treat each number as belonging to its own group. In the outer circle, we'll plot them as members of their original 3 groups.

The effect of the donut shape is achieved by setting a `width` to the pie's wedges through the _wedgeprops_ argument.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[size](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.3
[vals](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[60., 32.\], \[37., 40.\], \[29., 10.\]\])

[tab20c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= [plt.color\_sequences](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ColorSequenceRegistry.html#matplotlib.colors.ColorSequenceRegistry "matplotlib.colors.ColorSequenceRegistry")
\["tab20c"\]
[outer\_colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \[[tab20c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[i\] for i in \[0, 4, 8\]\]
[inner\_colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= \[[tab20c](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\[i\] for i in \[1, 2, 5, 6, 9, 10\]\]

[ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([vals](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.sum(axis\=1), radius\=1, colors\=[outer\_colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
       wedgeprops\=dict(width\=[size](https://docs.python.org/3/library/functions.html#float "builtins.float")
, edgecolor\='w'))

[ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([vals](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.flatten(), radius\=1\-[size](https://docs.python.org/3/library/functions.html#float "builtins.float")
, colors\=[inner\_colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
,
       wedgeprops\=dict(width\=[size](https://docs.python.org/3/library/functions.html#float "builtins.float")
, edgecolor\='w'))

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(aspect\="equal", title\='Pie plot with \`ax.pie\`')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Pie plot with `ax.pie`](https://matplotlib.org/stable/_images/sphx_glr_nested_pie_001_2_00x.png)

However, you can accomplish the same output by using a bar plot on Axes with a polar coordinate system. This may give more flexibility on the exact design of the plot.

In this case, we need to map x-values of the bar chart onto radians of a circle. The cumulative sum of the values are used as the edges of the bars.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(subplot\_kw\=dict(projection\="polar"))

[size](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.3
[vals](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[\[60., 32.\], \[37., 40.\], \[29., 10.\]\])
\# Normalize vals to 2 pi
[valsnorm](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [vals](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/[np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
([vals](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)\*2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\# Obtain the ordinates of the bar edges
[valsleft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.cumsum](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")
([np.append](https://numpy.org/doc/stable/reference/generated/numpy.append.html#numpy.append "numpy.append")
(0, [valsnorm](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.flatten()\[:\-1\])).reshape([vals.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
 \= [plt.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\["tab20c"\]
[outer\_colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
([np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(3)\*4)
[inner\_colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.ListedColormap.html#matplotlib.colors.ListedColormap "matplotlib.colors.ListedColormap")
(\[1, 2, 5, 6, 9, 10\])

[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
(x\=[valsleft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, 0\],
       width\=[valsnorm](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.sum(axis\=1), bottom\=1\-[size](https://docs.python.org/3/library/functions.html#float "builtins.float")
, height\=[size](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
       color\=[outer\_colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, edgecolor\='w', linewidth\=1, align\="edge")

[ax.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
(x\=[valsleft](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.flatten(),
       width\=[valsnorm](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.flatten(), bottom\=1\-2\*[size](https://docs.python.org/3/library/functions.html#float "builtins.float")
, height\=[size](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
       color\=[inner\_colors](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, edgecolor\='w', linewidth\=1, align\="edge")

[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(title\="Pie plot with \`ax.bar\` and polar coordinates")
[ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Pie plot with `ax.bar` and polar coordinates](https://matplotlib.org/stable/_images/sphx_glr_nested_pie_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
     / [`matplotlib.pyplot.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie "matplotlib.pyplot.pie")
    
*   [`matplotlib.axes.Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
     / [`matplotlib.pyplot.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
    
*   [`matplotlib.projections.polar`](https://matplotlib.org/stable/api/projections/polar.html#module-matplotlib.projections.polar "matplotlib.projections.polar")
    
*   `Axes.set` ([`matplotlib.artist.Artist.set`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set.html#matplotlib.artist.Artist.set "matplotlib.artist.Artist.set")
    )
    
*   [`matplotlib.axes.Axes.set_axis_off`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
    

Tags: [plot-type: pie](https://matplotlib.org/stable/_tags/plot-type-pie.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)
 [purpose: showcase](https://matplotlib.org/stable/_tags/purpose-showcase.html)

[`Download Jupyter notebook: nested_pie.ipynb`](https://matplotlib.org/stable/_downloads/5b2548c8549bd695e969cc65e29bd3c5/nested_pie.ipynb)

[`Download Python source code: nested_pie.py`](https://matplotlib.org/stable/_downloads/aeb91f5a1cf185045e90c1aa9f6d1c81/nested_pie.py)

[`Download zipped: nested_pie.zip`](https://matplotlib.org/stable/_downloads/6436f2b2833f023fa29a82ca341c7aec/nested_pie.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)