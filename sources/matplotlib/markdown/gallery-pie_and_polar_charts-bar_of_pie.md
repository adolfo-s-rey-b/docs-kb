[Skip to main content](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html#sphx-glr-download-gallery-pie-and-polar-charts-bar-of-pie-py)
 to download the full example code.

Bar of pie[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/bar_of_pie.html#bar-of-pie "Link to this heading")

============================================================================================================================

Make a "bar of pie" chart where the first slice of the pie is "exploded" into a bar chart with a further breakdown of said slice's characteristics. The example demonstrates using a figure with multiple sets of Axes and using the Axes patches list to add two ConnectionPatches to link the subplot charts.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [ConnectionPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")

\# make figure and assign axis objects
[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(9, 5))
[fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(wspace\=0)

\# pie chart parameters
[overall\_ratios](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[.27, .56, .17\]
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['Approve', 'Disapprove', 'Undecided'\]
[explode](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[0.1, 0, 0\]
\# rotate so that first wedge is split by the x-axis
[angle](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= \-180 \* [overall\_ratios](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\]
[pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 \= [ax1.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([overall\_ratios](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, autopct\='%1.1f%%', startangle\=[angle](https://docs.python.org/3/library/functions.html#float "builtins.float")
,
              [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [explode](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[explode](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

\# bar chart parameters
[age\_ratios](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[.33, .54, .07, .06\]
[age\_labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['Under 35', '35-49', '50-65', 'Over 65'\]
[bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1
[width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= .2

\# Adding from the top matches the legend.
for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
, ([height](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
) in enumerate(reversed(\[\*zip([age\_ratios](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
, [age\_labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
)\])):
    [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \-= [height](https://docs.python.org/3/library/functions.html#float "builtins.float")
    [bc](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 \= [ax2.bar](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
(0, [height](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
\=[bottom](https://docs.python.org/3/library/functions.html#float "builtins.float")
, color\='C0', [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
                 alpha\=0.1 + 0.25 \* [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [ax2.bar\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar_label.html#matplotlib.axes.Axes.bar_label "matplotlib.axes.Axes.bar_label")
([bc](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=\[f"{[height](https://docs.python.org/3/library/functions.html#float "builtins.float")\
:.0%}"\], label\_type\='center')

[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Age of approvers')
[ax2.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()
[ax2.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
('off')
[ax2.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(\- 2.5 \* [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 2.5 \* [width](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

\# use ConnectionPatch to draw lines between the two plots
[theta1](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [theta2](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [pie.wedges](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\].[theta1](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [pie.wedges](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\].[theta2](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
[center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [r](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [pie.wedges](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\].[center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [pie.wedges](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\].[r](https://docs.python.org/3/library/functions.html#int "builtins.int")
[bar\_height](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= sum([age\_ratios](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

\# draw top connecting line
[x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [r](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 180 \* [theta2](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
) + [center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\]
[y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [r](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 180 \* [theta2](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
) + [center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\]
[con](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
 \= [ConnectionPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
(xyA\=(\-[width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2, [bar\_height](https://docs.python.org/3/library/functions.html#float "builtins.float")
), coordsA\=[ax2.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
,
                      xyB\=([x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
), coordsB\=[ax1.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
)
[con.set\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color "matplotlib.patches.Patch.set_color")
(\[0, 0, 0\])
[con.set\_linewidth](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth")
(4)
[ax2.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([con](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
)

\# draw bottom connecting line
[x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [r](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 180 \* [theta1](https://docs.python.org/3/library/functions.html#float "builtins.float")
) + [center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\]
[y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [r](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 180 \* [theta1](https://docs.python.org/3/library/functions.html#float "builtins.float")
) + [center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[1\]
[con](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
 \= [ConnectionPatch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
(xyA\=(\-[width](https://docs.python.org/3/library/functions.html#float "builtins.float")
 / 2, 0), coordsA\=[ax2.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
,
                      xyB\=([x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
), coordsB\=[ax1.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
)
[con.set\_color](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_color "matplotlib.patches.Patch.set_color")
(\[0, 0, 0\])
[ax2.add\_artist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
([con](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
)
[con.set\_linewidth](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch.set_linewidth "matplotlib.patches.Patch.set_linewidth")
(4)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Age of approvers](https://matplotlib.org/stable/_images/sphx_glr_bar_of_pie_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar "matplotlib.axes.Axes.bar")
     / [`matplotlib.pyplot.bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar "matplotlib.pyplot.bar")
    
*   [`matplotlib.axes.Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
     / [`matplotlib.pyplot.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie "matplotlib.pyplot.pie")
    
*   [`matplotlib.patches.ConnectionPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.ConnectionPatch.html#matplotlib.patches.ConnectionPatch "matplotlib.patches.ConnectionPatch")
    

Tags: [component: subplot](https://matplotlib.org/stable/_tags/component-subplot.html)
 [plot-type: pie](https://matplotlib.org/stable/_tags/plot-type-pie.html)
 [plot-type: bar](https://matplotlib.org/stable/_tags/plot-type-bar.html)
 [level: intermediate](https://matplotlib.org/stable/_tags/level-intermediate.html)
 [purpose: showcase](https://matplotlib.org/stable/_tags/purpose-showcase.html)

[`Download Jupyter notebook: bar_of_pie.ipynb`](https://matplotlib.org/stable/_downloads/7a222153a650a0e97d03f638e371556f/bar_of_pie.ipynb)

[`Download Python source code: bar_of_pie.py`](https://matplotlib.org/stable/_downloads/b14f56c0ed0bf29c1b150290df6f369a/bar_of_pie.py)

[`Download zipped: bar_of_pie.zip`](https://matplotlib.org/stable/_downloads/c10a940ef73acb1dadf2c52ed37ee8a8/bar_of_pie.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)