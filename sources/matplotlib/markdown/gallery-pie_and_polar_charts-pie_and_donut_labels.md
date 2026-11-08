[Skip to main content](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-download-gallery-pie-and-polar-charts-pie-and-donut-labels-py)
 to download the full example code.

A pie and a donut with labels[#](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html#a-pie-and-a-donut-with-labels "Link to this heading")

============================================================================================================================================================================

Welcome to the Matplotlib bakery. We will create a pie and a donut chart through the [`pie method`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
 and show how to label them with a [`legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
 as well as with the [`pie_label method`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
 and [`annotations`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
.

As usual we would start by defining the imports and create a figure with subplots. Now it's time for the pie. Starting with a pie recipe, we create the data and a list of labels from it.

We then create the pie and store the returned [`PieContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 object for later.

We can provide the [`PieContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 and a format string to the [`pie_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
 method to automatically label each ingredient's wedge with its weight in grams and percentages.

The [`PieContainer`](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 has a list of patches as one of its attributes. Those are [`matplotlib.patches.Wedge`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
 patches, which can directly be used as the handles for a legend. We can use the legend's `bbox_to_anchor` argument to position the legend outside of the pie. Here we use the axes coordinates `(1, 0, 0.5, 1)` together with the location `"center left"`; i.e. the left central point of the legend will be at the left central point of the bounding box, spanning from `(1, 0)` to `(1.5, 1)` in axes coordinates.

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 3))

[recipe](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["375 g flour",\
          "75 g sugar",\
          "250 g butter",\
          "300 g berries"\]

[data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[int([x.split](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
()\[0\]) for [x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
 in [recipe](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\]
[ingredients](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[[x.split](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
()\[\-1\] for [x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
 in [recipe](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")\
\]

[pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 \= [ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

[ax.pie\_label](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
([pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
, '{frac:.1%}\\n({absval:d}g)',
             textprops\=dict(color\="w", size\=8, weight\="bold"))

[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
([pie.wedges](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [ingredients](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
,
          title\="Ingredients",
          loc\="center left",
          bbox\_to\_anchor\=(1, 0, 0.5, 1))

[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Matplotlib bakery: A pie")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Matplotlib bakery: A pie](https://matplotlib.org/stable/_images/sphx_glr_pie_and_donut_labels_001_2_00x.png)

Now it's time for the donut. Starting with a donut recipe, we transcribe the data to numbers (converting 1 egg to 50 g), and directly plot the pie. The pie? Wait... it's going to be donut, is it not? Well, as we see here, the donut is a pie, having a certain `width` set to the wedges, which is different from its radius. It's as easy as it gets. This is done via the `wedgeprops` argument.

We then want to label the wedges via [`annotations`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
. We first create some dictionaries of common properties, which we can later pass as keyword argument. We then iterate over all wedges and for each

*   calculate the angle of the wedge's center,
    
*   from that obtain the coordinates of the point at that angle on the circumference,
    
*   determine the horizontal alignment of the text, depending on which side of the circle the point lies,
    
*   update the connection style with the obtained angle to have the annotation arrow point outwards from the donut,
    
*   finally, create the annotation with all the previously determined parameters.
    

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 3), subplot\_kw\=dict(aspect\="equal"))

[recipe](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \["225 g flour",\
          "90 g sugar",\
          "1 egg",\
          "60 g butter",\
          "100 ml milk",\
          "1/2 package of yeast"\]

[data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[225, 90, 50, 60, 100, 5\]

[pie](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.PieContainer "matplotlib.container.PieContainer")
 \= [ax.pie](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
([data](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, wedgeprops\=dict(width\=0.5), startangle\=-40)

[bbox\_props](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(boxstyle\="square,pad=0.3", fc\="w", ec\="k", lw\=0.72)
[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(arrowprops\=dict(arrowstyle\="-"),
          bbox\=[bbox\_props](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, zorder\=0, va\="center")

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [p](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Wedge.html#matplotlib.patches.Wedge "matplotlib.patches.Wedge")
 in enumerate([pie.wedges](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [ang](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= ([p.theta2](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \- [p.theta1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)/2. + [p.theta1](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
    [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([ang](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
))
    [x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([ang](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
))
    [horizontalalignment](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= {\-1: "right", 1: "left"}\[int([np.sign](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
([x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
))\]
    [connectionstyle](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= f"angle,angleA=0,angleB={[ang](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
}"
    [kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["arrowprops"\].update({"connectionstyle": [connectionstyle](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
})
    [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
([recipe](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\], xy\=([x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
), xytext\=(1.35\*[np.sign](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
), 1.4\*[y](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
),
                [horizontalalignment](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[horizontalalignment](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("Matplotlib bakery: A donut")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Matplotlib bakery: A donut](https://matplotlib.org/stable/_images/sphx_glr_pie_and_donut_labels_002_2_00x.png)

And here it is, the donut. Note however, that if we were to use this recipe, the ingredients would suffice for around 6 donuts - producing one huge donut is untested and might result in kitchen errors.

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie "matplotlib.axes.Axes.pie")
     / [`matplotlib.pyplot.pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie "matplotlib.pyplot.pie")
    
*   [`matplotlib.axes.Axes.pie_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.pie_label.html#matplotlib.axes.Axes.pie_label "matplotlib.axes.Axes.pie_label")
     / [`matplotlib.pyplot.pie_label`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie_label.html#matplotlib.pyplot.pie_label "matplotlib.pyplot.pie_label")
    
*   [`matplotlib.axes.Axes.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
     / [`matplotlib.pyplot.legend`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend "matplotlib.pyplot.legend")
    

Tags: [component: label](https://matplotlib.org/stable/_tags/component-label.html)
 [component: annotation](https://matplotlib.org/stable/_tags/component-annotation.html)
 [plot-type: pie](https://matplotlib.org/stable/_tags/plot-type-pie.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

[`Download Jupyter notebook: pie_and_donut_labels.ipynb`](https://matplotlib.org/stable/_downloads/9a0785a0a15638a736f7c29ff78d9bfd/pie_and_donut_labels.ipynb)

[`Download Python source code: pie_and_donut_labels.py`](https://matplotlib.org/stable/_downloads/99cbf25b3f3fab0fe11b5d265af14565/pie_and_donut_labels.py)

[`Download zipped: pie_and_donut_labels.zip`](https://matplotlib.org/stable/_downloads/581347859c25676fd7d65ae34b4e2fd9/pie_and_donut_labels.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)