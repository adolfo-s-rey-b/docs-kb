[Skip to main content](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-download-gallery-pie-and-polar-charts-pie-features-py)
 to download the full example code.

Pie charts[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#pie-charts "Link to this heading")

==============================================================================================================================

Demo of plotting a pie chart.

This example illustrates various parameters of [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
.

Label slices[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#label-slices "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Plot a pie chart of animals and label the slices. To add labels, pass a list of labels to the _labels_ parameter

import matplotlib.pyplot as plt

[labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= 'Frogs', 'Hogs', 'Dogs', 'Logs'
[sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[15, 30, 45, 10\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)

![pie features](https://matplotlib.org/stable/_images/sphx_glr_pie_features_001_2_00x.png)

Each slice of the pie chart is a [`patches.Wedge`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
 object; therefore in addition to the customizations shown here, each wedge can be customized using the _wedgeprops_ argument, as demonstrated in [Nested pie charts](https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html)
.

Auto-label slices[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#auto-label-slices "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

Pass a function or format string to _autopct_ to label slices.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, autopct\='%1.1f%%')

![pie features](https://matplotlib.org/stable/_images/sphx_glr_pie_features_002_2_00x.png)

By default, the label values are obtained from the percent size of the slice.

Color slices[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#color-slices "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Pass a list of colors to _colors_ to set the color of each slice.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
,
       colors\=\['olivedrab', 'rosybrown', 'gray', 'saddlebrown'\])

![pie features](https://matplotlib.org/stable/_images/sphx_glr_pie_features_003_2_00x.png)

Hatch slices[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#hatch-slices "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Pass a list of hatch patterns to _hatch_ to set the pattern of each slice.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, hatch\=\['\*\*O', 'oO', 'O.O', '.||.'\])

![pie features](https://matplotlib.org/stable/_images/sphx_glr_pie_features_004_2_00x.png)

Swap label and autopct text positions[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#swap-label-and-autopct-text-positions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the _labeldistance_ and _pctdistance_ parameters to position the _labels_ and _autopct_ text respectively.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, autopct\='%1.1f%%',
       pctdistance\=1.25, labeldistance\=.6)

![pie features](https://matplotlib.org/stable/_images/sphx_glr_pie_features_005_2_00x.png)

_labeldistance_ and _pctdistance_ are ratios of the radius; therefore they vary between `0` for the center of the pie and `1` for the edge of the pie, and can be set to greater than `1` to place text outside the pie.

Explode, shade, and rotate slices[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#explode-shade-and-rotate-slices "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to the basic pie chart, this demo shows a few optional features:

*   offsetting a slice using _explode_
    
*   add a drop-shadow using _shadow_
    
*   custom start angle using _startangle_
    

This example orders the slices, separates (explodes) them, and rotates them.

[explode](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (0, 0.1, 0, 0)  \# only "explode" the 2nd slice (i.e. 'Hogs')

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [explode](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[explode](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, autopct\='%1.1f%%',
       shadow\=True, startangle\=90)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![pie features](https://matplotlib.org/stable/_images/sphx_glr_pie_features_006_2_00x.png)

The default _startangle_ is 0, which would start the first slice ("Frogs") on the positive x-axis. This example sets `startangle = 90` such that all the slices are rotated counter-clockwise by 90 degrees, and the frog slice starts on the positive y-axis.

Grow or shrink pie[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#grow-or-shrink-pie "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

By changing the _radius_ parameter, and often the text size for better visual appearance, the pie chart can be scaled.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

[ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, autopct\='%.0f%%',
       textprops\={'size': 'small'}, radius\=0.5)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![pie features](https://matplotlib.org/stable/_images/sphx_glr_pie_features_007_2_00x.png)

Modify shadow[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#modify-shadow "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

The _shadow_ parameter may optionally take a dictionary with arguments to the [`Shadow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Shadow.html#matplotlib.patches.Shadow "matplotlib.patches.Shadow")
 patch. This can be used to modify the default shadow.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([sizes](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [explode](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[explode](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\=[labels](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, autopct\='%1.1f%%',
       shadow\={'ox': \-0.04, 'edgecolor': 'none', 'shade': 0.9}, startangle\=90)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![pie features](https://matplotlib.org/stable/_images/sphx_glr_pie_features_008_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
     / [`matplotlib.pyplot.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie "matplotlib.pyplot.pie")
    

Tags: [plot-type: pie](https://matplotlib.org/stable/_tags/plot-type-pie.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 2.713 seconds)

[`Download Jupyter notebook: pie_features.ipynb`](https://matplotlib.org/stable/_downloads/73a60ebdc8c6b15650865a49a3bb7d44/pie_features.ipynb)

[`Download Python source code: pie_features.py`](https://matplotlib.org/stable/_downloads/d1637d3ecea58588a83ea116a2883a26/pie_features.py)

[`Download zipped: pie_features.zip`](https://matplotlib.org/stable/_downloads/bab3cc1aa40a5404e184d0d0600fcbc5/pie_features.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page