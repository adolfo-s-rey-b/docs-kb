[Skip to main content](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_label.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_label.html#sphx-glr-download-gallery-pie-and-polar-charts-pie-label-py)
 to download the full example code.

Labeling pie charts[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_label.html#labeling-pie-charts "Link to this heading")

=============================================================================================================================================

This example illustrates some features of the [`pie_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
 method, which adds labels to an existing pie chart created with [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
.

The simplest option is to provide a list of strings to label each slice of the pie.

import matplotlib.pyplot as plt

[data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[36, 24, 8, 12\]
[labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['spam', 'eggs', 'bacon', 'sausage'\]

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 \= [ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.pie\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
([pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

![pie label](https://matplotlib.org/stable/_images/sphx_glr_pie_label_001_2_00x.png)

If you want the labels outside the pie, set a _distance_ greater than 1. This is the distance from the center of the pie as a fraction of its radius.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 \= [ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.pie\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
([pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, distance\=1.1)

![pie label](https://matplotlib.org/stable/_images/sphx_glr_pie_label_002_2_00x.png)

You can also rotate the labels so they are oriented away from the pie center.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 \= [ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.pie\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
([pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, rotate\=True)

![pie label](https://matplotlib.org/stable/_images/sphx_glr_pie_label_003_2_00x.png)

Instead of explicit labels, pass a format string to label slices with their values...

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 \= [ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.pie\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
([pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
, '{absval:.1f}')

![pie label](https://matplotlib.org/stable/_images/sphx_glr_pie_label_004_2_00x.png)

...or with their percentages...

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 \= [ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.pie\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
([pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
, '{frac:.1%}')

![pie label](https://matplotlib.org/stable/_images/sphx_glr_pie_label_005_2_00x.png)

...or both.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 \= [ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.pie\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
([pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
, '{absval:d}\\n{frac:.1%}')

![pie label](https://matplotlib.org/stable/_images/sphx_glr_pie_label_006_2_00x.png)

Font styling can be configured by passing a dictionary to the _textprops_ parameter.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 \= [ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
[ax.pie\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
([pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, textprops\={'fontsize': 'large', 'color': 'white'})

![pie label](https://matplotlib.org/stable/_images/sphx_glr_pie_label_007_2_00x.png)

[`pie_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
 can be called repeatedly to add multiple sets of labels.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 \= [ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[ax.pie\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
([pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
, [labels](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, distance\=1.1)
[ax.pie\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
([pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
, '{frac:.1%}', distance\=0.7)
[ax.pie\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
([pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
, '{absval:d}', distance\=0.4)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![pie label](https://matplotlib.org/stable/_images/sphx_glr_pie_label_008_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
     / [`matplotlib.pyplot.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie "matplotlib.pyplot.pie")
    
*   [`matplotlib.axes.Axes.pie_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
     / [`matplotlib.pyplot.pie_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie_label.html#matplotlib.pyplot.pie_label "matplotlib.pyplot.pie_label")
    

Tags: [plot-type: pie](https://matplotlib.org/stable/_tags/plot-type-pie.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 2.501 seconds)

[`Download Jupyter notebook: pie_label.ipynb`](https://matplotlib.org/stable/_downloads/110ced5f6ef3c70f18c1dfe527715dc9/pie_label.ipynb)

[`Download Python source code: pie_label.py`](https://matplotlib.org/stable/_downloads/64dfd777742e3adf4632ef8014175a5d/pie_label.py)

[`Download zipped: pie_label.zip`](https://matplotlib.org/stable/_downloads/a416f8a1ffcd08b2fc4c82507a29a0b1/pie_label.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)