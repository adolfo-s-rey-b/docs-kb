[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_rotation_mode.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_rotation_mode.html#sphx-glr-download-gallery-text-labels-and-annotations-demo-text-rotation-mode-py)
 to download the full example code.

Text rotation mode[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/demo_text_rotation_mode.html#text-rotation-mode "Link to this heading")

================================================================================================================================================================

This example illustrates the effect of `rotation_mode` on the positioning of rotated text.

Rotated [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
s are created by passing the parameter `rotation` to the constructor or the Axes' method [`text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
.

The actual positioning depends on the additional parameters `horizontalalignment`, `verticalalignment` and `rotation_mode`. `rotation_mode` determines the order of rotation and alignment:

*   `rotation_mode='default'` (or None) first rotates the text and then aligns the bounding box of the rotated text.
    
*   `rotation_mode='anchor'` aligns the unrotated text and then rotates the text around the point of alignment.
    

import matplotlib.pyplot as plt

def test\_rotation\_mode([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, mode):
    ha\_list \= \["left", "center", "right"\]
    va\_list \= \["top", "center", "baseline", "bottom"\]
    axs \= [fig.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots.html#matplotlib.figure.Figure.subplots "matplotlib.figure.Figure.subplots")
(len(va\_list), len(ha\_list), sharex\=True, sharey\=True,
                       subplot\_kw\=dict(aspect\=1),
                       gridspec\_kw\=dict(hspace\=0, wspace\=0))

    \# labels and title
    for ha, ax in zip(ha\_list, axs\[\-1, :\]):
        ax.set\_xlabel(ha)
    for va, ax in zip(va\_list, axs\[:, 0\]):
        ax.set\_ylabel(va)
    axs\[0, 1\].set\_title(f"rotation\_mode='{mode}'", size\="large")

    kw \= (
        {} if mode \== "default" else
        {"bbox": dict(boxstyle\="square,pad=0.", ec\="none", fc\="C1", alpha\=0.3)}
    )

    texts \= {}

    \# use a different text alignment in each Axes
    for i, va in enumerate(va\_list):
        for j, ha in enumerate(ha\_list):
            ax \= axs\[i, j\]
            \# prepare Axes layout
            ax.set(xticks\=\[\], yticks\=\[\])
            ax.axvline(0.5, color\="skyblue", zorder\=0)
            ax.axhline(0.5, color\="skyblue", zorder\=0)
            ax.plot(0.5, 0.5, color\="C0", marker\="o", zorder\=1)
            \# add text with rotation and alignment settings
            tx \= ax.text(0.5, 0.5, "Tpg",
                         size\="x-large", rotation\=40,
                         horizontalalignment\=ha, verticalalignment\=va,
                         rotation\_mode\=mode, \*\*kw)
            texts\[ax\] \= tx

    if mode \== "default":
        \# highlight bbox
        [fig.canvas.draw](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw")
()
        for ax, text in texts.items():
            bb \= text.get\_window\_extent().transformed(ax.transData.inverted())
            rect \= [plt.Rectangle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle")
((bb.x0, bb.y0), bb.width, bb.height,
                                 facecolor\="C1", alpha\=0.3, zorder\=2)
            ax.add\_patch(rect)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 5))
[subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [fig.subfigures](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subfigures.html#matplotlib.figure.Figure.subfigures "matplotlib.figure.Figure.subfigures")
(1, 2)
test\_rotation\_mode([subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], "default")
test\_rotation\_mode([subfigs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\], "anchor")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![rotation_mode='default', rotation_mode='anchor'](https://matplotlib.org/stable/_images/sphx_glr_demo_text_rotation_mode_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
     / [`matplotlib.pyplot.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
    

**Total running time of the script:** (0 minutes 1.213 seconds)

[`Download Jupyter notebook: demo_text_rotation_mode.ipynb`](https://matplotlib.org/stable/_downloads/5b5d52ac8b43604288d79ae75c5a8dc5/demo_text_rotation_mode.ipynb)

[`Download Python source code: demo_text_rotation_mode.py`](https://matplotlib.org/stable/_downloads/58345f9f57bb466b821c32d7c2c5509e/demo_text_rotation_mode.py)

[`Download zipped: demo_text_rotation_mode.zip`](https://matplotlib.org/stable/_downloads/5574605b39e94be9f40b74b68ba68d03/demo_text_rotation_mode.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)