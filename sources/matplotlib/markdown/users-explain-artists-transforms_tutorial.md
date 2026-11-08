[Skip to main content](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#sphx-glr-download-users-explain-artists-transforms-tutorial-py)
 to download the full example code.

Transformations Tutorial[#](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transformations-tutorial "Link to this heading")

==========================================================================================================================================================

Like any graphics packages, Matplotlib is built on top of a transformation framework to easily move between coordinate systems, the userland _data_ coordinate system, the _axes_ coordinate system, the _figure_ coordinate system, and the _display_ coordinate system. In 95% of your plotting, you won't need to think about this, as it happens under the hood, but as you push the limits of custom figure generation, it helps to have an understanding of these objects, so you can reuse the existing transformations Matplotlib makes available to you, or create your own (see [`matplotlib.transforms`](https://matplotlib.org/stable/api/transformations.html#module-matplotlib.transforms "matplotlib.transforms")
). The table below summarizes some useful coordinate systems, a description of each system, and the transformation object for going from each coordinate system to the _display_ coordinates. In the "Transformation Object" column, `ax` is a [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 instance, `fig` is a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 instance, and `subfigure` is a [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")
 instance.

| Coordinate system | Description | Transformation object from system to display |
| --- | --- | --- |
| _data_ | The coordinate system of the data in the Axes. | `ax.transData` |
| _axes_ | The coordinate system of the [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")<br>; (0, 0) is bottom left of the Axes, and (1, 1) is top right of the Axes. | `ax.transAxes` |
| _subfigure_ | The coordinate system of the [`SubFigure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.SubFigure.html#matplotlib.figure.SubFigure "matplotlib.figure.SubFigure")<br>; (0, 0) is bottom left of the subfigure, and (1, 1) is top right of the subfigure. If a figure has no subfigures, this is the same as `transFigure`. | `subfigure.transSubfigure` |
| _figure_ | The coordinate system of the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br>; (0, 0) is bottom left of the figure, and (1, 1) is top right of the figure. | `fig.transFigure` |
| _figure-inches_ | The coordinate system of the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")<br> in inches; (0, 0) is bottom left of the figure, and (width, height) is the top right of the figure in inches. | `fig.dpi_scale_trans` |
| _xaxis_, _yaxis_ | Blended coordinate systems, using data coordinates on one direction and axes coordinates on the other. | `ax.get_xaxis_transform()`, `ax.get_yaxis_transform()` |
| _display_ | The native coordinate system of the output ; (0, 0) is the bottom left of the window, and (width, height) is top right of the output in "display units".<br><br>"Display units" depends on the backend. For example, Agg uses pixels, and SVG/PDF use points. | [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")<br>, or [`IdentityTransform()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform") |

The [`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 objects are naive to the source and destination coordinate systems, however the objects referred to in the table above are constructed to take inputs in their coordinate system, and transform the input to the _display_ coordinate system. That is why the _display_ coordinate system has [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
 for the "Transformation Object" column -- it already is in _display_ coordinates. The naming and destination conventions are an aid to keeping track of the available "standard" coordinate systems and transforms.

The transformations also know how to invert themselves (via [`Transform.inverted`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.inverted "matplotlib.transforms.Transform.inverted")
) to generate a transform from output coordinate system back to the input coordinate system. For example, `ax.transData` converts values in data coordinates to display coordinates and `ax.transData.inverted()` is a [`matplotlib.transforms.Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")
 that goes from display coordinates to data coordinates. This is particularly useful when processing events from the user interface, which typically occur in display space, and you want to know where the mouse click or key-press occurred in your _data_ coordinate system.

Note that specifying the position of Artists in _display_ coordinates may change their relative location if the `dpi` or size of the figure changes. This can cause confusion when printing or changing screen resolution, because the object can change location and size. Therefore, it is most common for artists placed in an Axes or figure to have their transform set to something _other_ than the [`IdentityTransform()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
; the default when an artist is added to an Axes using [`add_artist`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_artist.html#matplotlib.axes.Axes.add_artist "matplotlib.axes.Axes.add_artist")
 is for the transform to be `ax.transData` so that you can work and think in _data_ coordinates and let Matplotlib take care of the transformation to _display_.

Data coordinates[#](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#data-coordinates "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

Let's start with the most commonly used coordinate, the _data_ coordinate system. Whenever you add data to the Axes, Matplotlib updates the datalimits, most commonly updated with the [`set_xlim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
 and [`set_ylim()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
 methods. For example, in the figure below, the data limits stretch from 0 to 10 on the x-axis, and -1 to 1 on the y-axis.

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.patches as mpatches

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 10, 0.005)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/2.) \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 10)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-1, 1)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![transforms tutorial](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_001_2_00x.png)

You can use the `ax.transData` instance to transform from your _data_ to your _display_ coordinate system, either a single point or a sequence of points as shown below:

In \[14\]: type([ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
)
Out\[14\]: <class 'matplotlib.transforms.CompositeGenericTransform'>

In \[15\]: [ax.transData.transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
((5, 0))
Out\[15\]: array(\[ 335.175,  247.   \])

In \[16\]: [ax.transData.transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
(\[(5, 0), (1, 2)\])
Out\[16\]:
array(\[\[ 335.175,  247.   \],\
       \[ 132.435,  642.2  \]\])

You can use the [`inverted()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.inverted "matplotlib.transforms.Transform.inverted")
 method to create a transform which will take you from _display_ to _data_ coordinates:

In \[41\]: inv \= [ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
.inverted()

In \[42\]: type(inv)
Out\[42\]: <class 'matplotlib.transforms.CompositeGenericTransform'>

In \[43\]: inv.transform((335.175,  247.))
Out\[43\]: array(\[ 5.,  0.\])

If your are typing along with this tutorial, the exact values of the _display_ coordinates may differ if you have a different window size or dpi setting. Likewise, in the figure below, the display labeled points are probably not the same as in the ipython session because the documentation figure size defaults are different.

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 10, 0.005)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
/2.) \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 10)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-1, 1)

[xdata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [ydata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= 5, 0
\# This computing the transform now, if anything
\# (figure size, dpi, axes placement, data limits, scales..)
\# changes re-calling transform will get a different value.
[xdisplay](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [ydisplay](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= [ax.transData.transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
(([xdata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [ydata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
))

[bbox](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(boxstyle\="round", fc\="0.8")
[arrowprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(
    arrowstyle\="->",
    connectionstyle\="angle,angleA=0,angleB=90,rad=10")

[offset](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
 \= 72
[ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(f'data = ({[xdata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
:.1f}, {[ydata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
:.1f})',
            ([xdata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [ydata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
), xytext\=(\-2\*[offset](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
, [offset](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
), textcoords\='offset points',
            [bbox](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\=[bbox](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, [arrowprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\=[arrowprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[disp](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 \= [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(f'display = ({[xdisplay](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
:.1f}, {[ydisplay](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
:.1f})',
                   ([xdisplay](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [ydisplay](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
), xytext\=(0.5\*[offset](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
, \-[offset](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
),
                   xycoords\='figure pixels',
                   textcoords\='offset points',
                   [bbox](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\=[bbox](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
, [arrowprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\=[arrowprops](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![transforms tutorial](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_002_2_00x.png)

Warning

If you run the source code in the example above in a GUI backend, you may also find that the two arrows for the _data_ and _display_ annotations do not point to exactly the same point. This is because the display point was computed before the figure was displayed, and the GUI backend may slightly resize the figure when it is created. The effect is more pronounced if you resize the figure yourself. This is one good reason why you rarely want to work in _display_ space, but you can connect to the `'on_draw'` [`Event`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.Event "matplotlib.backend_bases.Event")
 to update _figure_ coordinates on figure draws; see [Event handling and picking](https://matplotlib.org/stable/users/explain/figure/event_handling.html#event-handling)
.

When you change the x or y limits of your axes, the data limits are updated so the transformation yields a new display point. Note that when we just change the ylim, only the y-display coordinate is altered, and when we change the xlim too, both are altered. More on this later when we talk about the [`Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
.

In \[54\]: [ax.transData.transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
((5, 0))
Out\[54\]: array(\[ 335.175,  247.   \])

In \[55\]: [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-1, 2)
Out\[55\]: (-1, 2)

In \[56\]: [ax.transData.transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
((5, 0))
Out\[56\]: array(\[ 335.175     ,  181.13333333\])

In \[57\]: [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(10, 20)
Out\[57\]: (10, 20)

In \[58\]: [ax.transData.transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform.transform "matplotlib.transforms.Transform.transform")
((5, 0))
Out\[58\]: array(\[-171.675     ,  181.13333333\])

Axes coordinates[#](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#axes-coordinates "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

After the _data_ coordinate system, _axes_ is probably the second most useful coordinate system. Here the point (0, 0) is the bottom left of your Axes or subplot, (0.5, 0.5) is the center, and (1.0, 1.0) is the top right. You can also refer to points outside the range, so (-0.1, 1.1) is to the left and above your Axes. This coordinate system is extremely useful when placing text in your Axes, because you often want a text bubble in a fixed, location, e.g., the upper left of the Axes pane, and have that location remain fixed when you pan or zoom. Here is a simple example that creates four panels and labels them 'A', 'B', 'C', 'D' as you often see in journals. A more sophisticated approach for such labeling is presented at [Labelling subplots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/label_subplots.html)
.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
()
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate(('A', 'B', 'C', 'D')):
    [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_subplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_subplot.html#matplotlib.figure.Figure.add_subplot "matplotlib.figure.Figure.add_subplot")
(2, 2, [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
+1)
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(0.05, 0.95, [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
            fontsize\=16, fontweight\='bold', va\='top')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![transforms tutorial](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_003_2_00x.png)

You can also make lines or patches in the _axes_ coordinate system, but this is less useful in my experience than using `ax.transAxes` for placing text. Nonetheless, here is a silly example which plots some random dots in data space, and overlays a semi-transparent [`Circle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
 centered in the middle of the Axes with a radius one quarter of the Axes -- if your Axes does not preserve aspect ratio (see [`set_aspect()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html#matplotlib.axes.Axes.set_aspect "matplotlib.axes.Axes.set_aspect")
), this will look like an ellipse. Use the pan/zoom tool to move around, or manually change the data xlim and ylim, and you will see the data move, but the circle will remain fixed because it is not in _data_ coordinates and will always remain at the center of the Axes.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 10\*[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(2, 1000)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 'go', alpha\=0.2)  \# plot some data in data coordinates

[circ](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
 \= [mpatches.Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((0.5, 0.5), 0.25, transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
,
                       facecolor\='blue', alpha\=0.75)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([circ](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![transforms tutorial](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_004_2_00x.png)

Blended transformations[#](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#blended-transformations "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

Drawing in _blended_ coordinate spaces which mix _axes_ with _data_ coordinates is extremely useful, for example to create a horizontal span which highlights some region of the y-data but spans across the x-axis regardless of the data limits, pan or zoom level, etc. In fact these blended lines and spans are so useful, we have built-in functions to make them easy to plot (see [`axhline()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhline.html#matplotlib.axes.Axes.axhline "matplotlib.axes.Axes.axhline")
, [`axvline()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline "matplotlib.axes.Axes.axvline")
, [`axhspan()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axhspan.html#matplotlib.axes.Axes.axhspan "matplotlib.axes.Axes.axhspan")
, [`axvspan()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvspan.html#matplotlib.axes.Axes.axvspan "matplotlib.axes.Axes.axvspan")
) but for didactic purposes we will implement the horizontal span here using a blended transformation. This trick only works for separable transformations, like you see in normal Cartesian coordinate systems, but not on inseparable transformations like the [`PolarTransform`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes.PolarTransform "matplotlib.projections.polar.PolarAxes.PolarTransform")
.

import matplotlib.transforms as transforms

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(1000)

[ax.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist "matplotlib.axes.Axes.hist")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, 30)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(r'$\\sigma=1 \\/ \\dots \\/ \\sigma=2$', fontsize\=16)

\# the x coords of this transformation are data, and the y coord are axes
[trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [transforms.blended\_transform\_factory](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.blended_transform_factory "matplotlib.transforms.blended_transform_factory")
(
    [ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
, [ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)
\# highlight the 1..2 stddev region with a span.
\# We want x to be in data coordinates and y to span from 0..1 in axes coords.
[rect](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
 \= [mpatches.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
((1, 0), width\=1, height\=1, transform\=[trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
,
                          color\='yellow', alpha\=0.5)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([rect](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![$\sigma=1 \/ \dots \/ \sigma=2$](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_005_2_00x.png)

Note

The blended transformations where x is in _data_ coords and y in _axes_ coordinates is so useful that we have helper methods to return the versions Matplotlib uses internally for drawing ticks, ticklabels, etc. The methods are [`matplotlib.axes.Axes.get_xaxis_transform()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_transform.html#matplotlib.axes.Axes.get_xaxis_transform "matplotlib.axes.Axes.get_xaxis_transform")
 and [`matplotlib.axes.Axes.get_yaxis_transform()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_yaxis_transform.html#matplotlib.axes.Axes.get_yaxis_transform "matplotlib.axes.Axes.get_yaxis_transform")
. So in the example above, the call to [`blended_transform_factory()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.blended_transform_factory "matplotlib.transforms.blended_transform_factory")
 can be replaced by `get_xaxis_transform`:

[trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.get\_xaxis\_transform()

Plotting in physical coordinates[#](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#plotting-in-physical-coordinates "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes we want an object to be a certain physical size on the plot. Here we draw the same circle as above, but in physical coordinates. If done interactively, you can see that changing the size of the figure does not change the offset of the circle from the lower-left corner, does not change its size, and the circle remains a circle regardless of the aspect ratio of the Axes.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(5, 4))
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 10\*[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(2, 1000)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*10., 'go', alpha\=0.2)  \# plot some data in data coordinates
\# add a circle in fixed-coordinates
[circ](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
 \= [mpatches.Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((2.5, 2), 1.0, transform\=[fig.dpi\_scale\_trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
,
                       facecolor\='blue', alpha\=0.75)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([circ](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![transforms tutorial](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_006_2_00x.png)

If we change the figure size, the circle does not change its absolute position and is cropped.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(7, 2))
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 10\*[np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(2, 1000)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*10., 'go', alpha\=0.2)  \# plot some data in data coordinates
\# add a circle in fixed-coordinates
[circ](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
 \= [mpatches.Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((2.5, 2), 1.0, transform\=[fig.dpi\_scale\_trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
,
                       facecolor\='blue', alpha\=0.75)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([circ](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![transforms tutorial](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_007_2_00x.png)

Another use is putting a patch with a set physical dimension around a data point on the Axes. Here we add together two transforms. The first sets the scaling of how large the ellipse should be and the second sets its position. The ellipse is then placed at the origin, and then we use the helper transform [`ScaledTranslation`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
 to move it to the right place in the `ax.transData` coordinate system. This helper is instantiated with:

[trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= ScaledTranslation(xt, yt, scale\_trans)

where _xt_ and _yt_ are the translation offsets, and _scale\_trans_ is a transformation which scales _xt_ and _yt_ at transformation time before applying the offsets.

Note the use of the plus operator on the transforms below. This code says: first apply the scale transformation `fig.dpi_scale_trans` to make the ellipse the proper size, but still centered at (0, 0), and then translate the data to `xdata[0]` and `ydata[0]` in data space.

In interactive use, the ellipse stays the same size even if the axes limits are changed via zoom.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[xdata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [ydata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (0.2, 0.7), (0.5, 0.5)
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([xdata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [ydata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, "o")
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 1)

[trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= ([fig.dpi\_scale\_trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
 +
         [transforms.ScaledTranslation](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
([xdata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\], [ydata](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
\[0\], [ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
))

\# plot an ellipse around the point that is 150 x 130 points in diameter...
[circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
 \= [mpatches.Ellipse](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
((0, 0), 150/72, 130/72, angle\=40,
                          fill\=None, transform\=[trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
)
[ax.add\_patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")
([circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")
)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![transforms tutorial](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_008_2_00x.png)

Note

The order of transformation matters. Here the ellipse is given the right dimensions in display space _first_ and then moved in data space to the correct spot. If we had done the `ScaledTranslation` first, then `xdata[0]` and `ydata[0]` would first be transformed to _display_ coordinates (`[ 358.4  475.2]` on a 200-dpi monitor) and then those coordinates would be scaled by `fig.dpi_scale_trans` pushing the center of the ellipse well off the screen (i.e. `[ 71680.  95040.]`).

Using offset transforms to create a shadow effect[#](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#using-offset-transforms-to-create-a-shadow-effect "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Another use of [`ScaledTranslation`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
 is to create a new transformation that is offset from another transformation, e.g., to place one object shifted a bit relative to another object. Typically, you want the shift to be in some physical dimension, like points or inches rather than in _data_ coordinates, so that the shift effect is constant at different zoom levels and dpi settings.

One use for an offset is to create a shadow effect, where you draw one object identical to the first just to the right of it, and just below it, adjusting the zorder to make sure the shadow is drawn first and then the object it is shadowing above it.

Here we apply the transforms in the _opposite_ order to the use of [`ScaledTranslation`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
 above. The plot is first made in data coordinates (`ax.transData`) and then shifted by `dx` and `dy` points using `fig.dpi_scale_trans`. (In typography, a [point](https://en.wikipedia.org/wiki/Point_%28typography%29)
 is 1/72 inches, and by specifying your offsets in points, your figure will look the same regardless of the dpi resolution it is saved in.)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()

\# make a simple sine wave
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0., 2., 0.01)
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2\*[np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
\*[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[line](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=3, color\='blue')

\# shift the object over 2 points, and down 2 points
[dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 2/72., \-2/72.
[offset](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
 \= [transforms.ScaledTranslation](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
([dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [fig.dpi\_scale\_trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
)
[shadow\_transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= [ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 + [offset](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")

\# now plot the same data with our offset transform;
\# use the zorder to make sure we are below the line
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, lw\=3, color\='gray',
        transform\=[shadow\_transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
,
        zorder\=0.5\*[line.get\_zorder](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.get_zorder.html#matplotlib.artist.Artist.get_zorder "matplotlib.artist.Artist.get_zorder")
())

[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('creating a shadow effect with an offset transform')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![creating a shadow effect with an offset transform](https://matplotlib.org/stable/_images/sphx_glr_transforms_tutorial_009_2_00x.png)

Note

The dpi and inches offset is a common-enough use case that we have a special helper function to create it in [`matplotlib.transforms.offset_copy()`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.offset_copy "matplotlib.transforms.offset_copy")
, which returns a new transform with an added offset. So above we could have done:

[shadow\_transform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
 \= transforms.offset\_copy([ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
,
         [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [dx](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [dy](https://docs.python.org/3/library/functions.html#float "builtins.float")
, units\='inches')

The transformation pipeline[#](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#the-transformation-pipeline "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

The `ax.transData` transform we have been working with in this tutorial is a composite of three different transformations that comprise the transformation pipeline from _data_ -> _display_ coordinates. Michael Droettboom implemented the transformations framework, taking care to provide a clean API that segregated the nonlinear projections and scales that happen in polar and logarithmic plots, from the linear affine transformations that happen when you pan and zoom. There is an efficiency here, because you can pan and zoom in your Axes which affects the affine transformation, but you may not need to compute the potentially expensive nonlinear scales or projections on simple navigation events. It is also possible to multiply affine transformation matrices together, and then apply them to coordinates in one step. This is not true of all possible transformations.

Here is how the `ax.transData` instance is defined in the basic separable axis [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 class:

self.transData \= self.transScale + (self.transLimits + self.transAxes)

We've been introduced to the `transAxes` instance above in [Axes coordinates](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#axes-coords)
, which maps the (0, 0), (1, 1) corners of the Axes or subplot bounding box to _display_ space, so let's look at these other two pieces.

`self.transLimits` is the transformation that takes you from _data_ to _axes_ coordinates; i.e., it maps your view xlim and ylim to the unit space of the Axes (and `transAxes` then takes that unit space to display space). We can see this in action here

In \[80\]: [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= plt.subplot()

In \[81\]: [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 10)
Out\[81\]: (0, 10)

In \[82\]: [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(\-1, 1)
Out\[82\]: (-1, 1)

In \[84\]: [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.transLimits.transform((0, \-1))
Out\[84\]: array(\[ 0.,  0.\])

In \[85\]: [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.transLimits.transform((10, \-1))
Out\[85\]: array(\[ 1.,  0.\])

In \[86\]: [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.transLimits.transform((10, 1))
Out\[86\]: array(\[ 1.,  1.\])

In \[87\]: [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.transLimits.transform((5, 0))
Out\[87\]: array(\[ 0.5,  0.5\])

and we can use this same inverted transformation to go from the unit _axes_ coordinates back to _data_ coordinates.

In \[90\]: inv.transform((0.25, 0.25))
Out\[90\]: array(\[ 2.5, -0.5\])

The final piece is the `self.transScale` attribute, which is responsible for the optional non-linear scaling of the data, e.g., for logarithmic axes. When an Axes is initially setup, this is just set to the identity transform, since the basic Matplotlib axes has linear scale, but when you call a logarithmic scaling function like [`semilogx()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.semilogx.html#matplotlib.axes.Axes.semilogx "matplotlib.axes.Axes.semilogx")
 or explicitly set the scale to logarithmic with [`set_xscale()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale "matplotlib.axes.Axes.set_xscale")
, then the `ax.transScale` attribute is set to handle the nonlinear projection. The scales transforms are properties of the respective `xaxis` and `yaxis` [`Axis`](https://matplotlib.org/stable/api/axis_api.html#matplotlib.axis.Axis "matplotlib.axis.Axis")
 instances. For example, when you call `ax.set_xscale('log')`, the xaxis updates its scale to a [`matplotlib.scale.LogScale`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.LogScale "matplotlib.scale.LogScale")
 instance.

For non-separable axes, there are some more pieces to consider, in particular the projection transformation. For example, the `transData` of [`matplotlib.projections.polar.PolarAxes`](https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes "matplotlib.projections.polar.PolarAxes")
 is more complex than that of a typical separable Axes:

self.transData \= (
    self.transScale + self.transShift + self.transProjection +
    (self.transProjectionAffine + self.transWedge + self.transAxes))

`transProjection` handles the projection from data coordinates (e.g., latitude and longitude for map data, or radius and theta for polar data), to a separable Cartesian coordinate system. There are several projection examples in the [`matplotlib.projections`](https://matplotlib.org/stable/api/projections_api.html#module-matplotlib.projections "matplotlib.projections")
 package, and the best way to learn more is to open the source for those packages and see how to make your own, since Matplotlib supports extensible axes and projections. Michael Droettboom has provided a nice tutorial example of creating a Hammer projection axes; see [Custom projection](https://matplotlib.org/stable/gallery/misc/custom_projection.html)
.

**Total running time of the script:** (0 minutes 3.825 seconds)

[`Download Jupyter notebook: transforms_tutorial.ipynb`](https://matplotlib.org/stable/_downloads/5386527d666afd4ca59df6c73e7bd9c9/transforms_tutorial.ipynb)

[`Download Python source code: transforms_tutorial.py`](https://matplotlib.org/stable/_downloads/4776d1658947f2a5be31f56f02a4454a/transforms_tutorial.py)

[`Download zipped: transforms_tutorial.zip`](https://matplotlib.org/stable/_downloads/68218fd9e3a4550a9b996329e13f8d72/transforms_tutorial.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page