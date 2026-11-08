[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/label_subplots.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/label_subplots.html#sphx-glr-download-gallery-text-labels-and-annotations-label-subplots-py)
 to download the full example code.

Labelling subplots[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/label_subplots.html#labelling-subplots "Link to this heading")

=======================================================================================================================================================

Labelling subplots is relatively straightforward, and varies, so Matplotlib does not have a general method for doing this.

We showcase two methods to position text at a given physical offset (in fontsize units or in points) away from a corner of the Axes: one using [`annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
, and one using [`ScaledTranslation`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
.

For convenience, this example uses [`pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
 and subplot labels as keys for the subplots. However, the approach also works with [`pyplot.subplots`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
 or keys that are different from what you want to label the subplot with.

import matplotlib.pyplot as plt

from matplotlib.transforms import [ScaledTranslation](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['a)', 'c)'\], \['b)', 'c)'\], \['d)', 'd)'\]\],
                              layout\='constrained')
for [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():
    \# Use Axes.annotate to put the label
    \# - at the top left corner (axes fraction (0, 1)),
    \# - offset half-a-fontsize right and half-a-fontsize down
    \#   (offset fontsize (+0.5, -0.5)),
    \# i.e. just inside the axes.
    [ax.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
(
        [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
        xy\=(0, 1), xycoords\='axes fraction',
        xytext\=(+0.5, \-0.5), textcoords\='offset fontsize',
        fontsize\='medium', verticalalignment\='top', fontfamily\='serif',
        bbox\=dict(facecolor\='0.7', edgecolor\='none', pad\=3.0))

![label subplots](https://matplotlib.org/stable/_images/sphx_glr_label_subplots_001_2_00x.png)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['a)', 'c)'\], \['b)', 'c)'\], \['d)', 'd)'\]\],
                              layout\='constrained')
for [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():
    \# Use ScaledTranslation to put the label
    \# - at the top left corner (axes fraction (0, 1)),
    \# - offset 20 pixels left and 7 pixels up (offset points (-20, +7)),
    \# i.e. just outside the axes.
    [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(
        0.0, 1.0, [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, transform\=(
            [ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
 + [ScaledTranslation](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.ScaledTranslation "matplotlib.transforms.ScaledTranslation")
(\-20/72, +7/72, [fig.dpi\_scale\_trans](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Affine2D "matplotlib.transforms.Affine2D")
)),
        fontsize\='medium', va\='bottom', fontfamily\='serif')

![label subplots](https://matplotlib.org/stable/_images/sphx_glr_label_subplots_002_2_00x.png)

If we want it aligned with the title, either incorporate in the title or use the _loc_ keyword argument:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(\[\['a)', 'c)'\], \['b)', 'c)'\], \['d)', 'd)'\]\],
                              layout\='constrained')
for [label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Normal Title', fontstyle\='italic')
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
([label](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontfamily\='serif', loc\='left', fontsize\='medium')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![a), Normal Title, c), Normal Title, b), Normal Title, d), Normal Title](https://matplotlib.org/stable/_images/sphx_glr_label_subplots_003_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.figure.Figure.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
     / [`matplotlib.pyplot.subplot_mosaic`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
    
*   [`matplotlib.axes.Axes.set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
    
*   [`matplotlib.axes.Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
    

**Total running time of the script:** (0 minutes 3.526 seconds)

[`Download Jupyter notebook: label_subplots.ipynb`](https://matplotlib.org/stable/_downloads/b1f5ca501205571bdd192ef9d081b1ef/label_subplots.ipynb)

[`Download Python source code: label_subplots.py`](https://matplotlib.org/stable/_downloads/827a1d72743e3fc3edb7c08e7b5a4f5c/label_subplots.py)

[`Download zipped: label_subplots.zip`](https://matplotlib.org/stable/_downloads/dae4bb6a1c2860477f2eb6b463b244a9/label_subplots.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)